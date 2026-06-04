#!/usr/bin/env python3
"""Generates sitemap.xml + sitemap-0.xml (alias) + sitemap-index.xml in dist/."""
import os, shutil
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, 'dist')

domain = "https://centrelinkofficesaustralia.com"
today = datetime.now(timezone.utc).strftime('%Y-%m-%d')

urls = []
for dirpath, dirnames, filenames in os.walk(DIST):
    if 'index.html' in filenames:
        fp = os.path.join(dirpath, 'index.html')
        with open(fp, encoding='utf-8') as f:
            html = f.read()
        if 'noindex' in html.lower():
            continue
        rel = os.path.relpath(dirpath, DIST)
        url_path = '/' if rel == '.' else f"/{rel.replace(os.sep, '/')}/"
        urls.append(url_path)

urls.sort()

xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for url in urls:
    priority = "1.0" if url == "/" else "0.9" if url.startswith("/state/") else "0.8"
    changefreq = "weekly" if url == "/" else "monthly"
    xml += f'  <url>\n    <loc>{domain}{url}</loc>\n    <lastmod>{today}</lastmod>\n    <changefreq>{changefreq}</changefreq>\n    <priority>{priority}</priority>\n  </url>\n'
xml += '</urlset>\n'

with open(os.path.join(DIST, 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write(xml)
shutil.copy(os.path.join(DIST, 'sitemap.xml'), os.path.join(DIST, 'sitemap-0.xml'))

xml_idx = '<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
xml_idx += f'  <sitemap>\n    <loc>{domain}/sitemap.xml</loc>\n    <lastmod>{today}</lastmod>\n  </sitemap>\n</sitemapindex>\n'
with open(os.path.join(DIST, 'sitemap-index.xml'), 'w', encoding='utf-8') as f:
    f.write(xml_idx)

# Robots.txt
robots = f"""User-agent: *
Allow: /

Sitemap: {domain}/sitemap-index.xml
"""
with open(os.path.join(DIST, 'robots.txt'), 'w', encoding='utf-8') as f:
    f.write(robots)

print(f"OK: {len(urls)} URLs")
print(f"  Files: sitemap.xml, sitemap-0.xml, sitemap-index.xml, robots.txt")
