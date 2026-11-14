#!/usr/bin/env bash
# Tells IndexNow (Bing, Yandex, Seznam, Naver, Yep) that the pages in a site's sitemap may have changed.
# Usage: indexnow.sh <host>. The key is public by design: it is also served at https://<host>/<key>.txt.
# Waits until the key file is live (a fresh deploy), then sends every <loc> in one request.
set -euo pipefail
host="$1"
key="3f52a42aa9df460cb325106fbdab06e3"
for i in $(seq 1 30); do
  [ "$(curl -fsS "https://$host/$key.txt" 2>/dev/null | tr -d "[:space:]")" = "$key" ] && break
  [ "$i" = 30 ] && { echo "::warning::IndexNow key file not live on $host"; exit 0; }
  sleep 20
done
urls=$(curl -fsS "https://$host/sitemap.xml" | grep -o "<loc>[^<]*</loc>" | sed -e "s#</*loc>##g" | sort -u)
[ -z "$urls" ] && { echo "::warning::No URLs in the sitemap of $host"; exit 0; }
body=$(HOST="$host" KEY="$key" URLS="$urls" python3 -c "import json,os; print(json.dumps({\"host\": os.environ[\"HOST\"], \"key\": os.environ[\"KEY\"], \"keyLocation\": \"https://%s/%s.txt\" % (os.environ[\"HOST\"], os.environ[\"KEY\"]), \"urlList\": os.environ[\"URLS\"].split()}))")
code=$(curl -sS -o /dev/null -w "%{http_code}" -X POST "https://api.indexnow.org/indexnow" -H "Content-Type: application/json; charset=utf-8" --data "$body")
n=$(echo "$urls" | wc -l | tr -d " ")
if [ "$code" = 200 ] || [ "$code" = 202 ]; then echo "::notice title=IndexNow::$n URLs from $host sent ($code)"; else echo "::warning title=IndexNow::$host answered $code"; fi
