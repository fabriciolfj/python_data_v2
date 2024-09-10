import pandas as pd
s = pd.Series(['a', 'b', 'c', 'd'] * 2)


cat_s = s.astype('category')
print(cat_s.cat.codes)
print("================")
#add novas categorias
actual_categories = ['a', 'b', 'c', 'd', 'e']

cat_s2 = cat_s.cat.set_categories(actual_categories)
print(cat_s2)
##removendo categoriAS SEM USO

cat_s3 = cat_s[cat_s.isin(['a', 'b'])]
print("=============antes de remover")
print(cat_s3)
cat_s3 = cat_s3.cat.remove_unused_categories()
print("=============apos remover")
print(cat_s3)