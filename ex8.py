formatter = "%r %r %r %r"
print(formatter)
print(formatter%("one","two","three","four"))
print(formatter%(True, False, False, True))
print(formatter%(formatter,formatter,formatter,formatter))
print(formatter%(
      "I had this thing.", "That you could type up right."
                 ,"But it didn't sing.",
                 "So I said goodnight."))
#有雙引號是因為內容裡有單引號 為了不搞混所以用雙引號 若內容沒有單引號，則顯示單引號
