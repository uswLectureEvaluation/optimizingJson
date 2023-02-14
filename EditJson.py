import json

filename = "230214"

# 수정할 json 파일 경로 입력
with open('C:\\Users\\aaa\\Desktop\\TimetableData\\' + filename + '.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)

# 삭제하면 안되는 키 배열
listToSave = ["estbDpmjNm", "trgtGrdeCd", "subjtCd", "diclNo", "subjtNm", "facDvnm", "reprPrfsEnoNm", 
            "timtSmryCn", "point"]
for data in json_data:
    for key in list(data.keys()):
        if key in listToSave:
            continue
        data.pop(key)

# 수정된 json 파일 저장 경로 입력
with open('C:\\Users\\aaa\\Desktop\\TimetableData\\' + filename + '_수정완료.json', 'w', encoding='utf-8') as make_file:
    json.dump(json_data, make_file, indent="\t", ensure_ascii=False)
    
print(json.dumps(json_data,indent='\t' ,ensure_ascii=False))
