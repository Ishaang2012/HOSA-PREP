import sys, re, json, os
hosa = sys.argv[1]
out = {}
BUL = r'^\s*(?:[●○•▪]|o\s|[a-z]\.\s)'
for line in open(os.path.join(hosa,'list.txt')):
    cat, id_, name, path = line.rstrip('\n').split('|')
    raw = open(os.path.join(hosa,'txt',id_+'.txt'), encoding='utf-8').read().replace('​','').replace('\f','\n')
    lines = [l.rstrip() for l in raw.split('\n') if not re.search(r'ILC Guidelines \(|Page \d+ of \d+|The expectation is that competitors|links for the detailed', l)]
    def label(l): return l[:36].strip()
    def section(start_re, same_label_re):
        res=[]; on=False
        for l in lines:
            lab=label(l)
            if not on:
                if re.match(start_re, lab, re.I): on=True; res.append(l[36:])
                continue
            if lab and not re.match(same_label_re, lab, re.I) and not re.match(BUL, lab) and not lab[0].isdigit() and len(l)-len(l.lstrip()) < 3:
                break
            res.append(l[36:] if lab and re.match(same_label_re, lab, re.I) else l)
        # merge wrapped lines into items
        items=[]
        for r in res:
            t=r.strip()
            if not t: continue
            m=re.match(r'^([●•▪]|[a-h]\.)\s*(.*)',t)
            sm=re.match(r'^(○|o)\s+(.*)',t)
            if m: items.append({'t':m.group(2).strip(),'sub':[]})
            elif sm and items: items[-1]['sub'].append(sm.group(2).strip())
            elif items:
                if items[-1]['sub']: items[-1]['sub'][-1]+=' '+t
                else: items[-1]['t']+=' '+t
            else: items.append({'t':t,'sub':[],'intro':True})
        return items
    refs = section(r'^(Official )?References?$|^Official$|^Resources$', r'^(Official )?References?$|^Official$|^Resources$')
    plan = section(r'^(Written )?Test Plan', r'^(Written )?Test Plan')
    hdr = raw.split('Event Summary')[0]
    fmt = re.search(r'Round One:\s*([^\n|]+?)(?:\s{2,}|\n)', hdr)
    team = re.search(r'(Solo Event[^\n]*?|Team Event[^\n]*?)(?:\s{2,}|\n|$)', hdr)
    summ = re.search(r'Event Summary\s*\n([\s\S]+?)\n\s*\n', raw)
    out[id_] = dict(category=cat, name=name, pdf='https://hosa.org/wp-content/uploads/'+path,
        round1=fmt.group(1).strip() if fmt else '', team=team.group(1).strip() if team else '',
        summary=re.sub(r'\s+',' ',summ.group(1)).strip() if summ else '',
        references=refs, testplan=plan)
json.dump(out, open(os.path.join(hosa,'extracted2.json'),'w'), indent=1, ensure_ascii=False)
for k,v in out.items():
    print(f"== {v['name']} [{v['round1']}] [{v['team']}]")
    for r in v['references']: print('   R:', r['t'][:150])
    for p in v['testplan']: print('   P:', p['t'][:100], ('('+'; '.join(p['sub'])[:120]+')') if p['sub'] else '')
