# -*- coding: utf-8 -*-
"""Inyecta enlaces contextuales DENTRO de los parrafos del dataset, con variacion semantica."""
import json, re, subprocess

d = json.load(open('data/sso.json', encoding='utf-8'))

# Patron regex (case insensitive) -> URL destino
LINK_MAP = [
    (r'\bEl Paso SSA office\b',               '/social-security-office-el-paso/'),
    (r'\bSSA office in El Paso\b',            '/social-security-office-el-paso/'),
    (r'\bschedule an appointment\b',          '/social-security-office-appointment-el-paso/'),
    (r'\bbook an appointment\b',              '/social-security-office-appointment-el-paso/'),
    (r'\boffice hours\b',                     '/social-security-office-hours-el-paso/'),
    (r'\bWednesday early-close\b',            '/social-security-office-hours-el-paso/'),
    (r'\brequired documents\b',               '/ssa-required-documents-el-paso/'),
    (r'\boriginal documents\b',               '/ssa-required-documents-el-paso/'),
    (r'\breplacement Social Security card\b', '/replace-social-security-card-el-paso/'),
    (r'\breplacement card\b',                 '/replace-social-security-card-el-paso/'),
    (r'\bSocial Security card\b',             '/apply-for-social-security-card-el-paso/'),
    (r'\bSSN card\b',                         '/apply-for-social-security-card-el-paso/'),
    (r'\bdisability benefits\b',              '/apply-for-disability-benefits-el-paso/'),
    (r'\bSocial Security Disability Insurance\b', '/apply-for-disability-benefits-el-paso/'),
    (r'\bSupplemental Security Income\b',     '/apply-for-ssi-el-paso/'),
    (r'\bretirement application\b',           '/apply-for-social-security-retirement-el-paso/'),
    (r'\bSocial Security retirement\b',       '/apply-for-social-security-retirement-el-paso/'),
    (r'\bMedicare enrollment\b',              '/apply-for-medicare-el-paso/'),
    (r'\bMedicare\b',                         '/apply-for-medicare-el-paso/'),
    (r'\bFull Retirement Age\b',              '/retirement-age-calculator/'),
    (r'\bdifference between SSDI and SSI\b',  '/ssi-vs-ssdi-difference/'),
    (r'\bSSDI vs SSI\b',                      '/ssi-vs-ssdi-difference/'),
    (r'\bwhen to start benefits\b',           '/when-to-apply-for-social-security-retirement/'),
    (r'\bSSA office locator\b',               '/social-security-office-near-me-el-paso/'),
    (r'\bSSA field office\b',                 '/social-security-office-near-me-el-paso/'),
    (r'\blegal name change\b',                '/change-name-on-social-security-card-el-paso/'),
    (r'\bnewborn\b',                          '/get-social-security-number-for-newborn-el-paso/'),
    (r'\bhow Social Security works\b',        '/what-is-social-security/'),
]

def inject_links(text, current_url, used_destinations, max_links=2):
    """Reemplaza primera ocurrencia de cada patron por <a> tag."""
    added = 0
    for pattern, url in LINK_MAP:
        if added >= max_links: break
        if url == current_url: continue
        if url in used_destinations: continue
        # Saltar si ya hay un <a href= en el texto cerca de la frase (evita doble-link)
        if re.search(r'<a [^>]*>[^<]*' + pattern, text, flags=re.IGNORECASE):
            continue
        def repl(m): return f'<a href="{url}">{m.group(0)}</a>'
        new_text, n = re.subn(pattern, repl, text, count=1, flags=re.IGNORECASE)
        if n > 0:
            text = new_text
            used_destinations.add(url)
            added += 1
    return text, used_destinations

total_pages_with_links = 0
total_links = 0

for silo_key in ['services', 'office', 'learn']:
    for page in d[silo_key]:
        current_url = f'/{page["slug"]}/'
        used = set()
        
        if 'intro' in page:
            page['intro'], used = inject_links(page['intro'], current_url, used, max_links=2)
        
        for sec in page.get('sections', []):
            if sec.get('type') == 'section':
                new_body = []
                for par in sec['body']:
                    par2, used = inject_links(par, current_url, used, max_links=2)
                    new_body.append(par2)
                sec['body'] = new_body
        
        if used:
            total_pages_with_links += 1
            total_links += len(used)
            print(f"  /{page['slug']}/ - {len(used)} links")

print(f"\nTotal: {total_links} links contextuales en {total_pages_with_links} paginas")
json.dump(d, open('data/sso.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
subprocess.run(['python3','scripts/build-datos-js.py'], check=True)
print("OK dataset + datos.js actualizados")
