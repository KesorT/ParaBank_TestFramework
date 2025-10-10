import xml.etree.ElementTree as ET

def parse_response(response):
    try:
        return response.json()
    except Exception:
        try:
            root = ET.fromstring(response.text)
            children = list(root)
            if not children:
                return {root.tag: root.text}
            tags = [c.tag for c in children]
            if len(set(tags)) == 1:  
                return {root.tag: [{sub.tag: sub.text for sub in child} for child in children]}
            else:
                return {child.tag: child.text for child in children}
        except Exception:
            return {"raw": response.text}

