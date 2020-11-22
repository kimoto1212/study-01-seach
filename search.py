import csv
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
        
    with open('new.csv', 'w') as file:    #既存でないファイル名を作成してください
        w = csv.writer(file)
        w.writerow(["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"])
        if word in source:
            print("{}が見つかりした".format(word))
        else:
            source.append(word)
            print("{}を追加しました".format(word))
            print(source)
            w.writerow([word])
            
    
    file.close()
    

if __name__ == "__main__":
    search()
