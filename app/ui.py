import json


def show_result(result):
    print("\n=== RESULTADO FINAL ===")
    print(json.dumps(result, indent=4, ensure_ascii=False))
