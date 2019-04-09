def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x in seen:
            continue
        seen.add(x)
        result.append(x)
    return result
	
import re
	
text = editor.getText();
result = re.findall('.*\n',text)
result = unique(result)
notepad.new();
for s in result:
	editor.addText(s);
