import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
import re
from tqdm import tqdm
from pathlib import Path

# ================== 基本配置 ==================
BASE_URL = "https://bgm.tv"
BROWSER_URL = "/anime/browser?sort=rank&page={}"
API_URL = "https://api.bgm.tv/v0/subjects/{}"

TARGET_COUNT = 10000
SAVE_FILE = "bangumi_anime.csv"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": (
        "text/html,application/xhtml+xml,application/xml;"
        "q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8"
    ),
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Referer": "https://bgm.tv/anime",
    "Connection": "keep-alive",
}

session = requests.Session()
session.headers.update(HEADERS)

# ================== 工具函数 ==================
def get_html(url, retry=3):
    for i in range(retry):
        try:
            r = session.get(url, timeout=50)
            if r.status_code == 200:
                return r.content.decode("utf-8", errors="ignore")
            else:
                print(f"HTTP {r.status_code}，重试 {i+1}/{retry}")
        except Exception as e:
            print(f"请求失败：{e}，重试 {i+1}/{retry}")

        time.sleep(2 + i * 2)

    raise RuntimeError(f"访问失败：{url}")


def extract_year(date_str):
    if not date_str:
        return None
    m = re.match(r"(\d{4})", date_str)
    return int(m.group(1)) if m else None


# ================== Step 1：收集 subject_id ==================
def collect_subject_ids(limit):
    ids = []
    page = 1

    print("开始收集 subject_id ...")

    while len(ids) < limit:
        url = BASE_URL + BROWSER_URL.format(page)
        soup = BeautifulSoup(get_html(url), "html.parser")

        items = soup.select("ul#browserItemList > li h3 > a")
        if not items:
            break

        for a in items:
            href = a.get("href", "")
            m = re.search(r"/subject/(\d+)", href)
            if m:
                ids.append(int(m.group(1)))
                if len(ids) >= limit:
                    break

        print(f"已收集 {len(ids)} 个 subject_id")
        page += 1
        time.sleep(2)

    return ids


# ================== Step 2：API ==================
def fetch_subject_api(subject_id):
    url = API_URL.format(subject_id)
    r = session.get(url, timeout=50)
    if r.status_code != 200:
        return None
    return r.json()


def parse_subject(data):
    if not data:
        return None

    rating = data.get("rating", {})
    total = rating.get("total", 0)

    # 只保留有评分的数据
    if total == 0:
        return None

    counts = rating.get("count", {})

    infobox = data.get("infobox", [])
    companies = []

    for item in infobox:
        if item.get("key") in ("动画制作", "制作"):
            v = item.get("value")
            if isinstance(v, list):
                companies.extend([x.get("v") for x in v if "v" in x])
            elif isinstance(v, str):
                companies.append(v)

    row = {
        "subject_id": data.get("id"),
        "name_cn": data.get("name_cn") or data.get("name"),
        "name": data.get("name"),
        "score": rating.get("score"),
        "total": total,
        "year": extract_year(data.get("date")),
        "company": ",".join(set(companies)),
    }

    # 各分数百分比
    for i in range(1, 11):
        row[f"rate_{i}"] = counts.get(str(i), 0)

    return row



# ================== 主流程 ==================
def main():
    if Path(SAVE_FILE).exists():
        df = pd.read_csv(SAVE_FILE)
        if "subject_id" in df.columns:
            done_ids = set(df["subject_id"].dropna().astype(int))
            print(f"检测到已有 {len(done_ids)} 条数据，继续爬取...")
        else:
            df = pd.DataFrame()
            done_ids = set()
    else:
        df = pd.DataFrame()
        done_ids = set()

    subject_ids = collect_subject_ids(TARGET_COUNT)
    buffer = []

    for sid in tqdm(subject_ids):
        if sid in done_ids:
            continue

        data = fetch_subject_api(sid)
        parsed = parse_subject(data)
        if parsed:
            buffer.append(parsed)

        time.sleep(random.uniform(1.0, 1.6))

        if len(buffer) >= 50:
            df = pd.concat([df, pd.DataFrame(buffer)], ignore_index=True)
            df.to_csv(SAVE_FILE, index=False, encoding="utf-8-sig")
            buffer.clear()

    if buffer:
        df = pd.concat([df, pd.DataFrame(buffer)], ignore_index=True)

    df.to_csv(SAVE_FILE, index=False, encoding="utf-8-sig")
    print(f"\n完成！共 {len(df)} 条数据，已保存 {SAVE_FILE}")


if __name__ == "__main__":
    main()
