# キーを使って、ディクショナリの要素wを特定
# 繰り返しfor文＋ディクショナリ

pp={"山田":45, "佐藤":67, "田中":38, "木村":87, "鈴木":56, "村田":78, "山下":91, "小島":45}

print("１回目>>>全要素をまとめて表示：")
print("pp=",pp)
print("要素を個別に表示：")
print("山田の点数=",pp["山田"])
print("田中の点数=",pp.get("田中"))
print("全要素の数=",len(pp))
print("要素の作成と修正：")
pp["木村"] = 88
pp["池田"] = 80
print("２回目>>>全要素をまとめて表示：")
print("pp=",pp)
