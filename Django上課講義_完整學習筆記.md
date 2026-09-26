# Django 上課講義完整學習筆記

> **已整合「Django上課講義」資料夾內全部七份PDF，共437頁。**
> 第一批主講義286頁保留；本次新增其餘六份151頁的文字、圖表與操作截圖知識，仍為同一份md。這是逐頁閱讀整理完成，不代表全部程式／安裝流程均已執行驗證。

## 如何閱讀這份筆記

1. 按原 PDF 頁序整理，主講義每頁都有 Pxxx 小節；其餘依檔案採 ENV-Pxxx、PS-Pxxx、WEB-Pxxx、API-Pxxx、DB-Pxxx、AI-Pxxx，可用搜尋找到與上課進度相同的位置；每節亦提供回原 PDF 的頁碼連結（是否直接跳頁取決於你的閱讀器）。
2. **這不是只有重點的摘要。**保留概念、參數表、操作步驟、主要範例、圖片流程、畫面結果及跨頁接續關係；相同畫面中重複的既有程式不無限重貼，但新增或不同內容各自記錄。
3. `講義／原稿／圖示結果` 表示來源內容；`補充／校正／疑點` 是整理時另外提出的辨析；`實測` 只用於確實執行過且附有結果的項目。
4. 原檔雖名「最新版」，實際混用 Python 2／3、不同年份的 Django、Linux/Windows 操作。**原稿範例不保證可原封不動放在同一套現代環境執行。** 舊語法與疑點不會默默改成原稿本來就正確。
5. 圖片已按頁檢視，不是只靠 OCR。程式碼、流程、欄位、操作結果已轉成可搜尋文字；模糊或原圖缺失的部分明列限制，不猜補。頁面截圖未大量內嵌，避免單一 md 依賴數百張附檔；原圖仍可從原 PDF 核對。
6. 本筆記是課堂知識整理，**不是你的 Django 作業專案修改指示**。教材的專案名、IP、port、帳密屬示範值，不代表你電腦的實際設定。沒有修改你的 Django 專案、MySQL 資料或系統安全設定。
7. 為避免整理时省略原句、參考網址或跨頁片段，末尾保留逐頁「原始文字層對照」。它是檢索／核對附件，不是已修好的可執行程式碼；圖片獨有內容以正文與原 PDF 為準。

## 講義範圍與整合進度

資料來源資料夾：`C:\hermes\學習筆記md檔案\Django上課講義`。上層另有 `pei_note` 筆記庫，**不屬於本次七份PDF講義的整理範圍**。

| 檔案 | 頁數 | 含圖片頁數 | 圖片物件出現次數 | 狀態 |
|---|---:|---:|---:|---|
| 20260907AI應用(20260915).pdf | 76 | 65 | 145 | 已完成逐頁整理及併入 |
| Django平台建置(windows) by venv(P).pdf | 17 | 17 | 212 | 已完成逐頁整理及併入 |
| PowerShell更改執行原則.pdf | 1 | 1 | 1 | 已完成逐頁整理及併入 |
| Python and Django(最新版)P.pdf | 286 | 242 | 687 | 已完成逐頁整理及併入 |
| api.pdf | 3 | 0 | 0 | 已完成逐頁整理及併入 |
| 網頁語言簡介P.pdf | 1 | 0 | 0 | 已完成逐頁整理及併入 |
| 資料庫正規化.pdf | 53 | 53 | 513 | 已完成逐頁整理及併入 |

圖片物件次數含同一圖片重複、圖示或截圖拆分，不是獨立教學截圖張數。頁數／圖像計數由 PDF 程式盤點；是否理解圖中知識則由逐頁閱讀與紀錄確認，兩者不是同一件事。

## 主題導航

### 其餘六份講義導航（已併入）

- [ENV：Windows venv／Django建置，17頁](#env-p001)
- [PS：PowerShell執行原則，1頁](#ps-p001)
- [WEB：前端、後端、資料庫與Web Server，1頁](#web-p001)
- [API：HTTP／JSON、PC／Pi／Android資料流，3頁](#api-p001)
- [DB：資料庫正規化、功能相依與正規形式，53頁](#db-p001)
- [AI：機器學習、線性迴歸、KNN與Django整合，76頁](#ai-p001)

同一概念在不同檔案重複出現時，保留各自的版本與案例，避免合併去重時把老師的操作差異一併刪掉。可先讀WEB/API建立整體架構，再配合ENV/PS建環境、主講義學Django、DB學設計、AI學模型與網站整合。此閱讀順序為整理者建議，不是老師另訂的作業要求。

### 主講義導航

- [P001–P040：Python 入門、資料型別、運算、流程控制、函式與模組](#p001)
- [P041–P070：作用域、參數、裝飾器、物件導向、套件、例外、執行緒、JSON](#p041)
- [P071–P111：Django 概念、Windows/Linux 建置、VS Code、專案與 app](#p071)
- [P112–P145：MVC/MVT、URL、view、static、template、GET/POST](#p112)
- [P146–P183：MariaDB/MySQL、模型欄位、migrations、原生 SQL CRUD](#p146)
- [P184–P205：ORM、資料庫比較與 ORM CRUD](#p184)
- [P206–P237：SQL/ORM 對照、查詢、聚合、修改、JOIN](#p206)
- [P238–P262：模型關聯、一對一／一對多／多對多、Cookie/Session](#p238)
- [P263–P286：Session、Auth、登入／登出、會員註冊](#p263)

---

## 第一部分：Python 基礎、資料結構與流程控制（P001–P040）

本部分來源：`Python and Django(最新版)P.pdf`，授課教師葉呈祥。頁碼採 PDF 實際頁序，亦與頁尾印刷數字一致。下面將課本概念與圖片知識轉為文字，不把「圖片已附上」當作已整理。標為「補充／校正」的內容不是原稿原句。

<a id="p001"></a>

### P001｜目錄：Python 入門知識路線

[核對原講義第 1 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=1)

- 第一章自 P005 起：交互式編程、脚本、中文編碼、保留字、縮排、多行語句、引號、註解、空行、程式區塊。
- 變數與資料類型、型別轉換、`print()`、字串、串列、元組與字典，接著學習比較、賦值、位元運算與優先順序。
- P031 起為條件與迴圈：`if`、成員測試、`for`、`break`、`continue`、迴圈 `else`、`while`；P039 函式，P040 模組，P042 補充作用域等。
- 圖面核對：本頁是完整文字目錄，沒有另外藏在插圖裡的範例。

<a id="p002"></a>

### P002｜目錄：進階 Python 與 Django 基礎

[核對原講義第 2 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=2)

- P042–P049：`*args`、`**kwargs`、`dir()`、`with ... as`、`help()`、裝飾器。
- P050–P070：物件導向、`__init__`、封裝、繼承、覆寫、`classmethod()`、套件、例外、多執行緒、JSON。
- P071 起原標題為「第三章：Python Web Djangle」；後續内容實際講 Django。原稿沒有在此插入第二章，勿為了補齊編號而杜撰內容。
- Django 依序為 Windows 安裝、VS Code、複製專案、Linux 與遠端開發、建立 project/application、view/URL、static、網址參數、template。
- 原稿同時有兩個「1.6」與多個「3-1」，這是原稿編號方式，不代表筆記遺漏。

<a id="p003"></a>

### P003｜目錄：模板、表單、資料庫與關聯

[核對原講義第 3 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=3)

- P124 模板變量；P126 標籤；P132 GET/POST。
- P146 MariaDB/MySQL 安裝、密碼、遠端連線、Workbench、mysqlclient、Django 欄位型別與選項。
- P163 原生 SQL CRUD；P184 ORM CRUD；P206 ORM 與 SQL 對照，含建立資料表、查詢、聚合、新增更新刪除、JOIN。
- P238 一對一、一對多、多對多；P252 JOIN 更新／刪除；P253 Cookie/Session。
- 圖面可確認目錄的兩組更新條目都印「使用 GET」；是否實作 POST 需依各正文，不以目錄文字判斷。

<a id="p004"></a>

### P004｜目錄：Cookie、Session 與使用者管理

[核對原講義第 4 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=4)

- P253 Cookie 概念、P254 Session 概念與 Cookie 操作、P262 Session 操作。
- P271 使用者管理、讀取 Django auth 使用者；P272 `HttpRequest.user`；P275 登入登出；P279 會員註冊登入小專案。
- 本頁下半大幅留白是目錄結束，不是文字擷取遺漏。

<a id="p005"></a>

### P005｜Python 的定位與互動式操作

[核對原講義第 5 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=5)

講義介紹 Python 由 Guido van Rossum 於 1989 年耶誕假期開始開發，強調易學易讀、跨平台、模組豐富，應用包含網頁、系統管理與 Raspberry Pi 硬體控制，並可與 C、C++、Java 等技術整合。這是講義的背景介紹，並非本次另行考據的歷史研究。

互動式編程是進入 Python 直譯器後直接輸入程式，不必先儲存 `.py`。講義的 Linux 安裝指令為：

```sh
apt-get install python python3
```

補充：這是原稿時代的套件命名，不能保證適用所有 Linux 發行版；本次只讀講義，沒有對你的電腦執行安裝。

講義所列延伸資源（保留原連結，不表示本次已逐站閱讀）：
- https://www.python.org/
- http://www.w3big.com/zh-TW/python3/default.html
- http://www.w3big.com/
- https://www.w3schools.com/python/
- https://www.tutorialspoint.com/index.htm
- http://www.w3big.com/python/default.html
- http://www.runoob.com/

<a id="p006"></a>

### P006｜互動式與腳本的兩種執行方式

[核對原講義第 6 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=6)

原稿分別以 `python`、`python3` 進入互動模式，再呼叫 `print("Hello Python")`，以 `exit()` 離開。`exit()` 應在 Python 互動提示符下輸入；原稿用 shell 提示字元排版，不要把提示字元本身當指令。

腳本方式：用文字編輯器建立 `hello.py`，將程式儲存，再交给直譯器：

```sh
nano hello.py
python hello.py
python3 hello.py
```

`hello.py` 的內容：

```python
print("Hello,Python!")
```

另一種 Linux 方式先查直譯器：`which python`，再把 `#!/usr/bin/python` 放在檔案第一行，讓作業系統知道直接執行此檔時要叫誰。此絕對路徑必須真的存在。原段落提到 `test.py`，實際指令用 `hello.py`，筆記保留這個差異。

<a id="p007"></a>

### P007｜可執行腳本、中文編碼與保留字

[核對原講義第 7 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=7)

- `chmod +x hello.py`：為檔案加入執行權限；`./hello.py`：執行目前目錄的檔案，搭配上一頁 shebang。
- 圖中實際錯誤為 `SyntaxError: Non-ASCII character ... but no encoding declared`，講義用它說明含中文字而未宣告原始碼編碼的舊版 Python 問題。
- 原稿處理方式（範例 `basic-01.py`）：

```python
#!/usr/bin/python
#coding=utf-8
print("Hello,Python!")
print("您好")
```

補充／版本校正：Python 3 原始碼預設 UTF-8，不能把「中文一定要加 coding 宣告，否則報錯」視為普遍規則。實際檔案編碼與宣告仍應一致。

保留字是語言已有特殊意義的名稱，不能直接拿來當一般變數或函式名稱。原稿稱所有關鍵字都是小寫，是舊資料；Python 3 的 `True`、`False`、`None` 都不是全小寫。下一頁表格亦屬舊版表。

<a id="p008"></a>

### P008｜關鍵字表與缩排

[核對原講義第 8 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=8)

圖片中的舊版保留字表逐項如下：`and`、`assert`、`break`、`class`、`continue`、`def`、`del`、`elif`、`else`、`except`；`exec`、`finally`、`for`、`from`、`global`、`if`、`import`、`in`、`is`、`lambda`；`not`、`or`、`pass`、`print`、`raise`、`return`、`try`、`while`、`with`、`yield`。

補充：Python 3 中 `print`、`exec` 是內建函式，不是這張舊表所稱的關鍵字；完整清單應由所用 Python 的 `keyword.kwlist` 檢視。

Python 使用縮排劃分區塊，不以 `{}` 當作 `if` 或函式的區塊邊界。同一區塊的各行要在同一縮排層級；不同巢狀層次才再往右。圖片範例用 Python 2 的 `print "True"`／`print "False"`：

```python
# 依圖片概念轉為 Python 3；不是原圖逐字程式
if True:
    print("True")
else:
    print("False")
```

補充：不同分支在語法上不必恰巧使用相同寬度，但學習及維護上應統一每層四個空格，避免 tab/空格混用。

<a id="p009"></a>

### P009｜縮排錯誤與多行語句

[核對原講義第 9 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=9)

- 圖中的錯誤程式頂層 `if True:` 前多了縮排，執行顯示 `IndentationError: unexpected indent`。另一種錯誤訊息是 `IndentationError: unindent does not match any outer indentation level`，表示退回的層級對不上。
- 不可把兩種訊息一律解讀成「必然混用 tab」：不合法的額外縮排、退格對不齊也會發生。圖片的 `else` 分支中 `print "False"` 亦未對齊。
- 一個敘述可以使用行尾反斜線 `\` 延續到下一行：

```python
total = item_one + \
        item_two + \
        item_three
```

- 在未閉合的 `[]`、`{}`、`()` 內可以自然換行，不需要反斜線。補充：通常以括號換行較容易維護；反斜線後不能再放一般文字或註解。

<a id="p010"></a>

### P010｜括號續行、字串引號及單行註解

[核對原講義第 10 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=10)

圖片承接上頁的例子：

```python
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
word = 'word'
sentence = "這是一個句子。"
paragraph = """這是一個段落。
包含了多個語句"""
```

- 單引號、雙引號都能界定字串，前後必須成對；三個單引號或三個雙引號能表達跨行字串。
- `#` 開始單行註解，能獨占一行或放在敘述後。圖片示範首行 shebang、次行編碼宣告、檔名註解，以及 `print "Hello, Python!"; # 第二個註解`。
- 補充：中文彎引號 `“ ”`、`‘ ’` 是排版字符，不是 Python 程式的引號；轉錄可執行版時要明確轉成 ASCII 引號。

<a id="p011"></a>

### P011｜註解與空行的用途

[核對原講義第 11 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=11)

- 上頁範例的圖片輸出是 `Hello, Python!`，註解本身不輸出。
- 行尾註解範例：`name = "Madisetti" # 這是一個註釋`。
- 圖片分別用 `'''...'''` 與 `"""..."""` 包住多行說明，原稿稱為多行註解。
- 補充／校正：三引號本質是字串；放在模組、函式或類別的首個敘述位置可形成 docstring，不等同於 `#` 註解。
- 空行用來分開不同功能、函式或類別區段，提高閱讀、維護及重構的可讀性；不像縮排，空行通常不改變腳本的區塊歸屬。

<a id="p012"></a>

### P012｜程式區塊、基礎型別與 NumPy

[核對原講義第 12 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=12)

`if`、`while`、`def`、`class` 等複合敘述的標頭以冒號結束，後面縮排的語句群為區塊（原稿稱代碼組／suite）；標頭與區塊合稱子句。圖片的結構是：

```text
if expression:
    suite
elif expression:
    suite
else:
    suite
```

講義先以五類建立入門分類：Numbers、String、List、Tuple、Dictionary。這是教學分類，不是 Python 型別的完整清單，還有布林、集合等。

NumPy 補充逐項：
1. 高效率的多維陣列運算。
2. 整合 C/C++ 與 Fortran 程式。
3. 支援線性代數與傅立葉轉換。
4. 可在適當數值運算情境以 NumPy Array 取代 list。
5. 可描述資料型態，使資料交換與其他資料系統整合較方便。

補充／校正：原稿「Python 本身無陣列類型」說法過廣；Python 標準函式庫有 `array` 模組，NumPy 的重點在多維數值陣列及運算，不是 Python 完全無法使用陣列。型別屬於物件，變數名称是與物件的綁定，不應把變數想成宣告後永遠固定型別的盒子。

<a id="p013"></a>

### P013｜ndarray、賦值與多重賦值

[核對原講義第 13 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=13)

- NumPy 的核心 `ndarray` 是 N 維陣列；`shape` 描述每個軸的長度，`dtype` 描述元素型別。講義將一維稱向量、二維稱矩陣。
- `=` 左方是要綁定的變數名，右方是運算出的值／物件。使用前需要先建立名稱。
- `basic-02.py` 的值為：

```python
counter = 100
miles = 1000.0
name = "John"
# 原稿使用 Python 2: print counter / print miles / print name
print(counter)
print(miles)
print(name)
```

- `a = b = c = 1` 是連鎖賦值，各名稱綁定到同一個右側結果。
- 補充：不可因這個數值例子就認為可變物件會被複製；連鎖賦值给 list 仍可能共用同一個 list。

<a id="p014"></a>

### P014｜解包賦值、數值不可變與 del

[核對原講義第 14 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=14)

- `a, b, c = 1, 2, "tony"` 將右邊各項依位置分別綁到左邊名稱。
- 数值不可變：名稱重新綁定到不同值，不代表原數字物件被原地改寫。
- 圖片以 `var1 = 1`、`var2 = 10` 示範建立數值綁定；`del var` 或 `del var_a, var_b` 移除名稱的綁定。這不是保證立即清空整個物件的記憶體；是否仍有其他引用是另一回事。
- 原圖列出 `int`、`long`、`float`、`complex`。其中獨立的 `long` 型別屬 Python 2；Python 3 整數統一為 `int`。

<a id="p015"></a>

### P015｜數值表示法與轉型表（前半）

[核對原講義第 15 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=15)

圖片表格展示正負整數、舊式八進位／十六進位、`L` 結尾的長整數、科學記號浮點數與 `j` 虛部：例如 `10`、`100`、`-786`、`0x69`、`51924361L`、`15.20`、`-21.9`、`32.3e+18`、`3.14j`、`45.j`、`9.322e-36j`。複數概念為 `a + bj` 或 `complex(a, b)`。

補充／校正：此表混有舊版語法和有疑問的數字（如 `080`、`-0490`）。Python 3 不接受整數尾綴 `L`，八進位應使用 `0o`；不能直接複製整張表當成 Python 3 合法常值集。

| 原圖項目 | 意義與使用界線 |
|---|---|
| `int(x[, base])` | 轉整數；字串可指定進位 |
| `long(x[, base])` | Python 2 的長整數轉型，Python 3 用 `int` |
| `float(x)` | 轉浮點數 |
| `complex(real[, imag])` | 建立複數 |
| `str(x)` | 可讀字串形式 |
| `repr(x)` | 便於除錯、辨識內容的表示字串；不保證任意物件都可還原 |
| `eval(str)` | 將字串當 Python 表達式求值，不是一般安全的字串轉型 |
| `tuple(s)` | 將可迭代資料建成元組 |

安全補充：不可對不可信輸入使用 `eval()`；它能執行程式碼。

<a id="p016"></a>

### P016｜轉型表（後半）與 int 範例

[核對原講義第 16 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=16)

| 原圖項目 | 意義與版本注意 |
|---|---|
| `list(s)` | 建立串列 |
| `set(s)` | 建立可變集合，元素需可雜湊 |
| `dict(d)` | 建立字典；圖以 `(key, value)` 配對序列示範，亦可由映射建立 |
| `frozenset(s)` | 建立不可變集合 |
| `chr(x)` | 整數碼位轉字元（Python 3） |
| `unichr(x)` | Python 2 的 Unicode 字元函式，Python 3 使用 `chr` |
| `ord(x)` | 一個字元轉整數碼位 |
| `hex(x)` | 整數轉十六進位字串 |
| `oct(x)` | 整數轉八進位字串 |

原稿案例：`int("124")` 成功；`int(123.45)` 截掉小數部分；`int("-123.45")` 失敗，因為它不是整數格式字串。`int()` 對浮點數是朝零截斷，不是四捨五入。本頁末段接 `float("124")`，下一頁繼續。

原稿採 `print "aa = ", aa` 舊式輸出。以下列為 Python 3 改寫，不假裝是原稿逐字碼：

```python
aa = int("124")
bb = int(123.45)
print("aa = ", aa)
print("bb = ", bb)
# 以下故意錯誤，應單獨測试，否則程式在此中斷：
# cc = int("-123.45")
```

<a id="p017"></a>

### P017｜float、str 與錯誤的種類

[核對原講義第 17 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=17)

原稿逐例：

```python
# 將原稿的 print 語法改為 Python 3；數值與轉型保留
aa = float("124")
bb = float("123.45")
cc = float(-123.6)
print(aa, bb, cc)
aa = str(123.4)
cc = str("-123.45")
print(aa)
print(cc)
```

- `float()` 可以解析包含小數點的數字字串；原稿輸出依序為 `124.0`、`123.45`、`-123.6`。
- `str(123.4)` 得到字串，而不是浮點數。原稿註記用引號標示字串型別，但 `print()` 本身不會為一般字串額外輸出引號。
- 原稿故意錯誤 `bb = str(-124.a)` 是語法錯誤，不是 `str()` 運算時的轉型錯誤。若它與其他程式放在同一份腳本，整份檔案解析就會失敗，不會先成功跑到前幾行。

<a id="p018"></a>

### P018｜print 的 sep/end 與三種字串格式化

[核對原講義第 18 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=18)

```python
print(str1 + " " + str2)
print(str1, str2, sep="", end="\n")
print(str1, str2, sep="&", end="")
```

`sep` 是多個引數之間的分隔字元，`end` 是整次輸出結尾；前面的 `+` 是先做字串串接，與 `sep` 不同。

講義 `%` 格式化完整組合（使用 `math.pi` 前需補 `import math`）：

```python
import math
print("the length of (%s) is %d" % ("Hello World", len("Hello World")))
print("PI = %f" % math.pi)
print("PI = %10.3f" % math.pi)
print("PI = %6d" % int(math.pi))
print("%4s %4d %4d" % ("王大明", 10, 100))
```

- `%s` 字串、`%d` 十進位整數、`%f` 浮點數。
- `%10.3f`：最小欄寬 10、小數點後 3 位；`%6d`：整數最小欄寬 6。寬度不是截斷規則。

```python
name = "林小明"
score = 80
print("{}的成績為{}".format(name, score))
text = 'world'
print(f'Hello, {text}')
```

原稿範例名 `basic-03.py`。補充／校正：原稿稱 `format()` 是 Python 3 後新增不夠精確；Python 2.6 已有 `str.format()`。f-string 自 Python 3.6 起可用。

字串下標從左 `0` 起、從右 `-1` 起；`s[start:stop]` 切片含起點不含終點，缺起點／終點可表示頭／尾；`+` 串接，`*` 重複。原稿「字串用 [] 標識」不精確：字串常值用引號，方括號用來索引或切片。

<a id="p019"></a>

### P019｜字串範例及串列建立

[核對原講義第 19 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=19)

圖片額外例子：`var1 = 'Hello World!'`、`var2 = 'Python w3big'`，讀取 `var1[0]` 及 `var2[1:5]`。

原稿 `basic-04.py` 使用變數名 `str`。為保留課堂對照，下面仍用原名，但這會遮蔽同名內建函式：

```python
# Python 3 輸出版；原稿為 print str 等 Python 2 語法
str = 'Hello World!'
print(str)
print(str[0])
print(str[2:5])
print(str[2:])
print(str * 2)
print(str + "TEST")
```

串列 `list` 是有序、可修改的序列，用 `[]` 包住逗號分隔的元素，可混合不同型別；下標也從 0 起。圖片的三個例子：

```python
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
```

序列常用操作有索引、切片、連接、重複、成員測試、長度與最大／最小值。補充：不是所有不同型別元素都能彼此比較大小；不要把「list 可混合型別」誤解為「任何混合 list 都能排序」。

<a id="p020"></a>

### P020｜讀取、更新、追加與刪除 list

[核對原講義第 20 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=20)

```python
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]
print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])
list2[2] = 20
print(list2[2])
```

以上是原稿轉 Python 3 並修正名稱的版本。原稿更新後寫的是 `print list[2];`，而不是 `print list2[2];`，不能照抄後以為印的是修改的串列。

- `list2[2] = 20` 原地修改第三個元素。
- `append(obj)` 在串列尾端加入一個元素。
- `del list2[2]` 刪除第三個位置；删除範例跨到下一頁。
- 原稿每行末尾分號是可省略的，不是 Python 一般換行必須的符號。

<a id="p021"></a>

### P021｜list 刪除、運算、成員與負下標

[核對原講義第 21 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=21)

刪除示範重新建立 `list2 = [1, 2, 3, 4, 5, 6, 7]`，然後 `del list2[2]` 再列印；不要把它誤讀成續接上一頁已修改的同一份執行狀態。

图片的運算表逐項：

| 表達式 | 原圖結果 | 意義 |
|---|---|---|
| `len([1, 2, 3])` | `3` | 元素數 |
| `[1, 2, 3] + [4, 5, 6]` | `[1, 2, 3, 4, 5, 6]` | 串接 |
| `['Hi!'] * 4` | `['Hi!', 'Hi!', 'Hi!', 'Hi!']` | 重複 |
| `3 in [1, 2, 3]` | `True` | 成員測試 |
| `for x in [1, 2, 3]: print x,` | `1 2 3` | 舊式逐項輸出 |

圖片設定 `L = ['Google', 'Runoob', 'Taobao']`：`L[2]` 是 `'Taobao'`、`L[-2]` 是 `'Runoob'`、`L[1:]` 是 `['Runoob', 'Taobao']`。

<a id="p022"></a>

### P022｜圖片中的全部 list 函式與方法

[核對原講義第 22 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=22)

本頁幾乎全是圖片；單讀 PDF 文字層只會得到頁碼，不能略過。

| 函式 | 用途／校正 |
|---|---|
| `cmp(list1, list2)` | 原圖舊式比較，Python 3 已無此內建函式 |
| `len(list)` | 元素數 |
| `max(list)` | 最大元素 |
| `min(list)` | 最小元素 |
| `list(seq)` | 可迭代資料轉串列（原圖以 tuple 為例） |

| 方法 | 用途／校正 |
|---|---|
| `append(obj)` | 尾端加「一個」物件 |
| `count(obj)` | 計算相等元素出現次數 |
| `extend(seq)` | 將另一可迭代物件的元素逐一加到尾端 |
| `index(obj)` | 第一個相符元素的下標；找不到時拋例外 |
| `insert(index, obj)` | 指定位置插入 |
| `pop([index])` | 按下標移除並回傳元素，省略時為最後一項 |
| `remove(obj)` | 移除第一個相等的值，不是按下標 |
| `reverse()` | 原地反轉 |
| `sort(...)` | 原地排序 |

原圖 `pop(obj=list[-1])` 易誤導：`pop` 引數是位置，不是元素值；原圖 `sort([func])` 是舊版接口描述。Python 3 常用 `sort(key=..., reverse=...)`。`append`／`extend` 的差異以及 `pop`／`remove` 的差異不可省略。

<a id="p023"></a>

### P023｜tuple：不可變序列與 list 對照

[核對原講義第 23 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=23)

圖中建立方式包含 `('physics', 'chemistry', 1997, 2000)`、`(1, 2, 3, 4, 5)` 及省略括號的 `"a", "b", "c", "d"`。

圖中紅框對照（原名）：

```python
tuple = ('abcd', 786, 2.23, 'john', 70.2)
list = ['abcd', 786, 2.23, 'john', 70.2]
# tuple[2] = 1000  # 不允許替換元組的元素
list[2] = 1000     # 允許替換串列元素
```

原稿另外定義 `tinytuple = (123, 'john')`，輸出整個 `tuple`、`tuple[0]`、`tuple[1:3]`、`tuple[2:]`，再於下一頁展示重複／相加。

補充：tuple 不可原地替換其元素，不代表變數不能重新賦值；元組若內含可變物件，那個物件自身仍可能改變。一般程式應避免用 `tuple`、`list` 當變數名以免遮蔽內建類型。

<a id="p024"></a>

### P024｜tuple 連接／del 與 dict 結構

[核對原講義第 24 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=24)

- `tinytuple * 2` 重複元組內容；`tuple + tinytuple` 產生連接的元組，不是修改原 tuple。
- 原稿 `basic-06.py` 接著寫 `del tup`、`print tup`，但前面定義名稱是 `tuple`，不是 `tup`。名稱不一致是教材問題；即便先定義 `tup`，刪除後再次存取亦會因名稱不存在而出錯。

字典是 key → value 映射，以鍵存取，不是像 list 依第幾個位置。圖片强调「鍵要唯一，值不必唯一」，語法 `{key1: value1, key2: value2}`。

```python
# 保留原稿命名；dict 會遮蔽內建名稱
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
```

原稿稱字典「無序」是舊式描述。補充／版本校正：Python 3.7 起語言規格保證插入順序，但讀取仍用鍵，不是把數字鍵當位置下標。鍵不僅限字串或數字，但必須可雜湊。

<a id="p025"></a>

### P025｜字典讀取、更新、刪除與內建函式

[核對原講義第 25 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=25)

`basic-07.py` 承接上一頁，用 `dict['one']`、`dict[2]` 讀取兩個鍵；`tinydict` 列印整份資料；`tinydict.keys()`／`values()` 取得鍵／值。

```python
# Python 3 版，修正原稿排版彎引號
tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
print(tinydict.keys())
print(tinydict.values())
tinydict['name'] = "marry"
print(tinydict['name'])
del tinydict['name']
# print(tinydict['name'])  # 原稿下一行：刪除後再讀會 KeyError
```

原稿兩次在單鍵讀取後寫「輸出所有值」，註解不正確；該表達式只讀指定鍵。`'Name'` 與 `'name'` 不相同，原稿刪除註解的大小寫亦不一致。

圖片函式表完整內容：`cmp(dict1, dict2)` 舊式比較、`len(dict)` 鍵數、`str(dict)` 可列印表示字串、`type(variable)` 物件型別。Python 3 沒有內建 `cmp`。

<a id="p026"></a>

### P026｜字典方法逐項表與 get

[核對原講義第 26 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=26)

| 原圖方法 | 用途與必要版本校正 |
|---|---|
| `clear()` | 清空原字典所有項目 |
| `copy()` | 淺複製；巢狀可變物件可能仍共用 |
| `fromkeys(seq[, val])` | 由一組鍵建立字典，各鍵使用同一個預設值物件 |
| `get(key[, default])` | 存在則回值，不存在回 default（預設 `None`） |
| `has_key(key)` | 舊版 API；Python 3 用 `key in d` |
| `items()` | 取得鍵值配對；Python 3 回傳 view，不是原圖所稱 list |
| `keys()` | 所有鍵；Python 3 回傳 view |
| `setdefault(key[, default])` | 不存在時插入預設值，再回傳該鍵值；不同於不插入的 get |
| `update(dict2)` | 將另一組鍵值更新進原字典，同鍵被覆蓋 |
| `values()` | 所有值；Python 3 回傳 view |
| `pop(key[, default])` | 移除指定鍵並回傳值；不存在且未給 default 則 KeyError |
| `popitem()` | 移除並回傳一個鍵值配對；Python 3.7+ 為後進先出，非原圖的「隨機」 |

原圖把 `dict.get(key, default=None)` 當接口說明，不代表所有內建方法都接受相同形式的關鍵字引數；課堂例子用位置引數。

例子 `list_test = {'a': 1, 'b': 2}` 是字典，名稱雖然含 list 不改變型別。`list_test.get('a')` 得到 `1`。

<a id="p027"></a>

### P027｜get 與下標遇到缺鍵的不同

[核對原講義第 27 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=27)

承接同一個 `list_test`：

| 表達式 | 講義結果與校正 |
|---|---|
| `list_test.get('c')` | `None`；原稿印小寫 none，但程式常值是大寫 N |
| `list_test.get('c', 3)` | 預設值 `3`，不因此插入 `c` |
| `list_test['b']` | `2` |
| `list_test['c']` | 拋 `KeyError`，不是回傳一個代表錯誤的普通值 |

原稿延伸連結：https://www.tutorialspoint.com/python/python_dictionary.htm 。

<a id="p028"></a>

### P028｜算術與比較運算子

[核對原講義第 28 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=28)

算術表設定 `a = 10`、`b = 20`，包含：
- `+` 加法、`-` 減法、`*` 乘法（亦可重複序列）。
- `/` 除法、`%` 餘數、`**` 次方、`//` 向下取整除法。
- 原圖的案例包括 `a + b`、`a - b`、`a * b`、`b / a`、`b % a`、`a ** b`、`9 // 2` 與 `9.0 // 2.0`。Python 3 的 `/` 真除法結果為浮點，不能照舊表認為兩整數相除一定得到 int。
- 補充：`//` 是向負無窮方向取整，不是一般的「直接砍小數」，負數時和 `int()` 對浮點數的截斷不同。

比較表包括 `==`、`!=`、`<>`、`>`、`<`、`>=`、`<=`；`<>` 是舊式不等於，Python 3 應用 `!=`。結果為 `True`／`False`，有大小寫。`=` 賦值不可與 `==` 相等比較混用。範例檔 `basic-08.py`。

<a id="p029"></a>

### P029｜增強賦值及位元運算

[核對原講義第 29 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=29)

增強賦值表：`=`、`+=`、`-=`、`*=`、`/=`、`%=`、`**=`、`//=`。原稿以 `c += a` 解釋成 `c = c + a`，其他運算同樣概念。

補充：對 list 等可變物件，增強賦值可能原地修改，不能認為兩種寫法在所有物件、所有別名情境下完全等價。

位元運算逐項：
- `&` 每一位都為 1 才為 1。
- `|` 每一位只要任一為 1 就為 1。
- `^` 每一位不同才為 1。
- `~` 位元反相。
- `<<` 左移、`>>` 右移。

原圖展示的結果為 `a & b = 12`、`a | b = 61`、`a ^ b = 49`、`~a = -61`、`a << 2 = 240`、`a >> 2 = 15`。注意：此組結果不是頁頂 `a=10,b=20` 得出的；該組對應的例子應採 `a=60,b=13`，已列入本筆記的隔離驗算。原圖示意 `~a` 為有限八位二進位，Python int 並沒有固定八位元寬度。

<a id="p030"></a>

### P030｜運算優先順序：保留原表並標示問題

[核對原講義第 30 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=30)

原圖從上到下列：`**`；`~ + -`（一元）；`* / % //`；`+ -`；`>> <<`；`&`；`^ |`；`<= < > >=`；`<> == !=`；各種賦值；`is/is not`；`in/not in`；`not/or/and`。

這張表不能直接背成 Python 3 的正確完整優先表：它把 `^` 與 `|` 合併、把比較與身份／成員分開，還把一般賦值混進表達式順位。此處明確保留原稿知識範圍，但校正其分組。

供本課範圍使用的正確簡化次序（高到低；不是全部 Python 語法的完整表）：
1. 括號控制的子表達式、呼叫與索引。
2. `**` 次方（與一元運算左右位置有細節）。
3. 一元 `+x`、`-x`、`~x`。
4. `* / // %`。
5. `+ -`。
6. `<< >>`。
7. `&`，再 `^`，再 `|`（各自不同層）。
8. 比較、`in/not in`、`is/is not` 同級，可做鏈式比較。
9. `not`，再 `and`，最後 `or`。

`is` 比較是否同一個物件，`==` 比較值相等；`in` 是成員判斷。一般 `=` 是賦值敘述，不是像加法那樣的表達式。遇到混合運算，使用括號表達意圖比猜順位穩妥。

<a id="p031"></a>

### P031｜if/else 與 if/elif/else

[核對原講義第 31 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=31)

`if 條件:` 成立執行其縮排區塊，否則進 `else`。多分支以 `elif` 依序測試，只執行第一個成立分支。

原稿用 `name == 'bill'` 時設 `flag = True`，印 `'Wlecome boss'`（原拼字），否則印 `name`；接著 `if flag:` 印 `name, "is my family!"`，否則印 `"Who are you?"`。

補充／缺少前置資料：該頁沒有先定義 `name`、`flag`。單獨跑時不能憑空已有值；尤其 name 不是 bill 的路徑不會替 flag 賦值。適合練習時先自行設定 `name` 與 `flag = False`，並將舊式 print 改為函式，這些需標示為補全而非原稿已有。

<a id="p032"></a>

### P032｜elif 範例、and/or 區間判斷與單行 if

[核對原講義第 32 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=32)

原稿 Python 3 輸出改寫，保留各分支：

```python
# num 需先給值
if num == 3:
    print('boss')
elif num == 2:
    print('user')
elif num == 1:
    print('worker')
elif num < 0:
    print('error')
else:
    print('roadman')

if num >= 0 and num <= 10:
    print('hello')

if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
    print('hello')
else:
    print('undefine')

var = 100
if var == 100: print("變量 var 的值為100")
print("Good bye!")
```

`and` 要兩個條件皆成立；`or` 任一成立。最後 `Good bye!` 未縮排到 if，屬分支之外。補充：`0 <= num <= 10` 可表達第一個區間；`and`、`or` 具短路行為，實際結果也不必總是 bool。

<a id="p033"></a>

### P033｜in 成員測試、字典分派與 for 結構

[核對原講義第 33 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=33)

圖片 `basic-11-2.py` 的資料 `test_list = [1, 6, 3, 5, 3, 4]`，先用迴圈逐項檢查，後用 `in` 簡化：

```python
test_list = [1, 6, 3, 5, 3, 4]
print("Checking if 4 exists in list ( using loop ) : ")
for i in test_list:
    if i == 4:
        print("Element Exists")
print("Checking if 4 exists in list ( using in ) : ")
if 4 in test_list:
    print("Element Exists")
```

原稿標出 `basic-09.py`、`basic-10.py`、`basic-11.py` 等配套檔名，但本頁沒有把這些外部檔案內容全部展示，不能靠檔名憑空補出。

教材說可用字典模擬 switch/case，例檔 `basic-12.py`；原稿連結 http://wyp8711.blogspot.com/2019/09/python-dict-caseswitch.html 。補充：Python 3.10 起有 `match/case` 結構化模式比對，但它不是直接照搬 C 的 switch，原稿「沒有 switch/case」需放回版本語境理解。

`for iterating_var in sequence:` 每次把下一個元素交给迴圈變數，執行縮排區塊；並非只能遍歷 list。

<a id="p034"></a>

### P034｜遍歷字串、list 與 range

[核對原講義第 34 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=34)

以下依原稿轉為 Python 3：

```python
for letter in 'python':
    print('current letter:', letter)

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
    print('current fruit:', fruit)

for num in range(1, 5):
    print(num)

print("1~10,num=num+2")
for num in range(1, 10, 2):
    print(num)
```

`range(start, stop, step)` 含 start、不含 stop；step 省略為 1。圖中文字「1~10」是顯示訊息，不會把 `range` 的 stop 變成包含。Python 3 的 range 是範圍物件，不是事先建立整個 list。

<a id="p035"></a>

### P035｜負步長 range

[核對原講義第 35 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=35)

```python
# 原稿的 print 語法已改為 Python 3
print("10~1,num=num-2")
for num in range(10, 1, -2):
    print(num)
```

負步長朝下降方向，仍不包含 stop。圖面只有這段續頁及 `basic-13.py`、`basic-14.py` 標籤，其餘留白，不是遺漏圖片。上頁兩個正向 range 與本頁倒數結果，均收在後附隔離驗算中。

<a id="p036"></a>

### P036｜break、continue、迴圈 else

[核對原講義第 36 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=36)

原稿 `basic-15.py` 的關鍵對照：

```python
for i in range(1, 11):
    if i == 6:
        break
    print(i)

for i in range(1, 11):
    if i == 6:
        continue
    print(i)
```

`break` 結束目前這層迴圈；`continue` 跳過本次後續內容，繼續下一次迭代。都不是結束所有程式。

`basic-16.py` 示意 `for ... else`：正常耗盡 iterable 才走 else；若由 `break` 結束，不走 else。`else` 與 `for` 對齊，不是與內部 `if` 對齊。

補充：空的 iterable 也可以進 else；`return`、例外等提前離開整段程式同樣不能保證執行迴圈 else。`while` 則在條件持續成立時重複執行。

<a id="p037"></a>

### P037｜while 計數、無限迴圈與質數範例上半

[核對原講義第 37 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=37)

`basic-17.py`：`count=0`，只要 `count < 9`，輸出 `The count is:` 與 count，再 `count = count + 1`。遞增是令條件最終不成立的關鍵。

`basic-18.py`：`while(True)` 不斷以 `raw_input("Enter a number :")` 接收輸入並印出，沒有 break；後面的 `Good bye!` 不會循正常流程抵達。補充：Python 3 用 `input()`，回傳仍是字串，要數字須另做轉型；不要把範例原封不動執行成無法停止的工作。

質數範例從本頁接到 P038。原稿比較符確認是 `<`，不是 `<=`：

```python
import math
num = int(input('請輸入一個整數？'))
j = 2
while j < math.sqrt(num):
    if num % j == 0:
        print(num, '不是質數')
        break
    j += 1
else:
    print(num, '是質數')
```

<a id="p038"></a>

### P038｜while else 的用途及質數邊界錯誤

[核對原講義第 38 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=38)

圖片為上一頁的完整續段：找到可整除的 j 就印不是質數並 break；while 因條件不成立而結束則由 else 印是質數。此範例適合說明迴圈 else，但不是正確完備的質數判斷器。

補充／校正（已做隔離驗算，完整輸出見驗算附錄）：
- `< sqrt(num)` 不檢查平方根邊界，會把某些完全平方數錯判。
- 沒有排除 `num < 2`。
- 負數使用 `math.sqrt` 有定義域問題。

教學修正版（不是原稿逐字碼）：

```python
def is_prime(num):
    if num < 2:
        return False
    j = 2
    while j * j <= num:
        if num % j == 0:
            return False
        j += 1
    return True
```

使用整數乘法判定邊界，避免以浮點平方根決定整數因數範圍。

<a id="p039"></a>

### P039｜函式、引數、return 與回傳 list

[核對原講義第 39 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=39)

原稿 `basic-19.py` 將可重用工作包進函式：

```python
def multiply(x, y):
    return x * y

def operation(x, y):
    multiply = x * y
    add = x + y
    minus = x - y
    divide = float(x) / float(y)
    return [multiply, add, minus, divide]

num1 = multiply(2, 3)
print("multiply:" + str(num1))
# 原稿下一行為 num=opertion(2,3)，少了 a；以下為修正：
num = operation(2, 3)
print("operation:" + str(num[0]))
print("operation:" + str(num[1]))
print("operation:" + str(num[2]))
print("operation:" + str(num[3]))
```

- `def` 建立函式；`x,y` 是形式參數，呼叫時傳入的數值是實際引數。
- `return` 把結果交回呼叫者；`operation` 回傳一個包含多項結果的 list，再用下標取各項。
- 函式内部的變數 `multiply` 是區域名稱；不要與外層同名函式混為一談。
- 原稿 `opertion` 拼字在未另定義此名稱時會 `NameError`；除數為 0 的情況也沒有防護。不能宣稱所有輸入皆可成功。

<a id="p040"></a>

### P040｜模組與四種 import 寫法

[核對原講義第 40 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=40)

把大型程式分成模組可利於分工與維護。教材要建立 `math_operation.py`，再由其他檔案匯入。模組名通常寫檔名去掉 `.py`，必須可由匯入路徑找到。

1. `basic-20.py` 匯入整個模組，以點號指出函式來源：

```python
import math_operation
num = math_operation.operation(4, 6)
```

2. `basic-21.py` 萬用匯入，不需前綴但可能名稱衝突：

```python
from math_operation import *
num = operation(4, 6)
```

3. `basic-22.py` 只匯入需要的名稱：

```python
from math_operation import operation
num = operation(10, 33)
```

4. `basic-23.py` 為模組取別名：

```python
import math_operation as m
num = m.operation(4, 6)
```

原稿說明中殘留 `hello_module`／`hello`，但實際碼是 `math_operation`／`operation`，應以前後一致的實際程式碼理解。`import *` 並非字面上匯入任意所有内部名稱，其行為也可能受 `__all__` 影響（補充）。


---

## PDF 第 41–70 頁完整知識筆記

> 依 PDF 實際頁碼逐頁整理，並親自檢視每頁影像。原稿混用 Python 2 與 Python 3；程式碼保留原稿語法，現代寫法與疑誤另外標示。標為「預期」的輸出係語義說明，不代表實際執行。

<a id="p041"></a>

### P041｜指定目錄匯入模組的參考文獻

[核對原講義第 41 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=41)

本頁承接前頁，只列參考文獻，沒有新增程式碼或操作圖：

- `http://wiki.alarmchang.com/index.php?title=Python_import_%E6%8C%87%E5%AE%9A%E7%9B%AE%E9%8C%84%E8%A3%A1%E9%9D%A2%E7%9A%84_.py_%E6%AA%94%E6%A1%88`
- 連結主題：Python import 指定目錄裡面的 `.py` 檔案。

<a id="p042"></a>

### P042｜區域／全域變數、type()、不定數量參數

[核對原講義第 42 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=42)

#### 區域與全域變數（來源：P042；basic-24.py、basic-25.py）

圖中第一段：

```python
#!/usr/bin/python
#coding=utf-8

def scope():
    var1 = 1  # 區域變數
    print(var1, var2)
var1 = 10  # 全域變數
var2 = 20  # 全域變數
scope()
print(var1, var2)
```

函式內的 `var1` 是自己的區域名稱，外面的 `var1` 不受影響；函式沒有建立區域 `var2`，讀取外層全域的 `20`。預期兩次列印的值分別為 `1,20` 與 `10,20`；Python 2 的 `print(a,b)` 會印出 tuple 形式，Python 3 則以空白分隔。

第二段：

```python
def scope():
    global var1  # 在函式內使用／重新綁定全域變數
    var1 = 1
    var2 = 2  # 區域變數
    print(var1, var2)
var1 = 10
var2 = 20
scope()
print(var1, var2)
```

此時 `global var1` 讓函式內賦值修改模組層級的 `var1`；`var2` 仍是區域變數。預期值先為 `1,2`，後為 `1,20`。**補充：只讀全域變數不需要 `global`；在函式內重新賦值給全域名稱才需要。**

#### type() 查資料型態（來源：P042）

單一參數的 `type(obj)` 回傳物件的型別。圖為 Raspberry Pi 終端執行 `python`，版本 Python 2.7.13、GCC 6.3.0、linux2；互動範例：

```python
print(type(1))                       # <type 'int'>
print(type('runbbo'))                 # <type 'str'>
print(type([2, 3]))                  # <type 'list'>
print(type({0: "zero", 1: "one"}))  # <type 'dict'>
```

Python 3 的顯示形式改為 `<class 'int'>` 等，不是原圖的 `<type ...>`。

#### *args 引入不定數量參數（來源：P042–P043）

一個星號可收集數量不固定的位置引數，實際例子接 P043。

<a id="p043"></a>

### P043｜*args、**kwargs、dir()

[核對原講義第 43 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=43)

#### 一個星號：tuple 與展開（來源：P043；basic-26.py）

```python
def buy(*price):
    print price

buy(1,2,3,4)
data=("bill",1,"tt")
buy(*data)
```

定義處的 `*price` 將位置引數收成 tuple；第一次的內容為 `(1, 2, 3, 4)`。呼叫處 `*data` 則把 tuple 展開，`price` 收到 `('bill', 1, 'tt')`。`args` 只是常用名稱，範例使用 `price`。原文 `print price` 是 Python 2 語法；Python 3 須改 `print(price)`。

#### 兩個星號：dict 與關鍵字引數（來源：P043；basic-27.py）

```python
def sell(**price):
    print price

sell(apple=10, ball=15, cat=25)
data = {"arg3": 3, "arg2": "two"}
sell(**data)
```

定義處 `**price` 將關鍵字引數收成 dict；第一次包含 `apple:10`、`ball:15`、`cat:25`。呼叫處 `**data` 展開成 `arg3=3, arg2='two'`。Python 2 字典的顯示順序不應當作固定保證；Python 3 的列印語法須更新。

#### dir() 查名稱（來源：P043）

原文：`dir([obj])` 查物件的屬性與方法，不帶參數列出「目前記憶體中的所有物件」。範例 `print(dir())`；圖中互動結果：

```text
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__']
```

**原稿說法需限縮：** `dir()` 無參數列出目前區域作用域的名稱，不是掃描所有記憶體物件；`dir(obj)` 也不保證列出物件所有可能的動態屬性。

<a id="p044"></a>

### P044｜with as：檔案處理與清理工作

[核對原講義第 44 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=44)

有些任務需要事前設置及事後清理，檔案處理即是先開啟取得檔案控制代碼、讀取，再關閉。

原稿未使用 `with` 的版本：

```python
file = open("/tmp/foo.txt")
data = file.read()
file.close()
```

問題是可能忘記關檔；若讀取時發生例外，流程也不會走到 `close()`。原稿較長的例外處理示意如下（`do something` 為佔位文字，不是可執行 Python）：

```text
try:
    f = open('xxx')
except:
    print 'fail to open'
    exit(-1)
try:
    do something
except:
    do something
finally:
    f.close()
```

`finally` 提供離開處理區塊時的清理。原文稱此段「執行良好」，但實際是含佔位文字的示意碼；不可直接複製執行。跨 P044–P045 的簡化版本：

```python
with open("/tmp/foo.txt") as file:
    data = file.read()
```

**補充／釐清：** `with open(...)` 在區塊退出時會關閉檔案，即使區塊拋出例外也會清理；但不會自動把例外吞掉，開檔失敗也仍會拋錯。

<a id="p045"></a>

### P045｜with 的協定、help()、裝飾器概念

[核對原講義第 45 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=45)

#### with 如何運作（來源：P045）

1. 求值 `with` 後面的運算式，取得 context manager。
2. 呼叫其 `__enter__()`，將**此方法的回傳值**指定給 `as` 後面的變數。
3. 執行縮排區塊；離開區塊時呼叫 `__exit__()` 進行清理。

**補充：** `__exit__(exc_type, exc_value, traceback)` 會收到例外資訊；若回傳真值可抑制例外。`__enter__()` 本身未成功完成時，不能假定 `__exit__()` 會被呼叫。

原參考：<https://icodding.blogspot.com/2016/05/python-with-as.html>。

#### help() 查操作說明（來源：P045）

```python
help(__builtins__)
```

`help(obj)` 顯示物件詳細說明。原圖為 Python 2 內建模組 `__builtin__` 的說明：NAME 顯示 Built-in functions, exceptions, and other objects，FILE 為 `(built-in)`；DESCRIPTION 提及 `None` 與 `Ellipsis`，CLASSES 樹狀列表顯示 `object`、`basestring` 下的 `str` 與 `unicode`，另有 `buffer`、`bytearray`。這些是文件內容而非新程式執行結果。

原參考：<https://note.pcwu.net/2017/03/03/python-arbitrary/>。

#### Decorator 裝飾器（來源：P045–P046）

裝飾器是包裝其他函式的函式，用來擴充被包裝函式的能力；大量函式庫都有使用。當不同責任的邏輯混在同一函式中，會降低可讀性，可藉裝飾器分離。原文列優點：降低程式碼重複率、提高易讀性與靈活度。

<a id="p046"></a>

### P046｜從質數程式到混合計時邏輯

[核對原講義第 46 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=46)

#### basic-28_1.py：純粹判斷及列印質數（來源：P046 圖）

```python
def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

def prime_nums():
    for i in range(2,100):
        if is_prime(i):
            print(i)

prime_nums()
```

小於 2 不是質數；2 是質數；其餘以 `range(2,num)` 試除，只要能整除即回傳 `False`，全部檢查後才回傳 `True`。列印範圍為 2 至 99，不包含 100。

#### basic-28_2.py：把計時混入 prime_nums（來源：P046 圖）

`is_prime()` 與上例完全相同；新增 `import time`，替換以下函式及呼叫：

```python
import time

def prime_nums():
    t1 = time.time()
    for i in range(2,100):
        if is_prime(i):
            print(i)
    t2 = time.time()
    print(t2-t1)

prime_nums()
```

此版在列完質數後印出時間差，包含迴圈、判斷、列印的時間。缺點是同一函式混合「列出質數」與「時間計算」。原文缺點敘述放在兩張圖之間；第一張沒有計時，實際應理解為第二張的問題。頁面未提供確切耗時輸出。

<a id="p047"></a>

### P047｜以高階函式手動包裝計時：basic-28_3.py

[核對原講義第 47 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=47)

本頁整張程式圖展示 `display_time` 接收函式並回傳內層 `wrapper`：

```python
#!/usr/bin/python
#coding=utf-8
import time

def display_time(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()
        print(t2-t1)
    return wrapper

def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

def prime_nums():
    for i in range(2,100):
        if is_prime(i):
            print(i)

f = display_time(prime_nums)  # return f which is a function
f()
```

`display_time(prime_nums)` 傳入函式物件而非立刻執行 `prime_nums()`，回傳 `wrapper` 給 `f`；執行 `f()` 時才先記錄時間、呼叫 `func()` 列印質數，再計算及顯示耗時。`return wrapper` 沒有括號，否則意義會變成立即呼叫。本版計時器只支援無參數函式，且沒有保留被包裝函式的回傳值。


<a id="p048"></a>

### P048｜@display_time 語法糖：basic-28_4.py

[核對原講義第 48 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=48)

圖中 `display_time(func)`、內層 `wrapper()`、`is_prime(num)` 與 P047 相同，改以以下結尾取代手動建立 `f`：

```python
@display_time
def prime_nums():
    for i in range(2,100):
        if is_prime(i):
            print(i)

prime_nums()
```

第 25 行 `@display_time` 指定裝飾器，第 26 行是原始函式定義，第 31 行呼叫。等價概念為定義原函式後執行 `prime_nums = display_time(prime_nums)`。圖上的紅箭頭由最下方呼叫指向裝飾位置／計時函式，再由 `func()` 指向原質數函式，意圖表達「計時包住原工作」。

**原稿教學疑誤：** 文字說「首先執行31行 prime_nums()，接著執行25行裝飾詞，因此執行第6行 display_time()」，將裝飾時機混淆成呼叫時機。正確順序是執行函式定義時先呼叫裝飾器建立 `wrapper` 並重新綁定名稱；第31行再呼叫時直接進入已建立的 `wrapper`，執行 `t1 → func() → t2 → print`。第12行 `return wrapper` 也屬裝飾器建立階段，不是每次計時完才執行。

<a id="p049"></a>

### P049｜轉送參數、保存回傳值：basic-28_5.py

[核對原講義第 49 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=49)

圖中紅框標出 `*args` 與 `maxnum`，表示包裝函式必須接收並傳遞參數。相較前頁增加 `result`，使結果可穿過裝飾器返回呼叫者。

```python
import time

def display_time(func):
    def wrapper(*args):
        t1 = time.time()
        result = func(*args)
        t2 = time.time()
        print(t2-t1)
        return result
    return wrapper

def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

@display_time
def count_prime_nums(maxnum):
    count = 0
    for i in range(2,maxnum):
        if is_prime(i):
            count = count + 1
    return count

count = count_prime_nums(100)
print(count)
```

與前例逐個列印質數不同，本例只累計數量，再返回 `count`；裝飾器先印耗時，外面的 `print(count)` 再印數量。**補充：** 此版本只轉送位置參數；若要支援關鍵字參數，需 `wrapper(*args, **kwargs)` 與 `func(*args, **kwargs)`。保留名稱、文件字串可再用 `functools.wraps(func)`；這些不是原圖已有的內容。

原參考：<https://www.maxlist.xyz/2019/12/07/python-decorator/>；<https://www.youtube.com/watch?v=QqRvteWBSWg>。

<a id="p050"></a>

### P050｜物件導向、class、self、__init__

[核對原講義第 50 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=50)

#### 物件導向概念（來源：P050）

原稿將 Python 類別機制描述為 C++ 與 Modula-3 的綜合體；不需要宣告類別／成員為 `public` 或 `private`，也不必先寫型態宣告。支援單一繼承及多重繼承，衍生／子類別（derived class）可覆寫基礎類別（base class）的方法，也可呼叫基礎類別同名方法。此章原編號亦為 **1.6**，與 P042 補充節重複，保留原章名，不擅自改號。

#### 定義類別（來源：P050；class-01.py）

```python
class MyClass:
    text="ABC"

    def clear(self):
        self.text=""
```

`class` 後接類別名稱。`text` 在類別本體中定義，`clear(self)` 將目前實例的 `text` 設為空字串。**補充：** 這個賦值建立／修改的是實例屬性，不等同把整個類別的 `MyClass.text` 清空。

#### 名稱遮蔽（來源：P050；class-02.py）

```python
class ShadowingTest:
    x=10
    y=50
    def printInfo(self,x):
        print("區域變數"+str(x))
        print("屬性"+str(self.x))
        print("屬性"+str(self.y))
        return ("x="+str(x+50))
```

參數 `x` 是區域名稱，`self.x`、`self.y` 是透過實例查得的屬性；名稱相同不表示同一個值。回傳的 `x=` 字串使用參數 `x+50`，不是 `self.x+50`。本頁圖片只展示類別定義，未給實例呼叫或輸出。

#### __init__ 與 self（來源：P050–P051）

實例方法的寫法像類別中的函式，第一個參數慣例命名 `self`，代表目前實例，概念近似其他語言的 `this`。建立實例時會呼叫 `__init__()` 做初始化，原稿比喻為建構函式。**補充：** `self` 是參數名稱而非關鍵字／敘述句；`__init__` 是初始化方法，真正建立物件的階段由 `__new__` 處理。`classmethod` 與 `staticmethod` 也不能一概說第一參數都必須是 `self`。

<a id="p051"></a>

### P051｜初始化實例、封裝與初始值

[核對原講義第 51 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=51)

#### 存款餘額（來源：P051；class-03.py）

```python
class TaipeiBank:
    balance=0
    def __init__(self, balance):
        self.balance=balance
    def printBalance(self):
        print("存款餘額:" + str(self.balance))
```

呼叫 `TaipeiBank(balance)` 時由初始化方法保存餘額，`printBalance()` 讀取實例的 `self.balance` 並轉字串輸出。本例只做記憶體物件示範，沒有資料庫或實際銀行操作。

#### 加法與乘法（來源：P051；class-04.py）

```python
class SmallMath:
    x=0
    y=0
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        print("加法結果:"+str(self.x+self.y))
    def mul(self):
        print("乘法結果:"+str(self.x*self.y))
```

初始化兩個操作數，再由 `add()`、`mul()` 列印加法／乘法結果；方法沒有 `return` 數值。

#### 封裝 Encapsulation（來源：P051）

原稿：可供外部引用的成員是公有屬性／公有方法；任意存取可能有安全疑慮，故提出 private 具有安全性、外部不能存取、僅內部使用，並稱屬性或方法前加 `__` 就成為 private。

**重要釐清：** Python 的雙底線前綴主要是名稱改寫（name mangling，例如 `__balance` 變成 `_TaipeiBank__balance`），避免無意衝突，不是不可繞過的資訊安全機制。外部仍可能以改寫後名稱存取，因此不應把它當安全邊界。

#### 初始化值（來源：P051–P052）

```python
digital_value = 0
str_value = ""
list_value = []
ditc_value = {}
tuple_value = ()
```

原稿稱「初始化為空值」；較精確地說是數值零、空字串、空串列、空字典、空元組，並不是統一的空值 `None`。字典變數名原稿拼作 `ditc_value`，此處保留。

<a id="p052"></a>

### P052｜私有名稱、getter／setter、繼承

[核對原講義第 52 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=52)

頁首補完初始化清單：`list_value=[]`、`ditc_value={}`、`tuple_value=()`，詳 P051。

#### 類別內存取雙底線屬性（來源：P052；class-05.py）

```python
class Student():
    Sno=""
    Sname=""
    Age = 18
    __Money = 100

    def Iam(self):
        print("I am " + self.Sno + ":" +self.Sname + " 3Q!")
        self.__Money = 120
        print("I hava " + str(self.__Money)+" dollors")
```

`Sno`、`Sname`、`Age` 是公有名稱，`__Money` 在類別內可正常讀寫。`Iam()` 先輸出學號與姓名，再將該實例金額改為 `120`，最後顯示金額。原圖字串拼作 `hava`、`dollors`，此處保留，並非標準英文 have/dollars。

#### 以公開方法操作內部屬性（來源：P052；class-06.py）

```python
class Student():
    Sno=""  #public
    Sname=""  #public
    Age = 18
    __Money = 100  #private

    def Iam(self):
        print("I am " + self.Sno + ":" +self.Sname + " 3Q!")
        print("I hava " + str(self.__Money)+" dollors")

    def setMoney(self,money):
        self.__Money = money

    def getMoney(self):
        return(self.__Money)
```

此版 `Iam()` 不再自行改成120；由 `setMoney(money)` 指定金額，`getMoney()` 回傳金額。這是一種 getter／setter 介面，但本例沒有檢查金額是否合法；雙底線限制仍是名稱改寫，不是安全防護。

#### 繼承基礎（來源：P052–P053）

原有類別稱 base class／parent class，衍生類別稱 derived class／child class。語法 `class 衍生類別(基礎類別):`。藉繼承重用屬性及方法，必要時再新增或改寫；`super().方法(...)` 可協作呼叫繼承鏈下一個實作（原稿用「基礎類別的函式」說明）。**補充：** Python 2 的 `super` 寫法及新式類別需求與 Python 3 不同，參 P054。

<a id="p053"></a>

### P053｜Animal／Bird 繼承與覆寫概念

[核對原講義第 53 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=53)

上方格式圖為 `class Monster(Animal):`，`Monster` 被標為子物件、`Animal` 被標為父物件，粗黑彎箭頭由父指向子，說明繼承關係；更精確的術語應為子類別與父類別。

#### class-07py（原稿檔名漏掉句點；來源：P053）

```python
class Animal():
    def __init__(self, name):
        self.name = name
    def fly(self):
        print(self.name + " fly!")

class Bird(Animal):
    def __init__(self, name):
        self.name = "red " + name
    def sing(self):
        print(self.name + " sing!")
```

`Bird` 繼承 `fly()`，新增 `sing()`，且覆寫 `__init__` 使名稱帶 `red ` 前綴。父類別初始化方法不會在這個子類別初始化方法中自動額外執行。原文「父類別的建構方法會被子類別覆寫」應加前提：**子類別自己定義 `__init__` 時才覆寫；若沒有則可以繼承父類別的初始化方法。** 若仍需要父類別初始化邏輯，應顯式呼叫 `super`。

#### Override（來源：P053）

在衍生類別重新定義基礎類別的同名方法，使同名方法在子類別具不同功能，稱覆寫。這不同於把父類別物件本身永久修改；只是方法查找優先使用子類別實作。

<a id="p054"></a>

### P054｜薪資規則覆寫、super 與新式類別

[核對原講義第 54 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=54)

#### class-08py：一般員工／經理（來源：P054 圖）

```python
class Emp:
    Salary=0
    def set_salary(self,Salary):
        if (Salary>40000):
            self.Salary=40000
        else:
            self.Salary=Salary
    def ShowSal(self):
        print(str(self.Salary))

class Manager(Emp):
    Bonus=0
    def set_salary(self,Salary):
        if (Salary>60000):
            self.Salary=60000
        else:
            self.Salary=Salary

    def ShowSal(self):
        print(str(self.Salary+self.Bonus))
```

`Emp.set_salary` 將薪資上限設為40000；`Manager` 覆寫成60000。經理 `ShowSal()` 也覆寫為薪資加獎金。`Bonus` 初值為0；負數或不合型態的輸入並未在此例驗證。圖片無實例測試或確切執行結果。

#### class-09py：覆寫中仍呼叫父類別（來源：P054 圖）

```python
__metaclass__ = type
class Father:
    x = 50
    def printInfo(self):
        print(".....1.....")

class Child(Father):
    x = 100
    def printInfo(self):
        super(Child, self).printInfo()
        print("父x="+str(Father.x))
        print("子x="+str(self.x))
```

`super(Child,self).printInfo()` 先跑父類別方法，再顯示明確指定的 `Father.x`（50）與透過實例找到的 `self.x`（100）。先前父類別同名方法並沒有被刪除，仍可經 `super` 呼叫。

原文英文補充：Python 2 的模組層級 `__metaclass__ = type` 可讓原本會產生舊式類別的宣告改為新式類別。**版本補充：** Python 3 所有類別已是新式類別，不需此設定；Python 3 的 metaclass 指定通常寫在 `class C(metaclass=...)`。不能把 Python 2 的設定方式當成 Python 3 通用語法功能。

<a id="p055"></a>

### P055｜繼承初始化、pass、classmethod

[核對原講義第 55 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=55)

#### class-10.py：重用父類別初始化（來源：P055）

```python
__metaclass__ = type
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name + "正在吃食物")

    def sleep(self):
        print(self.name + "正在睡覺")

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
```

`Dog` 自訂初始化但將 `name` 傳給父類別處理，並直接繼承 `eat`、`sleep`。圖未提供實例呼叫，不能當成有列印結果。

#### pass 與覆寫佔位方法（來源：P055；class-11.py）

`pass` 是空敘述，不做任何事，用於保留語法結構完整、充當尚未實作的區塊。

```python
class Animal(object):
    def __init__(self, name):
        self.name = name
    def sound(self):
        pass

class Dog(Animal):
    def __init__(self, name):
        super(Dog,self).__init__('小狗'+name)

    def sound(self):
        return '汪汪叫'
```

父類別 `sound()` 沒有動作，子類別回傳「汪汪叫」字串；`return` 不會自行印到終端。繼承 `object` 讓 Python 2 的類別成為新式類別；子類別初始化增加「小狗」前綴。

#### classmethod()（來源：P055）

原文：內建函式 `classmethod(function)`，接受函式作參數，回傳類方法。參考：<https://vimsky.com/zh-tw/examples/usage/classmethod-in-python.html>。本頁沒有 classmethod 範例程式圖。**補充：** 常見用法是 `@classmethod`，第一參數慣例為 `cls`，綁定的是類別而非單一實例；原文「接受函數名稱」應理解成函式物件，不是名稱字串。

<a id="p056"></a>

### P056｜套件目錄、__init__.py、幾何類別模組

[核對原講義第 56 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=56)

#### 將模組包成套件（來源：P056）

第一張目錄圖：

```text
sample_package/
├── __init__.py
├── sample_module.py
└── sample_module_import.py
```

原稿強調新增 `__init__.py`，即使為空也需有，用來宣告套件。若只進入該目錄跑原指令可能感覺沒有差別，但從專案其他位置匯入套件時，內部的 import 必須配合套件結構調整。

**版本補充：** 對傳統／regular package，`__init__.py` 是標準做法；Python 3 另支援不含此檔案的 namespace package，故「一定要有」不能概括所有現代套件。此處仍依教材的傳統套件結構學習。

第二個範例結構：

```text
專案目錄/
├── package-01.py
└── mypackage/
    ├── __init__.py
    ├── Hello.py
    └── myClass.py
```

#### myClass.py（來源：P056 圖；範例 package-01.py）

```python
#coding=utf-8
__metaclass__ = type
class Rectangle():  # 定義父類別
    def __init__(self, width,height):
        self.width = width    # 定義共用屬性
        self.height = height  # 定義共用屬性
    def area(self):           # 定義共用方法
        return self.width * self.height

class Triangle(Rectangle):  # 定義子類別
    def area(self):         # 定義子類別的共用方法
        return (self.width * self.height)/2
```

`Rectangle` 保存寬、高，面積為寬乘高；`Triangle` 繼承初始化方法、覆寫 `area()`，面積為寬乘高除以2。**補充：** 圖中註解稱「共用屬性」，但 `self.width`、`self.height` 是每個實例自己的屬性，不是類別共享變數。Python 2 對整數做 `/2` 可能截斷；Python 3 `/` 做真除法。

#### Hello.py（來源：P056 圖）

```python
def sayHello():
    print("Hello")
```

圖上可見編輯器分頁 `class-12.py`、`myClass.py`、`Hello.py`，但只顯示後兩者的內容；頁面沒有展示 `package-01.py` 主程式如何 import，不能憑檔名補造原稿。**補充示意（非原稿）：** 按此目錄可使用 `from mypackage.Hello import sayHello` 及 `from mypackage.myClass import Rectangle, Triangle`。

<a id="p057"></a>

### P057｜套件 import 參考文獻

[核對原講義第 57 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=57)

本頁只有參考文獻，沒有新增圖、程式碼或輸出：

<https://medium.com/pyladies-taiwan/python-%E7%9A%84-import-%E9%99%B7%E9%98%B1-3538e74f57e3>

主題為 Python 的 import 陷阱，承接 P056 的套件與模組匯入。

<a id="p058"></a>

### P058｜例外處理 try／except／else／finally

[核對原講義第 58 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=58)

執行期間發生錯誤且未處理時，程式流程會中斷並產生例外。原文提到將介紹自訂例外類別，但本頁及 P059 實際未提供自訂例外類別程式。

#### 圖示流程與年齡輸入（來源：P058）

第一個圖以黃色箭頭標示：可能出錯的程式放 `try` 區塊；出錯後處理放 `except`；區塊外 `print(...)` 代表處理完成後可繼續往下執行。第二張圖的程式：

```python
try:
    age=int(input("please input age:"))
    print(age)
except:
    print("請輸入整數數值")
```

字串需能轉成整數，否則跳到錯誤提示。圖中黃色說明框指向 `try`，綠色說明框指向 `except`。**補充：** 此寫法在 Python 3 的 `input()` 收字串；Python 2 的 `input()` 會求值輸入，行為不同且不適合不可信輸入。建議現代版本捕捉特定 `ValueError`，而非裸 `except` 捕捉所有例外。

#### try-01.py：密碼輸入（來源：P058）

```python
try:
    pwd = raw_input('請輸入密碼')
except:
    print('發生錯誤')
```

Python 2 `raw_input()` 可接受數字字元或一般文字，存成字串到 `pwd`；原文在 Unix 終端按 Ctrl+D 表示 EOF，會進入例外分支，顯示「發生錯誤」。**補充：** Windows 終端 EOF 操作可能不同；Python 3 改用 `input()`；這裡雖說輸入密碼但並不隱藏輸入，實際密碼讀取可用 `getpass`。

#### 四個區塊的責任（來源：P058–P059）

- `try`：放可能拋錯的工作。
- `except 錯誤型別`：只捕捉符合的例外，做後續處理。
- `else`：`try` 正常完成而未拋出例外時執行。
- `finally`：通常不論成功、失敗或準備離開區塊，都執行清理；不代表能涵蓋程序被強制殺死、斷電等情況。

**重要補充：** `else` 內新發生的例外，不會被同一組 `try` 的 `except` 捕捉；P059 原程式正好有此問題。

<a id="p059"></a>

### P059｜常見例外表與 try-02.py 的實際錯誤

[核對原講義第 59 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=59)

#### 原表完整內容（來源：P059）

| 型別 | 原稿用途說明與必要釐清 |
|---|---|
| `KeyboardInterrupt` | 使用者按 Ctrl+C 中斷。 |
| `ZeroDivisionError` | 除以0；取餘數的除數為0也會觸發。 |
| `EOFError` | 讀取輸入收到 EOF（end of file）。 |
| `NameError` | 找不到區域或全域名稱。 |
| `OSError` | 與作業系統有關的錯誤。 |
| `FileNotFoundError` | 找不到檔案或資料夾；此名稱是 Python 3 的例外類別。 |
| `ValueError` | 原表稱型別與預期不同；較精確地說是型別可接受但值不合法，例如 `int('abc')`。純型別不相容通常是 `TypeError`。 |

#### 原圖程式（來源：P059；try-02.py）

```python
try:
    a=int(input("請輸入第一個整數："))
    b=int(input("請輸入第二個整數："))
    r = a % b
except ValueError:
    print("發生輸入非數值的錯誤!")
except Exception as e:
    print("發生" + str(e) +"的錯誤，包括分母為 0 的錯誤!")
else:
    print("ans=" + r)
finally:
    print("一定會執行的程式區塊")
```

`%` 是取餘數，不是一般除法。先捕捉 `ValueError`，再由 `except Exception as e` 接住其他一般例外，`str(e)` 顯示實際訊息。**補充：** `KeyboardInterrupt` 不繼承 `Exception`，不是所有表中例外都會被第二分支接住。

**原稿重要錯誤：** `r` 是整數，`"ans=" + r` 會產生 `TypeError`，而且在 `else` 發生，不會回頭被上述 `except Exception` 接住。可明確修正為 `print("ans=" + str(r))` 或 `print("ans=", r)`，不可默默把原碼改掉。

#### 隔離實測紀錄（來源：P059 疑誤驗證，非原稿輸出）

在既有虛擬環境 Python **3.12.13** 執行 `verify_041_070.py`，使用記憶體中替代的 `input` 傳值，沒有修改系統、碰資料庫或存取外部資源：

| 輸入 | 實際 stdout | 未被捕捉的錯誤 |
|---|---|---|
| `5`, `2` | `一定會執行的程式區塊` | `TypeError: can only concatenate str (not "int") to str` |
| `5`, `0` | `發生integer modulo by zero的錯誤，包括分母為 0 的錯誤!`，接著 `一定會執行的程式區塊` | 無 |
| `abc`, `2` | `發生輸入非數值的錯誤!`，接著 `一定會執行的程式區塊` | 無；第一個輸入已觸發例外 |

同一隔離腳本也驗證：P048 裝飾器在呼叫前已記錄 `decorate`，呼叫後順序才為 `decorate → wrapper → body`；P051 `s.__Money` 拋 `AttributeError`，但 `s._Student__Money` 實際可讀出100；P049 的2至99質數數量實算為25（此處是等價計數驗證，不是宣稱執行原截圖整份檔案）。

<a id="p060"></a>

### P060｜多執行緒概念、優點與狀態圖

[核對原講義第 60 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=60)

#### Process 與 Thread（來源：P060）

原文引用：「程序是資源分配的最小單位，執行緒則是 CPU 排程的最小單位。」執行緒包含在程序內，是程序的實際運作單位；一條執行緒是一個單一順序控制流，同一程序可有多條執行緒併發處理不同任務。

原稿列的好處完整如下：

1. 易於排程。
2. 提高併發性，讓同一程式不同部分以不同執行緒處理。
3. 相比建立程序，建立執行緒通常較快、開銷較少。
4. 有利多處理器使用，讓不同執行緒利用不同處理器。
5. 把耗時任務放到背景處理。
6. 改善使用者介面回應，例如按鈕觸發工作後仍能顯示進度條。
7. 程式速度「可能」加快，並非保證。
8. 對等待輸入、檔案讀寫、網路收發等等待型任務特別有用；原稿並稱可釋放記憶體等資源。

**必要補充：** 併發不等於同一瞬間真正平行。在傳統有 GIL 的 CPython 中，CPU 密集的純 Python 工作不會僅因多執行緒就線性加速；I/O 等待仍適合使用。多執行緒也會消耗堆疊等記憶體，等待本身不保證釋放物件佔用的記憶體。此處為觀念釐清，未對本講義程式執行效能測試。

#### 狀態圖逐箭頭解讀（來源：P060 圖）

```text
新建 --初始化--> Runnable --調度--> Running --結束--> 結束
                    ^                 |
                    |解除             |阻塞
                    +---- Blocked <---+
```

`Blocked` 是綠框大區，內含 `Waiting`、`Locked`、`Sleeping` 三個狀態小框。解除阻塞後箭頭回到 `Runnable`，不是直接回到 `Running`；仍需排程獲得執行時間。圖是概念模型，不是 `threading.Thread` 可直接讀取的同名狀態列舉。

<a id="p061"></a>

### P061｜執行緒生命週期、阻塞原因與建立方式

[核對原講義第 61 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=61)

#### 五種狀態（來源：P061）

- **New／新建**：建立執行緒；原稿以建立後進入可執行狀態描述。
- **Runnable／可執行**：準備好但還未取得 CPU 時間片。
- **Running／執行中**：正式運作，過程可能進入阻塞。
- **Blocked／阻塞**：暫停運作，解除後回到 Runnable 等待排程。
- **Dead／結束**：工作方法執行完畢，或因例外結束。

原文以人生的出生、學習（工作前準備）、工作、休假作類比。Running 進入 Blocked 的例子：

1. 睡眠／等待結束：主動呼叫 `sleep` 或 `join`。
2. 條件等待：呼叫 `wait`，由其他執行緒 `notify` 喚醒。
3. 同步等待：要取得鎖，但資源／鎖已被其他執行緒持有。

**補充：** 建立 Python `Thread` 物件不等於已啟動，仍需 `start()`；`join()` 是等待另一執行緒完成，不是定時睡眠；`wait/notify` 通常透過 `threading.Condition`，不是每個 Thread 物件都有的方法。

#### 兩種指定執行工作的方法（來源：P061）

官方文件摘錄：Thread 表示在獨立控制執行緒中運行的活動，可以把 callable 傳給建構子，或繼承 Thread 並覆寫 `run()`；子類別應只覆寫 `__init__()` 與 `run()`，不要任意覆寫其他 Thread 生命週期方法。

原參考：<https://docs.python.org/2/library/threading.html?highlight=threading#module-threading>。

建立子執行緒範例開頭：

```python
#!/usr/bin/python
#coding=utf-8
import threading
import time
```

`job`、`start`、`join` 接 P062。原文預告同步與通訊，但 P061–P065 三份程式主要示範啟動及等待，不含鎖或 Condition 的完整實作。

<a id="p062"></a>

### P062｜單一子執行緒：thread-01.py

[核對原講義第 62 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=62)

承 P061 的匯入，完整工作部分：

```python
# 子執行緒的工作函數
def job():
    for i in range(5):
        print "Child thread:%d"% i
        time.sleep(1)

# 建立一個子執行緒
t = threading.Thread(target = job)
# 執行該子執行緒
t.start()

# 主執行緒繼續執行自己的工作
for i in range(3):
    print "Main thread:%d"% i
    time.sleep(1)

# 等待 t 這個子執行緒結束
t.join()
print("Done.")
```

- `target=job` 傳函式物件，不能為了相同目的改成 `target=job()`，後者會先在目前執行緒呼叫。
- 子執行緒輸出 `Child thread:0` 至 `Child thread:4`，每次停1秒；主執行緒輸出 `Main thread:0` 至 `Main thread:2`，也各停1秒。
- 兩路輸出交錯順序受排程影響，不應捏造唯一固定順序。
- `t.join()` 阻塞呼叫它的主執行緒，直到子工作完成，才輸出 `Done.`。
- 原碼使用 Python 2 `print` 敘述；Python 3 對應寫成 `print("Child thread:%d" % i)`、`print("Main thread:%d" % i)`。

本頁沒有終端輸出截圖；上述範圍是依碼解讀。頁尾開啟「多個子執行緒與參數」，程式於下一頁。

<a id="p063"></a>

### P063｜多個子執行緒與 args 參數

[核對原講義第 63 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=63)

#### thread-02.py 主體（來源：P063，結尾接 P064）

```python
#!/usr/bin/python
#coding=utf-8
import threading
import time

# 子執行緒的工作函數
def job(num):
    for i in range(10):
        print("Thread", num)
        time.sleep(1)

# 建立 5 個子執行緒
threads = []
for i in range(5):
    threads.append(threading.Thread(target = job, args = (i,)))
    threads[i].start()

# 主執行緒繼續執行自己的工作
# ...

# 等待所有子執行緒結束
for i in range(5):
    threads[i].join()
```

`threads` 儲存 Thread 物件；`args=(i,)` 是只有一個元素的 tuple，尾端逗號不可省略成一般括號。五個工作分別拿到編號0至4。每個 `job(num)` 都迴圈10次，列印的是固定的執行緒編號 `num`，不是該次迴圈的 `i`。

先將所有執行緒 `start()`，最後才逐一 `join()`，因此並不因 `join` 寫在迴圈裡就變成逐一開始、逐一完成。中間 `# ...` 是保留給主執行緒其他工作的註解，沒有隱藏實作。Python 2 的 `print("Thread", num)` 可能顯示 tuple 形式；Python 3 則以空白分隔。完成訊息接 P064。

<a id="p064"></a>

### P064｜thread-02 結尾與繼承 Thread 的 run()

[核對原講義第 64 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=64)

#### thread-02.py 結尾（來源：P064，承 P063）

```python
print("Done.")
```

放在所有 `threads[i].join()` 之後，表示所有子執行緒完成後才印完成訊息。

#### 以子類別覆寫 run（來源：P064；thread-03.py 前半）

本頁再次引用官方說明：傳 callable 給 Thread 建構子，或覆寫子類別的 `run()` 都可指定工作；紅字特別強調只覆寫 `__init__` 與 `run`。

```python
#!/usr/bin/python
#coding=utf-8
import threading
import time

# 繼承 threading.Thread 的子執行緒類別
class MyThread(threading.Thread):
    # 建構子
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    # 重新改寫基礎類別的函式 run
    def run(self):
        print("Thread", self.num)
        time.sleep(1)
```

先呼叫 `threading.Thread.__init__(self)` 初始化 Thread 的內部狀態，再保存自己的編號。`run()` 只印一次編號並睡1秒，與 P063 的十次迴圈不同。**補充：** 對物件呼叫 `start()` 才啟動另一執行緒；直接呼叫 `run()` 只是普通方法呼叫，不會自動建立並行工作。Python 3 可用 `super().__init__()` 表達父類別初始化，這是補充寫法而非原碼。

<a id="p065"></a>

### P065｜啟動自訂執行緒：thread-03.py 後半

[核對原講義第 65 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=65)

接 P064 `MyThread`：

```python
# 建立 5 個子執行緒
threads = []
for i in range(5):
    threads.append(MyThread(i))
    threads[i].start()

# 主執行緒繼續執行自己的工作
# ...

# 等待所有子執行緒結束
for i in range(5):
    threads[i].join()

print("Done.")
```

每個 `MyThread(i)` 的編號經 `__init__` 保存在 `self.num`，`start()` 使其 `run()` 在子執行緒執行；最後逐一等待，才印 `Done.`。相較 `Thread(target=job,args=(i,))`，本例把資料與工作行為一起封裝在類別。頁面沒有實際執行終端，也沒有提供固定交錯順序；不可把編號遞增建立誤當成輸出順序保證。

<a id="p066"></a>

### P066｜JSON 概念、優點與格式規則

[核對原講義第 66 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=66)

#### 定義與用途（來源：P066）

JSON 全名 **JavaScript Object Notation**，是一種輕量的資料交換格式，容易讓人閱讀及編寫，也容易讓機器解析與產生。原文追溯到 JavaScript／ECMA-262 第3版（1999年12月）的子集；格式本身獨立於特定程式語言，採用與 C、C++、C#、Java、JavaScript、Perl、Python 等熟悉的語法習慣。

它以純文字儲存、傳送結構資料，例如字串、數字、陣列、物件；也能透過巢狀物件或陣列組合較複雜資料，使不同程式交換資訊。

原文四項優點：相容性高；易懂、易讀、易修改；支援 number、string、booleans、nulls、array、associative array 等資料；許多語言已有讀寫 JSON 的函式庫。**補充：** JSON 正式稱為 object 的結構可類比關聯陣列；不是所有 Python 物件都能直接序列化成 JSON。

#### 建立 JSON 字串（來源：P066）

- 可包含 Array 或 Object。
- 陣列以 `[]` 包住資料；物件以 `{}` 包住成員。
- 物件的 name/value 成對，以冒號 `:` 分隔。
- 值可以是整數／浮點數、字串、布林值 `true` 或 `false`、陣列、物件、空值。
- 原稿字串以印刷用彎引號「” ”」示意，空值寫作大寫 `NULL`。

**原稿疑誤與語法補充：** 真正 JSON 字串／物件名稱需用半形雙引號 `"`，不是彎引號或 Python 單引號；空值必須是小寫 `null`，不是 `NULL` 或 Python 的 `None`。布林值是值而非原文所稱「布林函數」。陣列元素、物件成員以逗號分隔；JSON 頂層也可為單一純量值，不僅是 object/array。

<a id="p067"></a>

### P067｜JSON 在 Python 的使用與重複規則

[核對原講義第 67 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=67)

本頁重述 P066 的定義及規則，並不是新圖片或另有範例：JSON 是來自 JavaScript 語法但語言獨立的純文字交換格式，可由人編寫、由機器解析；以 object/array 組合字串、數字等簡單或巢狀資料。

本頁四項優點仍是：相容性高、便於閱讀修改、多種資料型態、跨語言函式庫支援。建立規則再列一次：陣列 `[]`、物件 `{}`、`name:value`；值的六類為數字、字串、`true/false`、陣列、物件、空值（原稿仍誤寫 `NULL`，正確為 `null`）。字串需半形雙引號，詳 P066 更正。

本頁新增的 Python 知識：自 Python **2.6** 起標準函式庫加入 `json` 模組，不需另外下載。Python JSON 的序列化稱為 **encoding**，反序列化稱為 **decoding**；對應 API 與型別轉換接 P068。此處 encoding 指 JSON 表示形式的轉換，不要與 UTF-8 等字元編碼混為一談。

<a id="p068"></a>

### P068｜json.dumps／loads 與完整型別轉換表

[核對原講義第 68 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=68)

#### Encoding 與 Decoding（來源：P068）

- Encoding：把 Python 物件轉成 JSON 字串。
- Decoding：把 JSON 格式字串轉成 Python 物件。

第一張「JSON 函數」圖片要求先 `import json`，列出：

| API | 作用 |
|---|---|
| `json.dumps` | 將 Python 物件編碼成 JSON 字串。 |
| `json.loads` | 將已編碼 JSON 字串解碼為 Python 物件。 |

原文說編碼結果與 `repr()` 常看起來相似，但不是相同格式，且某些型別會改變。例如 tuple 編碼成 JSON array，解碼回 Python 時成 list，不能保證型別完全往返保留。

#### Python → JSON（來源：P068 圖，原表為 Python 2）

| Python | JSON |
|---|---|
| `dict` | `object` |
| `list, tuple` | `array` |
| `str, unicode` | `string` |
| `int, long, float` | `number` |
| `True` | `true` |
| `False` | `false` |
| `None` | `null` |

#### JSON → Python（來源：P068 圖，原表為 Python 2）

| JSON | Python |
|---|---|
| `object` | `dict` |
| `array` | `list` |
| `string` | `unicode` |
| `number (int)` | `int, long` |
| `number (real)` | `float` |
| `true` | `True` |
| `false` | `False` |
| `null` | `None` |

原稿舉 `'abc'` 解碼後變為 `unicode`，反映 Python 2 的型別系統。**版本補充：** Python 3 的 JSON string 對應 `str`，整數為 `int`，不再使用分立的 `unicode` 與 `long` 類別名稱。

**原稿缺漏明示：** 文字提到「上例」「通過輸出的結果」，但本頁影像只有函式表、兩張型態對照表，沒有該段宣稱的 `repr()`／tuple／`abc` 原始測試程式或輸出截圖；P067 也沒有這段測試。以上保留文字概念，不補造未出現的實驗結果。

<a id="p069"></a>

### P069｜巢狀 JSON 實例與 Python 往返轉換

[核對原講義第 69 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=69)

#### 圖片中的完整 JSON 陣列（來源：P069 圖）

```json
[
  {
    "name": "Molecule Man",
    "age": 29,
    "secretIdentity": "Dan Jukes",
    "powers": [
      "Radiation resistance",
      "Turning tiny",
      "Radiation blast"
    ]
  },
  {
    "name": "Madame Uppercut",
    "age": 39,
    "secretIdentity": "Jane Wilson",
    "powers": [
      "Million tonne punch",
      "Damage resistance",
      "Superhuman reflexes"
    ]
  }
]
```

最外層是陣列，內含兩個物件；各物件有字串欄位 `name`、`secretIdentity`，數值欄位 `age`，及字串陣列 `powers`。圖片具體示範物件與陣列的巢狀組合、name/value 冒號及成員間逗號，並無 HTTP 操作或輸出畫面。

#### Encoding & decoding 原程式（來源：P069）

```python
# josn encoding
import json
#list 內放dict

data = [{"ID":"1","STATUS":"0"},{"ID":"2","STATUS":"1"}]
data_string = json.dumps(data) #encoding

# json decoding
decoded = json.loads(data_string) # decoding

id1 = decoded[0]["ID"]
status1 = decoded[0]["STATUS"]
id2 = decoded[1]["ID"]
status2 = decoded[1]["STATUS"]
```

原註解 `josn` 是拼字錯誤，保留原文。`data` 是 list 內放 dict，`dumps` 回傳 JSON 文字到 `data_string`，`loads` 再把文字還原為 list/dict 結構；`decoded[0]` 選第一筆、`decoded[1]` 選第二筆，再按鍵取值。

此例的 `ID` 與 `STATUS` 都加了引號，所以 `id1` 為字串 `'1'`，`status1` 為字串 `'0'`，`id2` 為字串 `'2'`，`status2` 為字串 `'1'`，不是整數。原程式沒有 `print`，因此不能說原圖展示這些終端輸出。上方英雄資料只作巢狀 JSON 示意，不是下方 `data` 的內容。

<a id="p070"></a>

### P070｜JSON 範例檔索引與參考資料

[核對原講義第 70 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=70)

本頁完整列出四個檔名：

- `json-01.py`
- `json-02.py`
- `json-03.py`
- `json-04.py`

影像只有四個黃色範例標籤及參考連結，**沒有這四個檔案各自的程式內容**；不應把自行推測的下載、解析或列印程式冒充教材原碼。

原參考文獻：

1. <https://www.cnblogs.com/huchong/p/9037142.html>
2. <http://opendata2.epa.gov.tw/AQI.json>

第二個網址以 `AQI.json` 作為 JSON 資料來源參考。此筆記保留講義原連結，未連線驗證其目前可用性，也未發出下載或 API 請求。


---

## 第三章 Django：逐頁完整知識筆記（P071–P111）

> 來源：《Python and Django(最新版)P.pdf》實體 PDF 第71–111頁。逐頁比對文字層及頁面圖片；以下命令、版本與成功畫面均為**講義歷史示範**，不是本次實際安裝／執行结果，也不是現行版本宣告。`#` 多為講義命令提示符，並非要輸入的命令部分。補充辨析與原稿疑點另標示。

<a id="p071"></a>

### P071｜Django 的定位、特性與安全觀念

[核對原講義第 71 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=71)

- 原章名寫作「第三章：Python Web Djangle」；本文實際介紹 **Django**（標題拼字疑誤）。授課教師：葉呈祥。
- Django 是高階 Python 網站框架，目標是快速建立安全、可維護的網站；框架處理常見網站基礎工作，讓開發者專注應用功能，不必重造已有功能。免費、開源，有活躍社群、文件，以及免費或付費解決方案。
- **完備**：採「功能完備／開箱即用」理念，提供網站開發常用功能。
- **通用**：可製作內容管理系統、維基、社群及新聞網站，可搭配不同客戶端框架；可輸出 HTML、RSS、JSON、XML 等內容。
- **安全**：提供使用者帳號、密碼及 session 管理機制。講義用「cookie 只放密鑰、實際 session 資料在資料庫」對比將 session 資料直接放 cookie；密碼應保存雜湊值而非明文。
- **密碼 hash**：將輸入密碼透過雜湊函式形成固定長度值，登入時驗證輸入與儲存資料是否相符；單向性使外洩的雜湊不易直接逆推原密碼。**補充辨析**：雜湊不是可逆加密，實務還有 salt、演算法與成本參數；弱密碼仍可能被猜解。Session 儲存後端不只資料庫，不能把本頁說明當成所有 Django 設定均如此。
- **可擴展**：基於組件的「無共享」架構，各部分可替換、修改；分離的快取、資料庫、應用程式伺服器可各自擴充硬體。
- **可維護**：遵循設計原則、模式及 DRY（Don't Repeat Yourself，不重複自己），減少重複程式碼，將功能組成可重用 app，再將相關程式組成模組；原文以 MVC（Model View Controller）說明，後面以 Django 的 MTV 分工展開。
- **可移植**：以 Python 撰寫，能在 Linux、Windows、Mac OS X 等平台執行，不綁單一伺服器平台。
- 本頁全為文字和條列，無操作截圖；頁底「Find your new favorite web framework」連結：https://hotframeworks.com/ 。〔來源：P071〕

<a id="p072"></a>

### P072｜框架比較圖與 Django HTTP 請求流程

[核對原講義第 72 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=72)

- 上方折線圖為歷史框架比較，橫軸約 Q2 2016–Q2 2021，縱軸75–100；圖例包含 React、ASP.NET MVC、Ruby on Rails、Angular、AngularJS、Vue.js、Django、Laravel、ASP.NET、Spring。React 曲線後段約98，ASP.NET MVC 約95；Vue.js 從約79上升至約93；Django 約91–93；ASP.NET 一度從100附近下跌至89附近。**原圖未註明縱軸指標定義，不應將數值說成市占率，也不能視為今天排名。**
- 傳統資料驅動網站先等待瀏覽器／其他客戶端的 HTTP 請求，以 URL 與 GET／POST 資料判斷所需內容，視需要讀寫資料庫或執行其他工作，再傳回回應。常見方式為把取得的資料填入 HTML 模板佔位符，動態產生 HTML。
- 下方方塊箭頭圖的完整分工：`HTTP Request → URLs (urls.py) → View (views.py) → HTTP Response (HTML)`；URL 到 View 的箭頭寫 `Forward request to appropriate view`。左側 `Model (models.py)` 與 View 間有雙向 `read/write data` 箭頭；下方 `Template (<filename>.html)` 向上供 View 使用。
- 重點是 URL 分派、資料存取、請求處理、版面呈現分檔，不把所有工作塞進單一函式。〔來源：P072〕

<a id="p073"></a>

### P073｜URLs、View、Models、Templates 職責

[核對原講義第 73 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=73)

- **URLs**：每個資源使用獨立視圖較易維護；URL 映射器依請求 URL 導向對應視圖，亦可匹配 URL 中字串／數字模式，把擷取值當參數交給視圖。**補充辨析**：原文稱「重定向」，這裡是伺服器內部路由分派，不必然是回傳 HTTP 3xx 的瀏覽器重新導向。
- **View**：接收 HTTP request、傳回 HTTP response 的請求處理函式；透過模型取得需要的資料，將回應呈現交給模板。
- **Models**：定義應用資料結構的 Python 物件，提供資料庫記錄新增、修改、刪除與查詢機制。
- **Templates**：定義文件結構／版面的文字檔，以佔位符表示待填入內容；視圖結合資料與模板產生 HTML，模板也能用於非 HTML 文件。
- 本頁沒有額外圖像；文末原參考網址：
  - https://developer.mozilla.org/zh-TW/docs/Learn/Server-side/Django/Introduction
  - https://developer.mozilla.org/zh-TW/docs/Learn/Server-side/Django/Models
  - https://www.liujiangblog.com/course/django/2
  以上保留講義網址，未宣稱本次已驗證連結現況。〔來源：P073〕

<a id="p074"></a>

### P074｜Windows：安裝 Python、PATH、版本與 pip

[核對原講義第 74 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=74)

1. 下載頁截圖為 `python.org/downloads/windows/`，可見 Python **3.8.10 — May 3, 2021**，列出 Windows embeddable package（32／64-bit）、help file、installer（32／64-bit）。圖中文字指出3.8.10不能用於 Windows XP 或更早；也可見 **Python 3.9.4 — April 4, 2021** 及不能用於 Windows 7 或更早的提示。
2. 安裝程式局部圖用紅框強調勾選 `Add Python 3.6 to PATH`，讓終端可找到 Python。**版本差異**：此圖為3.6，下載頁為3.8／3.9，不能誤當同一次安裝截圖。
3. 在命令提示字元確認 Python：
   ```bat
   python --version
   python -V
   pip list
   pip install virtualenv
   ```
4. 範例提示字元為 `C:\Users\tony>`；`python --version` 顯示 **Python 3.9.7**。`pip list` 是 Package listing，顯示已安裝套件及版本：`pip 21.2.3`、`setuptools 57.4.0`。
5. `pip install virtualenv` 安裝虛擬環境建立工具，下一頁再建立環境。〔來源：P074〕

<a id="p075"></a>

### P075｜virtualenv 建立、啟動與 Django 安裝

[核對原講義第 75 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=75)

- 頁首 `C:\Users\tony>pip list` 圖列出安裝工具後的套件：`distlib 0.3.6`、`filelock 3.9.0`、`pip 21.2.3`、`platformdirs 3.0.0`、`setuptools 57.4.0`、`virtualenv 20.19.0`。
- virtualenv 用來建立隔離的 Python 套件環境，在其中安裝所需函式庫；不用時可刪除該環境資料夾。**補充辨析**：這是 Python 套件隔離，不是隔離整個作業系統的虛擬機；程式仍可能讀寫環境以外的檔案，原文「完全不影響原有作業系統」不宜絕對化。
- 講義另列移除工具指令 `pip uninstall virtualenv`，這是移除 virtualenv 套件，不等於刪除已建立環境；不是安裝流程中必須先執行的步驟。
- Windows CMD 操作順序：
  ```bat
  cd c:\
  virtualenv dvds
  cd dvds
  Scripts\activate
  pip install Django
  ```
- `cd` 是 Change Directory。`virtualenv dvds` 在 `C:\` 建立 `C:\dvds`。建立畫面使用 **CPython 3.8.10 64-bit**，seed 套件為 `pip 21.1.2`、`setuptools 57.0.0`、`wheel 0.36.2`，列出 Bash、Batch、Fish、PowerShell、Python、Xonsh activator。這又是不同時間的截圖。
- 啟動前為 `c:\dvds>`，執行 `Scripts\activate` 後變成 `(dvds) c:\dvds>`；前綴是啟動狀態的可見線索。啟動後的 `pip install Django` 才是安裝至此環境。〔來源：P075〕

<a id="p076"></a>

### P076｜Windows：建立 project、app、templates、static

[核對原講義第 76 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=76)

- 套件查詢正文寫 `pip list`，截圖是 `(dvds) c:\dvds>pip3 list`，清單為 `asgiref 3.6.0`、`Django 4.1.6`、`pip 23.0`、`setuptools 67.1.0`、`sqlparse 0.4.3`、`tzdata 2022.7`、`wheel 0.38.4`。
- `deactivate` 用來離開虛擬環境。**流程疑點**：原稿把此命令放在建立專案之前，但後面截圖仍有 `(dvds)`；實際建立專案時應確認所用 Python／django-admin 仍來自所需環境，不應盲目照順序退出後繼續。
- 原命令及用途：
  ```bat
  Django-admin startproject project1
  cd project1
  python manage.py startapp myapp
  mkdir templates
  mkdir static
  ```
  `Django-admin`（原稿大小寫；常見寫法 `django-admin`）為 Django 的專案建立、管理、測試工具；`startproject` 產生專案，`manage.py startapp` 在專案內建立可獨立分工的功能模組。截圖路徑為 `(dvds) c:\dvds\project1>`。
- `mkdir` 是 Make Directory。`templates` 存 HTML 畫面模板；`static` 存圖片、CSS 樣式及前端 JavaScript 等靜態檔案。
- 用 VS Code 開啟 `project1` 資料夾，修改內層 `project1/settings.py`：
  ```python
  ALLOWED_HOSTS = ['*']
  ```
- **補充安全辨析**：原文稱它為限制可連線 IP 的白名單，但它主要驗證 HTTP Host 主機名稱，不是來源 IP 防火牆。`'*'` 接受所有 Host，僅記錄講義示範，不應直接作正式部署建議。〔來源：P076〕

<a id="p077"></a>

### P077｜settings.py：ALLOWED_HOSTS 與 INSTALLED_APPS

[核對原講義第 77 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=77)

- 上方 VS Code 圖路徑麵包屑 `project1 > project1 > settings.py`；左側有 `DVDS/Lib`、`project1/myapp`、內層 `project1`，內含 `__pycache__`、`__init__.py`、`asgi.py`、`settings.py`、`urls.py`。紅框強調 `ALLOWED_HOSTS = ['*']`，其上可見 `DEBUG = True`（開發設定）。
- 將自己的 `myapp` 加入 `INSTALLED_APPS`，Django 才會把它註冊為已安裝應用，納入相關模型等管理：
  ```python
  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'myapp',
  ]
  ```
- 原有六個 contrib 模組依序是管理介面、驗證、內容類型、session、訊息、靜態檔支援；這些角色為輔助解讀。下圖把 `settings.py` 與新添的 `'myapp',` 各自框出；最後一行後保留逗號。頁底 `TEMPLATES = [` 接續下頁，不是完整設定。〔來源：P077〕

<a id="p078"></a>

### P078｜模板搜尋目錄與繁中／台北設定

[核對原講義第 78 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=78)

- 接上頁的完整模板設定如下；新增的關鍵是 `DIRS`：
  ```python
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [BASE_DIR / 'templates'],
          'APP_DIRS': True,
          'OPTIONS': {
              'context_processors': [
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
              ],
          },
      },
  ]
  LANGUAGE_CODE = 'zh-Hant'
  TIME_ZONE = 'Asia/Taipei'
  ```
- `BACKEND` 指 Django 模板引擎；`DIRS` 是額外模板搜尋清單。`BASE_DIR` 是專案根目錄的絕對路徑；`BASE_DIR / 'templates'` 使用路徑物件的組合運算形成模板路徑。`APP_DIRS=True` 也讓引擎搜尋已安裝 app 的模板。四個 context processor 分別提供除錯、request、auth、messages 的模板脈絡（角色為補充解讀）。
- 圖中紅框是 `'DIRS': [BASE_DIR / 'templates'],`；上方還可見 `ROOT_URLCONF = 'project1.urls'`。
- `LANGUAGE_CODE` 決定預設顯示語系，原稿用 `zh-Hant` 表示繁體中文；`TIME_ZONE` 改為 `Asia/Taipei` 台北時區。〔來源：P078〕

<a id="p079"></a>

### P079｜靜態檔搜尋路徑與 VS Code 終端

[核對原講義第 79 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=79)

- 上圖續前頁，設定 `LANGUAGE_CODE = 'zh-Hant'`、`TIME_ZONE = 'Asia/Taipei'`，並保留 `USE_I18N = True`、`USE_TZ = True`；分別與國際化、時區支援相關。
- 靜態檔設定如下：
  ```python
  STATIC_URL = 'static/'
  STATICFILES_DIRS = [
      BASE_DIR / 'static',
  ]
  ```
  `STATIC_URL` 是靜態資源 URL 前綴；`STATICFILES_DIRS` 是額外靜態檔目錄清單，`BASE_DIR / 'static'` 指向自建資料夾，不要把 URL 前綴與磁碟路徑混為一談。圖中註解指出 CSS、JavaScript、Images，文件版本路徑含 `/en/4.1/howto/static-files`。
- 下圖由 VS Code 選單 **View（檢視）→ Terminal（終端）** 開啟整合终端，快捷鍵畫面為 Ctrl+`。左側 `PROJECT1` 下同層可見 `myapp`、內層 `project1`、`static`、`templates`、`manage.py`；app 包含 migrations、admin.py、apps.py、models.py、tests.py、views.py 等。〔來源：P079〕

<a id="p080"></a>

### P080｜CMD 啟動環境、建立與套用 migrations

[核對原講義第 80 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=80)

1. 預設整合終端可能是 PowerShell；若受指令碼執行原則阻擋而不能啟動 Python 環境，本頁採用終端下拉選單 **Command Prompt**，不是調低系統安全政策。圖上先見 `PS C:\dvds\project1>`，切換後為 `C:\dvds\project1>` 的 cmd。
2. 在專案目录先啟動上一層的環境，再執行：
   ```bat
   ..\Scripts\activate
   python manage.py makemigrations myapp
   python manage.py migrate
   dir
   ```
3. `makemigrations` 比對模型修改並產生遷移檔；指定 `myapp` 限定 app，省略 app 名可檢查整個專案的 app。`migrate` 依遷移套用資料庫結構變更；兩者並非同一動作。
4. 遷移截圖從 `(dvds) c:\dvds\project1>` 執行，說明 `Apply all migrations: admin, auth, contenttypes, sessions`；以下記錄逐一為 `OK`：`contenttypes.0001_initial`、`auth.0001_initial`、`admin.0001_initial`、`admin.0002_logentry_remove_auto_add`、`admin.0003_logentry_add_action_flag_choices`、`contenttypes.0002_remove_content_type_name`、`auth.0002_alter_permission_name_max_length`、`auth.0003_alter_user_email_max_length`、`auth.0004_alter_user_username_opts`、`auth.0005_alter_user_last_login_null`、`auth.0006_require_contenttypes_0002`、`auth.0007_alter_validators_add_error_messages`、`auth.0008_alter_user_username_max_length`、`auth.0009_alter_user_last_name_max_length`、`auth.0010_alter_group_name_max_length`、`auth.0011_update_proxy_permissions`、`auth.0012_alter_user_first_name_max_length`、`sessions.0001_initial`。
5. `dir` 列出目前資料夾的檔案、子目錄、日期、容量，结果接下一頁。〔來源：P080〕

<a id="p081"></a>

### P081｜確認 SQLite 檔案與啟動開發伺服器

[核對原講義第 81 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=81)

- `dir` 圖為 `c:\dvds\project1`，列出 `db.sqlite3`（131,072 bytes）、`manage.py`（686 bytes）及 `myapp`、`project1`、`static`、`templates` 資料夾；歷史時間為2021/06/11。可用此目錄對照确认位於含 manage.py 的外層專案根目錄。
- 啟動指令：
  ```bat
  python manage.py runserver 0.0.0.0:8080
  ```
  `runserver` 是 Django 內建開發伺服器；`0.0.0.0` 代表在所有 IPv4 網路介面監聽，8080 是本例連接埠，講義用它避開原本8000可能已被其他程式使用的情況。區網設備需以伺服器實際 IP 連線，不是把 `0.0.0.0` 當遠端主機位址。
- 圖示輸出：`Watching for file changes with StatReloader`、`Performing system checks...`、`System check identified no issues (0 silenced).`；時間 `June 11, 2021 - 16:01:42`，**Django 3.2.4**，settings 為 `'project1.settings'`，`Starting development server at http://0.0.0.0:8080/`，Windows 用 `CTRL-BREAK` 停止。
- **補充**：監聽全部介面不保證其他裝置必然連得上，還受網路、防火牆、Host 驗證影響；runserver 是開發工具，不是正式生產伺服器。此頁版本與前面4.1.6不同，屬歷史範例混編。〔來源：P081〕

<a id="p082"></a>

### P082｜用瀏覽器核對 Django 初始成功頁

[核對原講義第 82 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=82)

- 此頁主要內容是一張 Chrome 截圖：網址列 **`127.0.0.1:8080`**，分頁標題 `The install worked successfully!`，頁首 `django` 及 `View release notes for Django 3.2`，中央綠色火箭向上飛。
- 主訊息為 **`The install worked successfully! Congratulations!`**；下文說明看見本頁是因為設定檔 `DEBUG=True` 且尚未配置 URL。
- 知識重點：啟動終端顯示無錯誤後，仍應在瀏覽器以本機 loopback 與相同連接埠檢查回應；預設歡迎頁只代表基礎專案已可回應，不是已完成自訂 app 畫面或正式部署。本次僅閱讀此歷史成功畫面，未實際啟動服務。〔來源：P082〕

<a id="p083"></a>

### P083｜Windows + VS Code：擴充套件與 PATH

[核對原講義第 83 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=83)

- 安裝 VS Code 擴充套件：**Python、Django、Django Template**。此處是編輯器擴充功能，不是用 pip 安裝 Django 的替代步驟。
- 第一張圖在 Extensions 搜尋 `python`，選 Microsoft 的 **Python**（`ms-python.python`），介紹 IntelliSense／Pylance、Linting、Debugging 等功能，按 Install。第二張圖搜尋 `Dj`，選 **Django 1.6.0**、作者 Baptiste Darthenay、識別碼 `batisteo.vscode-django`，說明語法和程式片段支援。Django Template 本頁僅條列，未展示其作者或識別碼，不另猜測。
- 講義參考〈2021 Django Python 開發 VSCode 套件推薦 Top 10 [必裝]〉：https://www.codecroc.com.tw/2021/09/30/2021-django-python-dev-vscode-extension-recommendation-top-10-must-have/
- 原流程到 **本機 → 內容 → 進階設定 → 環境變數 → Path** 新增：
  ```text
  C:\dvds
  C:\dvds\Scripts
  ```
  應依實際 Python／環境位置調整。**補充辨析**：把某專案虛擬環境永久加到全域或使用者 PATH 並非每個專案必要；可能導致其他專案誤用該環境。此處只記錄講義作法，未變更任何環境變數。〔來源：P083〕

<a id="p084"></a>

### P084｜編輯 PATH、重啟 VS Code、選擇環境解譯器

[核對原講義第 84 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=84)

1. 第一圖是 `user 的使用者變數`，選中 PATH 後按「編輯」；可見 OneDrive、PATH、TEMP、TMP。
2. 第二圖「編輯環境變數」清單原有：
   ```text
   C:\Users\user\AppData\Local\Programs\Python\Python39\Scripts\
   C:\Users\user\AppData\Local\Programs\Python\Python39\
   C:\dvds\Scripts
   C:\dvds
   ```
   後兩項是此教學追加的環境路徑，右側提供「新增、編輯、瀏覽」。
3. 重啟 VS Code 後開專案，點狀態列左下／右下的 Python 版本，進入 **Select Interpreter**。清單同時有全域 Python 3.9.7 64-bit、Recommended／Global 標記及 **Python 3.9.7 ('dvds') `C:\dvds\Scripts\python.exe`**（Venv）；應選專案虛擬環境，不只看版本相同就認為是同一個 Python。亦可用 `Enter interpreter path...` 指定。
4. 圖中 `settings.py` 使用 `from pathlib import Path`，`BASE_DIR = Path(__file__).resolve().parent.parent`，終端在 `C:\dvds\project1>`；下一步點 **Start Debugging**。〔來源：P084〕

<a id="p085"></a>

### P085｜選 Django 偵錯設定並啟動

[核對原講義第 85 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=85)

- 第一圖選單 **Run → Start Debugging**（F5），另列 Run Without Debugging（Ctrl+F5）、Stop（Shift+F5）、Restart（Ctrl+Shift+F5）、Open Configurations、Add Configuration 等。
- 接著在偵錯設定選擇器點 **Django**（啟動並偵錯 Django 網路應用程式）；其他選項包含 Python 檔案、模組、遠端連結、使用處理程序 ID 連結、FastAPI，不應選錯成單純目前 Python 檔案。
- 本頁範例專案已切換為 **ALBUM**，不是前頁 project1；左側有 `album`、`albumapp`、`media`、`static`、`templates`、`db.sqlite3`、`manage.py`，templates 顯示 `adminadd.html`、`adminmain.html`、`base.html`、`baseadmin.html`。背景 urls.py 可見 `path('admin/', admin.site.urls)` 及 baseadmin、adminadd、adminmain 對應 views 的路由；這裡展示既有專案環境，不代表本頁已教授這些頁面實作。
- 下圖出現偵錯浮動工具列，狀態列變橘色；Python **3.8.10 64-bit**，終端 `System check identified no issues (0 silenced).`、`July 30, 2021 - 17:33:45`、**Django 3.2.4**、設定 `'album.settings'`，開發網址 **`http://127.0.0.1:8000/`**，停止為 `CTRL-BREAK`。此為預設本機8000，不是先前手動的8080。〔來源：P085〕

<a id="p086"></a>

### P086｜偵錯後瀏覽測試與新增非本機監聽設定

[核對原講義第 86 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=86)

- 上圖瀏覽器輸入 `127.0.0.1:8000`，出現 Django 3.2 火箭歡迎頁、安裝成功訊息及 `DEBUG=True`／未配置 URL 提示；本頁驗證位址對應上一頁預設8000。
- 原參考文獻：
  - https://yijay131724.blogspot.com/2021/02/python-visual-studio-code-python.html
  - https://dotblogs.com.tw/brian90191/2019/04/02/115926
- 下半開始「允許非本機連線」：在 VS Code **Run → Add Configuration...**；左側示範專案改為 **USERCREATIONFORM**，可見 `.vscode/launch.json` 與 `myapp`。新增偵錯設定的具體內容接下頁；不是只點此選項就已開放網路。〔來源：P086〕

<a id="p087"></a>

### P087｜launch.json：Django 偵錯監聽 0.0.0.0:8080

[核對原講義第 87 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=87)

- 本頁為單張 `.vscode/launch.json` 圖，紅框特別標示 `args` 內的 `runserver` 與監聽位址。完整設定（省略 VS Code 自帶說明註解；原註解指向 https://go.microsoft.com/fwlink/?linkid=830387）：
  ```json
  {
      "version": "0.2.0",
      "configurations": [
          {
              "name": "Python: Django",
              "type": "python",
              "request": "launch",
              "program": "${workspaceFolder}\\manage.py",
              "args": ["runserver", "0.0.0.0:8080"],
              "django": true,
              "justMyCode": true
          }
      ]
  }
  ```
- `version` 是偵錯設定格式版本，不是 Python／Django 版本；`name` 是選單顯示名；`type` 為當時 Python 擴充的偵錯類型；`request=launch` 是啟動程式；`${workspaceFolder}` 由 VS Code 展開為工作區根目錄，Windows 反斜線在 JSON 字串須寫 `\\`；`args` 傳入 manage.py 的命令及位址，`django=true` 啟用 Django 偵錯支援，`justMyCode=true` 以自己的程式碼為主。
- **歷史／安全註記**：保留原圖 `type: python`，未假稱適用所有現行偵錯器版本。開放監聽仍需配合合適 Host 設定與網路規則；勿將開發偵錯埠無限制暴露。〔來源：P087〕

<a id="p088"></a>

### P088｜複製專案：外層目錄與內層 package 都改名

[核對原講義第 88 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=88)

1. 複製既有專案後，將外層目錄改名 **test**，內層同名 Python 專案 package 也改成 **test**。不是只改 Windows 資料夾顯示名稱。
2. 第一張檔案總管圖位於 `C:\dvds`，選中 `test`，旁邊可見其他專案 login、news、newsadm、project1、project2、project3、tagfilter、webapi1 與環境 Scripts 等。
3. 第二圖進入 `C:\dvds\test`，內含 `.vscode`、`myapp`、`static`、`templates`、紅框內層 `test`、`db.sqlite3`、`manage.py`。這說明複製會帶入既有 app、模板、靜態資源與資料庫，而不是全新空專案。
4. 用 VS Code 開啟此專案，修改 **settings.py、wsgi.py、manage.py、asgi.py** 中的專案模組名稱，結果見P089–P090。**補充**：正式操作應檢查複製的資料庫內容、SECRET_KEY 和環境特定設定，不宜因檔案複製完成就視為獨立安全部署。〔來源：P088〕

<a id="p089"></a>

### P089｜重命名後的 URL、WSGI 與 settings module

[核對原講義第 89 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=89)

- 本頁四張程式截圖框出必要的名稱替換：
  ```python
  # test/settings.py
  ROOT_URLCONF = 'test.urls'
  WSGI_APPLICATION = 'test.wsgi.application'

  # test/wsgi.py
  import os
  from django.core.wsgi import get_wsgi_application
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test.settings')
  application = get_wsgi_application()

  # manage.py 的 main() 裡
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test.settings')
  ```
- `ROOT_URLCONF` 指向新的根路由模組；`WSGI_APPLICATION` 指向新 package 的 WSGI callable；`DJANGO_SETTINGS_MODULE` 告訴管理入口與 WSGI 使用哪個設定模組。不更新會繼續找旧模組或匯入失敗。
- wsgi.py 原註解可見文件連結 https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/ 。背景 settings.py 保留 session、common、CSRF、authentication、messages、clickjacking middleware；本步只是改模組名稱，不是刪除中介層。〔來源：P089〕

<a id="p090"></a>

### P090｜ASGI 名稱及跨檔案搜尋取代

[核對原講義第 90 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=90)

- 第一圖為 asgi.py，需配合同樣的設定模組名稱：
  ```python
  import os
  from django.core.asgi import get_asgi_application
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test.settings')
  application = get_asgi_application()
  ```
  文件註解指向 https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/ 。**原圖不一致**：工作區與內層目錄仍顯示 `UserCreationForm01`，docstring 顯示 sample project，紅框卻改成 `test.settings`；應以實際 package 名一致為準，不能直接抄混用名称。
- 第二種重命名方法：**Edit → Replace in Files**（Ctrl+Shift+H），在跨檔案搜尋輸入旧名、取代欄輸入新名，再使用 Replace All。圖中此例是把 **`homework5` 改成 `homework6`**，不是 test 範例；提示 **`Replaced 5 occurrences across 4 files with 'homework6'.`**。
- **補充操作辨析**：先檢查命中項目再取代，避免把無關字串一併修改；字串取代不會自動將外層與內層資料夾重新命名，仍要完成P088的目录改名。〔來源：P090〕

<a id="p091"></a>

### P091｜Linux：套件索引、virtualenv 與 Python 版本

[核對原講義第 91 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=91)

- Linux／Raspberry Pi 教學起始命令，僅保存原稿，**本次未執行安裝或系統升級**：
  ```bash
  sudo apt-get update -y
  sudo apt-get upgrade –y   # 原稿標明「先不要用」；其 – 是印刷長橫線
  python3 --version
  sudo pip3 install virtualenv
  sudo pip3 uninstall virtualenv
  pip3 list
  virtualenv dvds
  source dvds/bin/activate
  python --version
  deactivate
  pip3 install django
  ```
- `update` 更新套件索引；`upgrade` 是更新已安裝系統套件，原稿特別叫讀者先不要做。`sudo pip3 uninstall virtualenv` 只是對應移除指令，不能理解為建立環境前必須先卸載。
- 第一圖提示字元 `(dvdsenv) pi@raspberrypi:~/dvds2 $` 的 `python3 --version` 是 **Python 3.5.3**。建立環境圖卻用 `sudo virtualenv dvds`（與正文無 sudo 不同），目的地 `/home/pi/dvds`、CPython3.5.3 32-bit，seed `pip 20.3.4`、`setuptools 50.3.2`、`wheel 0.37.0`；建立的 activator 包含 Bash、Fish、CShell、Nushell、PowerShell、Python。
- 啟動圖從 `pi@raspberrypi:~ $ source dvds/bin/activate` 變為 `(dvds) pi@raspberrypi:~ $`；後面的 `python --version` 卻顯示 **3.9.2**，顯然混入不同環境或時間的截圖，不能當成 virtualenv 自動把3.5.3升級至3.9.2。
- **流程／安全補充**：安裝 Django 前應保持目標虛擬環境啟動，`deactivate` 是離開環境用的獨立指令；原稿排列在 pip 安裝之前有誤用風險。`sudo pip` 可能更動系統 Python 套件，建立環境使用 sudo 也可能造成 root 檔案擁有權問題；不把這些歷史指令當無條件推薦。〔來源：P091〕

<a id="p092"></a>

### P092｜Linux：Django 歷史安裝畫面、建立專案與 app

[核對原講義第 92 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=92)

- 最上方是舊 `pip install django` 畫面：警告 **Python 3.5 已在2020/09/13結束支援**，pip21.0將停止支援；索引為 `https://pypi.org/simple` 和 `https://www.piwheels.org/simple`，下載／使用快取 Django2.2.25、sqlparse0.4.2、pytz2021.3；最後 `Successfully installed django-2.2.25 pytz-2021.3 sqlparse-0.4.2`。
- 下一張 `pip3 list` 卻是新版環境：`asgiref 3.6.0`、`Django 4.1.6`、`pip 23.0`、`setuptools 67.1.0`、`sqlparse 0.4.3`、`wheel 0.38.4`。**這不是同一次安裝前後一致清單，不可推論Python3.5能安裝該Django4.1.6。**
- 保持 `(dvds)` 啟動狀態，Linux 指令流程：
  ```bash
  pip3 list
  cd dvds
  django-admin startproject project1
  ls
  cd project1
  python manage.py startapp myapp
  ls
  mkdir templates
  ```
- 在 `~/dvds` 的 `ls` 顯示 `bin lib project1 pyvenv.cfg`；`project1` 建在虛擬環境目录裡。進入 `~/dvds/project1` 後 `ls` 顯示 `manage.py myapp project1`，分清外層工作目录與內層 Python package；`mkdir templates` 建在含 manage.py 的層級。〔來源：P092〕

<a id="p093"></a>

### P093｜Linux：建立 static、用 Vim 設定 app 與 Host

[核對原講義第 93 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=93)

- 承上頁、目前在 `~/dvds/project1`：
  ```bash
  mkdir static
  vim project1/settings.py
  ```
- 設定內容：
  ```python
  ALLOWED_HOSTS = ['*']
  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'myapp',
  ]
  ```
- 終端標題是 `pi@raspberrypi: ~/dvds/project1`；Vim 底部 `-- INSERT --` 表示正編輯，紅框分別標示 `ALLOWED_HOSTS` 和清單末端 `'myapp',`。圖上方仍為 `DEBUG = True`，並含「不要在正式環境開啟除錯」以及保護 SECRET_KEY 的警告註解；截圖中開發用 secret 的具體隨機字串非應複製設定。
- **補充**：`'*'` 是 Host 驗證的廣泛開放，不是來源 IP 存取控制；新增 app 並不取代後續 migrations。〔來源：P093〕

<a id="p094"></a>

### P094｜Linux：模板設定完整內容

[核對原講義第 94 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=94)

- 用 Vim 在相同 settings.py 填入根目錄模板搜尋路徑；本頁雖與Windows相同，保留 Linux 路徑與畫面步驟：
  ```python
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [BASE_DIR / 'templates'],
          'APP_DIRS': True,
          'OPTIONS': {
              'context_processors': [
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
              ],
          },
      },
  ]
  ```
- `DIRS` 新增 `~/dvds/project1/templates` 所對應的绝對路徑；`BASE_DIR` 對應外層根目錄。`APP_DIRS=True` 的 app 模板搜尋與此額外目錄並存；OPTIONS 保留四個 context processor。
- 下方Vim圖的紅框定位 `DIRS`；同圖可見 `ROOT_URLCONF = 'project1.urls'` 與 `WSGI_APPLICATION = 'project1.wsgi.application'`，底部 `-- INSERT --`。〔來源：P094〕

<a id="p095"></a>

### P095｜Linux：繁中、時區與 static 設定

[核對原講義第 95 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=95)

- 同一個 `project1/settings.py` 的修改如下：
  ```python
  LANGUAGE_CODE = 'zh-Hant'
  TIME_ZONE = 'Asia/Taipei'
  USE_I18N = True
  USE_TZ = True

  STATIC_URL = 'static/'
  STATICFILES_DIRS = [
      BASE_DIR / 'static',
  ]
  ```
- 第一張Vim圖以紅框包住語系及時區，下面保留 `USE_I18N`／`USE_TZ`；上方還有 CommonPasswordValidator、NumericPasswordValidator 的既有設定。文件註解是 `/en/4.1/topics/i18n/`。
- 第二張圖在約119–123行框出 STATIC_URL 及 STATICFILES_DIRS，註解指出 CSS、JavaScript、Images，參考 `/en/4.1/howto/static-files/`；下方有 Default primary key field type 的說明，但具體欄位值在畫面外，不補造。
- 預期 templates／static 均在 `/home/pi/dvds/project1/` 下；URL `static/` 與磁碟目錄用途不同。〔來源：P095〕

<a id="p096"></a>

### P096｜Linux：沒有模型變更仍需遷移內建 app

[核對原講義第 96 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=96)

```bash
python manage.py makemigrations myapp
python manage.py migrate
ls
python manage.py runserver 0.0.0.0:8080
```

- 終端位於 `(dvds) pi@raspberrypi:~/dvds/project1 $`。`makemigrations myapp` 回覆 **`No changes detected in app 'myapp'`**；新建 app 尚未定義模型時可能沒有新遷移，這不是錯誤。
- `migrate` 仍有內建 app 的遷移要套用，清單 admin、auth、contenttypes、sessions。圖示逐一OK：`contenttypes.0001_initial`、`auth.0001_initial`、`admin.0001_initial`、`admin.0002_logentry_remove_auto_add`、`admin.0003_logentry_add_action_flag_choices`、`contenttypes.0002_remove_content_type_name`、`auth.0002_alter_permission_name_max_length`、`auth.0003_alter_user_email_max_length`、`auth.0004_alter_user_username_opts`、`auth.0005_alter_user_last_login_null`、`auth.0006_require_contenttypes_0002`、`auth.0007_alter_validators_add_error_messages`、`auth.0008_alter_user_username_max_length`、`auth.0009_alter_user_last_name_max_length`、`auth.0010_alter_group_name_max_length`、`auth.0011_update_proxy_permissions`、`sessions.0001_initial`。本圖未列P080中的 auth.0012，不能因同為遷移流程而抹去版本差異。
- `ls` 圖顯示 `db.sqlite3 manage.py myapp project1 static templates`；最後開放所有介面8080的 runserver，結果接下頁。〔來源：P096〕

<a id="p097"></a>

### P097｜Linux：Django4.1.6 伺服器紀錄與遠端瀏覽

[核對原講義第 97 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=97)

- 終端 `python manage.py runserver 0.0.0.0:8080`，StatReloader 監看變更，system check 無問題；畫面日期 **February 13, 2023 - 11:45:18**，版本 **Django4.1.6**，使用 `project1.settings`；啟動網址 `http://0.0.0.0:8080/`，Linux 用 **CONTROL-C** 停止。
- HTTP 日誌顯示 `/` 回覆200（10626），`/static/admin/css/fonts.css` 回覆200（423），Roboto Bold、Regular、Light 的 woff 字型各回覆200；只有 `/favicon.ico` 顯示 `Not Found`，狀態404（2116）。**補充解讀**：缺少網站小圖示不等於主頁失敗；應區分每一筆請求，而非見404就認為整個 Django 壞掉。
- 下方 Chrome 位址是 **`172.16.100.43:8080`**（不安全／HTTP提示），頁面改為繁中「安裝成功！恭喜！」，Django4.1 發行筆記連結，`DEBUG=True` 未配置網址提示；底部三項為 Django文件、教學：投票應用、Django社群。這個 IP 是示範遠端伺服器，不是每位讀者的固定值。
- 參考：https://mikesmithers.wordpress.com/2017/02/21/configuring-django-with-apache-on-a-raspberry-pi/ 、https://www.cnblogs.com/baby123/p/12122703.html 。〔來源：P097〕

<a id="p098"></a>

### P098｜延伸參考與 Remote Development 建立 SSH 主機

[核對原講義第 98 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=98)

- 上方延伸網址及原用途：
  - Django skeleton website：https://developer.mozilla.org/zh-TW/docs/Learn/Server-side/Django/skeleton_website
  - 「Django 中直接使用 sql 語句操作資料庫」：https://blog.csdn.net/haeasringnar/article/details/82080476
  - https://openhome.cc/Gossip/CodeData/PythonTutorial/AppModelPy3.html
  - 「在 Django 使用 MySQL 資料庫」：https://jerrynest.io/django-mysql-database/
  這裡僅提供參考連結，未在本頁展示 SQL／MySQL 安裝或查詢程式，不把外部文章內容冒充講義內文。
- 新節「Linux + Visual Studio Code + Remote Development」：先安裝 Microsoft **Remote Development** 擴充套件，再建立連結。
- 上圖打開 Remote Explorer，在 SSH 旁按 **+（New Remote）**，輸入 SSH Connection Command：
  ```bash
  ssh root@192.168.65.161
  ```
  Enter確認、Escape取消。**補充**：這是原圖示範登入帳號和私網IP，不代表應固定用root開發；不需也未嘗試連到此主機。
- 下圖選擇寫入 SSH 設定的檔案：**`C:\Users\tony\.ssh\config`**；另可選 `C:\ProgramData\ssh\ssh_config`，或 Settings 指定自訂設定檔、查看SSH設定說明。使用者設定與系統設定的作用範圍不同，不能混淆。〔來源：P098〕

<a id="p099"></a>

### P099｜SSH 連線、登入提示與 connected 狀態

[核對原講義第 99 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=99)

1. Remote Explorer 左側選 SSH 主機 **192.168.65.161**，按主機右側箭頭 **Connect in Current Window...**；同清單另有 **172.16.100.43** 及最近開啟的 dvds／pi 資料夾。
2. 第二圖是遮蔽字元的密碼輸入框，提示 Enter確認、Escape取消；講義未提供可讀密碼，不應猜测或把遮蔽圓點當密碼。
3. 連線成功時，主機後出現 **connected**（第三圖紅框），表示 SSH 工作階段已建立；這不等同 Django 服務已啟動。
4. 若未連線，可在主機右鍵選 **Connect in Current Window...**，也有 **Connect in New Window...**；第四圖示範主機改為172.16.100.43。左側遠端探索圖示均以紅框指示。〔來源：P099〕

<a id="p100"></a>

### P100｜遠端工作區要開環境根目錄

[核對原講義第 100 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=100)

- 連到遠端後尚未開資料夾，Explorer 顯示 `NO FOLDER OPENED`、`Connected to remote.`；可以按 **Open Folder**，或從 **File → Open Folder...**（Ctrl+K Ctrl+O）開啟。
- 講義紅字明確要求此套配置選 **`/home/pi/dvds/`**，**不要選 `/home/pi/dvds/projectName/`**。這是為了後續 `${workspaceFolder}/project1/manage.py` 的相對路徑布局，不是 VS Code 永遠不能以專案根目錄當工作區。
- 遠端 Open Folder 對話框輸入 `/home/pi/dvds/`，按OK；列表可見 `.vscode`、`bin`、`lib`、`project1`。旁有 **Show Local** 按鈕，提醒此時挑選的是遠端檔案系統而非Windows本機。
- 下圖可能再次要求登入驗證，仍是遮蔽密碼；Explorer 標示 `PI [SSH: 172.16.100.43]`。若已記錄資料夾連線，接下頁從遠端最近資料夾重開。〔來源：P100〕

<a id="p101"></a>

### P101｜重開遠端資料夾、在 SSH 主機安裝 Python 擴充

[核對原講義第 101 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=101)

1. 在 Remote Explorer 展開 `172.16.100.43 connected`，對底下 **dvds** 右鍵 → **Connect in Current Window...**；也能開新視窗或 `Remove from Recent List`（僅移除最近項目，不是刪除伺服器資料夾）。
2. 到 Extensions 搜尋 Python，選 Microsoft **Python v2023.2.0**，按 **Install in SSH: 172.16.100.43**。畫面提示擴充功能在此工作區尚未啟用，要安裝到指定SSH端；只在本機裝過不代表遠端也已裝好。
3. 點狀態列 Python 選 **Python 3.9.2 ('dvds': venv)**（Recommended）。圖中顯示 `/bin/python`，清單另有 Python3.9.2 32-bit 的全域項目。**原圖路徑疑點**：顯示文字沒有充分說明 `/bin/python` 與 `/home/pi/dvds/bin/python` 的關係；應核對實際解譯器，不能只因標記venv就假定路徑正確。
4. 左側工作區是 `DVDS [SSH: 172.16.100.43]`，包含 `.vscode/launch.json`、bin、lib、project1。下方綠色狀態列同樣標出SSH目標；最後 **Run → Start Debugging**（F5）。〔來源：P101〕

<a id="p102"></a>

### P102｜遠端 Django 偵錯入口與 Open Configurations

[核對原講義第 102 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=102)

- 偵錯設定選擇器點 **Django — Launch and debug a Django web application**；清單還列 Python File、Module、Remote Attach、Attach using Process ID、FastAPI、Flask、Pyramid。不要把 Remote SSH 開發與 `Remote Attach` 偵錯附加選項混為一談。
- 「Debug Django」輸入要啟動的 manage.py 路徑：
  ```text
  ${workspaceFolder}/project1/manage.py
  ```
  對應前頁開的 `/home/pi/dvds`，所以 manage.py 位於 `/home/pi/dvds/project1/manage.py`；Enter確認，Escape取消。
- 修正參數時從 **Run → Open Configurations**，打開工作區 `.vscode/launch.json`。下方圖同時框出Run選單、Open Configurations及launch.json；背景可見 program 指向上述路徑，args 有 `runserver`、`0.0.0.0:8080`，具體完整設定接P103。
- 圖片切换成 `DVDS [SSH: 192.168.1.2]`，與上方172.16.100.43不同，顯示這是另一套歷史示範，不能將全部IP當同一台機器。〔來源：P102〕

<a id="p103"></a>

### P103｜Linux 遠端 launch.json 與更換專案

[核對原講義第 103 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=103)

- `.vscode/launch.json` 上圖紅框含 `program` 與 `args`，完整設定如下（原圖是允許註解／尾逗號的 VS Code JSONC；此處去掉註解與尾逗號呈現等值JSON）：
  ```json
  {
      "version": "0.2.0",
      "configurations": [
          {
              "name": "Python: Django",
              "type": "python",
              "request": "launch",
              "program": "${workspaceFolder}/project1/manage.py",
              "args": ["runserver", "0.0.0.0:8080"],
              "django": true,
              "justMyCode": true
          }
      ]
  }
  ```
- 與P087 Windows設定的重要差異：Linux用正斜線，且工作區為 `dvds`，manage.py 在 `project1` 子目錄，所以不能省略 `/project1/`。
- 原文說想重來或改變專案，可以刪除或修改下圖參數；下圖小紅框專指 program 中的 **`project1`**，改成實際目標專案名。應讓工作區、program位置、解譯器以及專案內部settings名稱一致；不是只換偵錯設定的顯示name就能切換專案。〔來源：P103〕

<a id="p104"></a>

### P104｜遠端 VS Code 偵錯啟動的實際畫面證據

[核對原講義第 104 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=104)

- 上圖將整個 `configurations` 內的 Django 設定物件框起，和P103相同：`name=Python: Django`、`type=python`、`request=launch`、`${workspaceFolder}/project1/manage.py`、`runserver`／`0.0.0.0:8080`、`django=true`、`justMyCode=true`；上方有暫停、步進、重新啟動、停止的偵錯工具列。
- 下圖工作區 `DVDS [SSH: 172.16.100.43]`，目錄含 `.vscode`、bin、lib、project1、`.gitignore`、`pyvenv.cfg`；project1內有myapp、內層project1、static、templates、db.sqlite3、manage.py。開啟的是 `project1/myapp/views.py`，只有 `from django.shortcuts import render` 及 `# Create your views here.`，尚未寫自訂視圖。
- **已將原PDF終端區域局部重繪放大核讀**：自動啟動命令先 `cd /home/pi/dvds`，以 `/usr/bin/env /home/pi/dvds/bin/python` 呼叫 `/home/pi/.vscode-server/extensions/ms-python.python-2023.2.0/pythonFiles/lib/python/debugpy/adapter/../../debugpy/launcher`，當時launcher端口37701，再 `-- /home/pi/dvds/project1/manage.py runserver 0.0.0.0:8080`。這是擴充產生的暫態命令，不是要手抄固定37701。
- 此圖能確定實際執行用 **`/home/pi/dvds/bin/python`**，補足P101選單 `/bin/python` 短顯示的疑點。輸出：StatReloader、system checks無問題、**February 13, 2023 - 14:40:13**、**Django4.1.6**、`project1.settings`、`http://0.0.0.0:8080/`、CONTROL-C停止。
- 以上為教材圖中的執行證據，不是本次在環境中啟動的服務。〔來源：P104〕

<a id="p105"></a>

### P105｜远端瀏覽成功與 SSH 疑難排除的安全辨析

[核對原講義第 105 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=105)

- 上圖 Chrome 開 **`172.16.100.43:8080`**，HTTP「不安全」提示，Django4.1繁中火箭頁：「安裝成功！恭喜！」；下文 `DEBUG=True` 且未配置任何網址。這確認講義例子能從瀏覽器存取遠端開發伺服器。
- 原稿紅字：「若連線有問題，請將 windows 系統中，`c:\使用者\user\.ssh` 內的資料刪除」。下圖實際檔案總管為 `C: > 使用者 > tony > .ssh`，紅框只有 **`config`**、**`known_hosts`** 兩個檔案（圖示日期2023/4/7）。
- **重要補充／原稿風險**：不要把整個 `.ssh` 刪除當通用修復。`config` 儲存SSH連線設定，`known_hosts` 記錄已信任主機金鑰；實際 `.ssh` 還可能存放不可重建的私鑰。刪除全部會丟設定、破壞其他連線並取消既有主機驗證紀錄。若是主機金鑰變更，須先從可信途徑驗證新指紋，再只處理該主機項目；若是帳號／網路／路徑問題，刪known_hosts也不能解決。本次**未刪除任何SSH檔案或修改安全設定**。〔來源：P105〕

<a id="p106"></a>

### P106｜再次整理建立專案與 Project / Application 的關係

[核對原講義第 106 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=106)

- 「3-2 建立 Django 專案」列出的原流程：
  ```bash
  cd ~/dvds
  source ./dvds/dvdsenv/bin/activate
  django-admin startproject project1
  cd project1
  tree
  ```
- **原稿路徑疑點**：已 `cd ~/dvds` 後再用 `./dvds/dvdsenv/bin/activate` 會指向 `~/dvds/dvds/dvdsenv/bin/activate`；除非真的有這種巢狀布局，否則不合前面的 `~/dvds/bin/activate`。環境名稱也由dvds改為dvdsenv，不能默默合併修正。應以實際環境路徑為準。
- 第一張 `ls` 圖在 `(dvdsenv) pi@raspberrypi:~/dvds/project1`，已經有 `db.sqlite3 manage.py myapp project1 static templates`；因此不是純 `startproject` 剛建立的空專案。第二張 `tree` 圖卻在 `~/project1`，顯示較早版本初始結構：
  ```text
  .
  ├── manage.py
  └── project1
      ├── __init__.py
      ├── settings.py
      ├── urls.py
      └── wsgi.py
  # 1 directory, 5 files
  ```
- 檔案職責表：`manage.py` 為Python專案管理命令入口，可建app、啟動Server／Shell；`__init__.py` 為空檔，使目录成為Python package；`settings.py` 是設定；`urls.py` 是URL配置；`wsgi.py` 是網頁伺服器與Django的WSGI介面設定（託管）。此舊圖未含asgi.py，不能說所有版本均只有這五檔。
- 「3-3 建立 Application」：app 是project的功能元件，可作為其他專案的模組重用；一個project可包含一或多個app。頁末進入「建立應用程式」，命令接P107。〔來源：P106〕

<a id="p107"></a>

### P107｜app 骨架、MTV、templates/static 與設定入口

[核對原講義第 107 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=107)

- 原稿並列兩種歷史啟動方式（括號內原拼為pyhton3／pyhton2）：
  ```bash
  sudo python3 manage.py startapp myapp   # 原標Python3
  sudo python manage.py startapp myapp    # 原標Python2
  mkdir templates static
  tree
  vim project1/settings.py
  ```
- **補充／版本辨析**：`python` 不必然是Python2，要看實際解譯器；這些Python2例子屬歷史材料。建立自己的app通常不需要sudo，sudo可能改用另一個Python及留下root所有的檔案，不能因虛擬環境前綴仍在就保證sudo沿用它。
- Django 採 **MTV（Model、Template、View）** 分工；模板 `.html` 放templates，圖片、CSS、JavaScript放static。本講義採在專案最上層（manage.py同層）建這兩資料夾；**補充**：這是本例配置方式，不是Django只允許此配置，app內也能有模板和靜態目錄。
- `ls` 圖在 `(dvdsenv) ~/dvds/project1` 顯示 `manage.py myapp project1 static templates`。`tree` 圖主要展示 myapp：`admin.py`、`apps.py`、`__init__.py`、`migrations/__init__.py`、`models.py`、`tests.py`、`views.py`；還有 `__pycache__` 下 `admin.cpython-35.pyc`、`__init__.cpython-35.pyc`、`models.cpython-35.pyc`，以及 migrations內的 `__pycache__/__init__.cpython-35.pyc`。這些pyc是執行产生的快取，不是要手動建立的原始碼。
- 圖中tree還出現 `db.sqlite3` 與static/templates，但沒有完整展示前圖的內層project1，樹線有`?`亂碼；把它當局部／不同階段截圖，不用它刪減應有檔案。最後進入「除錯模式設定與權限瀏覽」，設定畫面接下頁；原文說`*`是全部IP，需按Host驗證概念理解。〔來源：P107〕

<a id="p108"></a>

### P108｜DEBUG、具體 Host 清單、註冊 app 與 os.path 模板路徑

[核對原講義第 108 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=108)

- 第一圖保留開發設定及安全警告：
  ```python
  DEBUG = True
  ALLOWED_HOSTS = ['*']
  ```
  圖中SECRET_KEY是教材開發隨機值；不可複用至正式專案。註解明言不要在production開DEBUG。
- 第二個小圖改示「add the original IP and/or hostname also」的具體清單，**忠實保留原示例**：
  ```python
  ALLOWED_HOSTS = [
      'localhost',
      '127.0.0.1',
      '111.222.333.444',
      'mywebsite.com'
  ]
  ```
  **原稿疑點**：`111.222.333.444` 不是有效IPv4（有超出合法八位組範圍的分段），僅能視為不合規示意字串，不能照貼當真實IP；應填實際主機名稱／位址。這項控制的是HTTP Host而非客戶端來源IP。
- Application註冊圖是以下完整清單：
  ```python
  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'myapp',
  ]
  ```
- 本頁模板路徑改採較早的 `os.path.join` 風格，**先加入 `import os`**，再於 `TEMPLATES` 字典設：
  ```python
  import os
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [os.path.join(BASE_DIR, 'templates')],
          'APP_DIRS': True,
          'OPTIONS': {
              'context_processors': [
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
              ],
          },
      },
  ]
  ```
- 紅框只改DIRS，其餘模板引擎和processor保留。與P078／P094 `BASE_DIR / 'templates'` 的差別是路徑API；應配合BASE_DIR實際型別，不把字串BASE_DIR誤當Path直接使用 `/`。正文 `TEMPATES` 為 `TEMPLATES` 的漏字拼誤。〔來源：P108〕

<a id="p109"></a>

### P109｜較早設定中的 USE_L10N、static 與 makemigrations

[核對原講義第 109 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=109)

- 語系與時區設定入口原命令 `sudo vim project1/settings.py`；第一張圖片包含：
  ```python
  LANGUAGE_CODE = 'zh-Hant'
  TIME_ZONE = 'Asia/Taipei'
  USE_I18N = True
  USE_L10N = True
  USE_TZ = True
  ```
  `USE_L10N=True` 是此舊設定圖特有的本地化格式開關，前面的新版圖未列。保留歷史差異，不假稱所有Django版本都使用這一項。
- 再列一次 `sudo vim project1/settings.py` 設靜態檔；正文與圖一致：
  ```python
  STATIC_URL = 'static/'
  STATICFILES_DIRS = [
      BASE_DIR / 'static',
  ]
  ```
  此頁卻混用較新的Path風格，與前頁os.path.join不必互斥，但必須檢查BASE_DIR定義，不能忽略版本／型別背景。
- migration把建立資料表的結構與版本記錄下來，以利日後追蹤。原稿：
  ```bash
  sudo python3 ./manage.py makemigrations  # Python3示例
  sudo python ./manage.py makemigrations   # Python2示例
  ```
- 實際教材圖命令是 `(dvdsenv) pi@raspberrypi:~/dvds2/project1 $ sudo ./manage.py makemigrations`，回覆 `No changes detected`，又與正文省略／指定解譯器的方式不同。直接執行manage.py還取決於檔案權限與shebang；在此不聲稱執行過。〔來源：P109〕

<a id="p110"></a>

### P110｜套用遷移與舊版專案檔案樹

[核對原講義第 110 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=110)

- 模型與資料庫同步原命令：
  ```bash
  sudo python3 ./manage.py migrate  # 原標Python3
  sudo python ./manage.py migrate   # 原標Python2
  tree
  ```
- 上圖則是 `(dvdsenv1) pi@raspberrypi:~/project1 $ sudo ./manage.py migrate`，說明套用admin、auth、contenttypes、sessions。逐項OK為：`contenttypes.0001_initial`、`auth.0001_initial`、`admin.0001_initial`、`admin.0002_logentry_remove_auto_add`、`contenttypes.0002_remove_content_type_name`、`auth.0002_alter_permission_name_max_length`、`auth.0003_alter_user_email_max_length`、`auth.0004_alter_user_username_opts`、`auth.0005_alter_user_last_login_null`、`auth.0006_require_contenttypes_0002`、`auth.0007_alter_validators_add_error_messages`、`auth.0008_alter_user_username_max_length`、`sessions.0001_initial`。這個較早清單沒有後來admin.0003及auth.0009以後的遷移。
- 下圖tree顯示 **1 directory, 9 files**，完整如下：
  ```text
  .
  ├── db.sqlite3
  ├── manage.py
  └── project1
      ├── __init__.py
      ├── __init__.pyc
      ├── settings.py
      ├── settings.pyc
      ├── urls.py
      ├── urls.pyc
      └── wsgi.py
  ```
- 資料庫同步後可見db.sqlite3與匯入產生的pyc；本圖舊式pyc與原始碼同層，和P107 `__pycache__/...cpython-35.pyc`不同。**原稿不連續**：環境由dvdsenv變dvdsenv1，路徑由dvds2/project1變~/project1，圖中也沒有前面建立的myapp/static/templates；不能視為同一專案被遷移自動刪掉這些目錄。〔來源：P110〕

<a id="p111"></a>

### P111｜專案結構圖與 Django2.2 遠端啟動示例

[核對原講義第 111 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=111)

- 上方資訊圖以 **mysite** 示意，而非固定使用project1。完整圖像對照：
  ```text
  mysite/                 ← 外層專案名稱，可任意命名
  ├── manage.py           ← 用來與專案互動的命令列程式
  ├── db.sqlite3          ← 資料庫檔案
  └── mysite/             ← 專案中實際的 Python 套件
      ├── __init__.py
      ├── settings.py     ← 專案設定／組態檔案
      ├── urls.py         ← 專案 URL 宣告檔案
      └── wsgi.py         ← WSGI 相容伺服器設定檔案
  ```
- 蓝色標籤分別連到外層／內層目錄、manage.py、db.sqlite3、settings.py、urls.py、wsgi.py。黄色便利貼說明Django主要部署平台為 **WSGI**；便利貼英文字樣看似「WSGL」，應辨識為拼字疑誤，下面藍框與檔名均是WSGI。**版本背景**：圖未含ASGI，僅展示此講義較早的結構，不否定前面asgi.py的存在。
- 「啟動Server」原命令：
  ```bash
  sudo python3 manage.py runserver 0.0.0.0:8080
  ```
  此頁仍以sudo示範，並不表示8080需要管理員權限；同前，應避免將sudo混入虛擬環境使用而改變解譯器／權限。監聽0.0.0.0、用實際伺服器IP瀏覽的概念不變。
- 下圖 Chrome 位址 **`192.168.57.236:8080`**（HTTP「不安全」）；歡迎頁顯示 **`View release notes for Django 2.2`**、綠色火箭、`The install worked successfully! Congratulations!`，以及DEBUG=True、尚未設定URLs的英文說明。這是另一個舊版IP／Django版本的示例，不能和P097/P105的172.16.100.43、Django4.1.6當成同一次執行。
- 本頁沒有伺服器終端輸出，因此不能由本頁猜測啟動時間或Django2.2的修補版本。〔來源：P111〕

#### 本範圍閱讀與使用界線

P071–P111已逐頁閱讀文字與圖片；只有P104細小終端另外從原PDF局部重繪核讀。筆記保留Windows/Linux、CMD/PowerShell、手動/VS Code/Remote SSH各流程差異，以及Django2.2／3.2／4.1與Python3.5／3.8／3.9混編的歷史畫面。所有「成功」「OK」均指講義截圖，不是本次執行结果；沒有安裝Django、資料庫、修改PATH、安全原則或刪除SSH設定。圖中文字不一致與原稿風險已在各頁明確辨析。


---

## 第112–145頁｜Django 視圖、路由、模板及表單完整筆記

> 範圍僅限原PDF第112–145頁。每頁文字層與頁面圖片均逐頁比對；程式碼以圖片可辨內容整理，補足縮排與一般半形引號。明列「原稿疑點／補充」者不是原稿原文。本筆記未執行講義的 Django 程式；「畫面結果」均指原稿截圖。各頁重複出現的既有程式，保留與該頁相關的新路由／函式，並指向完整前例，不假裝每段都是獨立專案。

<a id="p112"></a>

### P112｜MVC 與 Django MVT 架構

[核對原講義第 112 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=112)

- **MVC（Model–View–Controller）**由模型、視圖、控制器組成。
  - Model：商業邏輯及資料庫存取程式。
  - View：輸入、輸出畫面。
  - Controller：在 Model 與 View 間接收操作、判斷要呼叫哪個 Model，整合資料與畫面。
- **MVT（Model–View–Template）**由模型、視圖、模板組成。
  - Model：商業邏輯及資料庫存取。
  - View：處理 Model 的存取工作，並安排 Template 的輸入或顯示。
  - Template：輸入表單、顯示資料的介面。
- 圖片箭頭的完整意義：MVC 的表單 View「送出」→ Controller → Model →「儲存資料」至資料庫；資料庫「讀取資料」→ Model → Controller →表單 View「顯示」。下方 Django 圖把表單所在層標為 Template，把中央 Controller 改成 View，Model 與資料庫的往返不變。

|任務|MVC|Django MVT／MTV|
|---|---|---|
|資料庫存取|Model|Model|
|輸入表單、顯示資料|View|Template|
|控制、整合|Controller|View|

**原稿疑點：**頁面把 Django 拼作「Diango」；MVT 與表格中的 MTV 是排列方式不同，不是兩套架構。Controller 文字定義末尾「並透過」未完成，以上依圖解說其整合作用。[來源：P112]

<a id="p113"></a>

### P113｜註冊功能的 MVC／Django 九步驟圖解

[核對原講義第 113 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=113)

本頁核心資訊在兩張流程圖，不可視為只有參考網址的空白頁。左側瀏覽器含「使用者名稱、密碼、註冊」表單與結果畫面；右側是網站程式，最右側為資料庫。

**MVC 圖：**
1. 瀏覽器把使用者註冊資訊提交網站伺服器，交給 Controller 接收。
2. Controller 告訴 Model 將註冊資訊存進資料庫。
3. Model 執行資料庫儲存。
4. 資料庫把儲存結果回傳 Model。
5. Model 把結果回傳 Controller。
6. Controller 告訴 View 產生 HTML 結果頁。
7. View 將產生的 HTML 交回 Controller。
8. Controller 把 HTML 頁面內容傳送瀏覽器。
9. 瀏覽器顯示結果頁面。

**Django 圖：**九步驟資料方向相同，但原來 Controller 的工作改標為 **V：視圖**；原來產生 HTML 的 View 改標為 **T：模板**。因此是瀏覽器→View→Model→資料庫→Model→View→Template→View→瀏覽器，而不是把 Django View 誤認為單純畫面。

原稿參考：https://blog.csdn.net/u014745194/article/details/73718041 。[來源：P113]

<a id="p114"></a>

### P114｜`urls.py`、`urlpatterns` 與路徑轉換器

[核對原講義第 114 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=114)

設定分兩步：在專案 `project1/urls.py` 的 `urlpatterns` 串列對應網址與函式；在 app 的 `myapp/views.py` 實作函式。原稿以 `sudo vim project1/urls.py` 編輯：

```python
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.sayhello),
]
```

- `path(網址, 函式)` 是本頁簡化語法。空字串代表根網址；`admin/` 對應管理網站入口，例如 `127.0.0.1:8000/admin/`。
- 圖中紅框標出 `from myapp import views` 與 `path('', views.sayhello)`，表示接上自訂 app 的必要兩處。
- 動態路徑以 `<型別:參數名稱>` 標示，可擷取多個參數，轉型後交給 view。

|轉換器|匹配與回傳|
|---|---|
|`str`|非空、不含 `/` 的字串；未指定型別時的預設|
|`int`|零或正整數；回傳 Python `int`|
|`slug`|原稿描述此列有誤；正確用途是 ASCII 字母、數字、連字號 `-`、底線 `_` 的字串|
|`uuid`|格式化、小寫、含連字號的 UUID，例如 `075194d3-6885-417e-a8a8-6c931e272f00`；回傳 UUID 物件|
|`path`|非空字串，可包含路徑分隔符 `/`|

**原稿疑點／補充：**原稿寫 `<url.py>`，實際檔名是 `urls.py`；「參數型別為字典」不精確，應理解為命名擷取值以關鍵字參數送給 view，不是每個參數都變成字典；`slug` 不匹配 `/`；`admin.site.urls` 也不宜一概稱為普通 view 函式，而是 admin 的 URL 設定入口。

原稿參考：http://blog.e-happy.com.tw/django2-0-%E4%BB%A5-path-%E5%87%BD%E5%BC%8F%E8%A8%AD%E5%AE%9A-urlpatterns/ 。[來源：P114]

<a id="p115"></a>

### P115｜第一個 `HttpResponse` 與動態姓名路由

[核對原講義第 115 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=115)

在 `myapp/views.py` 定義根路由函式：

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sayhello(request):
    return HttpResponse("Hello Django!")
```

執行原稿指令 `sudo python3 manage.py runserver 0.0.0.0:8080`。原稿瀏覽器連到 `192.168.57.236:8080`，畫面只有 `Hello Django!`，此例直接回傳文字，未使用模板。

動態路由一般例：`path('hello/<str:name>/', hello)`；訪問 `/hello/david/` 會把 `name='david'` 傳入 `hello`。本頁實際專案截圖則在前頁串列新增：

```python
path('hello1/<str:username>', views.hello1),
```

注意圖片中的實作是 **hello1、username、沒有尾端斜線**，不要跟說明中的 `hello/<str:name>/` 混用。對應 `hello1` 定義續於P116。

**補充：**`request` 是 Django 傳入的 HTTP request 物件；`0.0.0.0` 為監聽所有網路介面的綁定位址，不是要求瀏覽器使用該位址。實際連線必須使用主機IP與同一埠號。原稿示意 `127.0.0.1/hello/david/` 省略開發伺服器埠號；照8080操作時須加 `:8080`。原稿使用 `sudo` 是其環境操作，不代表 Django 開發必須有 root 權限。[來源：P115]

<a id="p116"></a>

### P116｜擷取 `username` 與第一個 HTML 模板

[核對原講義第 116 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=116)

`myapp/views.py` 截圖沿用 `sayhello`，新增完整函式：

```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

def hello1(request, username):
    return HttpResponse("Hello " + username)
```

路由見P115。原稿以 `sudo python3 manage.py runserver 0.0.0.0:8080` 啟動，瀏覽器 `192.168.57.236:8080/hello1/bill` 顯示 `Hello bill`。`username` 由路徑取得，不是寫死在函式內。

使用模板的下一步：`vim templates/hello2.html`，圖片內容為：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>歡迎光臨:{{ username }}</h1>
    <h2>現在時刻:{{ now }}</h2>
</body>
</html>
```

`{{ username }}` 與 `{{ now }}` 是模板變數，不是普通 HTML 文字。頁尾提示接著編輯 `project1/urls.py`，具體程式續於P117。**補充：**Python 3 的字串本來就是 Unicode；圖片的 `unicode_literals` 是舊式相容寫法，不是本例在 Python 3 運作的必要條件。[來源：P116]

<a id="p117"></a>

### P117｜`render()`、時間資料與靜態檔案目錄

[核對原講義第 117 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=117)

在前例 `urlpatterns` 加入：

```python
path('hello2/<str:username>', views.hello2),
```

`myapp/views.py` 新增匯入與函式：

```python
from datetime import datetime

def hello2(request, username):
    now = datetime.now()
    return render(request, "hello2.html", locals())
```

- `datetime.now()` 取得產生回應時的時間，存入 `now`。
- `render` 將 request、模板名稱、context 組合為回應；`locals()` 讓模板取用函式區域名稱 `username`、`now` 等。
- 啟動指令仍是 `sudo python3 manage.py runserver 0.0.0.0:8080`。
- 原稿畫面 `192.168.57.236:8080/hello2/bill`：大標題「歡迎光臨:bill」，次標題「現在時刻:Feb. 3, 2021, 5:57 a.m.」。這是當時截圖的時間，不是固定輸出或目前時間。

**靜態檔案操作：**在專案的 `static` 目錄加入 `p1.jpg` 及 `style.css`。檔案總管圖位於 `/home/pidvds1/project1/static/`，兩個檔案名稱可辨；本頁未列 CSS 原始內容，不能由檔名杜撰樣式碼。設定與套用續於P118–119。[來源：P117]

<a id="p118"></a>

### P118｜設定 `STATICFILES_DIRS` 並建立 `hello3`

[核對原講義第 118 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=118)

1. 編輯 `project1/settings.py`，圖片設定：

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
```

`STATIC_URL` 是URL前綴；`STATICFILES_DIRS` 是額外尋找靜態檔案的實體目錄列表。**補充：**使用上述 `os.path.join` 時，設定檔需要 `import os`；本頁截圖只截取設定尾段，未展示匯入。

2. `sudo vim project1/urls.py`，在原先 admin、根、hello1、hello2 路由後新增：

```python
path('hello3/<str:username>', views.hello3),
```

3. `sudo vim myapp/views.py`，沿用 `render` 與 `datetime` 匯入，新增：

```python
def hello3(request, username):
    now = datetime.now()
    return render(request, "hello3.html", locals())
```

4. `vim templates/hello3.html`；模板全文於P119。

圖片紅框依序強調靜態目錄列表、hello3路由、hello3函式，構成設定→路由→view→模板的串接。[來源：P118]

<a id="p119"></a>

### P119｜模板載入 CSS／圖片與畫面中姓名消失的原因

[核對原講義第 119 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=119)

`templates/hello3.html` 圖片程式：

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>第一個模板</title>
{% load staticfiles %}
<link href="{% static './style.css' %}" rel="stylesheet" type="text/css" />
</head>
<body>
<h1>Flask網站
    <img src="{% static './p1.jpg' %}" width="100px"></img>
</h1>
<h2>{{name}}，歡迎光臨!!</h2>
<h4>現在時間:{{now}}</h4>
</body>
</html>
```

- 原稿說明必須先 `{% load staticfiles %}` 宣告載入靜態標籤，再以 `{% static '檔案路徑' %}` 生成資源URL。
- CSS用 `<link>` 載入，圖片用 `<img>` 載入；圖中圖片寬度100px。
- 原稿註「Windows請改為 `{% load static %}`」。**版本補充：**選 `staticfiles`／`static` 主要是 Django 版本差異，並非Windows/Linux的本質差異；現代 Django 應使用 `{% load static %}`。
- 原稿啟動8080後，瀏覽器 `/hello3/bill` 呈現**紅色背景、黃色文字、籃球照片**，標題卻寫「Flask網站」；這只是原模板殘留文字，程式仍是 Django。
- 截圖歡迎句前沒有 bill，只顯示標點與「歡迎光臨!!」；原因是P118 view有 `username`，本頁卻使用 `{{name}}`。**修正建議（非原稿）：**改成 `{{ username }}`。不要為了讓範例看似正確而隱瞞截圖的不一致。
- 畫面時間為 `Feb. 3, 2021, 6:30 a.m.`；CSS檔內容未展示，只能確定畫面樣式，不能反推完整CSS。
- **HTML補充：**`img` 是空元素，不需要 `</img>`；以上保留圖片原寫法。

頁尾開始「從網址中載取資料」，僅出現 `ex:`，實際雙參數範例在P120。[來源：P119]

<a id="p120"></a>

### P120｜多個動態路徑參數與固定路徑片段

[核對原講義第 120 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=120)

頁首一般語法示意：

```python
path('hello/<str:name1>/<str:name2>/', function)
path('hello/<str:name1>/hello/', function)
```

前者擷取兩個字串，後者只擷取 `name1`，末端 `hello/` 是必須匹配的固定字樣。實作於 `project1/urls.py` 新增：

```python
path('hello4/<str:username1>/<str:username2>/', views.hello4),
path('hello5/<str:username>/hello/', views.hello5),
```

`myapp/views.py`：

```python
def hello4(request, username1, username2):
    return HttpResponse("Hello " + username1 + " " + username2)

def hello5(request, username):
    return HttpResponse("Hello " + username)
```

使用P115已有的 `HttpResponse` 匯入。原稿啟動 `sudo python3 manage.py runserver 0.0.0.0:8080`，訪問 `192.168.57.236:8080/hello4/bill/marry/`，顯示 `Hello bill marry`。圖中紅框圈住網址，兩支紅箭頭將URL中的 `bill`、`marry` 對應到輸出，強調各段分別傳入不同參數。[來源：P120]

<a id="p121"></a>

### P121｜固定 `hello/` 不會變成姓名參數

[核對原講義第 121 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=121)

本頁只有一張結果截圖，並不是沒有教學內容。瀏覽器網址 `192.168.57.236:8080/hello5/bill/hello/`；頁面顯示 `Hello bill`。紅箭頭由路徑中的 `bill` 指向顯示文字，搭配P120的 `hello5/<str:username>/hello/`，說明末端 `hello/` 用來匹配路由，不會額外傳入函式或附加在姓名後。完整路由和view見P120。[來源：P121]

<a id="p122"></a>

### P122｜View 將區域變數／字典傳入模板

[核對原講義第 122 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=122)

預設 app 的 `views.py` 已有 `from django.shortcuts import render`。基本呼叫：

```python
render(request, template_name, locals())
```

- 第1參數：`HttpRequest` 物件。
- 第2參數：要載入的模板名稱。
- 第3參數：模板context；本例以 `locals()` 傳入區域名稱及值。

```python
no = 1
dict1 = {"name": "Amy", "age": 20}
return render(request, "dice.html", locals())
```

也可明確提供：

```python
return render(request, "dice.html", {
    "no": 1,
    "dict1": {"name": "Amy", "age": 20},
})
```

模板輸出一般變數寫 `{{ no }}`；輸出字典項目寫 `{{ 字典變數.鍵 }}`，例如 `{{ dict1.name }}` 讀出Amy。

**補充／原稿簡化：**`locals()` 取得的是所有目前區域變數，不只是示範的 `no`、`dict1`，view 的 `request` 等也在其中；原稿把結果簡化成只有兩個键的字典。上述兩種寫法是模板所需資料相同，不表示字典內容逐項完全相等。明確列context能減少意外暴露不需要的區域資料。頁尾準備編輯 `project1/urls.py`，擲骰程式續P123。[來源：P122]

<a id="p123"></a>

### P123｜三個隨機骰子點數：`dice1`

[核對原講義第 123 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=123)

路由圖片原文為 `ath('dice1/', views.dice1),`，放大原PDF後確認確實缺少開頭 `p`，不可照抄執行。**訂正後應寫：**

```python
path('dice1/', views.dice1),
```

`myapp/views.py` 截圖用紅框新增 `import random` 與以下函式，沿用先前 `render` 匯入：

```python
import random

def dice1(request):
    no1 = random.randint(1, 6)
    no2 = random.randint(1, 6)
    no3 = random.randint(1, 6)
    return render(request, "dice1.html", locals())
```

每次view執行分別產生三個1至6的整數；`randint` 兩端皆包含。模板以不同名稱取得各次結果。

`templates/dice1.html`：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h3>點數一:{{ no1 }}</h3>
    <h3>點數二:{{ no2 }}</h3>
    <h3>點數三:{{ no3 }}</h3>
</body>
</html>
```

頁尾「測試結果」續下頁。原稿截圖中保留的舊 `hello2`、`hello3` 等函式仍依前頁運作，不是骰子生成的必要部分。[來源：P123]

<a id="p124"></a>

### P124｜骰子畫面；模板變量、標籤與註解

[核對原講義第 124 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=124)

啟動 `sudo python3 manage.py runserver 0.0.0.0:8080`，截圖網址 `192.168.57.236:8080/dice1/` 顯示三行「點數一:5」「點數二:6」「點數三:3」。這是某次亂數結果，不保證重新整理後相同。

模板有自己的語法，負責變數呈現、條件、迴圈和註解：

|類型|用途／完整寫法|
|---|---|
|變量|`{{ username }}`：將view給的資料插入指定位置|
|標籤|`{% if found %}`、`{% for item in items %}`：流程控制，須配對結束標籤|
|多行註解|`{% comment %}` 開始、`{% endcomment %}` 結束|
|單行註解|`{# 這是註解文字 #}`|
|一般文字|HTML或純文字，例如 `<title>顯示的模板</title>`|

```django
{% comment %}
註解文字一
註解文字二
{% endcomment %}
{# 這是註解文字 #}
```

**變量讀取對照：**

|資料種類|模板|Python對應與解說|
|---|---|---|
|字典|`{{ dict1.name }}`|`dict1['name']`，name是字典鍵|
|物件方法|`{{ obj1.show }}`|模板可解析並呼叫無需參數的方法；一般Python要寫 `obj1.show()` 才是呼叫|
|串列|`{{ list1.0 }}`|`list1[0]`；例如 `list1=['a','b','c']` 取第一項|

**原稿疑點：**表中寫 `dict1[name]`，若 `name` 是文字鍵需加引號；寫 `obj1.show` 只取得方法物件，不等於Python呼叫。本表已明確訂正；模板不用在 `show` 後加括號。[來源：P124]

<a id="p125"></a>

### P125｜字典與串列索引實例：`dice2`

[核對原講義第 125 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=125)

`project1/urls.py` 在骰子路由後新增：

```python
path('dice2/', views.dice2),
```

同一圖中前頁錯字 `ath` 已顯示成正常 `path('dice1/', views.dice1)`。`myapp/views.py`：

```python
def dice2(request):
    student = {'id': '12345', 'name': '張三', 'sex': '男'}
    fruit = ['apple', 'banana', 'Guava']
    return render(request, 'dice2.html', locals())
```

`templates/dice2.html`：

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>第一個模板</title>
</head>
<body>
    <h4>姓名:{{ student.name }}</h4>
    <h4>性別:{{ student.sex }}</h4>
    <h4>最喜歡的水果:{{ fruit.2 }}</h4>
</body>
</html>
```

字典含 `id`，但模板只顯示name與sex；索引從0起算，所以 `fruit.2` 是第三個項目Guava，而不是banana。操作順序是編輯路由→view→模板，結果見P126。[來源：P125]

<a id="p126"></a>

### P126｜`dice2` 結果及模板條件運算子

[核對原講義第 126 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=126)

原稿指令 `sudo python3 manage.py runserver 0.0.0.0:8080`；網址 `/dice2/` 顯示「姓名:張三」「性別:男」「最喜歡的水果:Guava」，證明點號可存取字典及索引。

本頁進入「3-7 模板語言—標籤」。Operators截圖表格完整列出：

|運算子|條件意義|
|---|---|
|`==`|相等|
|`!=`|不相等|
|`<`|小於|
|`<=`|小於等於|
|`>`|大於|
|`>=`|大於等於|
|`and`|左右條件皆為真|
|`or`|左右至少一個條件為真|
|`in`|項目存在於容器中|
|`is`|物件身分相同（原圖簡寫為same value）|
|`is not`|物件身分不同（原圖簡寫為not same value）|
|`not in`|項目不存在於容器中|

**補充：**`is`／`is not` 不是一般值相等比較，不能和 `==`／`!=` 當作同義。原圖每列右側是綠色 `Example »` 連結按鈕，未展開更多例子。

頁底開始 `{% if 條件 %}` 及程式區塊，結束標籤跨至P127。原稿參考：https://www.w3schools.com/django/ref_tags_if.php 。[來源：P126]

<a id="p127"></a>

### P127｜`if`、`else` 與條件分支

[核對原講義第 127 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=127)

承接P126的單一條件，完整結構為：

```django
{% if 條件 %}
    程式區塊
{% endif %}
```

分數達60才顯示及格；低於60時不輸出該區塊：

```django
{% if score >= 60 %}
    及格
{% endif %}
```

二選一完整結構與範例：

```django
{% if 條件 %}
    程式區塊一
{% else %}
    程式區塊二
{% endif %}

{% if score >= 60 %}
    及格
{% else %}
    不及格
{% endif %}
```

頁底開始多分支：`{% if 條件一 %}`／區塊一／`{% elif 條件二 %}`／區塊二；其餘續P128。

**原稿疑點：**圖片範例寫 `score >=60` 或 `score>=60`；Django模板的比較運算子需要作為獨立token，因此以上訂正為 `score >= 60`，不能直接照原稿省略空白。[來源：P127]

<a id="p128"></a>

### P128｜多分支等第與 `and`

[核對原講義第 128 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=128)

跨P127–128的完整多分支結構：

```django
{% if 條件一 %}
    程式區塊一
{% elif 條件二 %}
    程式區塊二
{% elif 條件三 %}
    程式區塊三
{% else %}
    程式區塊四
{% endif %}
```

由上往下匹配第一個成立的條件。本頁分數等第示例，**將原稿的 `elseif` 訂正為 `elif`，且補齊比較符號兩側空白**：

```django
{% if score >= 90 %}
    優等
{% elif score >= 80 %}
    甲等
{% elif score >= 70 %}
    乙等
{% else %}
    丙等
{% endif %}
```

本例沒有另設「不及格」分支，低於70者都落入丙等；不能自行把門檻改成60或增加原稿未有分類。原稿一般語法寫 `elif`，實例卻寫 `elseif`，後者不是Django內建if標籤的分支語法。

頁底W3Schools圖片的 `and` 範例完整為：

```django
{% if greeting == 1 and day == "Friday" %}
    <h1>Hello Weekend!</h1>
{% endif %}
```

必須同時滿足 greeting為1、day為Friday，才顯示Hello Weekend!。[來源：P128]

<a id="p129"></a>

### P129｜`or`、`for` 與迴圈狀態

[核對原講義第 129 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=129)

頁首圖片 `or` 範例：

```django
{% if greeting == 1 or greeting == 5 %}
    <h1>Hello</h1>
{% endif %}
```

greeting等於1或5任一成立便顯示Hello。原稿參考：https://www.w3schools.com/django/django_tags_if.php 。

`for` 基本語法：

```django
{% for 變數 in 串列 %}
    程式區塊
{% endfor %}
```

例中Python端準備 `list1 = range(1, 6)`，傳入context後，模板：

```django
{% for i in list1 %}
    {{ i }}
{% endfor %}
```

範圍是1到5，結束值6不包含。**補充：**`list1 = range(1, 6)` 應在Python view準備，不是可直接放進Django模板執行的Python語句；若無HTML換行或區塊元素，原始碼換行未必變成畫面逐行顯示。

本頁與P130跨頁表格整理（N表示本次迴圈項目總數）：

|屬性|意義|
|---|---|
|`forloop.counter`|目前第幾次，從1至N|
|`forloop.counter0`|從0至N−1|
|`forloop.revcounter`|剩餘倒數，從N至1|
|`forloop.revcounter0`|從N−1至0|
|`forloop.first`|第一次為True，其他為False|
|`forloop.last`|最後一次為True，其他為False（續P130）|
|`forloop.parentloop`|巢狀迴圈中上一層forloop（續P130）|

**原稿疑點：**counter0寫到「迭代總數」、revcounter0寫從「元素總數」開始皆有一位偏差；上表已明確訂正。[來源：P129–130]

<a id="p130"></a>

### P130｜`dice3`：逐筆顯示字典串列與 `{% empty %}`

[核對原講義第 130 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=130)

頁首續表說明last、parentloop。路由截圖改採**直接匯入函式**，不同於前面匯入views模組：

```python
from django.contrib import admin
from django.urls import path
from myapp.views import sayhello, hello1, hello2, hello3, dice1, dice2, dice3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sayhello),
    path('hello1/<str:username>', hello1),
    path('hello2/<str:username>', hello2),
    path('hello3/<str:username>', hello3),
    path('dice1/', dice1),
    path('dice2/', dice2),
    path('dice3/', dice3),
]
```

這張截圖未列hello4／hello5；只是本頁路由清單與前例不同，不應混用 `dice3` 與未匯入的 `views.dice3`。

`myapp/views.py`：

```python
def dice3(request):
    person1 = {"name": "Amy", "phone": "049-1234567", "age": 20}
    person2 = {"name": "Jack", "phone": "02-4455666", "age": 25}
    person3 = {"name": "Nacy", "phone": "04-9876543", "age": 17}
    persons = [person1, person2, person3]
    return render(request, "dice3.html", locals())
```

**保留原稿名稱 `Nacy`**，不要自行改為Nancy。模板 `templates/dice3.html`：

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>基本資料</title>
</head>
<body>
    <h3>
    {% for person in persons %}
        <h2>第 {{forloop.counter}} 位員工</h2>
        <ul>
            <li>姓名：{{person.name}}</li>
            <li>手機：{{person.phone}}</li>
            <li>年齡：{{person.age}}</li>
        </ul>
    {% empty %}
        沒有任何資料
    {% endfor %}
    </h3>
</body>
</html>
```

每次取一個字典person，以點號讀姓名、電話、年齡；counter編號從1開始。`{% empty %}` 是圖片獨有的重要語法：persons沒有可迭代項目時輸出「沒有任何資料」，不必另包if。

**原稿疑點／補充：**標籤寫手機，但值像市話號碼，筆記保留原資料；`h3` 包住 `h2` 和 `ul` 不是合宜的HTML結構，可改用div包裝（補充建議，不是原碼）。[來源：P130]

<a id="p131"></a>

### P131｜`dice3` 迴圈輸出的完整結果

[核對原講義第 131 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=131)

原稿啟動 `sudo python3 manage.py runserver 0.0.0.0:8080`。瀏覽器網址為 `192.168.57.236:8080/dice3/`，頁籤為「基本資料」，依序呈現三組標題及項目符號：

|迴圈標題|姓名|畫面「手機」|年齡|
|---|---|---|---|
|第1位員工|Amy|049-1234567|20|
|第2位員工|Jack|02-4455666|25|
|第3位員工|Nacy|04-9876543|17|

`forloop.counter` 自動產生1、2、3；每組三項來自同一個person字典。因為persons非空，沒有顯示「沒有任何資料」。本頁未展示空串列測試，不宣稱原稿驗證過empty分支。

原稿參考：https://www.w3schools.com/django/django_tags_for.php 。[來源：P131]

<a id="p132"></a>

### P132｜GET／POST 的信封比喻與 Query String

[核對原講義第 132 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=132)

章節「3-8 以GET及POST傳送資料」。原稿以寄信比喻HTTP：信封格式對應協定、信封外面對應header、信內書信對應message-body，HTTP method是寄送方式。GET比喻明信片，把資料寫在外面；POST比喻信封內放信件，body可放資料或檔案。

**要保留的技術重點：**一般HTML GET表單將資料編成key/value形式的query string放在URL後；POST表單將資料放在request body。`?` 開始查詢字串，每組參數用 `&` 隔開，鍵和值用 `=` 連結。

圖中GET表單原碼：

```html
<form method="get" action="">
    <input type="text" name="id" />
    <input type="submit" />
</form>
```

假設輸入010101，送出後網址為 `http://xxx.toright.com/?id=010101`；`action=""` 向目前頁面送出。圖中另一個HTTP請求行示例：

```http
GET /getCustomer.aspx?Id=123&name=marcus HTTP/1.1
Host: www.testwebsite.com
```

此例傳入 `Id=123` 與 `name=marcus`，大小寫依原圖保留。

**原稿比喻的限制／補充：**query string是request target（URL）的一部分，不是任意header欄位；「較便宜／較貴」只是比喻，不是GET和POST有固定費用差異；POST藏在body並不等於加密或安全。原稿「包在裡面安全看不到」應配合P133的修正理解，敏感資料仍須HTTPS及適當伺服器保護。[來源：P132]

<a id="p133"></a>

### P133｜HTTP封包比較、表單編碼與安全性

[核對原講義第 133 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=133)

GET截圖的核心請求：

```http
GET /?id=010101 HTTP/1.1
Host: xxx.toright.com
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-tw,en-us;q=0.7,en;q=0.3
Accept-Encoding: gzip,deflate
Accept-Charset: UTF-8,*
Keep-Alive: 115
Connection: keep-alive
```

圖中也有 `User-Agent: Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-TW; rv:1.9.2.13) Gecko...`，右側遭截斷，不能恢復完整字串。表單值直接見於請求行及瀏覽器URL。

POST表單僅改method：

```html
<form method="post" action="">
    <input type="text" name="id" />
    <input type="submit" />
</form>
```

原稿說明網址列不因這個表單欄位值而增加query string。POST封包圖同樣列Host、User-Agent、Accept、語言、壓縮、字元集、Keep-Alive、Connection；不同關鍵片段如下：

```http
POST / HTTP/1.1
Host: xxx.toright.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 9

id=020202
```

**轉錄註：**上段為去除圖片排版殘留後的教學重點，不是逐字封包重放。原圖片在Content-Length前出現 `</code><code>`，應屬來源網頁標記污染；圖中宣告長度9，而顯示的body是否含未可見換行無法確認，故不把它當作已驗證的正確封包。POST參數此處是020202，不是GET的010101。

上傳檔案時原稿提 `multi-part`，表示檔案及其他欄位一起放body。**補充名稱：**HTML檔案表單通常用 `multipart/form-data`。

底部圖片的比較表完整意義：

|比較|GET|POST|
|---|---|---|
|網址差異|網址帶有HTML表單參數與資料|表單值通常不顯示在網址列|
|資料量|經URL攜帶，受URL長度限制|資料不放URL，較不受URL長度限制|
|可見性|URL可看到參數名稱和值|參數及值在HTTP body，不直接出現在URL|

**原稿疑點／必要補充：**
- 「GET不允許message-body」說得過度絕對；一般瀏覽器GET表單不用body，GET內容沒有普遍定義的語意，不能依賴伺服器支援；不要把教學表單行為擴大為任何HTTP實作的絕對禁令。
- POST仍可能帶query string；本例只說明表單資料所在位置，不能推論所有POST網址永遠不變。
- POST不是無限大小，仍受伺服器與應用程式限制。
- body可被開發者工具或未加密流量觀察；**不在URL不等於保密**，應用HTTPS。GET敏感值還可能落入瀏覽歷史、網址記錄等，因此不應用GET傳密碼。[來源：P133]

<a id="p134"></a>

### P134｜從 `request.GET`／`request.POST` 取得值

[核對原講義第 134 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=134)

URL語法整理為 `網址?參數1=值1&參數2=值2&參數3=值3`。原稿例：

```text
http://127.0.0.1:5000/test?name=bill&tel=092322423
```

此例僅示意query string，不等於本專案已有5000埠或test路由。參數為name與tel，電話宜保留字串避免丟失前導0。

Django取得表單值：

```python
request.GET['參數名稱']
request.POST['參數名稱']
```

**補充／原稿術語訂正：**request不是此處需要匯入的「模組」，GET／POST也不是這種寫法下呼叫的方法；request是HttpRequest物件，GET和POST是可按鍵取得值的QueryDict資料。用方括號讀不存在的鍵會出錯，後面get2範例處理此情況。

「使用GET傳遞參數（有參數）」：`sudo vim project1/urls.py`，截圖回到 `from myapp import views` 的方式，新增：

```python
path('get1', views.get1),
```

本頁get1路由**沒有尾端斜線**，圖片dice1／dice2／dice3也顯示為無尾斜線版本；應跟實際專案設定一致，不要直接沿用P130的尾斜線URL。頁尾提示編輯 `myapp/views.py`，函式接P135。[來源：P134]

<a id="p135"></a>

### P135｜`get1`：直接讀取name、city並顯示歡迎訊息

[核對原講義第 135 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=135)

承接P134路由，`myapp/views.py`：

```python
def get1(request):
    name = request.GET['name']
    city = request.GET['city']
    # print(name)
    # print(city)
    # return HttpResponse("test")
    return render(request, "get1.html", locals())
```

註解中的print／test是原圖保留的除錯碼，並未執行。兩個GET鍵必須存在，否則方括號讀取失敗。

`templates/get1.html` 完整關鍵HTML：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Django網站</h1>
    <h2>歡迎來自{{ city }}的{{ name }}光臨本網站</h2>
</body>
</html>
```

此節啟動埠改為8000：`sudo python3 manage.py runserver 0.0.0.0:8000`。截圖網址 `127.0.0.1:8000/get1?name=bill&city=台北`，大標題「Django網站」、次標題「歡迎來自台北的bill光臨本網站」。key名稱必須對應view的name、city。

頁底轉入「有參數與無參數」的get2，提示編輯 `project1/urls.py`，程式在P136。[來源：P135]

<a id="p136"></a>

### P136｜`get2`：先檢查鍵存在，避免遺漏參數直接出錯

[核對原講義第 136 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=136)

路由圖片新增：

```python
path('get2', views.get2),
```

`myapp/views.py` 完整函式：

```python
def get2(request, name=None, city=None):
    status = True
    if 'name' in request.GET:
        name = request.GET['name']
    else:
        status = False

    if 'city' in request.GET:
        city = request.GET['city']
    else:
        status = False

    return render(request, "get2.html", locals())
```

- name、city預設None；這裡query string**不會**自動填入Python函式參數，仍由 `request.GET` 明確取得。
- 先假設status為True；任一鍵缺少就設False。第二個條件即使有city也不會重設True，因此只有兩個鍵均存在才算成功。
- 這只檢查鍵存在，不檢查非空字串、城市是否合法，也不是身分驗證。`?name=&city=` 仍有兩個鍵。
- 頁尾提示 `sudo vim templates/get2.html`，模板及兩種畫面於P137。[來源：P136]

<a id="p137"></a>

### P137｜模板依 `status` 顯示成功或Error

[核對原講義第 137 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=137)

`templates/get2.html`：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    {% if status %}
        <h1>Django網站</h1>
        <h2>歡迎來自{{ city }}的{{ name }}光臨本網站</h2>
    {% else %}
        <h1>Error</h1>
    {% endif %}
</body>
</html>
```

啟動 `sudo python3 manage.py runserver 0.0.0.0:8000`，兩張原稿截圖對照：
1. `127.0.0.1:8000/get2` 沒有query string：只顯示 **Error**。
2. `127.0.0.1:8000/get2?name=bill&city=新竹`：顯示「Django網站」及「歡迎來自新竹的bill光臨本網站」。

**補充：**模板文字Error不是自動HTTP錯誤狀態；本例 `render()` 沒有指定錯誤status。頁尾開始「使用GET傳遞參數（使用表單）」，本頁尚未展示get3表單，勿把get2畫面誤認成get3。[來源：P137]

<a id="p138"></a>

### P138｜`get3`：同一view以load／save模式顯示或接收GET表單

[核對原講義第 138 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=138)

`project1/urls.py` 新增：

```python
path('get3/<str:mode>/', views.get3),
```

本頁截圖也將get1、get2顯示為 `get1/`、`get2/`，與P134–137版本不同；get3自身明確有尾斜線。

`myapp/views.py`：

```python
def get3(request, mode=None):
    if mode == "save":
        username = request.GET['username']
        passwd = request.GET['passwd']
        # return HttpResponse("test1")
        return render(request, "get3_response.html", locals())
    elif mode == "load":
        # return HttpResponse("test2")
        return render(request, "get3.html", locals())
```

`mode` 由路徑傳入；`username`、`passwd` 才是GET查詢參數。`load`呈現表單，`save`取值並呈現回應；本例的save名稱不表示真的存資料庫，函式內沒有儲存動作。

`templates/get3.html`：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Django網站</h1>
    <form action="/get3/save/" method="get">
        <p>帳號: <input type="text" name="username" id="username"></p>
        <p>密碼: <input type="password" name="passwd" id="passwd"></p>
        <p><button type="submit">確定</button> <button type="reset">清除</button></p>
    </form>
</body>
</html>
```

- action決定提交到 `/get3/save/`；method決定用GET。
- name決定送到伺服器的參數鍵；id是HTML元素識別名稱，不能只設id不設name。
- password輸入框只在畫面隱藏字元，不會加密提交值。
- submit提交，reset還原表單初始值。

**原稿風險／補充：**示範帳密透過GET會把密碼暴露在URL，不能作為正式登入方案；本函式未檢查鍵遺漏，也未處理其他mode，不匹配load/save時將缺少有效回應。筆記保留原稿流程，不自行捏造已驗證的安全版本。[來源：P138]

<a id="p139"></a>

### P139｜GET表單回應與密碼在URL中可見

[核對原講義第 139 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=139)

`templates/get3_response.html`：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>{{username}}您好!</h1>
    <h2>您的密碼為:{{passwd}}</h2>
</body>
</html>
```

原稿執行 `sudo python3 manage.py runserver 0.0.0.0:8000`，畫面完整流程：
1. 開啟 `127.0.0.1:8000/get3/load/`，看到「Django網站」、帳號與密碼欄、確定／清除按鈕。
2. 帳號輸入david，密碼欄以圓點遮蔽。
3. 按確定後網址變成 `127.0.0.1:8000/get3/save/?username=david&passwd=1234`。
4. 回應顯示「david您好!」與「您的密碼為:1234」。

圖片證明password欄遮蔽不能保護傳輸後的URL；模板又把passwd明文輸出。**安全補充：**這僅適合教學展示傳參數，不要使用真密碼，也不要在正式登入回應中顯示密碼。此程式沒有比對帳密，不是驗證成功的登入流程。[來源：P139]

<a id="p140"></a>

### P140｜`post1`：依HTTP method區分顯示表單與提交

[核對原講義第 140 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=140)

原標題是「使用POST傳遞參數（使用表單，單選題）」，但圖片實作是**帳密表單**，沒有radio單選題。

`project1/urls.py` 原圖新增：

```python
path('post1', views.post1),
```

`myapp/views.py`：

```python
def post1(request):
    if request.method == "POST":
        username = request.POST['username']
        passwd = request.POST['passwd']
        # print(username)
        # print(passwd)
        # return HttpResponse("有資料")
        if username == "david" and passwd == "1234":
            status = True
            # return HttpResponse("歡迎光臨本網站")
        else:
            status = False
            # return HttpResponse("帳號或密碼錯誤!")
        return render(request, "post1_response.html", locals())
    else:
        # return HttpResponse("無資料")
        return render(request, "post1.html", locals())
```

- HTTP method屬性通常是大寫字串，故比較 `"POST"`；這不是檢查query string的mode。
- 非POST請求回傳輸入頁（本課通常是瀏覽器GET）；POST從 `request.POST` 取欄位。
- 原稿硬編碼的測試條件是david與1234同時吻合，設定status供模板分支。
- print及HttpResponse測試行均為註解，真正回應為render。

**原稿疑點／安全補充：**本頁route沒尾斜線，P141表單action與P142結果卻使用 `/post1/`，需將實際路由和action統一，不能宣稱照圖原封貼上就完全匹配。硬編碼帳密只供示範，不包含Django正式認證、密碼雜湊、session登入等；缺少POST欄位也可能出錯。[來源：P140]

<a id="p141"></a>

### P141｜POST表單的 `{% csrf_token %}` 與403畫面

[核對原講義第 141 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=141)

`templates/post1.html`：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Django網站</h1>
    <form action="/post1/" method="post">
        {% csrf_token %}
        <p>帳號: <input type="text" name="username" id="username"></p>
        <p>密碼: <input type="password" name="passwd" id="passwd"></p>
        <p><button type="submit">確定</button> <button type="reset">清除</button></p>
    </form>
</body>
</html>
```

與GET版本相比，action改為post1端點、method改post，且**在form內**加入CSRF token。CSRF防護針對跨站請求偽造，不是把表單值加密，也不是驗證帳密。

原稿提醒POST表單應加 `{% csrf_token %}`，沒有時可能被Django拒絕。示意圖黃底錯誤區明確顯示：

```text
Forbidden (403)
CSRF verification failed. Request aborted.
```

圖片地址其實是 `192.168.57.236:8080/dice5/`，不是本節post1，應視為重用的CSRF錯誤示意，不能據此新增本範圍沒有定義的dice5函式。

**補充：**上述要求針對有Django CSRF保護的內部POST表單；token應搭配正常CSRF middleware與模板render。不要以停用CSRF作為正式解法；也不應把站內CSRF token提交到外部網址。頁尾開始編輯 `post1_response.html`，內容在P142。[來源：P141]

<a id="p142"></a>

### P142｜POST回應模板與帳密驗證成功畫面

[核對原講義第 142 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=142)

`templates/post1_response.html`：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    {% if status %}
        <h1>Django網站</h1>
        <h2>歡迎光臨{{ username }}</h2>
    {% else %}
        <h1>帳號或密碼錯誤!</h1>
    {% endif %}
</body>
</html>
```

原稿啟動 `sudo python3 manage.py runserver 0.0.0.0:8000`：
1. `127.0.0.1:8000/post1/` 顯示帳密表單，帳號david，密碼欄圓點遮蔽，按確定。
2. 下張圖仍是 `127.0.0.1:8000/post1/`，沒有username／passwd查詢字串。
3. 畫面「Django網站」「歡迎光臨david」，且不再印出密碼。

圖片只有成功結果；錯誤帳密會進入模板else是依程式邏輯說明，不是假稱看到錯誤帳密實測圖。這比GET示例少了URL明碼，但仍須HTTPS；且前頁所述尾斜線不一致必須修正。[來源：P142]

<a id="p143"></a>

### P143｜POST帳密錯誤結果；複選表單用 `getlist()`

[核對原講義第 143 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=143)

**頁首承接post1：**原稿瀏覽器截圖確實顯示「帳號或密碼錯誤!」，補上P142的else結果。網址欄因視窗寬度只露出 `127.0.0.1:8000/pos...`，不可聲稱本圖能讀到完整URL，也無法由圖得知此次輸入的錯誤帳密內容。

下半進入「使用POST傳遞參數（使用表單，複選題）」：`sudo vim project1/urls.py` 新增：

```python
path('post2/', views.post2),
```

同圖已把post1路由寫為 `path('post1/', views.post1)`，亦即在後續版本補上了前面不一致的尾斜線。

`myapp/views.py`：

```python
def post2(request):
    if request.method == "POST":
        items = request.POST.getlist('items')
        # print(request.POST.getlist('items'))
        # return HttpResponse("有資料")
        return render(request, "post2_response.html", locals())
    else:
        # return HttpResponse("無資料")
        return render(request, "post2.html", locals())
```

- 多個checkbox共用 `name="items"`，送出時同一鍵可能有多個值。
- `request.POST.getlist('items')` 取得**全部**已勾選值，存為items串列，不能以 `request.POST['items']` 代替並期待拿到全部。
- 非POST回傳表單；POST回傳所選項目列表。print／HttpResponse行是停用的測試註解。
- **補充：**全部不選時，瀏覽器不送這些checkbox值，getlist通常得到空串列；本例不另拒絕空選擇。
- 頁尾建立 `templates/post2.html`，全文在P144。[來源：P143]

<a id="p144"></a>

### P144｜四個同名checkbox、標籤對應與CSRF

[核對原講義第 144 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=144)

`templates/post2.html` 圖片程式如下；為完整呈現原稿，保留其PHP標籤錯誤與缺少form結尾的情況，訂正建議列於後文：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form method="POST" action="/post2/">
        {% csrf_token %}
        <div>您學會的項目為：</div>
        <div>
            <input type="checkbox" id="Linux" name="items" value="Linux"/>
            <label for="Linux">Linux</label>
            <input type="checkbox" id="Apache" name="items" value="Apache"/>
            <label for="Apache">Apache</label>
            <input type="checkbox" id="PHP" name="items" value="PHP"/>
            <label for="Linux">PHP</label>
            <input type="checkbox" id="MySQL" name="items" value="MySQL"/>
            <label for="MySQL">MySQL</label>
        </div>
        <div>
            <input type="submit" value="送出" />
        </div>
</body>
</html>
```

|選項文字|input id|送出用name|送出用value|原稿label for|
|---|---|---|---|---|
|Linux|Linux|items|Linux|Linux|
|Apache|Apache|items|Apache|Apache|
|PHP|PHP|items|PHP|Linux（錯誤）|
|MySQL|MySQL|items|MySQL|MySQL|

四個選項都沒有 `checked` 屬性，初始不預選。不同value用來區分選項；相同name讓view以同一鍵getlist取得多值。label的for應與對應input的id相同，不是對應name。

**原稿疑點／訂正：**PHP那行label應改為 `<label for="PHP">PHP</label>`，否則點PHP文字可能切換Linux；在 `</body>` 前需補上 `</form>`。這是原圖明確可見的問題，不默默改寫成原稿沒有的正確碼。

再次提醒form內需 `{% csrf_token %}`；缺少時圖示為 `Forbidden (403)`、`CSRF verification failed. Request aborted.`。同P141重用的圖片地址仍是 `192.168.57.236:8080/dice5/`，不是post2實際錯誤截圖。頁尾提示編輯 `post2_response.html`。[來源：P144]

<a id="p145"></a>

### P145｜將複選結果以模板迴圈輸出

[核對原講義第 145 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=145)

`templates/post2_response.html`：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <ul>
        {% for data in items %}
        <li>{{data}}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

迴圈對items中每個字串產生一個li，由ul呈現項目符號。沒有empty分支；若items為空，就沒有項目文字（這是程式推論，原圖未展示空提交結果）。

原稿操作指令 `sudo python3 manage.py runserver 0.0.0.0:8000`。圖片分為：
1. 表單初始畫面：「您學會的項目為：」後列Linux、Apache、PHP、MySQL四個未勾選框，下方「送出」按鈕。此張網址是 `127.0.0.1:8080/post2/`。
2. 結果圖網址 `127.0.0.1:8000/post2/`，顯示兩個項目符號：`Apache`、`MySQL`。

**圖片讀取限制／原稿疑點：**表單截圖未顯示實際勾選後狀態，能確認的是結果收到Apache與MySQL，不應聲稱親眼看到這兩框被勾選；表單圖使用8080、指令與結果使用8000，顯然是不同截圖環境或時次，實際操作應統一埠號。

**本段知識串連：**HTML同名checkbox→POST多值欄位→`getlist('items')`串列→`render(..., locals())`傳context→`{% for data in items %}`逐筆顯示。這是本範圍最後一頁；不延伸到P146以後。[來源：P145]


---

## Python and Django 講義 P146–183：資料庫與原生 SQL 完整知識筆記

**來源與方法：**依原 PDF 第 146–183 頁逐頁閱讀文字層及原頁圖片；所有頁面均實際開啟檢視，細小的程式與表格另以局部重繪確認。頁碼採 PDF／印刷頁碼一致的本次指定範圍。以下按頁保留操作、程式、參數、圖片結果與參考連結；跨頁程式會註明接續關係，缺失片段不自行補造成原稿。

**閱讀標記：**「原稿」為教材內容；「補充／疑點／安全」為整理者辨析，不與原稿混同。示例密碼、私網位址、資料表樣本均只為忠實閱讀而保留，非生產建議。安裝、系統權限、服務啟停、資料庫 SQL 及 runserver 皆未在本次環境執行。實際完成的操作僅為本地文件讀取、圖片渲染、筆記與稽核檔輸出。

<a id="p146"></a>

### P146｜MariaDB 安裝與本機 root 驗證

[核對原講義第 146 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=146)

本節為「3-9 Django 資料庫連結與應用（使用 MariaDB）」。教材先更新套件索引、搜尋伺服器套件，再安裝與確認服務狀態：
```sh
sudo apt update
apt-cache search mysql-server
sudo apt-get install mariadb-server
sudo systemctl status mariadb.service
```
截圖的 `pi@raspberry` 終端列出 `mariadb-server-10.3`（伺服器執行檔）、`mariadb-server-core-10.3`（核心檔）、`default-mysql-server`、`default-mysql-server-core`（後兩者為 metapackage）。因此搜尋畫面是 10.3，後續正文則明確談 Debian 11／MariaDB 10.5.12，並非同一版本的完整安裝實錄。

正文稱「本地無密碼直接登入」為待解決問題，示範將 root 驗證方式改成密碼：
```sh
sudo mysql -u root -p
```
```sql
use mysql;
SELECT * FROM global_priv;
ALTER USER root@localhost IDENTIFIED VIA mysql_native_password
USING PASSWORD("password");
flush privileges;
exit
```
`mysql` 為系統資料庫；`global_priv` 用來檢查帳號權限與驗證資料；`ALTER USER` 指定 `root@localhost` 的驗證外掛與密碼；教材將 `flush privileges` 解釋成刷新權限。

**原稿疑點／安全補充：**原文寫 `unix_socker`，正確名稱是 `unix_socket`。Socket 驗證是以作業系統帳號驗證，不等於任何人皆能無密碼登入，不應一律視為漏洞。這些是歷史環境的設定示範，未在本次整理中執行；`password` 是原稿弱密碼範例，非部署建議。

參考：<https://blog.csdn.net/csgd2000/article/details/82751606>。

<a id="p147"></a>

### P147｜安全初始化問答與 root 登入

[核對原講義第 147 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=147)

執行教材指令 `sudo mysql_secure_installation` 進入互動設定。頁面上半先顯示 root 已受保護，並在 `Switch to unix_socket authentication [Y/n]` 回答 `n`，延續前頁採用密碼驗證的情境。

圖片補足的完整問答順序：
1. `Enter current password for root (enter for none)`：範例要求直接按 Enter（只適用當時尚無該密碼的情境）。
2. `Set root password? [Y/n]`：`Y`；輸入 `New password`，再於 `Re-enter new password` 重複輸入。
3. `Remove anonymous users? [Y/n]`：`Y`，移除匿名帳號。
4. `Disallow root login remotely? [Y/n]`：圖片回答 `Y`，禁止 root 遠端登入。
5. `Remove test database and access to it? [Y/n]`：`Y`，移除測試資料庫及權限。
6. `Reload privilege tables now? [Y/n]`：`Y`，重新載入權限表。

正文把改密碼問題寫成 `Change the root password?`，與截圖的 `Set root password?` 有字樣差異。正文「不允許 root 遠端登入」一行又將 `[Y/n]` 的 `n` 標紅，與上方圖片明列 `Y` 的呈現不一致；安全意義應以問題文字辨別：回答 Y 才是禁止。

登入示範：
```sh
sudo mysql -u root -p
# 原稿另一寫法（明文密碼，不建議）
sudo mysql -uroot -p1qaz@wsx
```
`-u` 指定使用者；只寫 `-p` 讓程式互動詢問；直接把密碼接在 `-p` 後會增加 shell 歷史／程序參數洩漏風險。原稿密碼僅為教材範例，不應重用。

<a id="p148"></a>

### P148｜遠端連線前置：確認監聽與主設定檔

[核對原講義第 148 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=148)

教材以以下命令查出資料庫監聽狀況：
```sh
sudo netstat -tlnp | grep mariadb
sudo vim /etc/mysql/my.cnf
```
`netstat` 可顯示連線、路由、網路介面統計、偽裝連線與多播成員；此處各參數為：`-t` 只看 TCP、`-l` 只看監聽、`-n` 輸出數字位址而不作 DNS 反查、`-p` 顯示占用連線的行程。未加選項時通常不列監聽項目。`grep mariadb` 是依程序相關字串篩選，實際程序名稱依版本而不同。

主設定檔可能為 `/etc/mysql/my.cnf` 或 `/etc/my.cnf`；它可能只是再載入其他目錄的入口，需循 include 找真正伺服器設定，而不是只修改主檔。此頁是文字說明及命令框，沒有額外終端輸出。

參考：<https://websiteforstudents.com/mariadb-installed-without-password-prompts-for-root-on-ubuntu-17-10-18-04-beta/>。

<a id="p149"></a>

### P149｜設定檔引入順序與 bind-address 圖解

[核對原講義第 149 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=149)

上方圖片是 GNU nano 3.2 開啟 `/etc/mysql/my.cnf`，而正文命令使用 vim：兩者皆為編輯器，不能把畫面誤讀為 vim 輸出。圖片註解列出讀取順序：`/etc/mysql/mariadb.cnf` 設全域預設、`/etc/mysql/conf.d/*.cnf` 設全域選項、`/etc/mysql/mariadb.conf.d/*.cnf` 設 MariaDB 專用選項，最後 `~/.my.cnf` 設個人選項；同一設定重複定義時，後讀取值生效。`[client-server]` 表示客戶端與伺服器皆讀取。

紅框標出：
```ini
!includedir /etc/mysql/conf.d/
!includedir /etc/mysql/mariadb.conf.d/
```
教材接著列目錄並編輯伺服器檔：
```sh
ls /etc/mysql/mariadb.conf.d/
sudo vim /etc/mysql/mariadb.conf.d/50-server.cnf
```
目錄截圖含 `50-client.cnf`、`50-mysql-clients.cnf`、`50-mysqld_safe.cnf`、`50-server.cnf`。

下方設定截圖可見：
```ini
user = mysql
pid-file = /run/mysqld/mysqld.pid
socket = /run/mysqld/mysqld.sock
#port = 3306
basedir = /usr
datadir = /var/lib/mysql
tmpdir = /tmp
lc-messages-dir = /usr/share/mysql
#skip-external-locking
bind-address = 0.0.0.0
```
紅框重點是 `bind-address = 0.0.0.0`；上方註解原本描述只監聽 localhost 的預設情況。`#port` 行仍為註解，不是新開啟的設定。`0.0.0.0` 代表所有 IPv4 介面，須搭配來源網段限制、帳號最小權限與防火牆，不能直接當成安全的對外開放方案。

<a id="p150"></a>

### P150｜重啟監聽、root 遠端權限與新使用者

[核對原講義第 150 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=150)

教材說明綁定所有介面用 `0.0.0.0`；若只需其中幾個介面，教材做法仍綁定全部，再用防火牆擋不需要的介面。
```sh
sudo systemctl restart mysql
sudo netstat -tlnp | grep mariadbd
```
圖片實際篩選 `grep mysqld`，輸出關鍵內容是 `tcp ... 0.0.0.0:3306 ... 0.0.0.0:* LISTEN 6075/mysqld`，證明該截圖的服務已監聽所有 IPv4 介面的 3306 埠。正文 `mariadbd` 與圖中 `mysqld` 是版本／程序名稱差異，不能假設在每台機器都一樣。

**原稿方法一（高風險，非生產推薦）：**直接把 root 來源主機改成萬用來源：
```sql
update user set host = '%' where user = 'root';
```
需留意其依賴當時系統權限表結構／目前選定資料庫；直接改系統權限表不是跨版本可靠作法。將最高權限 root 開放所有來源尤其不宜。

**原稿方法二：**新增帳號，再授權；原文稱比直接改 root 好。
```sh
mysql -u root -p
```
```sql
CREATE USER admin IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'admin';
```
教材解釋 `'admin'@'localhost'` 只准本機，而省略 host 的 `'admin'` 表示萬用來源；文中 `hoot` 為 `host` 的筆誤。`*.*` 是「所有資料庫的所有資料表」範圍，`ALL PRIVILEGES` 才是授予全部適用權限，兩者不應混為同一概念。新帳號若仍拿到 `*.*` 的廣泛權限並對 `%` 開放，一樣不適合一般 Django 應用；應使用專用帳號、限制來源、限制特定資料庫與必要權限。

<a id="p151"></a>

### P151｜資料庫層級授權、使用者查詢／刪除／改密碼

[核對原講義第 151 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=151)

接續前頁，將授權範圍縮到單一資料庫的原稿寫法：
```sql
GRANT ALL PRIVILEGES ON database_name.* TO 'admin';
FLUSH PRIVILEGES;
```
`database_name.*` 指該資料庫內所有資料表；教材將 `FLUSH PRIVILEGES` 說明為重新載入使用者權限設定。

帳號管理補充：
```sql
SELECT User FROM mysql.user;
SELECT User, Host FROM mysql.user;
DROP USER 'admin';
```
第一個查帳號名稱，第二個連同允許連線的來源主機一起列出；同名使用者在不同 Host 下是不同帳號，管理時應辨清。`DROP USER` 是刪帳號，不是刪應用資料列。

原稿以 `mysql -uroot –p1qaz@wsx` 登入後示範：
```sql
SET PASSWORD FOR 'admin'@'localhost' = PASSWORD('password');
SET PASSWORD FOR 'admin' = PASSWORD('password');
flush privileges;
```
第一行針對本機帳號，第二行原稿標為可連遠端的帳號。**補充／疑點：**文字層的登入命令在 `p` 前為長破折號 `–`，不是 shell 選項需要的 ASCII `-`；不可直接複製。`PASSWORD()` 及帳號 DDL 的可用性依 MySQL／MariaDB 版本而異，原稿不能直接當成現代所有版本通用語法。明文及弱密碼均僅保留教材，不推薦使用。

<a id="p152"></a>

### P152｜匯入 SQL、建立 myproject 與 Workbench 鋪陳

[核對原講義第 152 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=152)

從 shell 將 SQL 檔送進 `class` 資料庫：
```sh
mysql -u root -p class < students.sql
```
`class` 是目標資料庫，`students.sql` 是輸入檔；`<` 是 shell 輸入重新導向，接著出現 `Enter password`。這不是把檔名當作 SQL 指令，且需事先確認資料庫與匯入檔內容。

另一段先以 `sudo mysql -u root -p` 登入，再執行：
```sql
CREATE DATABASE myproject CHARACTER SET UTF8;
show databases;
```
截圖結果為欄名 `Database`，列出 `information_schema`、`myproject`、`mysql`、`performance_schema`，最後 `4 rows in set (0.00 sec)`，之後 `exit`。畫面沒有 `class`；前一段匯入與此段建庫不可視為同一份連續成功實錄。

頁末引入「使用 Wordbench 開啟 MariaDB 資料庫」，其中 Wordbench 是原稿拼字；軟體畫面於次頁顯示 MySQL Workbench。

原稿參考：
- <https://www.ucamc.com/articles/430-mysql>
- <https://stackoverflow.com/questions/62564439/mysql-mariadb-server-raspberry-pi-remote-access>
- <https://magiclen.org/mysql-remote/>
- <https://emn178.pixnet.net/blog/post/87659567>
- <https://www.dotblogs.com.tw/CodeBrewTea/2022/02/15/150432>

**補充：**原稿建庫使用 `UTF8`，後文連線使用 `utf8mb4`；兩者在教材的資料庫版本下不宜直接視為相同的完整 Unicode 儲存能力，建庫／資料表／連線字元集要一致評估。

<a id="p153"></a>

### P153｜Workbench SSH 連線設定與遺忘 root 密碼救援

[核對原講義第 153 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=153)

上方 Workbench 首頁的 MySQL Connections 顯示本機 `Local instance MySQL80`（root、localhost:3306）與名為 `pi` 的遠端連線。下方 `Setup New Connection` 圖的欄位值為：

|欄位|畫面值／用途|
|---|---|
|Connection Name|`pi`，連線設定名稱|
|Connection Method|`Standard TCP/IP over SSH`，紅框特別標示|
|SSH Hostname|`192.168.58.90`|
|SSH Username|`pi`|
|SSH Password|`Store in Vault...`，紅框；可儲存 SSH 密碼|
|SSH Key File|空白，旁有瀏覽鈕，可改以私鑰認證|
|MySQL Hostname|`192.168.58.90`，相對於 SSH 主機連線的資料庫位址|
|MySQL Server Port|`3306`|
|Username|`admin`，資料庫帳號，不是 SSH 的 pi|
|Password|另一個 `Store in Vault...`，屬資料庫密碼|
|Default Schema|空白，表示稍後選資料庫|

底部可見 `Test Connection`、`Cancel`、`OK` 與 `Configure Server Management...`。重點是 SSH 帳號與 MariaDB 帳號是兩組獨立認證，不要混用。

頁下為 root 密碼重設程序（原稿救援示範，未執行）：
```sh
sudo systemctl stop mariadb
sudo mysqld_safe --skip-grant-tables --skip-networking &
# 教材要求按 Enter
sudo mysql -u root
```
停止正式服務後以略過權限表方式啟動；`--skip-networking` 同時關閉網路連線，`&` 代表 shell 背景執行。圖片回報 `mysqld_safe Logging to syslog` 與從 `/var/lib/mysql` 啟動 mysqld。略過權限檢查只應在受控救援期間使用；此頁未完成恢復正常服務流程，後續接 P154。

<a id="p154"></a>

### P154｜root 重設後半與 mysqlclient 安裝

[核對原講義第 154 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=154)

承 P153，登入略過權限檢查的服務後，原稿執行：
```sql
FLUSH PRIVILEGES;
ALTER USER 'root'@'localhost' IDENTIFIED BY '1234';
exit
```
再回 shell：`sudo mysql -u root -p`。教材意圖是重新設定 root 密碼後測試登入。

**安全／缺漏補充：**`1234` 為弱密碼教材例子，不應採用。這兩頁沒有交代停止救援程序並以一般權限驗證模式重啟正式服務；因此不能僅以這段流程認定系統已安全恢復。本次沒有執行任何上述系統／資料庫修改。

Django 使用 MySQL／MariaDB 前，教材安裝 Python 驅動 `mysqlclient`：
```sh
# Windows：原稿後綴 (Windows) 是說明，不是命令參數
pip install mysqlclient
# Debian / Ubuntu：以下為同一行，原稿因版面換行
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
# Red Hat / CentOS
sudo yum install python3-devel mysql-devel
# Linux 裝妥開發標頭／程式庫／編譯工具後
pip install mysqlclient
```
`python3-dev`／`python3-devel` 提供 Python 開發檔，MySQL client dev 套件提供 client 標頭與程式庫，`build-essential` 提供建置工具。此頁沒有實際安裝成功輸出，只有步驟框。參考：<https://pypi.org/project/mysqlclient/>。實際可用套件與建置需求仍取決於當時作業系統及驅動版本，原稿是歷史教學命令。

<a id="p155"></a>

### P155｜資料庫選擇與 SQLite 設定

[核對原講義第 155 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=155)

上半附 mysqlclient 網頁截圖：重複 P154 的 Debian/Ubuntu、Red Hat/CentOS 前置套件，以及 `pip install mysqlclient`。圖片警語指出這只是基本步驟，無法涵蓋所有環境，遇到環境建置錯誤需自行排查或在使用者論壇求助；不是一張安裝完成畫面。

原稿比较 SQLite3、MySQL、PostgreSQL：SQLite 是不需獨立伺服器的單一檔案資料庫，備份方便，教材定位为測試開發／小型專案；MySQL、PostgreSQL 則常用於正式部署。原稿另稱 Django 社群偏愛 PostgreSQL，並舉當時 Heroku 支援 PostgreSQL 為例，這是教材時點的敘述，非本次核實的現行平台方案。

編輯 `project1/settings.py`，原稿片段：
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
# 原稿到此，缺外層結尾 }
```
`default` 是預設連線別名；`ENGINE` 選 SQLite 後端；此後端的 `NAME` 是檔案路徑。此舊式寫法需要 `os` 可用。

**原稿敘述的限制：**原稿寫「建立第一個 App 時產生 db.sqlite3」、「與 MySQL 相容」、「ORM 只需改設定，不需改程式」。應理解為入門簡化：`startapp` 本身不是建立 SQLite 資料庫的保證；SQLite 與 MySQL 並非檔案或所有 SQL 語法相容；ORM 能減少後端差異，但資料迁移、欄位限制、特有 SQL、交易與併發行為仍需檢查。這些為補充，不是默改原文。

<a id="p156"></a>

### P156｜MySQL 連線參數與 PostgreSQL 範例前半

[核對原講義第 156 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=156)

正文 MySQL 設定（保留原稿結構）：
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myproject',
        'USER': 'tony',
        'PASSWORD': '1qaz2wsx',
        'HOST': 'localhost',
        'PORT': '3306',
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        'charset': 'utf8mb4',
    }
}
```
`ENGINE` 決定 Django 資料庫後端；`NAME` 為庫名，`USER`／`PASSWORD` 為 DB 帳密，`HOST`／`PORT` 為連線主機與埠。MariaDB 在這個教學使用 Django MySQL 後端。`init_command` 用來在建立連線時啟用嚴格交易表 SQL mode；`charset` 為連線字元集。

**圖片與正文差異必須保留：**中間 settings.py 截圖把舊 SQLite 的 ENGINE、NAME 註解掉；MySQL 帳號用 `root` 而非正文 `tony`，且正確把兩個驅動選項包在：
```python
'OPTIONS': {
    'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
    'charset': 'utf8mb4',
}
```
所以正文把兩項直接放 `default` 層級是疑點；後文 P163 也採用 `OPTIONS` 包法。密碼明文與 root 連線都僅是原稿示範，應改用安全密鑰來源及最小權限專用帳號，不要把這組值用於部署。

圖片下方補充對應：MySQL → `django.db.backends.mysql`；SQLite3 → `django.db.backends.sqlite3`；PostgreSQL → `django.db.backends.postgresql_psycopg2`。最後開始 PostgreSQL（原稿標題誤寫 `Postgree`）設定：
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'tony',
        'PASSWORD': '1qaz2wsx',
```
主機與埠接到 P157；後端名稱是教材歷史寫法，不在此默換新版名稱。

<a id="p157"></a>

### P157｜Migration、註冊 myapp 與 student 模型

[核對原講義第 157 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=157)

PostgreSQL 設定承接上頁：
```python
        'HOST': 'localhost',
        'PORT': '5432',
    }
# 原稿此處仍未顯示 DATABASES 外層的 }
```
MySQL 例用 3306，PostgreSQL 例用 5432；原稿跨頁結尾不完整，複製時要自行確認括號平衡。

教材命令與原解釋：
```sh
sudo python3 manage.py makemigrations
sudo python3 manage.py migrate
source ./dvdsenv/bin/activate
cd project1/
vim project1/settings.py
sudo vim myapp/models.py
```
`makemigrations` 將模型變更產生 migration 檔案，原文稱建立資料庫與 Django 間的中介檔／表結構快取；`migrate` 把 migration 套用到資料庫、建立或更新結構。兩者不是同一操作。原稿順序先列指令再補虛擬環境與檔案準備；真實操作需先用正確環境並完成設定、模型註冊。通常不需要 sudo 跑 Django，sudo 可能繞過虛擬環境或產生 root 擁有檔案。

`INSTALLED_APPS` 圖包含 `django.contrib.admin`、`auth`、`contenttypes`、`sessions`、`messages`、`staticfiles`，最後加入 `'myapp'`。

模型圖比本頁文字層完整，完整六欄如下（正文下半接到 P158）：
```python
from django.db import models

class student(models.Model):
    cName = models.CharField(max_length=20, null=False)
    cSex = models.CharField(max_length=2, default='M', null=False)
    cBirthday = models.DateField(null=False)
    cEmail = models.EmailField(max_length=100, blank=True, default='')
    cPhone = models.CharField(max_length=50, blank=True, default='')
    cAddr = models.CharField(max_length=255, blank=True, default='')
```
名稱最多 20 字元；性別最多 2，預設 M；生日不可 NULL；email 最多 100、電話 50、地址 255，後三者允許表單留白、預設空字串。`null=False` 是資料庫不可 NULL，與表單 `blank` 不同。模型在此是單數 `student`；P164 改為複數 `students`，資料表名稱不可混用。

<a id="p158"></a>

### P158｜ORM 對應與欄位型別表（上）

[核對原講義第 158 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=158)

頁首續寫 P157 的 `cBirthday`、`cEmail`、`cPhone`、`cAddr` 四行；六欄完整程式已併列在 P157。資料模型繼承 `django.db.models.Model`：

|ORM 模型概念|關聯式資料庫對應|
|---|---|
|類別 Class|資料表 Table|
|物件 Object（類別實體）|一筆記錄 Row / Record|
|屬性 Attribute|欄位 Field|
|方法 Method|CRUD 操作|

以上也是中間圖片表格的全部四組對照。欄位型別逐項如下：

|原稿名稱|參數／用途|應注意的解釋|
|---|---|---|
|`BooleanField`|True / False；教材連結至 checkbox 輸入|布林值|
|`CharField`|`max_length` 指最大字串長度；單行字串|長度以字元為核心概念，不是任意二進位位元組大小|
|`SlugField`|類似 CharField，用於 URL 的一部分|slug 不是完整 URL；表中未展開允許字元規則|
|`TextField`|多行字串；HTML 表單常對應 textarea|適合較長文字|
|`IntegerField`|整數 `-2147483648` 至 `2147483647`|原稿給的是常見 32 位元可攜範圍|
|`BigInteger()`|64 位元大整數|**原稿名稱疑誤：Django 欄位名為 `BigIntegerField`，不是 `BigInteger`**|
|`PositiveIntegerField()`|`0` 至 `2147483647`|原稿稱正整數，但範圍包含 0，較精確為非負整數|
|`DecimalField()`|`max_digits` 最大總位數；`decimal_places`|固定精度十進位數，Python Decimal 物件；**原稿把 decimal_places 寫成「整數位數」，應為小數位數**|
|`FloatField()`|浮點數|與固定精度 Decimal 不同，不保證十進位精確表示|
|`DateField()`|`auto_now` 自動儲存今日日期；`auto_now_add` 僅建立時儲存今日日期（句子接 P159）|Python `datetime.date`|

**補充界線：**欄位型別對應表單元件的描述主要針對 Django 自動產生的表單／admin；手寫 HTML 與原生 SQL 不會僅因模型定義就獲得所有表單驗證。

<a id="p159"></a>

### P159｜欄位型別表（下）、自增主鍵與外鍵

[核對原講義第 159 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=159)

|欄位|原稿參數與說明|
|---|---|
|`DateTimeField()`|`auto_now` 儲存今日日期時間；`auto_now_add` 只在建立時儲存；Python 型別 `datetime.datetime`|
|`EmailField()`|`max_length` 最大字元數，原稿標「上限 254」；儲存有效電子郵件|
|`FileField()`|檔案上傳欄位|
|`ImageField()`|圖片欄位，繼承 FileField，須配合 Pillow 套件|
|`URLField()`|`max_length` 預設 200；儲存完整 URL，繼承 CharField|
|`AutoField()`|`primary_key=True`，自動增量主鍵|
|`ForeignKey()`|第一參數為所指資料表的模型類別；`on_delete=models.CASCADE` 決定被參照列刪除時的處理；預設指向對方主鍵|

**補充與原稿限制：**EmailField 的 254 是 Django 的預設最大長度，不宜描述成使用者不可更改的硬上限；「有效電子郵件」依賴驗證流程，不代表資料庫會替所有原生 SQL 寫入自動驗證。FileField／ImageField 在資料庫一般儲存檔案參照路徑，並非自動把完整檔案內容塞入欄位。

原稿指出 Django 若未指定主鍵，會自動增加 `id`；若欲自行指定自增主鍵，可用 `AutoField(primary_key=True)`。補充：自動 id 實際欄位型別也受 Django 版本與 `DEFAULT_AUTO_FIELD` 設定影響，不能一律假定為舊式 AutoField。

外鍵示範是另一組 `users`、`nations` 概念表，不是前面的 student 模型：
```python
nationality = models.ForeignKey(nations, on_delete=models.CASCADE)
```
`users.nationality` 指向 `nations` 模型的主鍵（教材以 id 說明）。`on_delete` 不是刪除 `nationality` 欄位本身，而是當被參照的 nations 資料列刪除時如何處理相依 users 資料列。

參考：<https://developer.mozilla.org/zh-TW/docs/Learn/Server-side/Django/Models>。

<a id="p160"></a>

### P160｜外鍵圖、五種刪除策略與九種欄位選項

[核對原講義第 160 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=160)

圖片左側黃色 `users` 表內標 `nationality`，箭頭指到右側藍色 `nations` 表；右表列 `Taiwan`、`UK`、`USA`、`Vietname`（最後拼字依圖保留）。箭頭示意外鍵參照，不表示把整個國名清單直接複製到每個 users 欄位。

`ForeignKey` 的 `on_delete` 原稿逐項：
1. `models.CASCADE`：被參照列刪除時，同步刪除相依列。
2. `models.PROTECT`：阻止刪除，拋出 `ProtectedError`。
3. `models.SET_NULL`：外鍵改為 NULL，欄位必須先設 `null=True`。
4. `models.SET_DEFAULT`：改成 `default` 所定義的預設值，需事先提供預設值。
5. `models.DO_NOTHING`：Django 不代為處理。**補充：**不代表資料庫參照完整性約束消失；可能仍觸發完整性錯誤。

欄位通用選項完整表：

|選項|原稿意義與預設值|補充辨識|
|---|---|---|
|`null`|能否為 NULL；預設 False|資料庫儲存層面|
|`blank`|能否空白；預設 False|驗證／表單層面，與 null 分開|
|`default`|預設值或可呼叫物件|函式本身與呼叫後的值不同，見 P161|
|`unique`|值是否唯一；預設 False|約束重複值|
|`primary_key`|是否主鍵；預設 False|主鍵識別每列|
|`editable`|是否顯示在 admin；預設 True|不只 admin，亦影響自動產生 ModelForm 等；非禁止所有程式更改|
|`choices`|select 選項，可用 list 或 tuple|通常為儲存值與顯示標籤配對|
|`help_text`|表單元件額外說明|提供使用者填寫提示|
|`verbose_name`|人類可讀欄位名稱；未指定則由欄位名、底線換空白產生|顯示名稱不等於 DB 欄位更名|

參考：<https://docs.djangoproject.com/en/3.1/topics/db/models/#automatic-primary-key-fields>。

<a id="p161"></a>

### P161｜blank/null 錯誤辨析與四種時間預設值（圖片完整補錄）

[核對原講義第 161 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=161)

原稿紅字補充為：「使用 blank=True（允許空值），會設定 null=True（欄位內容允許 null）；空值 ⇒ 白紙，null ⇒ 沒有東西。」**這句因果關係有誤**：`blank=True` 不會自動設定 `null=True`。一個控制驗證是否可空，一個控制資料庫是否能存 SQL NULL；空字串 `''` 與 NULL 不同。保留原文比喻，但不可據此混用。

圖片標題「django 設置字段動態默認時間的四種方式」，上方正文特別提醒「要使用 ORM 寫法才有效果」。圖中程式（保留 `tow` 拼字及 `now()` 差異）：
```python
from django.db import models
from datetime import datetime

class User(models.Model):
    id = models.BigAutoField('主键', primary_key=True)
    name = models.CharField('名字', max_length=20, db_index=True, default='')
    create_time_one = models.DateTimeField('创建时间', default=datetime.now())
    update_time_one = models.DateTimeField('更新时间', default=datetime.now)
    create_time_tow = models.DateTimeField('创建时间', auto_now_add=True)
    update_time_tow = models.DateTimeField('更新时间', auto_now=True)
```
`BigAutoField` 為大整數自增主鍵；`db_index=True` 對 name 建索引；欄位第一個中文字串是 `verbose_name`。

圖片下面逐項原意與必要訂正：
1. **`default=datetime.now()`：**圖先稱 model 每次初始化時會把預設設為初始化時間，最後又警告它會得到專案啟動時間，通常是錯誤寫法。較精確是 Python 執行欄位定義時即呼叫一次，所得固定 datetime 物件被用作後續預設；不是每次新建物件重新呼叫。
2. **`default=datetime.now`：**圖稱每次新增或修改都自動設為操作時間，且仍可 ORM 手動改欄位。**其中「每次修改也會自動更新」不正確**：傳函式物件只在需要預設值（例如新建且未指定值）時呼叫，日後一般 save 不會因 default 自動更新。
3. **`auto_now_add=True`：**圖說預設 False，True 時新增會自動設操作時間，使用 ORM 手動填入會被覆寫；應理解為一般模型新增／save 路徑的行為，不是任意 SQL 或所有 ORM 更新路徑都會強制覆寫。
4. **`auto_now=True`：**圖說預設 False，True 時新增／修改都會自動設操作時間，手填會被覆寫；較精確是模型 `save()` 相關欄位處理會更新，`QuerySet.update()` 等不會等價地呼叫模型 save。
5. **圖片末尾注意事項：**除非刻意想拿專案啟動附近的固定時間，否則不要用 `default=datetime.now()` 作「動態」預設值。

**額外補充：**啟用 Django 時區支援時，常用 `django.utils.timezone.now` 作可呼叫預設值；這是整理者補充，不是圖中的原始程式。原生 SQL 不會執行這些 Python 欄位自動時間邏輯。

原稿參考：<https://docs.djangoproject.com/en/3.1/ref/models/fields/>、<https://sites.google.com/site/djangonote/basic/models/field-type>、<https://blog.csdn.net/kuanggudejimo/article/details/99291026>。

<a id="p162"></a>

### P162｜模型／MySQL 教學參考頁

[核對原講義第 162 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=162)

本頁已檢視整張頁面：只有「參考文獻」及五個連結，無程式截圖、無新操作步驟；其餘為留白。
1. <https://www.techiediaries.com/django/django-3-tutorial-and-crud-example-with-mysql-and-bootstrap/>
2. <https://www.jianshu.com/p/02732229fe59>
3. <https://djangogirlstaipei.gitbooks.io/django-girls-taipei-tutorial/content/django/models.html>
4. <https://my.oschina.net/yimingkeji/blog/2873227>
5. <https://www.jianshu.com/p/bc41a8bf9d9b>

連結是原稿參考資料的保留，本次閱讀範圍不包含這些網站的延伸全文，亦未聲稱已驗證現況。

<a id="p163"></a>

### P163｜原生 SQL CRUD 原理與 project2 連線設定

[核對原講義第 163 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=163)

章節「3-11 資料庫新增、刪除、修改與查詢（使用 SQL 語法）」；CRUD：Create 新增、Read 讀取、Update 修改、Delete 刪除。

當 `Manager.raw()` 不足以處理無法完整映射為 model 的查詢，或需執行 `UPDATE`、`INSERT`、`DELETE`，可直接使用 SQL。教材說明匯入 `django.db.connection` 代表目前資料庫連線，經 `connection.cursor()` 取得遊標後存取資料庫；此路徑繞過模型層，因此不能假設會執行 Model.save、欄位驗證、自動時間或模型事件。

`vim project2/settings.py` 的完整設定：
```python
DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myproject',
        'USER': 'tony',
        'PASSWORD': '1qaz2wsx',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        }
    }
}
```
與 P156 文字例不同，此次 `init_command`、`charset` 明確在 `OPTIONS` 內。帳密依原稿保留，不能拿明文弱密碼設定當生產部署建議。

參考：<https://docs.djangoproject.com/en/3.2/topics/db/sql/>、<https://docs.djangoproject.com/zh-hans/4.2/topics/db/sql/>、<https://github.com/twtrubiks/django-rest-framework-tutorial>。

<a id="p164"></a>

### P164｜students 模型與畫面／正文差異

[核對原講義第 164 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=164)

上方再次附 settings.py 圖：MySQL、`myproject`、`localhost:3306`、`OPTIONS` 的嚴格模式及 utf8mb4，圖中 `USER='root'`，與 P163 文字的 `tony` 不同。圖下重申 ENGINE 為後端名稱、NAME 為資料庫名称。

`sudo vim myapp/models.py`，本次模型類別為**複數** `students`：
```python
from django.db import models

class students(models.Model):
    cName = models.CharField(max_length=20, null=False)
    cSex = models.CharField(max_length=2, default='M', null=False)
    cBirthday = models.DateField(null=False)
    cEmail = models.EmailField(max_length=100, blank=True, default='')
    cPhone = models.CharField(max_length=50, blank=True, default='')
    cAddr = models.CharField(max_length=255, blank=True, default='')
```
以上依正文轉錄，圖片 `cPhone` 卻是 `max_length=20`，不是 50；不得忽略此差異。欄位其餘參數意義與 P157 相同；預設資料表命名通常組合 app label 與小寫模型名，後續 SQL 的目標正是 `myapp_students`。這與 P157 單數 `student` 的 `myapp_student` 不同，若沿用先前模型而不核對，後續查詢會找錯表。

**必要辨識：**模型預設增加 id 後，後續查詢結果包含 id 加上這六欄；原稿以 `cursor.description` 的欄名順序配對每列值，轉成字典後再讓模板用 `data.id`、`data.cName` 等名稱讀取，不是直接以數字索引讀模板資料。

<a id="p165"></a>

### P165｜Migration 畫面解讀與 list 路由

[核對原講義第 165 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=165)

教材指出 migration 記錄資料表架構與版本，以便日後追蹤：
```sh
sudo python3 ./manage.py makemigrations
sudo python3 ./manage.py migrate
```
第一張圖片实际在虛擬環境提示符下執行 `sudo ./manage.py makemigrations`，得到 **`No changes detected`**，不是成功生成 students migration 的證據。

第二張圖 `sudo ./manage.py migrate` 顯示 `Apply all migrations: admin, auth, contenttypes, sessions`，接著逐項 OK：
```text
contenttypes.0001_initial
auth.0001_initial
admin.0001_initial
admin.0002_logentry_remove_auto_add
contenttypes.0002_remove_content_type_name
auth.0002_alter_permission_name_max_length
auth.0003_alter_user_email_max_length
auth.0004_alter_user_username_opts
auth.0005_alter_user_last_login_null
auth.0006_require_contenttypes_0002
auth.0007_alter_validators_add_error_messages
auth.0008_alter_user_username_max_length
sessions.0001_initial
```
**原稿證據限制：**可見的已套用 migration 沒有 `myapp`，所以不能從這張圖斷言 `myapp_students` 已建立；真正操作需確認 app 已註冊、產生自己的 migration 並套用。截圖工作目錄是 project1，而正文操作下一段改為 project2；是教學素材混用，非一路照抄即可的單一專案。

新增瀏覽位置：`sudo vim project2/urls.py`。截圖可見以下片段（截圖在 list 行後結束，結尾括號未顯示）：
```python
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', views.list),
```
`/list/` 對應 `myapp.views.list`；admin 匯入不在截圖可见范围内，不能由此認定不存在。完整 URL list 須在實際檔案閉合，view／template 接 P166。

<a id="p166"></a>

### P166｜SELECT 遊標、參數化查詢與 tuple 轉字典

[核對原講義第 166 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=166)

新增 `myapp/views.py` 的 `list(request)`。圖片分為第 8–28 行與第 52–75 行，**中間 29–51 行未呈現**；下面只拼接可見且屬同一流程的程式，不宣稱是整個原檔逐位元複製：
```python
def list(request):
    if 'cName' in request.GET:
        # print("ok")
        cName = request.GET['cName']
    else:
        cName = None
        # print("false")
    print(cName)

    # 原始寫法
    if cName:
        sql = "SELECT * FROM myapp_students WHERE cName= %s"
        val = [cName]
        # print("ok")
    else:
        sql = "SELECT * FROM myapp_students"
        val = []
        # print("false")
    cursor = connections['default'].cursor()  # 連接資料庫
    cursor.execute(sql, val)  # 執行 SQL 語法
    result = cursor.fetchall()  # 取得資料

    # 圖片中間有未展示的程式行；下列接第二張圖
    # 轉換格式
    field_name = cursor.description  # 取得資料表欄位名稱
    cursor.close()
    # print(field_name)
    resultList = []
    # 兩層 foreach
    for data in result:
        # print(data)
        i = 0
        dict_data = {}
        for d in data:
            # print(d)
            dict_data[field_name[i][0]] = d
            i = i + 1
        resultList.append(dict_data)

    errormessage = ""
    if not resultList:  # 判斷有無資料
        errormessage = "無此資料"
    # print(errormessage)
    # print(resultList)
    # return HttpResponse("test...")
    return render(request, "list.html", locals())
```

流程與參數：
- `request.GET` 有 `cName` 才取值；缺少時設 None。第二次 `if cName` 以真值判斷，所以空字串也會走「列全部」分支。
- `WHERE cName=%s` 是姓名**完全相等**，不是 LIKE 模糊搜尋。值交給 `execute(sql, val)`，`%s` 不加引號，也不在 Python 端以 `%` 或 f-string 插入；這一例已採參數化。
- `connections['default']` 選連線別名，需有 `from django.db import connections`（**必要匯入補充，該頁截圖未显示匯入行**）。前頁講 `connection` 單數，實作改用 `connections` 多連線介面，兩者不可混淆。
- `fetchall()` 得到列序列，每列是欄位值序列。`cursor.description` 的每個欄位描述第一項是欄名；將欄名對上值，得到 `{'id': ..., 'cName': ..., ...}` 的字典列表，讓 template 用 `data.cName` 取值。
- 遊標取得結果／描述後關閉。無資料則設定提示；`locals()` 把本地變數傳入模板，教材較簡便，正式專案宜只明確傳需要的 context。

**檔名疑點：**正文說「新增 template list.html」、view 也 render `list.html`，但命令寫 `sudo vim templates/listall.html`；次頁截圖標籤仍是 `list.html`。應保持檔案與 render 一致，不要默認兩檔同一個。

<a id="p167"></a>

### P167｜list.html 完整展示與查詢結果

[核對原講義第 167 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=167)

模板截圖使用 HTML5、`lang="en"`、UTF-8、`X-UA-Compatible=IE=edge`、viewport `width=device-width, initial-scale=1.0`、標題 `Document`；body 的有效程式如下：
```html
<!-- <h1>test</h1> -->
<h1>{{ errormessage }}</h1>
{% for data in resultList %}
    <h2>顯示student資料表的資料</h2>
    編號:{{ data.id }} <br>
    姓名:{{ data.cName }} <br>
    性別:{{ data.cSex }} <br>
    生日:{{ data.cBirthday }} <br>
    郵件:{{ data.cEmail }} <br>
    電話:{{ data.cPhone }} <br>
    地址:{{ data.cAddr }} <br>
{% endfor %}
```
`resultList` 每筆字典產生一組標題加七欄，`errormessage` 無資料時顯示；`for` 迴圈對空列表不產生資料區塊。生日顯示可受 Django 格式／語系影響，不必與資料庫的 ISO 字串外觀相同。

教材測試命令：`sudo python3 manage.py runserver 0.0.0.0:8080`；但瀏覽器圖片網址是 **`127.0.0.1:8000/list/`**，埠號不同，屬素材不一致。`0.0.0.0` 是監聽位址，不是應直接當作使用者端網址；runserver 是開發伺服器。

可見結果有兩筆（僅描述畫面可見，不推定全部資料只有兩筆）：
- 編號 3，潘四敬，F；生日畫面為「八月 11, 1987」；`sugie@superstar.com`；`0914530768`；台北市中央路201號7樓。
- 編號 4，賴勝恩，M；生日「六月 20, 1984」；`shane@superstar.com`；`0946820035`；台北市建國路177號6樓。

這些皆是教材示例資料，不是本次執行查詢所得。

<a id="p168"></a>

### P168｜有結果／無結果的姓名查詢與搜尋入口

[核對原講義第 168 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=168)

本頁上方實際展示 P166 的條件分支結果：
- `127.0.0.1:8000/list/?cName=aa`：編號 11，姓名 aa，性別 M，生日「九月 1, 2022」，郵件 aa，電話與地址留白。
- `127.0.0.1:8000/list/?cName=cc`：顯示大標題「無此資料」，沒有資料列。

**驗證提醒：**畫面 cEmail 為 `aa`，並非有效 email；這正顯示單有 EmailField 不能保證繞過驗證的資料始終合法。

在 `project2/urls.py` 新增：
```python
path('search_name/', views.search_name),
```
截圖同時保留既有 `admin/` 與 `list/` 路由。新增 view：
```python
def search_name(request):
    # return HttpResponse("test...")
    return render(request, "search_name.html", locals())
```
此 view 只顯示搜尋表單，不自行查資料庫；查詢仍由 `/list/` 的 view 處理。頁末要求新增 `search_name.html`，程式接 P169。

<a id="p169"></a>

### P169｜GET 搜尋表單與送出結果

[核對原講義第 169 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=169)

`search_name.html` 的 head 與 P167 同為 HTML5／UTF-8／IE=edge／viewport／Document，body 程式：
```html
<!-- <h1>test</h1> -->
<form action="/list/" method="GET">
    <label for="fname">姓&nbsp;&nbsp;&nbsp;名:</label>
    <input type="text" name="cName" id="cName">
    <p><button type="submit">搜尋</button></p>
</form>
```
`action` 決定送到 `/list/`；`method=GET` 把欄位 `name=cName` 變成 query string，與 P166 `request.GET['cName']` 精確對應；`id` 是 DOM 識別，不決定送出的參數名稱。**原稿可及性小錯：**`label for="fname"` 不等於輸入框 `id="cName"`，點標籤不會正確關聯輸入框，整理時保留原稿而另行指出。

圖片第一步在 `127.0.0.1:8000/search_name/` 填 `aa`，按「搜尋」後第二張網址變 `127.0.0.1:8000/list/?cName=aa`，結果與 P168 同：id 11、aa、M、2022-09-01、email aa、電話地址空白。這是從表單到 query string 再到 SELECT 與 template 的完整資料流。

測試命令仍寫 `sudo python3 manage.py runserver 0.0.0.0:8080`，圖片仍為 8000；GET 用於這種純讀取搜尋合適，但不能據此推廣成以 GET 修改或刪除資料。

<a id="p170"></a>

### P170｜index 清單首頁：查全部、狀態與筆數

[核對原講義第 170 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=170)

`project2/urls.py` 圖中匯入 `admin`、`path`、`views`，保留 `admin/`、`listone/`，紅框新增：
```python
path('index/', views.index),
```
前面實作是 `list/`，此圖卻出現 `listone/` 指到 `views.listone`；這是圖中既存路由，未在本頁提供其函式，不應擅自當成前文 list 的更名指令。

view 圖片只展示數段（115–123、131–144、154–163 行），函式宣告與省略段未呈現。可見的核心流程：
```python
sql = "SELECT * FROM myapp_students"
cursor = connections['default'].cursor()
cursor.execute(sql, [])
result = cursor.fetchall()
# print(result)
# 轉換格式
field_name = cursor.description
# print(field_name)

resultList = []
for data in result:
    i = 0
    dict_data = {}
    for d in data:
        # print(d)
        dict_data[field_name[i][0]] = d
        i = i + 1
    print(dict_data)
    resultList.append(dict_data)
print(resultList)

errormessage = ""
status = True
if not resultList:
    errormessage = "無此資料"
    status = False
# print(errormessage)
data_count = len(resultList)
# print(data_count)
# return HttpResponse("test...")
return render(request, 'index.html', locals())
```
與 P166 同樣將資料列轉字典，這次沒有 cName 條件，額外提供 `status` 控制顯示清單或無資料提示，`data_count` 計算取回資料的筆數。`print(dict_data)` 與 `print(resultList)` 是實際開啟的除錯輸出，會把個資寫入伺服器終端／日誌，部署前應留意。

**證據限制／補充：**圖中未見 cursor.close，可能位於省略區段，不能斷言原檔一定沒有；實務可採 context manager 確保資源釋放。`len(resultList)` 的前提是所有列已抓到記憶體，資料量大時應考慮分頁與資料庫 COUNT，不在此冒充原稿內容。

<a id="p171"></a>

### P171｜base.html 繼承與首頁表格

[核對原講義第 171 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=171)

`vim templates/base.html` 的完整可見骨架：
```html
<!-- base.html -->
<!DOCTYPE html>
<html>
<head>
    {% block title %}{% endblock %}
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```
圖片紅框圈 `title` 與 `content` 兩個 block，讓子模板覆寫。原稿未在這個 base 骨架內顯示 charset／viewport，不應假稱已有。

`templates/index.html` 前三行為：
```django
{% extends 'base.html' %}
{% block title %}
<title>學生資料管理系統</title>
```
圖片略過 4–33 行，接著顯示 34–62 行：
```html
<div>
{% if status %}
<table>
    <tr>
        <th>學號</th><th>姓名</th><th>性別</th><th>生日</th>
        <th>信箱</th><th>電話</th><th>地址</th><th>編輯</th>
    </tr>
    {% for data in resultList %}
    <tr>
        <td>{{ data.id }}</td>
        <td>{{ data.cName }}</td>
        <td>{% if data.cSex == "M" %}男{% else %}女{% endif %}</td>
        <td>{{ data.cBirthday }}</td>
        <td>{{ data.cEmail }}</td>
        <td>{{ data.cPhone }}</td>
        <td>{{ data.cAddr }}</td>
        <td>
            <a href="/edit1/{{ data.id }}/load/">編輯1</a> <!-- get -->
            <a href="/edit2/{{ data.id }}/">編輯2</a> <!-- post -->
            <a href="/delete/{{ data.id }}/">刪除</a> <!-- get -->
        </td>
    </tr>
    {% endfor %}
</table>
{% else %}
<h1>無資料</h1>
{% endif %}
</div>
```
可見內容沒有 `block content` 開始與結尾，因此上面是**原圖可見片段**，不是直接可用的完整 index.html。`status=False` 不顯示空表，改顯示「無資料」。性別以 M 為男，其他一律女，對空值／未知代碼無額外分支，實際系統需定義資料驗證與顯示規則。

三個連結帶 id：`edit1` 載入模式、`edit2` 編輯入口、`delete` 刪除。即使註解 `<!-- post -->`，`<a href>` 本身仍發 GET；「post」指後續編輯表單的送出方式，不是此連結會用 POST。此圖刪除入口註解為 GET，但 P176 的實際 view 是 GET 顯示確認頁、POST 才刪除；不要把入口連結誤認為直接 GET 刪資料。直接以 GET 刪除仍是不安全做法。

測試命令仍為 `sudo python3 manage.py runserver 0.0.0.0:8080`，結果接 P172。

<a id="p172"></a>

### P172｜首頁十筆資料與 POST 新增 view 前半

[核對原講義第 172 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=172)

首頁結果圖的網址 `127.0.0.1:8000/index/`，大標「學生資料管理系統」、副標「目前的資料筆數:10」、連結「新增學生資料」。每列尾端皆有編輯1、編輯2、刪除；表格的十筆教材資料經局部重繪核讀如下（空白以「空」註記）：

|學號|姓名|性別|生日|信箱|電話|地址|
|---|---|---|---|---|---|---|
|3|潘四敬|女|1987-08-11|sugie@superstar.com|0914530768|台北市中央路201號7樓|
|4|賴勝恩|男|1984-06-20|shane@superstar.com|0946820035|台北市建國路177號6樓|
|5|黎楚寧|女|1988-02-15|ivy@superstar.com|0920981230|台北市忠孝東路520號6樓|
|6|蔡中穎|男|1987-05-05|zhong@superstar.com|0951983366|台北市三民路1巷10號|
|7|徐佳瑩|女|1985-08-30|lala@superstar.com|0918123456|台北市仁愛路100號|
|8|林雨媗|女|1986-12-10|crystal@superstar.com|0907408965|台北市民族路204號|
|9|林心儀|女|1988-12-01|peggy@superstar.com|0916456723|台北市建國北路10號|
|10|王燕博|男|1993-08-10|albert@superstar.com|0918976588|台北市北環路2巷80號|
|11|aa|男|2022-09-01|aa|空|空|
|12|bb|男|2022-09-08|bb33|空|空|

圖片生日以 ISO 形狀顯示，與 P167 逐筆頁的本地化文字不同；本頁未解釋這個格式差異，不應自行補稱原模板已有 date filter。

進入「資料新增（SQL-INSERT 語法）」。正文改寫 `sudo vim project1/urls.py`，前面多為 project2，屬專案名稱混用。圖中 `from myapp import views` 紅框強調，新增：
```python
path('post1/', views.post1),
```
`myapp/views.py` 的可見前半：
```python
from django.shortcuts import redirect

def post1(request):
    if request.method == "POST":
        cName = request.POST["cName"]
        cSex = request.POST["cSex"]
        cBirthday = request.POST["cBirthday"]
        cEmail = request.POST["cEmail"]
        cPhone = request.POST["cPhone"]
        cAddr = request.POST["cAddr"]
```
全部值取自 POST 表單，六個 key 必須與 input `name` 一致；中間 174–185 行未展示，SQL 與回應接 P173。直接用 `request.POST[...]` 遇缺欄位會出錯，且本頁可見程式未展示伺服器端驗證。

<a id="p173"></a>

### P173｜INSERT 字串拼接、redirect 與 post1 模板上半

[核對原講義第 173 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=173)

續 P172，截圖標「可檢查版本」的 INSERT 程式（行 186–199）：
```python
        # 可檢查版本
        sql = "INSERT INTO myapp_students (cName,cSex,cBirthday,cEmail,cPhone,cAddr)"
        sql += "VALUES('%s','%s','%s','%s','%s','%s')"
        sql %= (cName, cSex, cBirthday, cEmail, cPhone, cAddr)
        # print(sql)
        cursor = connections["default"].cursor()
        cursor.execute(sql, [])
        cursor.close()
        # return HttpResponse("已送出...")
        return redirect('/index/')  # 自動轉址
    else:
        # return HttpResponse("test...")
        return render(request, 'post1.html', locals())
```
`INSERT INTO` 指定六個欄位，省略自增 id；六個值按同一順序填入。POST 完成後 redirect 回 `/index/`，非 POST 則顯示表單，構成「先 GET 顯示，再 POST 寫入，再 redirect GET 清單」的流程。原稿 SQL 字串在 `)` 與 `VALUES` 間沒有明示空白，依原圖保留；關鍵安全問題不是空白，而是使用 Python `%=` 把輸入直接拼成 SQL。

**高風險原稿示範，非生產推薦：**`cursor.execute(sql, [])` 的空列表不會讓已被插入字串的使用者輸入重新變安全；單引號姓名會破壞語句，更可能造成 SQL injection。應另行改用參數化，例如以下為**整理者安全補充，不是原稿**：
```python
sql = ("INSERT INTO myapp_students "
       "(cName,cSex,cBirthday,cEmail,cPhone,cAddr) VALUES (%s,%s,%s,%s,%s,%s)")
cursor.execute(sql, [cName, cSex, cBirthday, cEmail, cPhone, cAddr])
```
placeholder 不自行加引號，也不先做字串格式化；尚需伺服器端格式／長度／權限驗證。

`templates/post1.html` 可見上半：
```html
{% extends 'base.html' %}
{% block title %}
<title>學生資料管理系統-新增資料</title>
<style>
    h1, h3 { text-align: center; }
    table { margin-left: auto; margin-right: auto; }
    table, th, td { border: 1px solid black; border-collapse: collapse; }
</style>
{% endblock %}
{% block content %}
<div>
    <h1 class="title">學生資料管理系統-新增資料</h1>
    <a href="/index/"><h3>回首頁</h3></a>
</div>
```
標題置中、表格水平置中、黑色 1px 邊線合併。此頁尚未顯示 form；表單下半接 P174，不可把這一段當成完整新增頁。

<a id="p174"></a>

### P174｜新增表單完整欄位、CSRF 與瀏覽器樣貌

[核對原講義第 174 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=174)

接續 post1.html 的 content 區塊，圖中 27–65 行主體（僅合併排版，保留欄位命名與原稿錯字）：
```html
<div>
<form action="/post1/" method="POST">
    {% csrf_token %}
    <table>
        <tr>
            <th>*姓名</th>
            <td><input type="text" id="cName" name="cName" required placeholder="請輸入姓名"></td>
        </tr>
        <tr>
            <th>*性別</th>
            <td>
                <input type="radio" id="cSex" name="cSex" value="M" checked>男
                <input type="radio" id="cSex" name="cSex" value="F">女
            </td>
        </tr>
        <tr>
            <th>*生日</th>
            <td><input type="date" id="cBirthday" name="cBirthday" required></td>
        </tr>
        <tr>
            <th>*信箱</th>
            <td><input type="mail" id="cEmail" name="cEmail" required placeholder="請輸入mail"></td>
        </tr>
        <tr><th>電話</th><td><input type="text" id="cPhone" name="cPhone"></td></tr>
        <tr><th>地址</th><td><input type="text" id="cAddr" name="cAddr"></td></tr>
        <tr>
            <th colspan="2" style="text-align:center;">
                <input type="submit" name="button" id="button" value="儲存">
                <input type="reset" name="button2" id="button2" value="清除">
            </th>
        </tr>
    </table>
</form>
</div>
{% endblock %}
```

資料流細節：
- `POST /post1/` 與 view 的 `request.method == "POST"` 對應。
- `{% csrf_token %}` 為 Django POST 表單提供 CSRF token；它防的是跨站請求偽造，不是 SQL injection，也不是登入／物件權限檢查。
- 性別 radio 共享 `name=cSex`，只提交所選 M 或 F，M 預選；但兩個 radio 共用相同 `id=cSex` 是原稿 HTML 重複 id 問題。
- 姓名、生日、信箱有 required；電話、地址無 required。星號是視覺提示，真正瀏覽器必要欄位由 required 決定。
- **原稿 `type="mail"` 不是標準 email input type**，通常退回 text，不能期待電子郵件格式驗證。正確 email 型別與伺服器端驗證應另行补上。
- 模型 `cEmail` 是 `blank=True`，這個手寫表單卻強制 required，兩層規則不一致但不會自動互相修正。
- reset 是把表單恢復初始值，不會刪除資料庫資料；submit 才送出。

瀏覽器 `127.0.0.1:8000/post1/` 顯示置中的新增標題、回首頁、六欄表格，姓名與信箱提示文字、預選男、生日日期元件，底下「儲存／清除」。**這張圖只是空白新增表單，不是新增成功／筆數增加證據**。命令仍列 `sudo python3 manage.py runserver 0.0.0.0:8080`，與圖片埠不同。

<a id="p175"></a>

### P175｜刪除入口路由與整體 CRUD URL 對照

[核對原講義第 175 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=175)

本頁標題「資料刪除（SQL-DELETE 語法）」，編輯 `project2/urls.py`。圖中完整有效路由內容如下：
```python
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', views.list),
    path('search_name/', views.search_name),
    path('index/', views.index),
    path('post1/', views.post1),
    path('edit1/<int:id>/<str:mode>/', views.edit1),
    path('edit2/<int:id>/', views.edit2),
    path('delete/<int:id>/', views.delete),
]
```
紅框圈出 `delete/<int:id>/`。`<int:id>` 是路徑轉換器，把符合整數格式的 URL 段轉成 Python int 傳入 view；此 id 為資料列識別，不是表單 name 或欄位索引。`edit1` 額外接受 `<str:mode>` 決定載入／儲存；`edit2` 只帶 id，改由 HTTP 方法區分操作。

頁下要求新增 `myapp/views.py` view functions，但**程式實際接在 P176**，本頁沒有刪除成功畫面。

<a id="p176"></a>

### P176｜刪除實作：GET 查詢確認、POST 才 DELETE

[核對原講義第 176 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=176)

本頁完整可見 `delete(request, id=None)`。它不是點 GET 連結立即刪除；實際程式先依 HTTP 方法分流：
```python
def delete(request, id=None):
    if request.method == "POST":
        sql = "DELETE FROM myapp_students WHERE id=%s"
        sql %= (id)
        cursor = connections["default"].cursor()
        cursor.execute(sql, [])
        cursor.close()
        print(sql)
        # return HttpResponse("按刪除")
        return redirect('/index/')
    else:
        sql = "SELECT * FROM myapp_students WHERE id = %s" % (id)
        # print(sql)
        cursor = connections["default"].cursor()
        cursor.execute(sql, [])
        result = cursor.fetchall()  # 資料
        # print(result)
        field_names = cursor.description  # 欄位名稱
        # print(field_names)
        cursor.close()

        dict_data = {}
        for data in result:
            i = 0
            for d in data:
                # print(d)
                dict_data[field_names[i][0]] = d
                i = i + 1
            # print(dict_data)
        print(dict_data)
        # return HttpResponse("test...")
        return render(request, "delete.html", locals())
```

逐步說明：
1. 清單連結 GET `/delete/id/` 時執行 SELECT，取指定列及欄名，關閉遊標。
2. 把那一列轉為 `dict_data`，交給 `delete.html` 顯示確認資料；因 id 是主鍵，理想上最多一列。
3. 確認頁用 POST 再送至同一路由，才執行 `DELETE ... WHERE id=...`，關閉遊標並 redirect `/index/`。
4. `WHERE` 必須保留，否則可能變成全表刪除。原稿 `print(sql)`、`print(dict_data)` 是除錯輸出，包含敏感資料風險。

**原稿風險／缺漏：**仍用 Python 字串插值而非 DB 參數；雖路由 `<int:id>` 限定整數，不能因此把這種拼接教成通用安全方式。安全補充可改 `cursor.execute("DELETE FROM myapp_students WHERE id=%s", [id])`。沒有看到登入／物件存取權限檢查或找不到資料的 404 處理；空結果會留下 `{}`。範圍內沒有 `delete.html` 原碼，無法確認該表單是否有 `{% csrf_token %}`，不可聲稱已具備。

**釐清前面註解：**P171 的刪除 `<a>` 註解 get 只說入口請求；此頁實作已改成 POST 真正刪除。任何另行以 GET 直接執行 DELETE 的版本都只應視為不安全教學，不能用於部署。測試命令列 runserver 8080，確認頁結果接 P177。

<a id="p177"></a>

### P177｜刪除確認畫面與 GET 更新路由

[核對原講義第 177 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=177)

上方瀏覽器畫面標題為「學生資料管理系統-刪除資料—(POST)」，有回首頁連結、資料確認表及「刪除」按鈕。表格內容：姓名潘四敬、性別女、生日 1987-08-11、信箱 `sugie@superstar.com`、電話 `0914530768`、地址台北市中央路201號7樓。地址列因欄寬較滿；URL 只看得到 `127.0.0.1:8000/delete...`，完整 id 在截圖被瀏覽器省略，不能聲稱網址明確顯示 `/delete/3/`，雖資料與前文 id 3 相同。

這是**刪除前的確認頁**，沒有刪除後清單或筆數變化，不能把它誤記為刪除成功證據。

下半開始「資料更新（使用 GET）（SQL-UPDATE 語法）」，`project2/urls.py` 圖紅框：
```python
path('edit1/<int:id>/<str:mode>/', views.edit1),
```
保留其他路由，包括 edit2 與 delete。清單上的 `/edit1/{{ data.id }}/load/` 提供 `id` 和 `mode='load'`；`load` 用來載入資料到表單，後續 `edit` 會用 GET 參數儲存，程式接 P178。

**安全先讀：**GET 用於讀取及呈現編輯表單可以，但以 GET 執行 UPDATE 不符合安全方法語意，會把個資放入網址並暴露於歷史、日誌或 Referer；也可能受預載／爬蟲等觸發。本節保留原稿示範，非生產推薦；P181–183 再展示 POST 版。

<a id="p178"></a>

### P178｜edit1：load 載入、edit 以 GET 寫入 UPDATE

[核對原講義第 178 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=178)

`myapp/views.py` 的三張程式圖，經局部重繪確認分支字樣是 **`mode == "edit"`** 與 `mode == "load"`，沒有 `save` 分支。原圖跳過 211–220 行，後兩張行號還有重疊，表示是多張摘錄，不是連續完整原檔。可見程式依邏輯重排如下：
```python
def edit1(request, id=None, mode=None):
    # print(id)
    # print(mode)
    if mode == "edit":
        cName = request.GET["cName"]
        cSex = request.GET["cSex"]
        cBirthday = request.GET["cBirthday"]
        cEmail = request.GET["cEmail"]
        cPhone = request.GET["cPhone"]
        cAddr = request.GET["cAddr"]
        # 原圖此處有未展示的程式段
        sql = "UPDATE myapp_students SET "
        sql += "cName='%s', cSex='%s',cBirthday='%s', cEmail='%s', cPhone='%s', cAddr='%s' WHERE id=%s"
        sql %= (cName, cSex, cBirthday, cEmail, cPhone, cAddr, id)
        print(sql)
        cursor = connections["default"].cursor()
        cursor.execute(sql, [])
        cursor.close()
        # return HttpResponse("修改.......")
        return redirect('/index/')
    elif mode == "load":
        sql = "SELECT * FROM myapp_students WHERE id = %s" % (id)
        # print(sql)
        cursor = connections["default"].cursor()
        cursor.execute(sql, [])
        result = cursor.fetchall()
        print(result)
        field_names = cursor.description
        cursor.close()
        print(field_names)
        dict_data = {}
        for data in result:
            i = 0
            for d in data:
                # print(d)
                dict_data[field_names[i][0]] = d
                i = i + 1
            # print(dict_data)
        print(dict_data)
        # return HttpResponse("test.......")
        return render(request, "edit1.html", locals())
```

操作順序：先 GET `/edit1/id/load/`，SELECT 主鍵列、轉 `dict_data`、render 編輯模板；表單再 GET `/edit1/id/edit/?cName=...&cSex=...`，六值連同 URL 的 id 被填進 UPDATE，執行後 redirect `/index/`。`SET` 列出欲修改的六欄，`WHERE id` 限定目標，主鍵本身未修改。

**原稿限制／安全補充：**
- 以 GET 做寫入會使 URL、瀏覽器歷史與伺服器日誌攜带全部表單值，不應部署。
- `%=` 的 SQL 字串插值仍可被使用者輸入破壞／注入；應採獨立參數。例如安全補充寫法是 `cursor.execute("UPDATE myapp_students SET cName=%s,cSex=%s,cBirthday=%s,cEmail=%s,cPhone=%s,cAddr=%s WHERE id=%s", [cName,cSex,cBirthday,cEmail,cPhone,cAddr,id])`，並配合 POST、CSRF、授權與驗證。
- 圖中沒有其他 mode 的 return；若 mode 是未知值，view 可能回 None 而報錯，需另加拒絕／404 分支。
- 查不到 id 的情況沒有明確處理；`dict_data` 會空。`print` 結果、欄位描述、整條 SQL 會造成日誌資訊暴露。

頁末 `sudo vim templates/edit1.html`，模板接 P179。

<a id="p179"></a>

### P179｜編輯模板完整帶值與另一組測試資料

[核對原講義第 179 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=179)

本頁模板經重繪，date 的 value **確實沒有 date filter**。原圖可見程式（僅換行排版）：
```html
{% extends 'base.html' %}
{% block title %}
<title>學生資料管理系統-修改資料—(GET)</title>
{% endblock %}
{% block content %}
<h1>學生資料管理系統-修改資料—(GET)</h1>
<a href="/index/"><h3>回首頁</h3></a>
<form action="/edit1/{{dict_data.id}}/edit/" method="get">
<table>
    <tr><th>姓名</th><td><input type="text" id="cName" name="cName" value="{{ dict_data.cName }}"></td></tr>
    <tr><th>性別</th><td>
        <input type="radio" id="cSex" name="cSex" value="M" {% if dict_data.cSex == "M" %} checked {% endif %}>男
        <input type="radio" id="cSex" name="cSex" value="F" {% if dict_data.cSex == "F" %} checked {% endif %}>女
    </td></tr>
    <tr><th>生日</th><td><input type="date" id="cBirthday" name="cBirthday" value="{{ dict_data.cBirthday }}"></td></tr>
    <tr><th>信箱</th><td><input type="text" id="cEmail" name="cEmail" value="{{ dict_data.cEmail }}"></td></tr>
    <tr><th>電話</th><td><input type="text" id="cPhone" name="cPhone" value="{{ dict_data.cPhone }}"></td></tr>
    <tr><th>地址</th><td><input type="text" id="cAddr" name="cAddr" value="{{ dict_data.cAddr }}"></td></tr>
    <tr><th colspan="2" style="text-align:center;">
        <input type="submit" name="button" id="button" value="儲存">
        <input type="reset" name="button2" id="button2" value="重設">
    </th></tr>
</table>
</form>
{% endblock content %}
```

`value` 帶入現有欄值；radio 用 if 判斷哪一個 checked，避免一律預選男；仍有兩個同名 id 的原稿問題。`type=date` 的 HTML value 應為 `YYYY-MM-DD`；如果 `dict_data.cBirthday` 是 Python date 而被本地化，可能不合 date input 規格。**補充修法**可用 `{{ dict_data.cBirthday|date:'Y-m-d' }}` 或在 view 明確格式化；原稿沒有這行，不默改。email 這次是 text 型別，也沒有 required，與新增表單不同；reset 恢復頁面載入時的值，不是儲存修改。

頁下測試已換另一批舊版畫面：`192.168.57.236:8080/index/`，標題「顯示 student 資料表所有資料」，連結「新增資料」，欄名「編號、姓名、性別、生日、郵件帳號、電話、地址、編輯」。可見三筆：
- id 6：bb、M、2021年2月11日、`bb@gmial.com`、電話 bb、地址 bb。
- id 7：aa、M、2021年2月10日、`bb@gmial.com`、電話 `09222222`、高雄市。
- id 8：aa、M、2021年2月1日、`aa@google.com.tw`、電話 `09222222`、高雄市。

這批 id 6 已非 P172 的蔡中穎；郵件 `gmial` 依圖保留，不能修成 gmail。截圖與上方模板的頁面標題、按鈕文字也有差異，顯示不是完全相同版本的實錄。測試指令 `sudo python3 manage.py runserver 0.0.0.0:8080` 在這組圖與瀏覽器埠一致。

<a id="p180"></a>

### P180｜GET 更新請求日誌、302 轉址及資料變動

[核對原講義第 180 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=180)

本頁多張圖片已局部重繪核讀。上方載入編輯畫面網址 **`192.168.57.236:8080/edit1/6/load`**（圖中末尾沒有 slash），標題「student 資料表修改(一)」：姓名 bb、男生已勾、日期 `2021/02/11`、郵件 `bb@gmial.com`、電話 bb、地址 bb；按鈕是「送出／重設」，不是前頁模板的「儲存」。

中間終端顯示歷史教材環境而非本次執行：
```text
System check identified no issues (0 silenced).
June 07, 2021 - 10:59:59
Django version 2.2.18, using settings 'project2.settings'
Starting development server at http://0.0.0.0:8080/
Quit the server with CONTROL-C.
web get
[07/Jun/2021 10:59:59] "GET /edit1/6/load HTTP/1.1" 200 1271
form get
```
接著一條綠色 GET 儲存請求開頭為 `GET /edit1/6/edit?cName=bb&cSex=M&cBirthday=2021`，**中段被原始截图裁切**，可見尾段 `b&cAddr=bb&button=%E9%80%81%E5%87%BA HTTP/1.1" 302 0`；下一行：
```text
[07/Jun/2021 11:00:06] "GET /index/ HTTP/1.1" 200 11271
```
紅框標出 `form get`；重点是編輯表單真的透過 GET query string 送值，view 回 302 轉址，瀏覽器跟隨 GET 首頁並收到 200。不補造被裁掉的生日／郵件／電話參數。完整 query string 可包含隱私資料，這也是不用 GET 寫入的理由。

下方另外一張首頁狀態：id 6 改為 `bb111`、M、2021年6月11日、`bb@gmial.com11`、電話 `bb11`、地址 `bb11`；id 7 仍 aa、M、2021年2月10日、`bb@gmial.com`、`09222222`、高雄市。這張圖是另一個操作後狀態，不能說正是上面送 bb 的那條請求所產生。

最後再次編輯表單：姓名 `bb000`、男、生日 `2021/06/12`、郵件 `bb@gmial.com00`、電話 `09999111`、地址 `000`；點送出後的結果接 P181。這些不合一般真實資料格式的 email／電話依原稿保留；本次未向任何系統送出。

<a id="p181"></a>

### P181｜GET 更新結果與 edit2 路由（標題誤植）

[核對原講義第 181 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=181)

頁首接 P180 最後一個表單，`192.168.57.236:8080/index/` 的可見資料列：id 6、姓名 `bb000`、性別 M、生日 2021年6月12日、email `bb@gmial.com00`、電話 `09999111`、地址 `000`，右側仍有編輯一、編輯二、刪除。這與前頁最後輸入值相符，展示回首頁後的狀態；截圖只見首筆及下方部分內容，不把它誤認為整個資料庫只剩一筆。

下半標題仍寫「資料更新（使用 GET）（SQL-UPDATE 語法）」，但紅框新增的是：
```python
path('edit2/<int:id>/', views.edit2),
```
其餘路由同 P175。此頁只指示編輯 `myapp/views.py`，程式接 P182，**實際後續以 POST 更新，因此本頁 GET 標題是誤植／複製未改**。

與 edit1 比較：edit2 的 URL 不帶 mode，靠 HTTP method 區分 GET 載入與 POST 儲存；使用者從首頁「編輯二」連結 GET 進入，仍是合理的讀取請求，不能誤認入口連結本身用 POST。

<a id="p182"></a>

### P182｜edit2：POST 更新與 GET 載入的完整 view

[核對原講義第 182 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=182)

上半兩張程式圖已局部重繪，明確以 `request.method == "POST"` 分支，證實 P181「使用 GET」標題不符本例。可見程式：
```python
def edit2(request, id=None):
    # print(id)
    if request.method == "POST":
        cName = request.POST["cName"]
        cSex = request.POST["cSex"]
        cBirthday = request.POST["cBirthday"]
        cEmail = request.POST["cEmail"]
        cPhone = request.POST["cPhone"]
        cAddr = request.POST["cAddr"]
        sql = "UPDATE myapp_students SET "
        sql += "cName='%s', cSex='%s',cBirthday='%s', cEmail='%s', cPhone='%s', cAddr='%s' WHERE id=%s"
        sql %= (cName, cSex, cBirthday, cEmail, cPhone, cAddr, id)
        print(sql)
        cursor = connections["default"].cursor()
        cursor.execute(sql, [])
        cursor.close()
        # return HttpResponse("修改.......")
        return redirect('/index/')
    else:
        sql = "SELECT * FROM myapp_students WHERE id = %s" % (id)
        # print(sql)
        cursor = connections["default"].cursor()
        cursor.execute(sql, [])
        result = cursor.fetchall()  # 資料
        print(result)
        field_names = cursor.description  # 欄位名稱
        print(field_names)
        cursor.close()
        dict_data = {}
        for data in result:
            i = 0
            for d in data:
                # print(d)
                dict_data[field_names[i][0]] = d
                i = i + 1
            # print(dict_data)
        print(dict_data)
        # return HttpResponse("test.......")
        return render(request, "edit2.html", locals())
```

與 edit1 的精確差異：
- URL 只要 id；不使用 mode。
- POST 從 `request.POST` 取六欄並 UPDATE；else 先 SELECT、轉字典、render `edit2.html`。
- 儲存後仍 redirect `/index/`，避免重整結果頁就重複送出同一份 POST。
- 圖中 else 不只明文檢查 GET，其他非 POST 方法也會進入；正式程式宜明確限制允許的方法。

**安全／缺件：**POST 不等於自動安全；SQL 仍以 `%=` 拼字串，需改獨立參數化。還需認證、列層級授權、CSRF token、伺服器端驗證、找不到記錄的處理與適當日誌策略。**P146–183 範圍沒有展示 `edit2.html` 程式碼**，只有 view 與結果，故無法由教材圖片核實它的 form action、CSRF、date 格式等。可推知為達成此 view 必須向對應 `/edit2/id/` 送 POST 並提供六個同名欄位，但這是必要條件說明，不冒充原稿模板轉錄。

頁下命令 `sudo python3 manage.py runserver 0.0.0.0:8080`，瀏覽器 `192.168.57.236:8080/index/` 的三筆畫面如下：

|id|姓名|性別|生日|郵件帳號|電話|地址|
|---|---|---|---|---|---|---|
|6|bb|F|2021年6月12日|bb@gmial.com|09999|空白|
|7|aa|M|2021年2月10日|bb@gmial.com|09222222|高雄市|
|8|aa|M|2021年2月1日|aa@google.com.tw|09222222|高雄市|

游標停在首筆「編輯二」。此頁 id6 又是 bb/F，不是前頁 bb000/M，表示不同測試時點的畫面，不硬拼成無縫的單次操作。

<a id="p183"></a>

### P183｜POST 編輯表單與回首頁結果（圖片頁，不是空白頁）

[核對原講義第 183 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=183)

本頁文字層幾乎只有教師頁眉與頁碼，**主要知識全在上方兩張瀏覽器截圖**，已親自檢視並局部重繪。

第一張「student 資料表修改(二)」表單，輸入內容：
- 姓名：`bb33`。
- 性別：左側標籤仍帶 `F`（顯示原資料碼），radio 卻已勾選「男生」，表示使用者正把 F 改為 M；不能只讀標籤認定提交 F。
- 生日：`2021/06/12`。
- 郵件帳號：`bb33@gmial.com`（原圖 gmial，不改成 gmail）。
- 電話：`0999933`。
- 地址：`pp`。
- 按鈕：「送出」與「重設」，游標在送出附近。上方網址受窄幅裁切，無法讀完整 edit2 路徑或 id，不補造。

第二張顯示回到 `192.168.57.236:8080/index/`，標題「顯示 student 資料表所有資料」、新增資料連結及首筆更新結果：

|編號|姓名|性別|生日|郵件帳號|電話|地址|操作|
|---|---|---|---|---|---|---|---|
|6|bb33|M|2021年6月12日|bb33@gmial.com|0999933|pp|編輯一、編輯二、刪除|

這與第一張表單的新值一致，展示 edit2 接收 POST 更新再轉址的教材預期結果。畫面只截到一列，不等於資料庫總共一列；此頁沒有 HTTP POST 日誌或直接 SQL 驗證輸出，因此僅作教材圖片結果記錄，不宣稱本次實際執行成功。

**本範圍整體界線：**已閱讀 P146–183 的文字與每一頁圖像，保留 DB 安裝／設定、欄位型別與選項、SQL CRUD、模板、URL、參數及圖中資料變化。所有安裝、帳號、資料庫及伺服器命令均僅轉錄解說，未執行；原稿缺圖外程式與圖文矛盾均明確標示，不替它編造缺失的完整應用。



---

## Python and Django 講義逐頁完整知識筆記：P184–P205

> 範圍僅為原 PDF 第184–205頁；文字層與每頁圖片交叉閱讀。以下保留原稿的專案、模型、變數與範例資料名稱；原稿錯字、過時判斷及安全問題另以「補充／疑點」標明，不把修正版冒充原稿。程式以閱讀、轉錄為目的，未對真實資料庫執行新增、刪除或更新。

<a id="p184"></a>

### P184｜3-12 資料庫查詢（使用 ORM）

[核對原講義第 184 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=184)

- Django 以物件方法包裝底層 SQL，不必每次自行撰寫 SQL。`django.db.models.Model` 是應用程式與資料庫的介面，也就是 MTV 架構中的 **M（Model）**；模型類別及其實例對應資料表與資料。
- 原文前段把 ORM 寫為 `Object Relational Model`，後段則為 `Object-Relational Mapping`。其核心是把關聯式資料庫與程式中的業務實體物件建立映射，開發者以熟悉的程式語言完成資料操作，不必直接寫 SQL 或預存程序。
- 不同資料庫的 SQL 方言存在差異；ORM 封裝差異，使 SQLite、MySQL、原文所稱 Postgre 之間的切換較容易，通常先調整後端設定，而不是重寫全部 ORM 呼叫。

| CRUD | 英文 | 中文 | 對應 SQL 操作 |
|---|---|---|---|
| C | Create | 新增 | INSERT |
| R | Read | 讀取／查詢 | SELECT |
| U | Update | 修改 | UPDATE |
| D | Delete | 刪除 | DELETE |

**圖解完整閱讀：**左側紅框為 `django`，分為「物件的增加、修改、刪除」與「查詢」；箭頭指向中央 `ORM`。上半部把操作轉為特定資料庫的 `insert、update、delete` 語句；下半部把查詢轉為特定資料庫的 `select` 語句，從資料庫取回資料集，再轉為 Python 中的列表。中央與右側資料庫之間有雙向箭頭；右側三個紅框由上而下為 `mysql`、`orcale`（原圖拼字）、`sqlite`。圖的重點是「物件操作→SQL→資料庫」及「資料庫結果→Python 物件／集合」的雙向轉換。

ORM 三項主要任務：
1. 根據物件的類型生成資料表結構。
2. 將物件、列表的操作轉換成 SQL。
3. 將 SQL 查詢結果轉換成物件、列表。

本頁開始列優點：隱藏資料存取細節、提供資料庫映射，讓取得資料像操作物件一樣。

**補充／疑點：**ORM 的慣用全名是 Object-Relational Mapping；Django 查詢一般回傳 `QuerySet`，不是一律立即建立 Python `list`。切換資料庫也可能需要驅動、資料遷移、欄位／索引與後端相容性處理，「只改設定即可」是概念性簡化。

<a id="p185"></a>

### P185｜ORM 優缺點與 SQLite 優點

[核對原講義第 185 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=185)

承接 P184 的 ORM 優點：
2. 提高開發效率；模型可用來描述、建構關聯式資料庫結構。
3. 將資料模型與特定資料庫解耦，透過設定切換資料庫。

原稿列出的四項 ORM 缺點：
1. 各 ORM 框架嘗試採用 `LazyLoad`、`Cache` 處理相關問題；原句只寫「實踐這塊」，沒有清楚交代問題主詞。
2. 複雜查詢較難表達，例如分組計算、`case`、`group`、`order by`、`exists`。
3. 把全部資料取回並建立記憶體物件，再於應用端過濾／加工，可能增加記憶體與效能成本。
4. 複雜性可能從資料庫／預存程序轉移到應用程式，使 Python 程式碼量增加。

講義列出的延伸閱讀（僅保留來源連結，未在本次範圍外展開）：
- Django 模型（model）系統—常用查詢語法：<https://www.itread01.com/content/1543740968.html>
- Django 筆記—模型與資料庫：<http://dokelung-blog.logdown.com/posts/220606-django-notes-5-model-and-database>

**SQLite vs MySQL vs PostgreSQL：SQLite 優點**
1. **占用空間小、獨立：**講義指出函式庫可小於 `600KiB`，實際大小依安裝系統而異；不必額外安裝外部相依項才能執行。
2. **使用方便／零配置：**SQLite 不以獨立伺服器程序運作，不必啟動、停止、重新啟動資料庫服務，也沒有需要管理的伺服器設定檔，因此容易整合至應用程式。
3. **可攜性：**整個資料庫存於單一檔案，而非大量獨立檔案；檔案可放在目錄樹中的位置，透過可移動媒體或檔案傳輸協定分享。

**圖片／版面：**此頁無額外程式截圖；上下為文字清單，兩個延伸閱讀網址以藍色底線顯示，SQLite 缺點標題在頁末，內容接 P186。

**補充／疑點：**這些 ORM 缺點不是 Django「不能做」的功能清單。Django 的 QuerySet 可將篩選、排序、聚合等轉為資料庫端 SQL；只有取出全部資料後在 Python 過濾才會產生上述特定問題。SQLite 體積數字屬講義時點與編譯條件的描述，不是固定容量保證。

<a id="p186"></a>

### P186｜SQLite 限制、MySQL 優點與限制

[核對原講義第 186 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=186)

**SQLite 缺點**
1. **有限的並行寫入：**多程序可同時存取／查詢，但同一時間只有一個寫入者能更改資料庫；適用性不如 MySQL、PostgreSQL 這類客戶端／伺服器 RDBMS 的高並行寫入情境。
2. **沒有資料庫使用者管理：**直接讀寫一般磁碟檔案，存取控制主要依賴作業系統檔案權限；不能像伺服器資料庫那樣為不同資料庫帳號設定個別資料表權限，對多種權限的應用不合適。
3. **程序隔離及精細控制：**講義認為獨立伺服器引擎有助於把客戶端錯誤與伺服器隔離，例如客戶端錯誤指標不能直接破壞伺服器記憶體；伺服器可更精細控制資料存取、鎖定及並行。

**MySQL 優點**
1. **普及、易上手：**管理員、紙本與線上文件多；有 `phpMyAdmin` 等第三方管理工具。
2. **安全與帳號管理：**安裝後可透過安全設定腳本設定密碼安全級別、設定 `root` 密碼、刪除匿名帳號與預設測試資料庫；支援逐一使用者授權。
3. **速度：**原文認為其設計偏向速度與易用性，部分 SQL 功能取捨有助於效能；也承認其他 RDBMS（如 PostgreSQL）的某些基準可匹敵或接近。這是講義比較敘述，不是所有工作負載的定論。
4. **複製（replication）：**在兩個以上主機間分享資料，提高可靠性、可用性與容錯能力，可協助備份方案與橫向擴充。

**MySQL 缺點（本頁前兩項）**
1. 功能／SQL 標準限制：講義以不支援 `FULL JOIN` 子句為例。
2. 雙重授權：免費開源社群版採 `GPLv2`，亦有專有授權的付費商業版；某些功能或外掛只在專有版本提供。

**圖片／版面：**純文字，SQLite 三項缺點位於上半部，MySQL 四項優點居中，下方為兩項缺點，第三項續下頁。

**補充／疑點：**複製不能直接等同完整備份，誤刪也可能同步。安全性與速度皆須結合配置、版本、工作負載判斷，不能只依資料庫名稱排序。

<a id="p187"></a>

### P187｜PostgreSQL 比較及 MySQL 連線設定（上）

[核對原講義第 187 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=187)

**承接 MySQL 缺點第三項：**原稿稱 MySQL 於2008年被 Sun Microsystems 收購、2009年被 Oracle Corporation 收購後，使用者抱怨開發速度減慢，社群快速回應與改動的能力降低。此為原稿歷史敘述及主觀評價，非本筆記對現況的判定。

**PostgreSQL 優點**
1. **SQL 相容性：**原文說比 SQLite、MySQL 更嚴格遵循標準，支援179項 SQL:2011 核心要求功能及許多選用功能。
2. **開源、社群驅動：**原始碼完全開放，由龐大專業社群開發；有官方文件、PostgreSQL Wiki、論壇等資源。
3. **可擴充性：**可透過目錄驅動運作與動態載入，以程式擴充；例如指定共享函式庫等目的碼檔案，由 PostgreSQL 按需載入。

**PostgreSQL 缺點（原稿觀點）**
1. 每個新客戶端連線會衍生新程序；原文估計每個程序約需 `10MB` 記憶體，大量連線時成本增長，並稱某些簡單而繁重的操作效能可能不如 MySQL。
2. 原文認為其歷史普及度低於 MySQL，第三方管理工具與有經驗管理員相對少。

**開始設定 Django 連 MySQL：**編輯 `project2/settings.py`，把 SQLite 的 `ENGINE`、`NAME` 註解，改為 MySQL。此頁設定框的下半部以紅色呈現 `ENGINE`、`NAME`、`USER`、`PASSWORD`。完整字典跨至 P188，於下一頁合併轉錄，避免漏掉括號。

```bash
vim project2/settings.py
```

本頁具體值：`ENGINE='django.db.backends.mysql'`、`NAME='myproject'`、`USER='tony'`、`PASSWORD='1qaz2wsx'`（講義範例密碼）。

**補充／疑點：**SQL 支援項數、每連線記憶體、效能、流行度均屬講義時點／環境資訊，不能當成固定現況。原稿 Oracle 收購年份沒有區分宣布與完成。範例密碼只供辨識原文，部署應改用環境變數／秘密管理，勿硬編碼或沿用。

<a id="p188"></a>

### P188｜MySQL 連線設定（下）與 students 模型截圖

[核對原講義第 188 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=188)

合併 P187–188 的文字版完整設定：

```python
DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myproject',
        'USER': 'tony',
        'PASSWORD': '1qaz2wsx',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        }
    }
}
```

- `default`：預設資料庫連線；`ENGINE`：後端引擎；`NAME`：資料庫名稱；`USER/PASSWORD`：連線帳密；`HOST/PORT`：主機與連接埠。
- `init_command`：連線初始化時設定 SQL 模式 `STRICT_TRANS_TABLES`；`charset='utf8mb4'`：指定連線字元集。
- 圖中引擎對照：MySQL 為 `django.db.backends.mysql`，SQLite 3 為 `django.db.backends.sqlite3`，PostgreSQL 為 `django.db.backends.postgresql_psycopg2`（原圖舊名稱）。
- 上方 Vim 黑底截圖標示 Django 2.2 設定文件網址；截圖的 `USER` 是 **`root`**，與文字設定的 `tony` 不同；其他可見值為 `myproject`、`1qaz2wsx`、`localhost`、`3306`、`STRICT_TRANS_TABLES`、`utf8mb4`。

建立 student 資料模型：

```bash
sudo vim myapp/models.py
```

下方 VS Code 圖中的完整模型：

```python
from django.db import models

class students(models.Model):
    cName = models.CharField(max_length=20, null=False)
    cSex = models.CharField(max_length=2, default="M", null=False)
    cBirthday = models.DateField(null=False)
    cEmail = models.EmailField(max_length=100, blank=True, default='')
    cPhone = models.CharField(max_length=20, blank=True, default='')
    cAddr = models.CharField(max_length=255, blank=True, default='')
```

**補充／疑點：**`USER` 的截圖／文字版本不同，需依實際帳號設定；不建議應用程式用資料庫 root。`cPhone.max_length` 在本頁截圖為20，下一頁文字版為50，不能默默視作同一版本。原文未在此處展示 MySQL 驅動安裝、建立資料庫及授權等前置步驟。

<a id="p189"></a>

### P189｜模型欄位、makemigrations 與 migrate

[核對原講義第 189 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=189)

本頁再次列出 `students` 的文字版，與 P188 圖的唯一明顯欄位差異是電話長度：

```python
from django.db import models

class students(models.Model):
    cName = models.CharField(max_length=20, null=False)
    cSex = models.CharField(max_length=2, default='M', null=False)
    cBirthday = models.DateField(null=False)
    cEmail = models.EmailField(max_length=100, blank=True, default='')
    cPhone = models.CharField(max_length=50, blank=True, default='')
    cAddr = models.CharField(max_length=255, blank=True, default='')
```

| 欄位 | 類型與限制 | 用途 |
|---|---|---|
| `cName` | `CharField(max_length=20, null=False)` | 姓名 |
| `cSex` | `CharField(max_length=2, default='M', null=False)` | 性別，預設 M |
| `cBirthday` | `DateField(null=False)` | 生日 |
| `cEmail` | `EmailField(max_length=100, blank=True, default='')` | 電子郵件，可空白 |
| `cPhone` | `CharField(max_length=50, blank=True, default='')` | 電話，可空白，保留字串中的前導0 |
| `cAddr` | `CharField(max_length=255, blank=True, default='')` | 地址，可空白 |

`null=False` 是資料庫層面的 NULL 限制，`blank=True` 是驗證層允許空白，`default=''` 提供空字串預設值；三者不可混為一談。後續畫面使用 `id` 主鍵，原模型沒有明確宣告，屬 Django 自動加入的主鍵欄位。

**建立 migration 資料檔：**記錄資料表結構及版本以利追蹤；先偵測模型改動、產生遷移檔，再同步資料庫。

```bash
sudo python3 ./manage.py makemigrations
sudo python3 ./manage.py migrate
```

圖中實際終端命令省略 `python3`，分別是 `sudo ./manage.py makemigrations` 與 `sudo ./manage.py migrate`。第一張於 `(dvdsenv) pi@raspberrypi:~/dvds2/project1` 顯示 **`No changes detected`**。第二張於 `(dvdsenv1) pi@raspberrypi:~/project1` 顯示：

```text
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying sessions.0001_initial... OK
```

頁末開始「資料庫查詢（SQL-SELECT 語法）」並要求新增 `urls.py` 瀏覽位置。

**補充／疑點：**圖中的 `No changes detected` 不是「成功產生 students migration」的證據；第二張只列內建 app，沒有 `myapp`，所以也不能從此圖確認學生資料表已建立。實務需檢查 app 註冊與遷移狀態。`sudo` 及專案目錄因講義沿用不同環境而不一致，不應直接照搬至虛擬環境。

<a id="p190"></a>

### P190｜SELECT：list 路由、姓名包含查詢及排序

[核對原講義第 190 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=190)

編輯 `project2/urls.py`，圖中加入：

```python
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', views.list),
]
```

`admin` 的匯入不在此截圖範圍；既有檔案需有 `from django.contrib import admin`。編輯 `myapp/views.py`，圖中函式如下（保留重要註解）：

```python
def list(request):
    # 可檢查sql寫法
    if 'cName' in request.GET:
        # print("ok")
        cName = request.GET['cName']
        print(cName)
        # ORM:
        resultList = students.objects.filter(cName__contains=cName)
    else:
        # print("false")
        # resultList = students.objects.all().order_by("-cID")
        # 讀取資料表，依 id 遞減排序（原圖註解）
        # ORM:
        resultList = students.objects.all().order_by("id")
        # 讀取資料表，依 id 遞增排序

    errormessage = ""
    if not resultList:  # 判斷有無資料
        errormessage = "無此資料"
    # print(errormessage)
    # print(resultList)
    # return HttpResponse("test...")
    return render(request, "list.html", locals())
```

- `request.GET` 存放 URL 查詢參數；有 `cName` 時做姓名包含查詢，例如 `/list/?cName=陳`。
- `students.objects` 為模型管理器；`filter(cName__contains=cName)` 回傳姓名中含有輸入字串的符合資料集合；雙底線 `__contains` 是欄位查詢運算，不是另一個模型欄位。
- 沒有 `cName` 參數時，`all()` 取所有資料、`order_by('id')` 依主鍵遞增排序。
- `if not resultList` 檢查集合是否為空；空集合顯示「無此資料」。`render` 使用 `list.html`，`locals()` 把區域變數傳給模板。
- 圖末標題是「新增 template list.html」，但下方命令是 `sudo vim templates/listall.html`；實際 view 及下一頁檔案均使用 **`list.html`**。

**補充／疑點：**原圖註解的 `order_by('-cID')` 與模型只有 `id` 不一致；若要依現有主鍵降冪應為 `order_by('-id')`，但原稿註解仍在上方保留。函式名 `list` 遮蔽 Python 內建名稱。必要匯入（例如 `render`、`students`）未在本頁截圖呈現。`locals()` 雖方便，明確的 context 字典較易控制傳入資料。

<a id="p191"></a>

### P191｜list.html 全部資料逐筆顯示與瀏覽器結果

[核對原講義第 191 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=191)

圖中 `templates/list.html`：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <!-- <h1>test</h1> -->
    <h1>{{ errormessage }}</h1>
    {% for data in resultList %}
        <h2>顯示student資料表的資料</h2>
        編號:{{ data.id }} <br>
        姓名:{{ data.cName }} <br>
        性別:{{ data.cSex }} <br>
        生日:{{ data.cBirthday }} <br>
        郵件:{{ data.cEmail }} <br>
        電話:{{ data.cPhone }} <br>
        地址:{{ data.cAddr }} <br>
    {% endfor %}
</body>
</html>
```

`{% for %}` 控制迴圈，`{{ ... }}` 輸出變數／欄位；每位學生都會重複顯示 h2 標題及七項資料，`<br>` 逐行換行。結果為空時迴圈不輸出，頁首 h1 顯示錯誤訊息。

文字測試命令：

```bash
sudo python3 manage.py runserver 0.0.0.0:8080
```

瀏覽器圖實際位置為 `127.0.0.1:8000/list/`，可見兩筆資料：

| 編號 | 姓名 | 性別 | 生日（畫面格式） | 郵件 | 電話 | 地址 |
|---|---|---|---|---|---|---|
| 3 | 潘四敬 | F | 八月 11, 1987 | sugie@superstar.com | 0914530768 | 台北市中央路201號7樓 |
| 4 | 賴勝恩 | M | 六月 20, 1984 | shane@superstar.com | 0946820035 | 台北市建國路177號6樓 |

**補充／疑點：**文字命令是8080，截圖網址是8000；要以實際啟動的埠測試。圖只顯示視窗內兩筆，不能由截圖斷言資料表總共只有兩筆。生日未使用 `date` filter，呈現為當時語系格式。

<a id="p192"></a>

### P192｜包含查詢的成功／無結果畫面與 search_name 路由

[核對原講義第 192 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=192)

上半頁以兩個瀏覽器截圖驗證 P190 的 `list`：
- `127.0.0.1:8000/list/?cName=aa` 顯示標題「顯示student資料表的資料」，編號11、姓名`aa`、性別`M`、生日「九月 1, 2022」、郵件`aa`，電話與地址為空白。
- `127.0.0.1:8000/list/?cName=cc` 只顯示大標題「無此資料」。此為空 QuerySet 分支，不是程式當掉。

新增 `search_name` 搜尋頁，於 `project2/urls.py` 既有路由列表追加：

```python
path('search_name/', views.search_name),
```

圖中還保留 `admin/`、`list/`；新增 view：

```python
def search_name(request):
    # return HttpResponse("test...")
    return render(request, "search_name.html", locals())
```

此 view 只顯示輸入表單，不直接查詢資料庫；真正查詢交給表單的 action `/list/`。頁末要求新增 `search_name.html`，內容接 P193。

**補充／疑點：**示例郵件值`aa`不符合一般 email 格式，表示不能只因模型用了 `EmailField` 就推論此處資料經過驗證；直接 `.save()` 不會自動替代完整表單驗證。

<a id="p193"></a>

### P193｜search_name.html：GET 搜尋表單與查詢流程

[核對原講義第 193 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=193)

完整圖中模板：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <!-- <h1>test</h1> -->
    <form action="/list/" method="GET">
        <label for="fname">姓&nbsp;&nbsp;&nbsp;名:</label>
        <input type="text" name="cName" id="cName">
        <p><button type="submit">搜尋</button></p>
    </form>
</body>
</html>
```

- `action='/list/'` 指定送出目的地；`method='GET'` 把輸入內容放進 URL query string。
- `name='cName'` 決定參數名稱，必須對上 view 的 `request.GET['cName']`；`id` 主要供 HTML 標籤關聯／選取。
- `&nbsp;` 產生姓名標籤中的間距；提交按鈕文字是「搜尋」。
- 原圖 `label for='fname'` 與 input 的 `id='cName'` 不一致，點標籤不能正確關聯此欄位；若修正應讓兩者相同。

文字啟動命令仍為 `sudo python3 manage.py runserver 0.0.0.0:8080`。畫面操作順序：開啟 `127.0.0.1:8000/search_name/` → 在姓名框輸入`aa` → 按「搜尋」→ 到 `127.0.0.1:8000/list/?cName=aa`。結果再次顯示編號11、aa、M、九月1日2022、郵件aa、電話與地址空白，和 P192 相符。

<a id="p194"></a>

### P194｜學生資料管理首頁、筆數計算及模板繼承

[核對原講義第 194 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=194)

於 `project2/urls.py` 加入紅框標記的：

```python
path('index/', views.index),
```

路由圖包含 `from django.contrib import admin`、`from django.urls import path`、`from myapp import views`；另有既存 `admin/` 與 `listone/`，其中 `listone` 的實作沒有在本頁提供。

`myapp/views.py` 的首頁函式：

```python
def index(request):
    resultList = students.objects.all().order_by("id")
    # 讀取資料表，依 id 遞增排序
    errormessage = ""
    status = True
    if not resultList:  # 判斷有無資料
        errormessage = "無此資料"
        status = False
    # print(errormessage)
    data_count = len(resultList)
    # print(data_count)
    # return HttpResponse("test...")
    return render(request, "index.html", locals())
```

`status` 讓模板決定要畫資料表還是「無資料」；`data_count` 是查到的集合筆數。`len(resultList)` 計算集合長度；在本例列表還會被模板使用。若只需資料庫計數，可另考慮 `.count()`（補充，非原圖程式）。

新增 `templates/base.html` 與 `templates/index.html`。base 圖的兩個紅框分別標出 title/content 插槽：

```html
<!-- base.html -->
<!DOCTYPE html>
<html>
    <head>
        {% block title %}{% endblock %}
    </head>
    <body>
        {% block content %} {% endblock %}
    </body>
</html>
```

此父模板提供 HTML 骨架；子模板覆寫 `title`、`content`，將可共用結構與各頁內容分開。截圖底部是 Windows 使用者 `tony` 經 MobaXterm RemoteFiles 編輯的視窗，與上方 Linux `vim` 命令屬不同展示方式，不是另一種模板語法。

<a id="p195"></a>

### P195｜index.html 的資料表、性別轉換與操作連結

[核對原講義第 195 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=195)

本頁截圖**不是完整 index.html 檔案**：只顯示第1–3行，以及第34–62行；第4–33行與結尾未展示。保留可見部分如下，不虛構中間 CSS／HTML：

```django
{% extends 'base.html' %}
{% block title %}
<title>學生資料管理系統</title>
```

```html
<div>
    {% if status %}
    <table>
        <tr>
            <th>學號</th><th>姓名</th><th>性別</th><th>生日</th>
            <th>信箱</th><th>電話</th><th>地址</th><th>編輯</th>
        </tr>
        {% for data in resultList %}
        <tr>
            <td>{{ data.id }}</td>
            <td>{{ data.cName }}</td>
            <td>{% if data.cSex == "M" %} 男 {% else %} 女 {% endif %}</td>
            <td>{{ data.cBirthday }}</td>
            <td>{{ data.cEmail }}</td>
            <td>{{ data.cPhone }}</td>
            <td>{{ data.cAddr }}</td>
            <td>
                <a href="/edit1/{{ data.id }}/load/">編輯1</a> <!-- get -->
                <a href="/edit2/{{ data.id }}/">編輯2</a> <!-- post -->
                <a href="/delete/{{ data.id }}/">刪除</a> <!-- get -->
            </td>
        </tr>
        {% endfor %}
    </table>
    {% else %}
        <h1>無資料</h1>
    {% endif %}
</div>
```

- `extends` 使用 P194 的父模板；`status` 控制是否顯示資料表。
- 表格把主鍵 `id` 顯示為「學號」，與前面清單的「編號」指同一值。
- 性別值`M`轉成「男」，其餘值一律顯示「女」；這不是嚴格性別驗證。
- 每筆資料有「編輯1」「編輯2」「刪除」，URL 內放入該資料主鍵。`load` 是下一節 GET 編輯 view 的模式值；圖註解說 edit1/get、edit2/post，但連結本身仍是 GET 載入頁面，後續表單才決定如何提交。

測試命令仍是 `sudo python3 manage.py runserver 0.0.0.0:8080`。瀏覽器 `127.0.0.1:8000/index/` 顯示置中標題「學生資料管理系統」、文字「目前的資料筆數:10」、連結「新增學生資料」，下方表格如下（已放大原PDF圖核對）：

| 學號 | 姓名 | 性別 | 生日 | 信箱 | 電話 | 地址 |
|---|---|---|---|---|---|---|
| 3 | 潘四敬 | 女 | 1987-08-11 | sugie@superstar.com | 0914530768 | 台北市中央路201號7樓 |
| 4 | 賴勝恩 | 男 | 1984-06-20 | shane@superstar.com | 0946820035 | 台北市建國路177號6樓 |
| 5 | 黎楚寧 | 女 | 1988-02-15 | ivy@superstar.com | 0920981230 | 台北市忠孝東路520號6樓 |
| 6 | 蔡中翔 | 男 | 1987-05-05 | zhong@superstar.com | 0951983366 | 台北市三民路1巷10號 |
| 7 | 徐佳瑩 | 女 | 1985-08-30 | lala@superstar.com | 0918123456 | 台北市仁愛路100號 |
| 8 | 林雨婕 | 女 | 1986-12-10 | crystal@superstar.com | 0907408965 | 台北市民族路204號 |
| 9 | 林心儀 | 女 | 1988-12-01 | peggy@superstar.com | 0916456723 | 台北市建國北路10號 |
| 10 | 王燕博 | 男 | 1993-08-10 | albert@superstar.com | 0918976588 | 台北市北環路2巷80號 |
| 11 | aa | 男 | 2022-09-01 | aa | （空白） | （空白） |
| 12 | bb | 男 | 2022-09-08 | bb33 | （空白） | （空白） |

所有列的最後一欄均有「編輯1 編輯2 刪除」三連結。

**補充／疑點：**圖中程式直接輸出 `cBirthday`，結果卻為 ISO 日期，與 P191 的語系日期不同；可能有頁面未展示的設定，不能憑此圖還原。刪除若直接由 GET 觸發有安全問題，詳 P198–199。未展示的 index.html 中間行不可當作已取得的完整原始碼。

<a id="p196"></a>

### P196｜INSERT：post1 路由及 POST 新增資料

[核對原講義第 196 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=196)

原文命令為 `sudo vim project1/urls.py`（此處是 project1，不同於先前 project2），圖中紅框再次提醒 `from myapp import views`，路由新增：

```python
path('post1/', views.post1),
```

編輯 `myapp/views.py`，可見完整主要程式：

```python
from django.shortcuts import redirect

def post1(request):
    if request.method == "POST":
        cName = request.POST["cName"]
        cSex = request.POST["cSex"]
        cBirthday = request.POST["cBirthday"]
        cEmail = request.POST["cEmail"]
        cPhone = request.POST["cPhone"]
        cAddr = request.POST["cAddr"]
        # 原圖另有註解print，串接上述六個值供除錯
        # orm:
        add = students(cName=cName, cSex=cSex, cBirthday=cBirthday,
                       cEmail=cEmail, cPhone=cPhone, cAddr=cAddr)
        add.save()
        # return HttpResponse("已送出...")
        return redirect('/index/')  # 自動轉址
    else:
        # return HttpResponse("test...")
        return render(request, "post1.html", locals())
```

- GET（或非 POST）先顯示新增表單；POST 才讀取六個欄位。
- `students(...)` 建立尚未儲存的模型實例，把左側模型欄位對應到右側表單值；`add.save()` 寫入新資料，對應 INSERT。
- 主鍵沒有手動指定，由資料庫／模型機制生成。
- 成功後 `redirect('/index/')` 回列表，形成 POST → Redirect → GET 流程，避免重新整理結果頁就直接重送同一張表單。
- `request.POST[...]` 要求欄位存在；缺少 key 會拋例外，原稿沒有處理缺欄、無效生日或儲存失敗。

頁末要求新增 `templates/post1.html`：`sudo vim templates/post1.html`。

**補充／疑點：**原例只是教學 CRUD，未包含登入授權、伺服器端欄位驗證、錯誤回饋與交易設計；瀏覽器 required 不是可信的安全界線。

<a id="p197"></a>

### P197｜post1.html：模板繼承、CSS、CSRF 與六欄新增表單

[核對原講義第 197 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=197)

本頁由三段連續程式截圖構成；除了空白行外，可見模板自第1行至第65行，主要完整內容如下（只整理縮排）：

```html
{% extends 'base.html' %}

{% block title %}
<title>學生資料管理系統-新增資料</title>
<style>
    h1, h3 {
        text-align: center;
    }
    table {
        margin-left: auto;
        margin-right: auto;
    }
    table, th, td {
        border: 1px solid black;
        border-collapse: collapse;
    }
</style>
{% endblock %}

{% block content %}
<div>
    <h1 class="title">學生資料管理系統-新增資料</h1>
    <a href="/index/"><h3>回首頁</h3></a>
</div>
<div>
    <form action="/post1/" method="POST">
        {% csrf_token %}
        <table>
            <tr>
                <th>*姓名</th>
                <td><input type="text" id="cName" name="cName" required placeholder="請輸入姓名"></td>
            </tr>
            <tr>
                <th>*性別</th>
                <td>
                    <input type="radio" id="cSex" name="cSex" value="M" checked>男
                    <input type="radio" id="cSex" name="cSex" value="F">女
                </td>
            </tr>
            <tr>
                <th>*生日</th>
                <td><input type="date" id="cBirthday" name="cBirthday" required></td>
            </tr>
            <tr>
                <th>*信箱</th>
                <td><input type="mail" id="cEmail" name="cEmail" required placeholder="請輸入mail"></td>
            </tr>
            <tr>
                <th>電話</th>
                <td><input type="text" id="cPhone" name="cPhone"></td>
            </tr>
            <tr>
                <th>地址</th>
                <td><input type="text" id="cAddr" name="cAddr"></td>
            </tr>
            <tr>
                <th colspan="2" style="text-align:center;">
                    <input type="submit" name="button" id="button" value="儲存">
                    <input type="reset" name="button2" id="button2" value="清除">
                </th>
            </tr>
        </table>
    </form>
</div>
{% endblock %}
```

**每項設定的意義：**
- `title` block 內包含文件標題及 CSS；`content` block 放實際表單。
- h1/h3 文字置中；table 左右 margin 設為 auto 使表格置中；table/th/td 為1px黑實線，`border-collapse: collapse` 合併相鄰框線。
- 回首頁連結指向 `/index/`。
- 表單 action `/post1/`、method POST；`{% csrf_token %}` 在表單內產生防跨站請求偽造 token，須配合 Django middleware 檢查。
- 星號標示姓名、性別、生日、信箱；姓名、生日、信箱具有 `required`。性別 radio 共用 `name='cSex'`，只送出一個 M/F 值，預設選男。
- 日期 input 提供日期輸入介面，電話與地址為可空白文字欄位。
- 按「儲存」提交；按「清除」是 HTML reset，回復表單初始狀態（本例大多是空白、男性預設），不是資料庫 DELETE。
- `colspan='2'` 使按鈕列橫跨兩欄。

**補充／疑點：**原圖是 `type='mail'`，不是有效的 HTML email input 類型；正確 email 型別應為 `type='email'`。兩個性別 radio 使用重複 `id='cSex'`，宜有不同 id 而共用 name。表單信箱必填但模型 `blank=True`，兩層規則不同。此處原碼仍按原圖保留，沒有悄悄修正。

<a id="p198"></a>

### P198｜新增頁測試畫面與 DELETE 路由

[核對原講義第 198 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=198)

上方測試命令仍為：

```bash
sudo python3 manage.py runserver 0.0.0.0:8080
```

瀏覽器實際顯示 `127.0.0.1:8000/post1/`：大標題「學生資料管理系統-新增資料」、回首頁連結，下方兩欄表格依次為`*姓名`（placeholder「請輸入姓名」）、`*性別`（男預選、女未選）、`*生日`（年／月／日及月曆按鈕）、`*信箱`（placeholder「請輸入mail」）、電話、地址；底部「儲存」「清除」。這是**空白輸入表單**截圖，本頁沒有新增成功後資料表變化的證據。

下半頁進入「資料刪除（SQL-DELETE 語法）」。`sudo vim project2/urls.py`，紅框新增 `delete/<int:id>/`；圖中完整可見路由列表為：

```python
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', views.list),
    path('search_name/', views.search_name),
    path('index/', views.index),
    path('post1/', views.post1),
    path('edit1/<int:id>/<str:mode>/', views.edit1),
    path('edit2/<int:id>/', views.edit2),
    path('delete/<int:id>/', views.delete),
]
```

`<int:id>` 把 URL 段轉為整數傳給 view；`<str:mode>` 是後續 edit1 的模式參數。刪除是針對指定主鍵，不是刪除全部資料。頁末要求 `sudo vim myapp/views.py`，實作接 P199。

<a id="p199"></a>

### P199｜DELETE：先 GET 確認、再 POST 刪除

[核對原講義第 199 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=199)

完整 view：

```python
def delete(request, id=None):
    if request.method == "POST":
        # orm:
        delete_data = students.objects.get(id=id)
        delete_data.delete()
        # return HttpResponse("按刪除")
        return redirect('/index/')
    else:
        # orm:
        dict_data = students.objects.get(id=id)
        # return HttpResponse("test.......")
        return render(request, "delete.html", locals())
```

- **GET 分支只讀取並顯示確認畫面**：`get(id=id)` 取回單一學生物件，變數雖叫 `dict_data`，其實不是 Python dict。
- **POST 分支才執行刪除**：取得物件後呼叫 `.delete()`，相當於 DELETE，之後轉到 `/index/`。
- 這與 P195「刪除連結旁註 get」不矛盾：GET 開確認頁，POST 才真正修改狀態。不可把本例誤記為「點 GET 連結立即刪資料」。
- `.get()` 與 `.filter()` 不同：前者預期恰一筆，後者是可有零筆或多筆的 QuerySet；本例 id 為主鍵，一般至多一筆，但不存在時會拋 `students.DoesNotExist`。原例未處理，實務可用 `get_object_or_404`（補充）。

文字再次列啟動命令 `sudo python3 manage.py runserver 0.0.0.0:8080`。瀏覽器畫面標題為「學生資料管理系統-刪除資料—(POST)」，有回首頁連結、待刪資料及「刪除」按鈕：

| 顯示欄 | 待刪內容 |
|---|---|
| 姓名 | 潘四敬 |
| 性別 | 女 |
| 生日 | 1987-08-11 |
| 信箱 | sugie@superstar.com |
| 電話 | 0914530768 |
| 地址 | 台北市中央路201號7樓 |

**重要證據界線：**本頁沒有提供 `delete.html` 原始碼，只展示瀏覽器確認頁；所以 POST action、token、按鈕 HTML 不可聲稱逐行取得。也沒有刪除後的列表截圖，不能宣稱該筆已從資料庫移除。實作應檢查 POST 表單有 CSRF token 及操作權限。本次僅閱讀，不執行刪除。

頁末開始下一節「資料更新（使用 GET）（SQL-UPDATE 語法）」。

<a id="p200"></a>

### P200｜UPDATE（GET）：edit1 的 edit 模式與模型欄位指派

[核對原講義第 200 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=200)

`sudo vim project2/urls.py`，紅框 route：

```python
path('edit1/<int:id>/<str:mode>/', views.edit1),
```

- `id` 識別哪筆學生，`mode` 區分「load 載入編輯頁」及「edit 寫回資料」。
- 首頁連結先進入 `/edit1/<id>/load/`；表單送到 `/edit1/<id>/edit/`。
- 本例以 `request.GET` 取值，並非 P196 的 POST 新增。

`myapp/views.py` 的函式跨 P200–201，合併完整主要程式如下（逐項除錯 print 以註解保留）：

```python
def edit1(request, id=None, mode=None):
    # print(id)
    # print(mode)
    if mode == "edit":
        cName = request.GET["cName"]
        cSex = request.GET["cSex"]
        cBirthday = request.GET["cBirthday"]
        cEmail = request.GET["cEmail"]
        cPhone = request.GET["cPhone"]
        cAddr = request.GET["cAddr"]
        # print(cName)
        # print(cSex)
        # print(cBirthday)
        # print(cEmail)
        # print(cPhone)
        # print(cAddr)

        # orm:
        update = students.objects.get(id=id)
        update.cName = cName
        update.cSex = cSex
        update.cBirthday = cBirthday
        update.cEmail = cEmail
        update.cPhone = cPhone
        update.cAddr = cAddr
        update.save()
        # 下列 return 與 load 分支見 P201
        # return HttpResponse("修改.......")
        return redirect('/index/')
    elif mode == "load":
        # orm:
        dict_data = students.objects.get(id=id)
        # return HttpResponse("test.......")
        return render(request, "edit1.html", locals())
```

**與新增的差別：**新增是直接 `students(...)` 建立新實例後 `.save()`；更新先 `objects.get(id=id)` 取出已存在實例，再逐欄改值、`.save()` 寫回，因此目標主鍵不變。這裡 `update` 只是變數名稱，**不是**呼叫 QuerySet 的 `.update()` 方法。

**補充／疑點：**以 GET 修改資料違反安全方法應無副作用的慣例；URL 會包含姓名、生日、郵件、電話、地址，可能進入瀏覽器歷史、伺服器日誌或其他紀錄，也可能被預載／重訪誤觸。正式系統應採 POST 加 CSRF、驗證與授權。本例也未處理未知 mode（沒有回傳 response）、不存在 id、缺少查詢參數或無效資料。

<a id="p201"></a>

### P201｜edit1 的 load 分支與回填編輯模板

[核對原講義第 201 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=201)

頁頂接 P200：更新後 `redirect('/index/')`；`mode == 'load'` 時以主鍵 `.get()` 取資料到 `dict_data`，`render(request, 'edit1.html', locals())`。編輯命令為 `sudo vim templates/edit1.html`。

模板兩段圖已放大核對，完整主要內容：

```html
{% extends 'base.html' %}

{% block title %}
<title>學生資料管理系統-修改資料一(GET)</title>
{% endblock title %}

{% block content %}
<h1>學生資料管理系統-修改資料一(GET)</h1>
<a href="/index/"><h3>回首頁</h3></a>
<form action="/edit1/{{dict_data.id}}/edit/" method="get">
    <table>
        <tr>
            <th>姓名</th>
            <td><input type="text" id="cName" name="cName" value="{{ dict_data.cName }}"></td>
        </tr>
        <tr>
            <th>性別</th>
            <td>
                <input type="radio" id="cSex" name="cSex" value="M" {% if dict_data.cSex == "M" %} checked {% endif %}>男
                <input type="radio" id="cSex" name="cSex" value="F" {% if dict_data.cSex == "F" %} checked {% endif %}>女
            </td>
        </tr>
        <tr>
            <th>生日</th>
            <td><input type="date" id="cBirthday" name="cBirthday" value="{{ dict_data.cBirthday }}"></td>
        </tr>
        <tr>
            <th>信箱</th>
            <td><input type="text" id="cEmail" name="cEmail" value="{{ dict_data.cEmail }}"></td>
        </tr>
        <tr>
            <th>電話</th>
            <td><input type="text" id="cPhone" name="cPhone" value="{{ dict_data.cPhone }}"></td>
        </tr>
        <tr>
            <th>地址</th>
            <td><input type="text" id="cAddr" name="cAddr" value="{{ dict_data.cAddr }}"></td>
        </tr>
        <tr>
            <th colspan="2" style="text-align:center;">
                <input type="submit" name="button" id="button" value="儲存">
                <input type="reset" name="button2" id="button2" value="重設">
            </th>
        </tr>
    </table>
</form>
{% endblock content %}
```

- `value` 使用原物件各欄位回填，使用者不必從空表單重打；主鍵在 action URL，沒有 hidden id 欄位。
- 性別以兩個 `{% if %}` 條件輸出 `checked`，對應資料庫現值；兩者仍重複 `id='cSex'`。
- 「重設」回復載入時的資料值，不是刪除紀錄，也不是強制清空。
- 本 GET 表單沒有 CSRF token，並且沒有 `required` 屬性。

**補充／疑點：**生日原圖確實是 `{{ dict_data.cBirthday }}`，**沒有 `date` filter**。HTML date 的 value 需要 `YYYY-MM-DD`；若 Django 依語系輸出其他格式，日期框可能空白。可靠寫法可改為 `value="{{ dict_data.cBirthday|date:'Y-m-d' }}"`（這是補充修法，非原碼）。此頁僅含模板與「測試結果」標題，實際結果在下頁。

<a id="p202"></a>

### P202｜GET 更新的瀏覽器流程、日誌與另一組測試資料

[核對原講義第 202 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=202)

本頁兩個區塊各列 `sudo python3 manage.py runserver 0.0.0.0:8080`。截圖環境改為 `192.168.57.236:8080`，資料也與 P195 的十筆學生不同，不宜強行串成同一資料庫的連續狀態。

**第一個列表畫面：**位址 `192.168.57.236:8080/index/`，標題「顯示 student 資料表所有資料」、旁有「新增資料」。每列末欄「編輯一／編輯二／刪除」。可見完整三筆：

| 編號 | 姓名 | 性別 | 生日（畫面） | 郵件帳號 | 電話 | 地址 |
|---|---|---|---|---|---|---|
| 6 | bb | M | 2021年2月11日 | bb@gmial.com | bb | bb |
| 7 | aa | M | 2021年2月10日 | bb@gmial.com | 09222222 | 高雄市 |
| 8 | aa | M | 2021年2月1日 | aa@google.com.tw | 09222222 | 高雄市 |

**點編輯一：**滑鼠位於編號6的「編輯一」。開啟 `192.168.57.236:8080/edit1/6/load`（截圖沒有結尾斜線），標題「student 資料表修改(一)」。表單姓名bb、男性已選、日期`2021/02/11`、郵件`bb@gmial.com`、電話bb、地址bb，底部「送出」「重設」。原圖性別標籤還直接印出`性別M`。

**終端圖：**

```text
System check identified no issues (0 silenced).
June 07, 2021 - 10:59:59
Django version 2.2.18, using settings 'project2.settings'
Starting development server at http://0.0.0.0:8080/
Quit the server with CONTROL-C.
web get
[07/Jun/2021 10:59:59] "GET /edit1/6/load HTTP/1.1" 200 1271
form get
```

接著可見時間`11:00:06`的 `GET /edit1/6/edit?cName=bb&cSex=M&cBirthday=2021...`，後段有 `cAddr=bb&button=%E9%80%81%E5%87%BA`，回應 **`302 0`**，再有：

```text
[07/Jun/2021 11:00:06] "GET /index/ HTTP/1.1" 200 11271
```

長 GET request 在原截圖被右側裁掉，不能取得完整 query string；此處用省略標記說明，不補造缺失欄位。`web get`、`form get` 是原圖的除錯輸出；紅框特別圈出 `form get`，證明此操作以 GET 表單提交。`200` 代表頁面回應成功、`302` 是轉址；末尾數字為記錄中的回應大小，不是資料筆數。

**下半部另一張結果圖：**同一 `/index/` 可見編號6改為姓名`bb111`、M、`2021年6月11日`、郵件`bb@gmial.com11`、電話`bb11`、地址`bb11`；編號7仍為aa、M、2021年2月10日、`bb@gmial.com`、`09222222`、高雄市。畫面右側及下方被截，不能認定資料表只剩兩筆。

**補充／疑點：**保留原示例的拼字 **`gmial`**，沒有擅改為 gmail。上方日誌送出bb，而下方結果是bb111，屬不同次示範；不可聲稱每一張都是同一次 request。P201 程式頁標題／按鈕文字與此處舊截圖也不同。原圖沒有完整 URL query，不另行猜測。

<a id="p203"></a>

### P203｜GET 更新結果與 edit2 路由（原標題誤植）

[核對原講義第 203 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=203)

上方繼續示範編輯一：表單「student 資料表修改(一)」填入下列值，男性 radio 勾選，底部按「送出」，回 `/index/` 的編號6列顯示一致結果：

| 欄位 | 編輯表單 | 列表結果 |
|---|---|---|
| 主鍵 | URL所指的資料 | 6 |
| 姓名 | bb000 | bb000 |
| 性別 | 男生 | M |
| 生日 | 2021/06/12 | 2021年6月12日 |
| 郵件帳號 | bb@gmial.com00 | bb@gmial.com00 |
| 電話 | 09999111 | 09999111 |
| 地址 | 000 | 000 |

列表仍有「新增資料」「編輯一」「編輯二」「刪除」。此圖只能證明可見編號6的值，底部其他列已裁掉。

下半頁標題原文仍寫 **「資料更新（使用 GET）（SQL-UPDATE 語法）」**，但紅框為 **edit2** 路由：

```python
path('edit2/<int:id>/', views.edit2),
```

`sudo vim project2/urls.py`，其餘路由與 P198 相同。與 edit1 不同，edit2 只有 id，沒有 mode 字串；由 HTTP method 區分載入／儲存。頁末「新增 view functions」的實作接 P204。

**補充／疑點：**此節標題「GET」與 P204 的 `request.method == 'POST'`、`request.POST` 矛盾，應標為 **POST 更新示範**。原標題保留，但實際功能不能被誤植標題誤導。

<a id="p204"></a>

### P204｜UPDATE（POST）：edit2 寫回現有物件

[核對原講義第 204 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=204)

`sudo vim myapp/views.py`；兩段截圖合併：

```python
def edit2(request, id=None):
    # print(id)
    if request.method == "POST":
        cName = request.POST["cName"]
        cSex = request.POST["cSex"]
        cBirthday = request.POST["cBirthday"]
        cEmail = request.POST["cEmail"]
        cPhone = request.POST["cPhone"]
        cAddr = request.POST["cAddr"]
        # print(cName)
        # print(cSex)
        # print(cBirthday)
        # print(cEmail)
        # print(cPhone)
        # print(cAddr)

        # orm:
        update = students.objects.get(id=id)
        update.cName = cName
        update.cSex = cSex
        update.cBirthday = cBirthday
        update.cEmail = cEmail
        update.cPhone = cPhone
        update.cAddr = cAddr
        update.save()
        # return HttpResponse("修改.......")
        return redirect('/index/')
    else:
        # orm:
        dict_data = students.objects.get(id=id)
        print(dict_data)
        # return HttpResponse("test.......")
        return render(request, "edit2.html", locals())
```

- GET（非 POST）取得現有物件，印出 `dict_data` 供除錯，再回填到 `edit2.html`。
- POST 收六個欄位，以 URL id 取得原物件，逐項指定並 `.save()`，最後轉回首頁。這是 UPDATE，不因姓名改變而換一筆主鍵。
- 與 edit1 的差異：沒有 mode；`request.GET` 改成 `request.POST`；資料不放在 query string。
- **POST 並非加密**，仍需要 HTTPS；而且應配合 CSRF、權限檢查及伺服器驗證。

本頁測試命令為 `sudo python3 manage.py runserver 0.0.0.0:8080`。下方 `192.168.57.236:8080/index/` 圖中滑鼠位於編號6的「編輯二」，表格可見：

| 編號 | 姓名 | 性別 | 生日 | 郵件帳號 | 電話 | 地址 |
|---|---|---|---|---|---|---|
| 6 | bb | F | 2021年6月12日 | bb@gmial.com | 09999 | （空白） |
| 7 | aa | M | 2021年2月10日 | bb@gmial.com | 09222222 | 高雄市 |
| 8 | aa | M | 2021年2月1日 | aa@google.com.tw | 09222222 | 高雄市 |

**補充／疑點：**本範圍沒有展示 `edit2.html` 原始碼，不能把推測的 POST action、CSRF token 或回填語法冒充原稿。僅依 view 可確定模板名及 POST 欄位契約，依下一頁可確定畫面操作。正式實作要另確認 POST 表單存在 token。這張編號6又回到bb/F，和 P203 不同，顯示教材混合多次測試狀態。

<a id="p205"></a>

### P205｜POST 編輯二：表單內容及更新後列表

[核對原講義第 205 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=205)

本頁只有上半部一組框線內的兩張瀏覽器圖片，沒有額外程式／終端日誌，下半頁空白。

**上圖：**標題「student 資料表修改(二)」，編輯欄位如下：
- 姓名：`bb33`。
- 性別：標籤仍顯示`性別F`，但「男生」radio 已選取、「女生」未選，表示使用者正把原來的 F 改為 M。
- 生日：`2021/06/12`，有日期選擇器圖示。
- 郵件帳號：`bb33@gmial.com`（保留原拼字）。
- 電話：`0999933`。
- 地址：`pp`，圖中此欄有焦點底色。
- 按鈕：「送出」「重設」，游標停在送出。

**下圖：**回到 `192.168.57.236:8080/index/`，標題「顯示 student 資料表所有資料」，旁有新增資料連結；可見一筆：

| 編號 | 姓名 | 性別 | 生日 | 郵件帳號 | 電話 | 地址 | 編輯 |
|---|---|---|---|---|---|---|---|
| 6 | bb33 | M | 2021年6月12日 | bb33@gmial.com | 0999933 | pp | 編輯一／編輯二／刪除 |

該列保留同一主鍵6、生日不變，姓名／性別／信箱／電話／地址對應表單的新值，展示 edit2 更新後的可見結果。圖片裁在第一筆之下，不能由此宣稱總資料筆數為1。

**補充／疑點：**本頁沒有 POST 網路／終端日誌；POST 方法的直接證據來自 P204 程式，而不是假稱圖片顯示了 request。性別標籤F與新選擇男生是舊值提示和正在編輯的值，結果列M才是儲存後示範值。

#### 本範圍的 CRUD 方法與資料流對照（整理，不新增原稿未示範的 API）

| 功能 | route／輸入 | ORM 核心 | 輸出 |
|---|---|---|---|
| 全部查詢 | `/list/`、`/index/` | `objects.all().order_by('id')` | QuerySet，清單／表格 |
| 姓名包含 | `/list/?cName=...` | `objects.filter(cName__contains=cName)` | 零到多筆；無符合顯示無此資料 |
| 指定學生 | URL中的`id` | `objects.get(id=id)` | 單一模型實例，供編輯／刪除確認 |
| 新增 | `/post1/`，POST六欄 | `students(...); add.save()` | 轉到`/index/` |
| 刪除 | `/delete/<id>/`，GET載入、POST確認 | `get(...); delete_data.delete()` | 轉到`/index/` |
| GET更新（教學示例，不宜部署） | `/edit1/<id>/load/` → `/edit1/<id>/edit/?...` | 取得原物件→改六欄→`save()` | 轉到`/index/` |
| POST更新 | `/edit2/<id>/`，GET載入、POST儲存 | 取得原物件→改六欄→`save()` | 轉到`/index/` |

> 閱讀界線：本筆記已逐頁親閱 P184–P205 的全部頁圖並對較小的表格／程式進行局部重繪核對。原稿未提供的模板區段、被裁掉的長 request、版本混用及語意／安全疑點均另行標示；沒有對真實資料庫執行任何 CRUD 寫入。






---

## P206–P237｜Django ORM 與 SQL 完整逐頁筆記

> 範圍僅限 PDF 第 206–237 頁；依原頁文字與逐頁圖片閱讀整理。SQL／Python 是講義教學範例，**本次未連線、建立、修改或刪除任何資料庫，也未執行講義程式**。「圖示結果」指原講義截圖，不是本次執行結果。換行造成的程式斷裂會在可確定時接回；原稿的語意或語法問題另外標示。

<a id="p206"></a>

### P206｜建立 DB 專案、ORM 欄位型別（上）

[核對原講義第 206 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=206)

本節題名為「3-13 Django 使用 ORM vs SQL 語法」，以 SQL 與 Django 模型操作相互對照。

```bash
cd ~/dvds
source ./dvds/dvdsenv/bin/activate
django-admin startproject DB
cd DB
tree
```

- `source` 啟動虛擬環境；`startproject DB` 建立專案；`tree` 檢視目錄樹。
- **原稿路徑疑點**：先進 `~/dvds`，再使用 `./dvds/dvdsenv/bin/activate`，代表實際尋找的是其下再一層 `dvds`。須依環境檔案位置確認，不宜直接假設此相對路徑正確。
- `CharField`：短字串欄位，以 `max_length` 指定長度，對應常見的 `VARCHAR`。表格寫成 `maxlength`，Python 參數應為 `max_length`。
- `IntegerField`：整數。
- `FloatField`：浮點數，講義以 `double` 說明，例 `models.FloatField(null=True)`。
- `DecimalField`：以 `max_digits` 指定總位數（不含符號與小數點）、`decimal_places` 指定小數位數，例 `models.DecimalField(..., max_digits=5, decimal_places=2)`。**補充／修正**：這是固定精度十進位數，不是與 `FloatField` 相同的二進位浮點數；原稿說「最大值 999、小數點後 2 位」不夠精確，此設定可容納三位整數與兩位小數。
- `AutoField`：新增資料時自動遞增的整數欄位，例 `my_id = models.AutoField(primary_key=True)`；沒有自行指定主鍵時，Django 會新增預設主鍵。
- `BooleanField`：`True`／`False`，admin 通常使用 checkbox 呈現。
- **圖片觀察**：本頁是建立環境命令框與六種欄位型別表；沒有另藏程式截圖。

<a id="p207"></a>

### P207｜ORM 欄位型別（下）與通用參數

[核對原講義第 207 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=207)

| 欄位 | 用途／參數 |
|---|---|
| `TextField` | 大容量文字。 |
| `EmailField` | 帶 Email 格式驗證的字串欄位。原稿稱不接受 `maxlength`。**修正**：正確參數名為 `max_length`，`EmailField` 可設定此參數；模型 `save()` 也不等於自動執行所有欄位驗證。 |
| `DateField` | 日期；可設定 `auto_now`／`auto_now_add`。 |
| `DateTimeField` | 日期與時間；支援相同自動時間選項。 |
| `ImageField` | 類似檔案欄位，增加圖片有效性檢查。 |
| `FileField` | 上傳檔案欄位。 |

| 通用參數 | 講義重點與精確區別 |
|---|---|
| `null=True` | 資料庫允許 `NULL`；預設 `False`。 |
| `blank=True` | 表單／驗證允許留白；預設 `False`。與 `null` 是不同層次。 |
| `default` | 可指定固定值或 callable；callable 會於需要預設值的新物件建立時呼叫。既有資料表新增不可空欄位時，需要考慮既有列如何填值，常以遷移預設值處理。 |
| `primary_key=True` | 指定模型主鍵；未指定時由 Django 自動提供主鍵。**補充**：實際自動欄位型別受 `DEFAULT_AUTO_FIELD` 等設定影響，不宜一概稱普通 `IntegerField`。 |
| `unique=True` | 此欄位的值在整張表中必須唯一。 |
| `auto_now_add=True` | 初次建立時設定日期／時間，適合建立時間。 |
| `auto_now=True` | 透過模型儲存流程更新日期／時間，適合最後修改時間。**補充**：`QuerySet.update()` 不會自動走模型 `save()`，不能把它理解成任何 SQL 更新都會自動更新此欄位。 |

- `DateField` 儲存日期，不會因使用 `auto_now` 而變成含時分秒的時間戳；需要時間使用 `DateTimeField`。
- 原頁參考：https://iter01.com/432964.html 。
- **圖片觀察**：兩張表分別延續欄位型別與通用引數，頁尾開始「建立資料表」。

<a id="p208"></a>

### P208｜students／scorelist 模型、一對多與 migrations

[核對原講義第 208 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=208)

**上方資料表規劃圖**：

| 中文意義 | 欄位 | SQL 型別／設定 | 允許 NULL |
|---|---|---|---|
| 座號 | `cID` | `TINYINT(2)`，圖中屬性拼作 `USIGNED ZEROFILL`，主鍵、`auto_increment` | 否 |
| 姓名 | `cName` | `VARCHAR(20)` | 否 |
| 性別 | `cSex` | `ENUM('F','M')`，預設 `F`（female） | 否 |
| 生日 | `cBirthday` | `DATE` | 否 |
| 電子郵件 | `cEmail` | `VARCHAR(100)` | 是 |
| 電話 | `cPhone` | `VARCHAR(50)` | 是 |
| 住址 | `cAddr` | `VARCHAR(255)` | 是 |

編輯 `DBapp/models.py`，圖片內程式如下：

```python
from django.db import models

class students(models.Model):
    cID = models.AutoField(primary_key=True)
    cName = models.CharField(max_length=20, blank=False)
    cSex = models.CharField(max_length=1, blank=False, default='F')
    cBirthday = models.DateTimeField(auto_now_add=False)
    cEmail = models.CharField(max_length=100, blank=False)
    cPhone = models.CharField(max_length=50, blank=False)
    cAddr = models.CharField(max_length=255, blank=False)
    cHeight = models.IntegerField(blank=True, null=True)
    cWeight = models.IntegerField(blank=True, null=True)

# 一個學生有多個成績（one to many）：students to scorelist
class scorelist(models.Model):
    id = models.AutoField(primary_key=True)
    cID = models.ForeignKey('students', on_delete=models.CASCADE, null=True)
    course = models.CharField(max_length=20, blank=False)
    score = models.IntegerField(blank=False)
```

- `students` 一筆學生對應 `scorelist` 多筆科目成績；外鍵放在「多」的一方。
- `on_delete=models.CASCADE`：刪除被參照學生時，Django 的關聯刪除流程會連帶刪除其成績。此行不可當成無害示範操作。
- 外鍵允許 `NULL`，但未設定 `blank=True`；資料庫允許空關聯與表單允許不填是不同議題。
- `scorelist.cID` 是學生模型關聯物件；其原始主鍵值可由 `cID_id` 取得。未另外設定時，實體外鍵欄名預設會是 `cID_id`，不是原 SQL 範例的 `cID`。
- 沒有 `Meta.db_table`；預設模型資料表名稱帶 app label，後頁截圖也出現 `dbapp_students` 與 `dbapp_scorelist`。原文 SQL 常寫 `students`、`scorelist`，使用時要配合實際 schema。
- **規劃圖與模型不完全相同**：SQL 日期是 `DATE`，模型卻是 `DateTimeField`；`ENUM` 改成一般單字元字串，未設定 `choices`；SQL 規劃允許空的郵件／電話／地址，模型沒有 `null=True`；模型另增身高、體重。不要把兩者當成完全相同 DDL。

```bash
sudo python3 manage.py makemigrations
sudo python3 manage.py migrate
```

- `makemigrations` 建立模型變更的遷移檔，`migrate` 套用遷移至資料庫。
- 終端圖片顯示 `DBapp\migrations\0001_initial.py`、`Create model students`、`Applying DBapp.0001_initial... OK`；這張操作截圖列出的是 `students` 建模，不足以證明同張圖也建立了 `scorelist`。
- 截圖另有 `(mysql.W002) MariaDB Strict Mode is not set for database connection 'default'`，提醒啟用 strict mode，避免截斷等資料完整性問題。
- **補充**：命令前的 `sudo` 是原稿寫法，正常虛擬環境執行 Django 不應無條件使用 `sudo`，以免切換 Python 或造成權限混亂。本次未執行命令。

<a id="p209"></a>

### P209｜匯入範例資料與路由設定入口

[核對原講義第 209 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=209)

- phpMyAdmin 圖片顯示伺服器 `127.0.0.1`、資料庫 `class`；上圖操作 `dbapp_students`，下圖操作 `dbapp_scorelist`。
- 學生資料有 10 筆，欄位包含 `cID, cName, cSex, cBirthday, cEmail, cPhone, cAddr, cHeight, cWeight`。日期時間圖示為各生日午夜。
- 以下保留示範資料方便理解後續篩選、排序。已從原 PDF 重繪局部，交叉檢查 P209 學生表、P212 終端、P235 姓名表；仍無法確定的**個別字元直接標為〔待辨〕**：6、7、8 號姓名末字，以及 1 號地址的路名前二字。這些不是資料庫空值，也不是可直接匯入的真實欄位值；其餘欄位按可辨內容記錄。

| cID | 姓名 | cSex | cBirthday（日期部分） | cEmail | cPhone | cAddr | cHeight | cWeight |
|---|---|---|---|---|---|---|---|---|
| 1 | 簡奉君 | F | 1987-04-04 | elven@superstar.com | 0922988876 | 台北市〔待辨：路名前二字〕北路12號 | 160 | 49 |
| 2 | 黃靖輪 | M | 1987-07-01 | jinglun@superstar.com | 0918181111 | 台北市敦化南路93號5樓 | 175 | 72 |
| 3 | 潘四敬 | M | 1987-08-11 | sugie@superstar.com | 0914530768 | 台北市中央路201號7樓 | 162 | 65 |
| 4 | 賴勝恩 | M | 1984-06-20 | shane@superstar.com | 0946820035 | 台北市建國路177號6樓 | 178 | 72 |
| 5 | 黎楚寧 | F | 1988-02-15 | ivy@superstar.com | 0920981230 | 台北市忠孝東路520號6樓 | 164 | 45 |
| 6 | 蔡中〔待辨〕 | M | 1987-05-05 | zhong@superstar.com | 0951983366 | 台北市三民路1巷10號 | 172 | 75 |
| 7 | 徐佳〔待辨〕 | F | 1985-08-30 | lala@superstar.com | 0918123456 | 台北市仁愛路100號 | 158 | 56 |
| 8 | 林雨〔待辨〕 | F | 1986-12-10 | crystal@superstar.com | 0907408965 | 台北市民族路204號 | 166 | 48 |
| 9 | 林心儀 | F | 1988-12-01 | peggy@superstar.com | 0916456723 | 台北市建國北路10號 | 168 | 50 |
| 10 | 王燕博 | M | 1993-08-10 | albert@superstar.com | 0918976588 | 台北市北環路2巷80號 | 169 | 68 |

**成績截圖**：狀態列寫總計 30 筆；實際可見的是 `id, cID, course, score`，前十筆為國文，學生 1–10 的分數依序 `82, 68, 78, 85, 80, 76, 90, 87, 78, 65`；下一筆顯示 `id=11, cID=1, course='英文', score=67`。未顯示的其餘 19 筆不能由這張圖補造。

- 準備編輯專案路由：`sudo vim DB/urls.py`。
- **圖片疑點**：成績圖直接列 `cID`，與 P208 外鍵模型預設 `cID_id` 不一致；可能使用不同建表版本或另有未示出的 schema 設定，原頁未交代。

<a id="p210"></a>

### P210｜URL、view、開發伺服器與 SELECT 全欄位

[核對原講義第 210 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=210)

URL 圖片接續 P209，保留預設 admin 路由並加入 `/test/`：

```python
from django.urls import path
from DBapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test),
]
```

- 截圖從檔案第 17 行開始，`admin` 的匯入未出現在裁圖範圍；一般完整檔案須有 `from django.contrib import admin`（補充，不冒充本圖可見行）。

編輯 `DBapp/views.py`：

```python
from django.shortcuts import render
from django.http import HttpResponse

def test(request):
    return HttpResponse("Hello Django!")
```

```bash
sudo python3 manage.py runserver 0.0.0.0:8080
```

- `0.0.0.0` 表示監聽所有網路介面，`8080` 是連接埠；只應用於受控開發環境，不是正式部署方案。
- **圖示結果與疑點**：瀏覽器開的是 `127.0.0.1:8000/test/`，頁面內容 `Hello Django!`；這與印刷命令的 `8080` 不同，依實際啟動 port 瀏覽。

全欄位查詢：

```sql
SELECT * FROM `students`;
```

`*` 表示所有欄位，未使用 `WHERE` 則不先限制資料列。相對應的 ORM 在下一頁。

<a id="p211"></a>

### P211｜all()、模型物件與輸出所在位置

[核對原講義第 211 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=211)

```python
datas = students.objects.all()
```

- `objects` 是模型 manager，`all()` 回傳 `QuerySet`；迭代時取得模型物件。
- 上方 phpMyAdmin 圖顯示 SQL `students` 全部學生，座號在 SQL 表中以 `01`–`10` 呈現，與規劃的 ZEROFILL 顯示方式呼應。
- views 圖片可見以下程式；**補充前提**：須先從 `DBapp.models` 匯入 `students`。

```python
def test(request):
    datas = students.objects.all()
    for data in datas:
        print('%s %s %s %s %s %s %s' % (
            data.cID, data.cName, data.cSex, data.cBirthday,
            data.cEmail, data.cPhone, data.cAddr,
        ))
    return HttpResponse("Hello Django!")
```

- 使用 `data.cID` 等物件屬性讀欄位；身高、體重雖可能在模型中，這個 `print` 沒有列印它們。
- 程式的 `print()` 輸出在伺服器終端，**不是瀏覽器 HTML**；下方瀏覽器仍顯示 `Hello Django!`，完整終端輸出在 P212。
- 本頁再列 `sudo python3 manage.py runserver 0.0.0.0:8080`，但瀏覽器依然是 `8000`。

<a id="p212"></a>

### P212｜values() 指定欄位、字典存取與 DISTINCT

[核對原講義第 212 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=212)

- 頁頂終端是 P211 的輸出：10 筆學生，每列依序座號、姓名、性別、生日、Email、電話、地址。生日顯示午夜並帶 `+00:00`，圖片環境為 Django `3.2.4`，使用 `DB.settings`，server 在 `http://127.0.0.1:8000/`。HTTP log 為 `/test/` 回應 `200`。

```python
datas = students.objects.values('cID', 'cName', 'cEmail')
for data in datas:
    print('%s %s %s' % (data['cID'], data['cName'], data['cEmail']))
```

- 只選取座號、姓名、Email；每列變為字典，應用 `data['cID']` 而非 `data.cID`。
- 終端第二張圖正好改成三欄，仍包含 1–10 號，Email 依序為 `elven, jinglun, sugie, shane, ivy, zhong, lala, crystal, peggy, albert`，網域均為 `superstar.com`。
- 講義稱其為 `ValuesQuerySet`；**補充**：可理解成「迭代回傳字典的 QuerySet」，不必依賴舊版本內部類別名稱。
- **SQL 對照補充**：`SELECT cID, cName, cEmail FROM students;` 對應上述指定欄位操作。

`SELECT DISTINCT` 只顯示不同值一次，例：查看全班有幾種性別。

```sql
SELECT DISTINCT `cSex` FROM `students`;
```

這不是取出「每種性別的一位完整學生」，而是對所選的性別欄位去重；後頁接 ORM 與計數結果。

<a id="p213"></a>

### P213｜distinct().count()、values 與 values_list

[核對原講義第 213 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=213)

**SQL 結果圖**：`SELECT DISTINCT cSex FROM students` 回傳兩列，`F` 與 `M`；狀態列也標示總計 2 筆。

```python
datas = students.objects.values('cSex').distinct()
print(datas)
# 講義終端：<QuerySet [{'cSex': 'F'}, {'cSex': 'M'}]>

datas = students.objects.values('cSex').distinct().count()
print(datas)
# 講義終端：2
```

- `values('cSex')` 決定要去重的欄位；`distinct()` 排除重複；`count()` 計算去重後的列數，因此是性別種類數，不是學生總數。
- `values()`：迭代產生字典，不是模型實例。
- `values_list()`：迭代產生 tuple；指定單欄且 `flat=True` 時，改為純欄位值。
- **原稿編排疑點**：`values` 標題下面放了 `values_list` 範例，另一標題拼成 `value_list`，下一頁又放 `values` 範例。應依真正呼叫的方法判斷，不能依錯置標題判斷。

```python
list(Article.objects.values_list('id', flat=True))
# 講義示例：[1, 2, 3, 4, 5, 6]
```

**補充**：沒有 `flat=True` 的單欄 `values_list('id')`，每列會是 `(1,)`、`(2,)` 這類一元素 tuple；`flat=True` 只適用選取單一欄位。

<a id="p214"></a>

### P214｜WHERE、get() 與 filter() 差異

[核對原講義第 214 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=214)

接續上一頁字典範例：

```python
list(Article.objects.values('id'))
# 講義示例：[{'id': 1}, {'id': 2}, {'id': 3},
#            {'id': 4}, {'id': 5}, {'id': 6}]
```

WHERE 限制要回傳的資料列，灰底圖片語法：

```sql
SELECT 欄位名稱 FROM 資料表名稱 WHERE 條件敘述句;
```

例：選座號 1。

```sql
-- 原印刷行把欄名寫成含尾端空白的 `cID `，此處明確修正為 cID：
SELECT * FROM `students` WHERE `cID` = 1;
```

```python
datas = students.objects.get(cID=1)       # 單一模型物件
# 或：
datas = students.objects.filter(cID=1)    # QuerySet

# 只適用於上面的 filter() 分支：
for data in datas:
    print('%s %s %s %s %s %s %s' % (
        data.cID, data.cName, data.cSex, data.cBirthday,
        data.cEmail, data.cPhone, data.cAddr,
    ))
```

- `get()` 要求恰好一筆；**補充**：無資料會拋出 `DoesNotExist`，多於一筆會拋出 `MultipleObjectsReturned`。主鍵查詢具有唯一性，但仍可能查無資料。
- `filter()` 不論符合零筆、一筆、多筆都回傳 QuerySet；可用 `for` 逐筆處理。
- **重要差異**：不要把 `get()` 的單一物件直接放進這個 `for data in datas`。
- 圖片 phpMyAdmin 與終端都只列座號 `1`、`F`、生日 `1987-04-04`、`elven@superstar.com`、電話 `0922988876`，顯示等值篩選。

<a id="p215"></a>

### P215｜等值篩選、比較運算子、AND

[核對原講義第 215 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=215)

例：挑出男性。

```sql
SELECT * FROM `students` WHERE `cSex` = 'M';
```

```python
datas = students.objects.filter(cSex='M')
for data in datas:
    print('%s %s %s %s %s %s %s' % (
        data.cID, data.cName, data.cSex, data.cBirthday,
        data.cEmail, data.cPhone, data.cAddr,
    ))
```

- **圖片結果**：SQL 表格與 ORM 終端均有座號 `2, 3, 4, 6, 10`，`cSex` 都是 `M`；圖中以框線標示性別欄。
- 比較運算子表列出 `=, !=, <>, <, >, <=, >=, IS NULL`。`!=`、`<>` 都用於不等於；判斷 SQL 空值用 `IS NULL`，不是 `= NULL`。
- `AND`、`OR`、`NOT` 可連接／否定多個條件。

例：座號大於 5 且為男生。

```sql
SELECT * FROM `students` WHERE `cID` > 5 AND `cSex` = 'M';
```

兩條件必須同時成立；下一頁 ORM 以同一 `filter()` 的兩個參數表示。

<a id="p216"></a>

### P216｜lookup 比較、exclude 與 NOT 範圍陷阱

[核對原講義第 216 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=216)

頁頂圖片接 P215，結果為座號 `6` 與 `10`，且均為 `M`。

```python
datas = students.objects.filter(cID__gt=5, cSex='M')
for data in datas:
    print('%s %s %s %s %s %s %s' % (
        data.cID, data.cName, data.cSex, data.cBirthday,
        data.cEmail, data.cPhone, data.cAddr,
    ))
```

- 雙底線 `__` 連接欄位與 lookup，`gt` 是大於、`gte` 大於等於、`lt` 小於、`lte` 小於等於。
- `欄位__isnull=True` 對應空值；`False` 對應非空值。
- 同一 `filter()` 多個條件預設是 `AND`。

**中間深色圖片完整比較範例**：

| ORM 圖片行 | 正確意義 |
|---|---|
| `.filter(id__gt=1)` | `id > 1` |
| `.filter(id=1)` | `id = 1` |
| `.filter(id__lt=1)` | `id < 1` |
| `.filter(id__lte=1)` | `id <= 1` |
| `.filter(id__gte=1)` | `id >= 1` |
| `.exclude(id__gt=1)` | 排除 `id > 1`；不是 `id != 1`。原圖片右側寫 `!= 1`，此處為原稿錯誤。要不等於 1 應使用 `.exclude(id=1)`。 |
| `.filter(id__gt=1, id__lt=10)` | `1 < id < 10` |

末段題目說「座號不大於 5 的男生」，但原稿 SQL 是：

```sql
SELECT * FROM `students` WHERE !(`cID` > 5 AND `cSex` = 'M');
```

**重要勘誤**：`NOT (A AND B)` 不等於 `(NOT A) AND B`。原 SQL 否定整組條件，會連所有女性都納入；圖中卻只顯示男生 `2, 3, 4`，與原 SQL 不相符。

若依題意與圖片，應改為：

```sql
SELECT * FROM `students` WHERE NOT (`cID` > 5) AND `cSex` = 'M';
-- 這個非空主鍵例也可寫：WHERE cID <= 5 AND cSex = 'M'
```

下一頁 ORM 的 `~Q(cID__gt=5), cSex='M'` 正是只否定座號條件，符合題意，不等價於本頁印錯括號的 SQL。

<a id="p217"></a>

### P217｜Q 表達式、複合查詢與圖片 Book 範例勘誤

[核對原講義第 217 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=217)

多個 `filter` 參數預設是 AND；需要 OR／NOT 或指定括號組合時使用：

```python
from django.db.models import Q
```

- `Q(...) & Q(...)`：AND。
- `Q(...) | Q(...)`：OR。
- `~Q(...)`：NOT。
- Q 是可組合查詢條件，不要以 Python `and`／`or` 取代 `&`／`|`。

**第一張深色圖的三條例子**：

```python
.filter(Q(id__gt=10))
.filter(Q(id=8) | Q(id__gt=10))
.filter(Q(Q(id=8) | Q(id__gt=10)) & Q(caption='root'))
```

依序為大於 10；等於 8 或大於 10；前述 OR 群組成立且 `caption='root'`。

**第二張圖是 Book 關聯查詢，已局部放大閱讀**。題目說「作者姓名中包含方／少／偉三字、書名不包含偉，並且出版社地址以山西開頭」。原圖程式實際為：

```python
book = models.Book.objects.filter(
    Q(
        Q(author__name__contains='方') |
        Q(author__name__contains='少') |
        Q(author__name__contains='偉') |
        Q(title__icontains='偉')
    ) &
    Q(publish__addr__contains='山西')
).values('title')
```

- `author__name__contains`：沿 `author` 關聯找 `name` 再做包含判斷；`publish__addr__contains` 沿出版者關聯找地址；`values('title')` 只輸出書名字典。
- **原圖不等價於題意**：它把「書名包含偉」當 OR 的另一分支，沒有 NOT；地址使用 `contains`，不是「以山西開頭」。
- **依題意修正的補充版本**（並非原稿已執行結果）：

```python
book = models.Book.objects.filter(
    (Q(author__name__contains='方') |
     Q(author__name__contains='少') |
     Q(author__name__contains='偉')) &
    ~Q(title__icontains='偉') &
    Q(publish__addr__startswith='山西')
).values('title')
```

圖下注記「Q 查詢和非 Q 查詢混合使用，非 Q 查詢一定要放在 Q 查詢後面」，亦即位置參數形式的 `Q(...)` 放在關鍵字參數之前。

接續 P216「座號不大於 5 的男生」：

```python
datas = students.objects.filter(~Q(cID__gt=5), cSex='M')
for data in datas:
    print('%s %s %s %s %s %s %s' % (
        data.cID, data.cName, data.cSex, data.cBirthday,
        data.cEmail, data.cPhone, data.cAddr,
    ))
```

**圖示結果**：終端只顯示男生 `2, 3, 4`，與此 ORM 一致；不能把它拿來證明 P216 原印 SQL 的整組 NOT 正確。

<a id="p218"></a>

### P218｜Q OR 與 BETWEEN 包含邊界

[核對原講義第 218 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=218)

例：座號等於 1，或座號大於等於 9。

```sql
SELECT * FROM `dbapp_students` WHERE `cID` = 1 OR `cID` >= 9;
```

```python
from django.db.models import Q

datas = students.objects.filter(Q(cID=1) | Q(cID__gte=9))
for data in datas:
    print('%s %s %s %s %s %s %s' % (
        data.cID, data.cName, data.cSex, data.cBirthday,
        data.cEmail, data.cPhone, data.cAddr,
    ))
```

- 圖片 SQL 與終端均顯示座號 `1, 9, 10`，性別依序 `F, F, M`。
- `|` 任一條件成立即可；原 SQL 此頁用 `dbapp_students`，不是其他頁常見的 `students`，須留意資料表名稱版本。

例：找座號大於等於 4 且小於等於 6。

```sql
SELECT * FROM `students` WHERE `cID` BETWEEN 4 AND 6;
```

`BETWEEN` 包含兩端；不是 Python 切片的右界排除。下一頁有 ORM 與結果。

<a id="p219"></a>

### P219｜range 閉區間、IN 多個指定值與 exclude

[核對原講義第 219 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=219)

頁頂 phpMyAdmin 圖接 `BETWEEN 4 AND 6`，顯示座號 `4, 5, 6`。深色小圖另有：

```python
.filter(id__range=[1, 3])  # 1 到 3，包含兩端
```

本例 ORM：

```python
datas = students.objects.filter(cID__range=[4, 6])
for data in datas:
    print('%s %s %s %s %s %s %s' % (
        data.cID, data.cName, data.cSex, data.cBirthday,
        data.cEmail, data.cPhone, data.cAddr,
    ))
```

終端亦顯示 `4, 5, 6`；性別依序 `M, F, M`。

`IN`：指定多個候選值，例只要座號 1、3、5、7、9。

```sql
SELECT * FROM `students`
WHERE `students`.`cID` IN (1, 3, 5, 7, 9);
```

SQL 圖確實顯示這五個座號。頁底圖片列出：

```python
.filter(id__in=[1, 2, 3])
.exclude(id__in=[1, 2, 3])
```

- 第一行保留在集合中的列；第二行排除集合中的列，對應 `NOT IN`。
- **圖片勘誤**：原圖第二行右側也寫成 `in [1,2,3]`，漏了否定，不應照抄成相同語意。
- **補充**：IN 清單指定的是值，不是輸出排序；需要順序應另外 `order_by`。

<a id="p220"></a>

### P220｜IN ORM、SQL LIKE 萬用字元與 lookup 全表

[核對原講義第 220 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=220)

```python
datas = students.objects.filter(cID__in=[1, 3, 5, 7, 9])
for data in datas:
    print('%s %s %s %s %s %s %s' % (
        data.cID, data.cName, data.cSex, data.cBirthday,
        data.cEmail, data.cPhone, data.cAddr,
    ))
```

- 終端圖片保留五列，座號正是 `1, 3, 5, 7, 9`，對應上一頁 SQL。

**SQL LIKE 萬用字元圖片**：

| 字元 | 定義 | 圖片例子 |
|---|---|---|
| `_`（底線） | 任何單一字元；一個中文字也視作一個字元 | `LIKE '文_閣'` 可匹配「文淵閣」，不匹配「文藏經閣」。 |
| `%` | 零個或多個字元的字串 | `LIKE '文%閣'` 可匹配「文淵閣」與「文藏經閣」。 |

**ORM 對照表**（保留全部項目，並將原稿錯字與概念校正分開）：

| lookup | 意義／典型 SQL 概念 |
|---|---|
| `__exact` | 完全相等；原稿寫 `like 'aaa'`，實際應理解為精確等值比較，不保證後端用 LIKE。 |
| `__iexact` | 忽略大小寫的精確比對；原稿以 `ilike 'aaa'` 表意，實際 SQL 依後端。 |
| `__contains` | 包含某子字串，概念如 `LIKE '%aaa%'`。 |
| `__icontains` | 忽略大小寫的包含。原稿此格有「忽然大小寫我喜歡」等誤植；應理解為 case-insensitive contains。 |
| `__startswith` | 以指定字串開頭，概念 `LIKE 'aaa%'`。 |
| `__istartswith` | 忽略大小寫的開頭比對。 |
| `__endswith` | 以指定字串結尾，概念 `LIKE '%aaa'`。 |
| `__iendswith` | 忽略大小寫的結尾比對。 |
| `__range` | 落於包含端點的範圍內。 |
| `__year` | 依日期欄位的年份查詢。 |
| `__month` | 依月份查詢。 |
| `__day` | 依日期中的日查詢。 |

- 原稿指出 SQLite 的 `contains` 效果可與 `icontains` 相同；**補充**：字串大小寫行為與資料庫、collation、字元範圍有關，不能保證所有後端都完全相同。
- **使用提醒**：Django 的 `contains='aaa'` 不需手動加 `%`；ORM 會處理 LIKE pattern 與參數，SQL 示例的萬用字元不能不加區分直接搬入 lookup 的值。

<a id="p221"></a>

### P221｜電話開頭比對與地址子字串

[核對原講義第 221 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=221)

例：找出電話以 `0918` 開頭的學生。

```sql
SELECT * FROM `students` WHERE `cPhone` LIKE '0918%';
```

```python
datas = students.objects.filter(cPhone__istartswith='0918')
for data in datas:
    print('%s %s %s %s %s %s %s' % (
        data.cID, data.cName, data.cSex, data.cBirthday,
        data.cEmail, data.cPhone, data.cAddr,
    ))
```

- **SQL／ORM 圖片結果**：座號 `2, 7, 10`，電話依序為 `0918181111`、`0918123456`、`0918976588`；SQL 圖用框線突顯電話欄。
- 數字字串沒有大小寫差別，這個例子用 `startswith` 也能表達同樣的前綴條件；保留原講義的 `istartswith`。
- 圖中的額外範例：

```python
.filter(name__contains="ven")
.filter(name__icontains="ven")  # i：忽略大小寫
```

- 同圖列舉 `startswith, istartswith, endswith, iendswith`，提示包含、開頭、結尾是不同匹配位置。

例：地址包含「建國」。

```sql
SELECT * FROM `students` WHERE `cAddr` LIKE '%建國%';
```

兩側 `%` 允許「建國」出现在地址任意位置；並不限於地址以它開頭或結尾。

<a id="p222"></a>

### P222｜地址 contains、ORDER BY 基本語法

[核對原講義第 222 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=222)

```python
datas = students.objects.filter(cAddr__contains='建國')
for data in datas:
    print('%s %s %s %s %s %s %s' % (
        data.cID, data.cName, data.cSex, data.cBirthday,
        data.cEmail, data.cPhone, data.cAddr,
    ))
```

- **圖片結果**：兩筆，座號 `4` 的「台北市建國路177號6樓」、座號 `9` 的「台北市建國北路10號」。一個地址是「建國路」，一個是「建國北路」，都包含相同子字串。
- 圖中 SQL 使用 `dbapp_students`，再次與正文的 `students` 名稱不同。

排序灰底語法圖：

```sql
SELECT 欄位名稱
FROM 資料表名稱
ORDER BY 指定排序的欄位 排序方式;
```

- `ASC`（ascending）：遞增，小到大；指定 `ORDER BY` 欄位但省略方向時預設 ASC。
- `DESC`（descending）：遞減，大到小。
- **補充**：沒有 `ORDER BY` 不是「預設按主鍵遞增」，不能依畫面偶然順序推斷保證順序。

例：全班按生日遞減。

```sql
SELECT * FROM `students` ORDER BY `cBirthday` DESC;
```

日期值越晚越前面，不是按月份忽略年份排序；這裡等於較晚出生的學生排在前面。

<a id="p223"></a>

### P223｜order_by 升降冪與完整排序結果

[核對原講義第 223 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=223)

深色小圖先示範「先篩選再排序」：

```python
.filter(name='seven').order_by('id')   # ASC
.filter(name='seven').order_by('-id')  # DESC
```

- 字串前的 `-` 表示遞減，不是把資料內容取負值。

生日範例：

```python
# 遞增：
datas = students.objects.all().order_by('cBirthday')

# 遞減：
datas = students.objects.all().order_by('-cBirthday')
for data in datas:
    print('%s %s %s %s %s %s %s' % (
        data.cID, data.cName, data.cSex, data.cBirthday,
        data.cEmail, data.cPhone, data.cAddr,
    ))
```

**圖片 SQL 與 ORM 終端的遞減順序**：

| 順序（由上而下） | cID | cBirthday |
|---|---|---|
| 1 | 10 | 1993-08-10 |
| 2 | 9 | 1988-12-01 |
| 3 | 5 | 1988-02-15 |
| 4 | 3 | 1987-08-11 |
| 5 | 2 | 1987-07-01 |
| 6 | 6 | 1987-05-05 |
| 7 | 1 | 1987-04-04 |
| 8 | 8 | 1986-12-10 |
| 9 | 7 | 1985-08-30 |
| 10 | 4 | 1984-06-20 |

- 本頁列了遞增和遞減兩條指派，但圖示實際結果是遞減；若把兩條依序執行，後一條會覆蓋 `datas`。

<a id="p224"></a>

### P224｜多欄排序優先順序與 LIMIT 的用途

[核對原講義第 224 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=224)

例：先按性別遞增，同性別內再按生日遞減。

```sql
SELECT * FROM `students` ORDER BY `cSex` ASC, `cBirthday` DESC;
```

```python
datas = students.objects.all().order_by('cSex', '-cBirthday')
for data in datas:
    print('%s %s %s %s %s %s %s' % (
        data.cID, data.cName, data.cSex, data.cBirthday,
        data.cEmail, data.cPhone, data.cAddr,
    ))
```

- 第一排序鍵優先；只有第一鍵相同才比較第二鍵，不是先排完性別又把全表重新依生日排序。
- **圖片結果**：F 組為 `9, 5, 1, 8, 7`，M 組為 `10, 3, 2, 6, 4`。例如 10 號生日比所有女生晚，仍在 F 組之後，證明性別是第一排序鍵。
- SQL 圖欄位頂端以 `1`、`2` 標示性別與生日的排序先後；終端顯示相同順序。
- 頁末介紹 `LIMIT`：限制從查詢結果哪一筆開始，以及取多少筆，常用於分頁或取前幾筆；真正語法圖片在下一頁。

<a id="p225"></a>

### P225｜LIMIT 與 QuerySet 切片的逐項對照

[核對原講義第 225 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=225)

灰底語法圖片為：

```sql
SELECT 欄位名稱
FROM 資料表名稱
LIMIT 開始顯示的筆數, 顯示多少筆資料;
```

- MySQL `LIMIT offset, count` 第一數字是略過多少列，以 0 起算；第二數字是最多取多少列，不是結束索引。
- `LIMIT` 從查詢結果擷取資料；若同時排序，SQL 順序應把 `LIMIT` 放在 `ORDER BY` 之後。
- 搭配排序可取最前／最後若干筆。**補充**：若要固定分頁且排序鍵有重複，可再以主鍵作次排序鍵，避免相同排序值間順序不穩定。

先性別 ASC、生日 DESC，取前五筆：

```sql
SELECT * FROM `students`
ORDER BY `students`.`cSex` ASC, `students`.`cBirthday` DESC
LIMIT 5;
```

```python
datas = students.objects.all().order_by('cSex', '-cBirthday')[:5]
for data in datas:
    print('%s %s %s %s %s %s %s' % (
        data.cID, data.cName, data.cSex, data.cBirthday,
        data.cEmail, data.cPhone, data.cAddr,
    ))
```

原稿把 `datas =` 和右側分在不同實體行；此處接回合法 Python 行。

本頁其餘所有 SQL 變體與下頁 ORM 對照：

| SQL | ORM | 意義 |
|---|---|---|
| `SELECT * FROM students LIMIT 2` | `students.objects.all()[:2]` | 最前兩筆。 |
| `SELECT * FROM students LIMIT 0,2` | `students.objects.all()[0:2]` | 跳過零筆，取兩筆。 |
| `SELECT * FROM students LIMIT 1,2` | `students.objects.all()[1:3]` | 跳過一筆，取兩筆。 |
| `SELECT * FROM students LIMIT 4,2` | `students.objects.all()[4:6]` | 跳過四筆，取兩筆。 |
| `SELECT * FROM students LIMIT 3,4` | `students.objects.all()[3:7]` | 跳過三筆，取四筆。 |

**深色切片圖片另含三種語法**：

```python
.all()[10:20]
.all()[::2]
.all()[6]       # 索引
```

- `[start:stop]` 左界包含、右界排除；索引是查詢結果的位置，不是主鍵值。
- **補充**：帶 step 的 `[::2]` 會評估 QuerySet 並在 Python 端切片，不能簡單視為一般 SQL LIMIT；`[6]` 取得第七個結果物件，沒有那一列時可能拋 `IndexError`。

<a id="p226"></a>

### P226｜切片畫面結果與 scorelist 規劃

[核對原講義第 226 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=226)

本頁用終端圖片逐一示範，所有圖仍列七個學生欄位：

| 操作 | 講義圖中座號 |
|---|---|
| 承上一頁排序後 `[:5]` | `9, 5, 1, 8, 7`（都是 F 組） |
| `all()[:2]` 或 `all()[0:2]` | `1, 2` |
| `all()[1:3]` | `2, 3` |
| `all()[4:6]` | `5, 6` |
| `all()[3:7]` | `4, 5, 6, 7` |

- 以上座號是截圖當時結果順序；這些 `all()` 沒有明確排序，不能保證所有資料庫／所有狀態都按座號。

為示範統計函式，講義說在 `class` 資料庫加入 `scorelist`。圖片表格的全部欄位：

| 中文名稱 | 欄位 | SQL 型別 | 屬性／其他 | NULL |
|---|---|---|---|---|
| 編號 | `id` | `TINYINT(4)` | 原圖拼 `USIGNED`，意圖應為 `UNSIGNED`；主鍵、`auto_increment` | 否 |
| 座號 | `cID` | `TINYINT(2)` | 原圖拼 `USIGNED ZEROFILL` | 否 |
| 科目 | `course` | `ENUM('國文','英文','數學')` | 預設國文 | 否 |
| 分數 | `score` | `TINYINT(3)` | 無另外屬性 | 否 |

- 每筆成績代表某一學生某一科的分數；一個學生可以有國文、英文、數學三列，不能直接把成績列數當學生人數。
- **與 P208 模型差異**：此規劃的 `course` 是 ENUM 且有預設，模型只是 `CharField(max_length=20)`；規劃的 `cID` 不許 NULL，模型外鍵允許 NULL。圖中 `TINYINT(4)` 的括號也不代表能存四位數值，欄位範圍取決於資料型別與是否 unsigned。

<a id="p227"></a>

### P227｜SUM、aggregate 與整體／先篩選後彙總

[核對原講義第 227 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=227)

全班國文、英文、數學所有成績的總分：

```sql
SELECT SUM(`score`) FROM `scorelist`;
```

**SQL 圖示結果**：`SUM(score) = 2178`。

```python
from DBapp.models import scorelist
from django.db.models import Sum, Count, Max, Min, Avg

datas = scorelist.objects.aggregate(Sum('score'))
print(datas)
# 講義終端：{'score__sum': 2178}
```

- `aggregate()` 對目前 QuerySet 執行聚合，回傳字典，不是逐筆模型 QuerySet。
- 預設結果鍵為欄位名與聚合名組合，例如 `score__sum`。
- **原稿語法缺漏**：印刷程式 `aggregate(Sum('score')` 少一個右括號；上面已明確補齊。圖中已有成功輸出，但不能以圖認定印刷的缺括號程式可執行。
- **補充**：可用 `aggregate(total=Sum('score'))` 自訂結果鍵 `total`，本例原稿沒有使用 alias。

只算國文總分：

```sql
SELECT SUM(`score`) FROM `scorelist` WHERE `course` = '國文';
```

**SQL 圖示結果**：`789`。WHERE 先限制成績列，再對剩下的國文列加總；不是全科總分再篩選。

<a id="p228"></a>

### P228｜國文 SUM、AVG 與 COUNT 入口

[核對原講義第 228 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=228)

接上頁國文合計：

```python
from DBapp.models import scorelist
from django.db.models import Sum, Count, Max, Min, Avg

datas = scorelist.objects.filter(course='國文').aggregate(Sum('score'))
print(datas)
# 講義終端：{'score__sum': 789}
```

原頁字串 `'國文'` 被版面換行拆開，本筆記接回同一字串，沒有在字串中加入換行。

國文平均：

```sql
SELECT AVG(`score`) FROM `scorelist` WHERE `course` = '國文';
```

**SQL 圖示結果**：`78.9000`。

```python
from django.db.models import Sum, Count, Max, Min, Avg

datas = scorelist.objects.filter(course='國文').aggregate(Avg('score'))
print(datas)
```

- `Avg` 計算符合篩選條件的分數平均，預設字典鍵為 `score__avg`。
- **證據界線**：本頁 AVG 顯示的是 SQL `78.9000`，下方 ORM 框只有程式，沒有獨立 ORM 終端結果；不把推測的字典當原圖輸出。
- 頁末開始 `COUNT()` 計次，以 `students` 全班人數為例；真正 SQL 與結果接 P229。
- **補充統計語意**：SQL `SUM/AVG` 忽略 NULL 欄值；有資料、沒有資料、分數為零是不同概念，之後 LEFT JOIN 的無成績情況尤其要注意。

<a id="p229"></a>

### P229｜COUNT、國文 MAX、數學 MIN

[核對原講義第 229 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=229)

全班人數：

```sql
SELECT COUNT(`students`.`cID`) FROM `students`;
```

```python
from django.db.models import Sum, Count, Max, Min, Avg

datas = students.objects.aggregate(Count('cID'))
print(datas)
# 講義終端：{'cID__count': 10}
```

- **SQL 圖示結果**：`10`，但圖中欄頭寫的是 `COUNT(*)`，不是上方印刷的 `COUNT(students.cID)`。
- **語意補充**：`COUNT(*)` 算所有列；`COUNT(欄位)` 算欄位非 NULL 的列。此處 `cID` 是不可空主鍵，兩者人數一致，但不要推論任意可空欄位也一樣。
- `students.objects.count()`（補充）可直接取得整數，和 `aggregate(Count('cID'))` 回傳字典的形式不同。

國文最高分：

```sql
SELECT MAX(`score`) FROM `scorelist` WHERE `course` = '國文';
```

```python
from django.db.models import Sum, Count, Max, Min, Avg

datas = scorelist.objects.filter(course='國文').aggregate(Max('score'))
print(datas)
# 講義終端：{'score__max': 90}
```

- MAX 得到最高「分數值」，不是該學生完整紀錄；若多人同分，這條聚合也不會列出得分者。

數學最低分：

```sql
SELECT MIN(`score`) FROM `scorelist` WHERE `course` = '數學';
```

本頁以此 SQL 結束；ORM 與最低分結果接下一頁。

<a id="p230"></a>

### P230｜MIN、GROUP BY、annotate 與結果型態

[核對原講義第 230 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=230)

數學最低分 ORM：

```python
from django.db.models import Sum, Count, Max, Min, Avg

datas = scorelist.objects.filter(course='數學').aggregate(Min('score'))
print(datas)
# 講義終端：{'score__min': 38}
```

每位學生各自的總分：

```sql
SELECT `cID`, SUM(`score`) FROM `scorelist` GROUP BY `cID`;
```

```python
from django.db.models import Sum, Count, Max, Min, Avg

datas = scorelist.objects.values_list('cID').annotate(Sum('score'))
print(datas)
```

**終端圖片完整結果**：

```text
<QuerySet [(1, 236), (2, 207), (3, 242), (4, 233), (5, 207),
           (6, 218), (7, 193), (8, 195), (9, 257), (10, 190)]>
```

- 每組 tuple 第一項是 `cID` 值，第二項是該學生各科 `score` 的加總。
- `values_list('cID')` 在 `annotate()` 前，先指定以哪些值分組，再替每組加入 `Sum('score')`。
- `aggregate()` 是整個查詢的一份彙總字典；`annotate()` 可替每個查詢結果或每個分組增加計算欄位，仍回傳 QuerySet。
- 原稿列出的可用查詢表達式有聚合函式、`F` 表達式、`Q` 表達式、`Func` 表達式。
- **原稿說法限制**：文字說 annotate 回傳的 QuerySet「存儲的是模型對象」，本例卻先用了 `values_list()`，因此實際是 tuple；若先用 `values()` 則為字典；未轉換輸出型態的模型 QuerySet 才是帶註記屬性的模型物件。
- **補充**：標題寫「分組排列」，但 `GROUP BY` 的核心是分組，不是保證結果排序；要固定順序應再加 `ORDER BY`／`order_by()`。
- 本頁末開始「HAVING：GROUP BY 的條件式」。

<a id="p231"></a>

### P231｜HAVING／WHERE 的層次與 CRUD 入口

[核對原講義第 231 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=231)

題目：只顯示座號 1–5 的分數總計。

```sql
SELECT `cID`, SUM(`score`)
FROM `scorelist`
GROUP BY `cID`
HAVING `cID` <= 5;
```

```python
from django.db.models import Sum, Count, Max, Min, Avg

datas = (
    scorelist.objects.filter(cID__lte=5)
    .values_list('cID')
    .annotate(Sum('score'))
)
print(datas)
```

**SQL 表格與 ORM 終端一致**：

```text
(1, 236), (2, 207), (3, 242), (4, 233), (5, 207)
```

- 印刷把 `annotate` 分成 `annota`／`te`，本筆記已接回；另外使用括號表達合法跨行 Python。
- 題目寫座號 1–5，但實際條件只有 `<=5`，沒有下界；範例資料的主鍵由 1 起算，所以結果符合題目，不代表條件明示了 `>=1`。

**重要觀念修正**：原稿紅字說「若對 GROUP BY 加條件，不能用 WHERE，只能用 HAVING」過度概括。

1. `WHERE`：分組前篩選原始資料列。
2. `HAVING`：分組後篩選群組／聚合結果，例如 `SUM(score) > 某值`。
3. 此頁只篩選分組鍵 `cID <= 5`，可在 WHERE 先做，所以 ORM 的 `filter(cID__lte=5)` 是分組前篩選，**不是展示 ORM 產生 HAVING 的典型寫法**；對這份資料可得到相同結果。

**真正對聚合條件篩選的補充示例**（非原頁執行紀錄）：

```sql
SELECT cID, SUM(score) AS total
FROM scorelist
GROUP BY cID
HAVING SUM(score) > 230;
```

```python
scorelist.objects.values('cID').annotate(total=Sum('score')).filter(total__gt=230)
```

- 這裡先註記 `total` 再依聚合結果篩選，才清楚表達 HAVING 層次。
- 頁末轉入新增、更新、刪除：查詢讀取資料，INSERT／UPDATE／DELETE 則維護資料內容；INSERT 基本語法在 P232 圖片。

<a id="p232"></a>

### P232｜INSERT 完整欄位、建立物件後 save、UPDATE 基本式

[核對原講義第 232 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=232)

INSERT 灰底基本語法：

```sql
INSERT [INTO] 資料表名稱 [(欄位名稱1, 欄位名稱2, ...)]
VALUES (值1, 值2, ...);
```

- 欄位清單和 VALUES 值的順序要一一對應；方括號為講義表示可選語法的記號，不要原樣輸入 SQL。

**新增學生資料表**（原稿說「5 位」，但圖片實際只列 3 位）：

| 座號 | 姓名 | 性別 | 生日 | 電子郵件 | 電話 | 地址 | 身高 | 體重 |
|---|---|---|---|---|---|---|---|---|
| 留白 | Bill1 | 男 | 1988-02-10 | Bill1@bb.com | 0925932221 | 台北 | 176 | 89 |
| 留白 | Bill2 | 男 | 1988-02-10 | Bill2@bb.com | 0925932222 | 新竹 | 170 | 81 |
| 留白 | Bill3 | 男 | 1988-02-10 | Bill3@bb.com | 0925932223 | 桃園 | 172 | 84 |

單筆新增原稿 SQL（版面斷行已接回，內容保留）：

```sql
INSERT INTO `students`
(`cName`, `cSex`, `cBirthday`, `cEmail`, `cPhone`, `cAddr`, `cHeight`, `cWeight`)
VALUES ('Bill1', '男', '1988-02-10', 'Bill1@bb.com', '0925932221', '台北', '176', '89');
```

- 未提供自動遞增 `cID`，由資料庫配置。
- **原稿資料規格問題**：若依先前 `ENUM('F','M')`，`'男'` 不在允許值內；不能以中文性別直接當作 `'M'`。數值被單引號包住也是原稿寫法，不是必須。

ORM 是另一筆不同的資料：

```python
add = students(
    cName="bill", cSex="M", cBirthday="2021-08-08",
    cEmail="bill@yahoo.com.tw", cPhone="0922222", cAddr=" 新竹",
    cHeight=0, cWeight=0,
)
add.save()
```

- `students(...)` 建立 Python 模型物件；呼叫 `.save()` 才將新物件寫入資料庫。
- **不可宣稱兩例新增相同資料**：姓名、性別表示、生日、郵件、電話、地址、身高、體重均與 Bill1 SQL 不同。地址印刷含前置空白，保留為 `" 新竹"`；若實際程式字串含空白，空白會成為資料內容。
- 生日模型先前為 `DateTimeField`，此處卻傳只有日期的字串；是否允許與時區警告需依實際模型、設定確認，勿把它當成理想的時區處理示範。

UPDATE 灰底語法：

```sql
UPDATE 資料表名稱
SET 欄位名稱1 = 值1, 欄位名稱2 = 值2, ...
WHERE 條件式;
```

- UPDATE 可改多列；所有符合 WHERE 的列都會修改，缺少 WHERE 可能改整表。
- 頁末題目：修改座號 11 的身高體重，下一頁接具體值。
- **安全提醒**：以上是筆記程式，沒有執行資料新增或更新；測試應使用獨立測試資料庫、備份與交易，先確認篩選的目標列。

<a id="p233"></a>

### P233｜UPDATE／DELETE 對照與高風險原稿錯配

[核對原講義第 233 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=233)

修改座號 11：

```sql
UPDATE `students` SET `cHeight` = 174, `cWeight` = 92 WHERE `cID` = 11;
```

```python
update = students.objects.get(cID=11)
update.cHeight = 180
update.cWeight = 60
update.save()
```

- 模型流程：`get()` 取出既有物件，修改屬性，再 `.save()` 寫回。
- **兩例值不相同**：SQL 改成 `174 / 92`，ORM 改成 `180 / 60`。二者示範更新方式，但不是相同更新的等價對照。
- **補充**：`get(cID=11)` 找不到會拋例外；不能假設前頁新增一定取得主鍵 11。

DELETE 灰底基本式：

```sql
DELETE FROM 資料表名稱
WHERE 條件式;
```

- DELETE 同樣可作用於多列，所有符合 WHERE 的列都會刪除。缺少 WHERE 可能刪除整表內容。
- 本頁題目：「刪除座號大於 11 的同學」。

```sql
DELETE FROM `students` WHERE `cID` > 11;
```

但原稿 ORM 寫的是另一個危險且完全不同的條件：

```python
# 以下為原稿錯配示例，切勿視為上面 SQL 的等價語句：
delete = students.objects.filter(cID__lte=5)  # cID <= 5
delete.delete()
```

- **重要勘誤**：它刪的是座號小於等於 5，不是大於 11；應先把查詢條件修成 `students.objects.filter(cID__gt=11)`，確認選中列後才討論刪除。
- P208 的 `scorelist` 外鍵採 `CASCADE`，透過 Django 刪除學生還可能一併刪除其成績。影響範圍不只學生表。
- 本次沒有執行 UPDATE／DELETE，也沒有假稱刪除成功；僅記錄與校對原稿。
- 原頁參考：https://www.geeksforgeeks.org/django-orm-inserting-updating-deleting-data/ 。

<a id="p234"></a>

### P234｜多表關聯、INNER JOIN 與國文成績

[核對原講義第 234 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=234)

- 多表查詢能同時選取不同表的欄位；本例透過學生座號把學生基本資料與多筆成績連結。
- SQL JOIN 的連結條件要正確；資料庫未宣告外鍵也可能用 SQL 連結，但宣告外鍵有助於維護參照完整性（補充）。

灰底 JOIN 基本式：

```sql
SELECT 顯示欄位...
FROM 資料表A [INNER] JOIN 資料表B
ON A.相關欄位 = B.相關欄位;
```

- `INNER` 可省略；此處 `JOIN` 就是內連接。
- ON 決定哪些 A、B 列互相匹配。每位學生多筆成績時，連接後會有多列，並非永遠一學生一列。
- 原文說兩邊都須有資料，沒有登錄成績的學生不會出現在結果；**修正其適用範圍**：這是 INNER JOIN 的特性，不是它原文「無論何種方式結合」都如此；後面的 LEFT／RIGHT JOIN 正為保留未匹配列。

顯示學生座號、姓名及國文成績：

```sql
SELECT `students`.`cID`, `students`.`cName`, `scorelist`.`score`
FROM `students` JOIN `scorelist`
ON `students`.`cID` = `scorelist`.`cID`
WHERE `scorelist`.`course` = '國文';
```

1. FROM／JOIN 連結學生和成績。
2. ON 以座號匹配，避免任意學生配任意成績。
3. WHERE 保留國文成績。
4. SELECT 只顯示座號、姓名、分數。

- **欄位名稱注意**：此為講義 SQL schema；若真正使用 P208 外鍵模型，右表資料欄名預設是 `cID_id`，需依實際資料表調整，不能盲目照抄。
- **ORM 對照補充**（原頁沒有 JOIN ORM；假設 P208 模型關聯確實存在）：

```python
scorelist.objects.filter(course='國文').values('cID', 'cID__cName', 'score')
```

`cID` 取關聯主鍵值，`cID__cName` 沿外鍵取學生姓名；這是補充解釋，不是聲稱原稿程式已驗證執行。

<a id="p235"></a>

### P235｜國文 JOIN 結果、外連接語法與舊式多表查詢

[核對原講義第 235 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=235)

**頁頂結果表**接 P234，只有三欄 `cID, cName, score`。本次從原 PDF 局部放大交叉辨讀：

| cID | cName | 國文 score |
|---|---|---|
| 01 | 簡奉君 | 82 |
| 02 | 黃靖輪 | 68 |
| 03 | 潘四敬 | 78 |
| 04 | 賴勝恩 | 85 |
| 05 | 黎楚寧 | 80 |
| 06 | 蔡中〔待辨〕 | 76 |
| 07 | 徐佳〔待辨〕 | 90 |
| 08 | 林雨〔待辨〕 | 87 |
| 09 | 林心儀 | 78 |
| 10 | 王燕博 | 65 |

- 三個姓名末字雖已放大並對照 P209、P212，仍無法可靠確認，逐格保留〔待辨〕；不影響座號、成績、JOIN 關係的判讀。

LEFT／RIGHT JOIN 通式：

```sql
SELECT 顯示欄位...
FROM 資料表A LEFT|RIGHT JOIN 資料表B
ON A.相關欄位 = B.相關欄位;
```

- `LEFT|RIGHT` 表示二擇一，不是把豎線打進 SQL。
- **概念補充**：LEFT JOIN 保留左表每一列，沒匹配右表時右側欄值為 NULL；RIGHT JOIN 反過來保留右表每一列。

例：希望列出全班每個人的成績總分與平均。講義先示範舊式逗號連表：

```sql
SELECT `students`.`cID`, `students`.`cName`,
       SUM(`scorelist`.`score`), AVG(`scorelist`.`score`)
FROM `students`, `scorelist`
WHERE `students`.`cID` = `scorelist`.`cID`
GROUP BY `students`.`cID`, `students`.`cName`;
```

- 逗號列出兩表，再用 WHERE 座號相等限制，實際上相當於本例 INNER JOIN；尚未保留沒有成績的學生。
- GROUP BY 以座號與姓名分組，SUM 加總每人的成績，AVG 算其已存在成績的平均。
- **警告補充**：若漏了 WHERE 的連結條件，就會造成所有學生與所有成績交叉配對，使彙總錯誤。

<a id="p236"></a>

### P236｜INNER JOIN 分組結果、表別名與勘誤

[核對原講義第 236 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=236)

**頁頂圖示完整結果**（姓名沿用 P235，以座號識別；平均數保留原圖顯示四位小數）：

| cID | SUM(score) | AVG(score) |
|---|---|---|
| 01 | 236 | 78.6667 |
| 02 | 207 | 69.0000 |
| 03 | 242 | 80.6667 |
| 04 | 233 | 77.6667 |
| 05 | 207 | 69.0000 |
| 06 | 218 | 72.6667 |
| 07 | 193 | 64.3333 |
| 08 | 195 | 65.0000 |
| 09 | 257 | 85.6667 |
| 10 | 190 | 63.3333 |

改以明確 JOIN 語法：

```sql
SELECT `students`.`cID`, `students`.`cName`,
       SUM(`scorelist`.`score`), AVG(`scorelist`.`score`)
FROM `students` INNER JOIN `scorelist`
ON `students`.`cID` = `scorelist`.`cID`
GROUP BY `students`.`cID`;
```

- 這版 GROUP BY 只列 `cID`，上一頁列 `cID, cName`。若 `cID` 是學生主鍵，某些資料庫／SQL 模式可依函數相依性接受姓名欄；若想讓跨資料庫範例更明確，應同列 `cID, cName`，不能假設任何 schema 都接受。

**原稿表別名範例完整保留**：

```sql
SELECT `students`.`cID`, `students`.`cName`,
       SUM(`scorelist`.`score`), AVG(`scorelist`.`score`)
FROM `students` st INNER JOIN `scorelist` sc
ON st.`cID` = sc.`cID`
GROUP BY st.`cID`;
```

- `st` 是 students 的別名、`sc` 是 scorelist 的別名；原圖以紅字標出 FROM 與 ON 的替代名稱。
- **原稿錯誤**：FROM 既已給別名，SELECT 卻仍用原表名限定欄位，MySQL 等環境會報未知欄位／無法解析。須把 SELECT 一併改成別名。

**一致且較清楚的修正版**：

```sql
SELECT st.`cID`, st.`cName`,
       SUM(sc.`score`) AS total, AVG(sc.`score`) AS average
FROM `students` AS st INNER JOIN `scorelist` AS sc
ON st.`cID` = sc.`cID`
GROUP BY st.`cID`, st.`cName`;
```

- 此頁實際圖片是結果表與兩段 SQL，**沒有 JOIN 維恩圖或架構圖**。
- **ORM 對照補充**：對 P208 未設定 `related_name` 的模型，可透過反向查詢名稱 `scorelist` 做 `students.objects.filter(scorelist__isnull=False).values('cID', 'cName').annotate(total=Sum('scorelist__score'), average=Avg('scorelist__score'))`；此補充未執行，原頁僅教 SQL。

<a id="p237"></a>

### P237｜LEFT JOIN 保留無成績學生與 NULL 聚合

[核對原講義第 237 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=237)

- 頁頂再顯示 INNER JOIN 的 10 筆結果，數字與 P236 表相同，沒有 Bill1／Bill2／Bill3。

改用 LEFT JOIN：

```sql
SELECT `students`.`cID`, `students`.`cName`,
       SUM(`scorelist`.`score`), AVG(`scorelist`.`score`)
FROM `students` LEFT JOIN `scorelist`
ON `students`.`cID` = `scorelist`.`cID`
GROUP BY `students`.`cID`, `students`.`cName`;
```

- 以 students 為左表，所有學生都保留；右側 scorelist 能找到的才帶入。
- 原有座號 1–10 的總分與平均維持 P236 的數值。
- **下方圖片額外列出三筆**：

| cID | cName | SUM(score) | AVG(score) |
|---|---|---|---|
| 11 | Bill1 | NULL | NULL |
| 14 | Bill2 | NULL | NULL |
| 15 | Bill3 | NULL | NULL |

- 原圖主鍵是 `11, 14, 15`，不是連續的 `11, 12, 13`；不能依新增順序自行修成連續座號。自動遞增主鍵可能有缺號，而講義未交代缺號經過。
- NULL 表示沒有可彙總的成績，不等於分數是 0；在這個資料中，`SUM` 與 `AVG` 對無可用成績均顯示 NULL。
- 這正是 LEFT JOIN 相對 INNER JOIN 的重點：即使學生沒有登錄成績，仍能知道這個學生存在，而不是在報表消失。

**補充：篩選位置會改變外連接的保留效果**。

- 若要「保留所有學生，但只連結國文成績」，條件應放在 ON：

```sql
SELECT st.cID, st.cName, sc.score
FROM students AS st
LEFT JOIN scorelist AS sc
  ON st.cID = sc.cID AND sc.course = '國文';
```

- 若改在最後加 `WHERE sc.course = '國文'`，沒有匹配成績而被補 NULL 的列會被過濾掉，失去保留所有學生的效果。
- 若報表想把無成績總分顯示為零，可另用 `COALESCE(SUM(sc.score), 0)`，但這是顯示／業務規則選擇，不代表原資料真有零分；平均分是否也要補零須另外決定。
- **ORM 對照補充**（依 P208 模型、未執行）：

```python
students.objects.values('cID', 'cName').annotate(
    total=Sum('scorelist__score'),
    average=Avg('scorelist__score'),
)
```

反向聚合可保留學生並計算其關聯成績；不要先加排除無成績者的條件，否則與原頁 LEFT JOIN 目的不同。

> 範圍結束：以上只記錄至 P237；未把後頁當作本範圍證據。原稿截圖數值均已與圖片閱讀對照；補充版本均標明，沒有宣稱以真實 DB 執行或驗證。


---

## P238–P262｜關聯式資料、Django ORM、Cookie 與 Session

> 範圍：PDF 實體頁 238–262。以下逐頁對照文字層及頁面圖片；將圖片內的程式、表格與操作納入。程式碼只整理排版與換行，原稿的命名及差異另列「原稿疑點」；「補充」不是原稿內容。所有新增、更新、刪除及遷移命令僅作筆記，未對真實資料庫執行。

<a id="p238"></a>

### P238｜七種 SQL JOIN 圖解與 ORM 關聯基礎

[核對原講義第 238 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=238)

[本頁原圖（含完整畫面細節）](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=238)

**圖片完整解讀：**「SQL JOINS」用 A、B 兩個重疊圓形表示左右兩張表，紅色部分是想保留的結果。七種圖形分別是：左外連接保留整個 A；右外連接保留整個 B；內連接只保留交集；左排除連接只保留 A 中沒有 B 配對者；右排除連接反之；全外連接保留 A、B 全部；外排除連接保留兩邊各自未配對的部分、不保留交集。

| 圖片名稱 | 圖中集合表示／意義 | SQL 重點 |
|---|---|---|
| Left Outer Join | A ∪ (A ∩ B)，即全部 A | `LEFT JOIN` |
| Right Outer Join | (A ∩ B) ∪ B，即全部 B | `RIGHT JOIN` |
| Inner Join | A ∩ B | `INNER JOIN` |
| Left Excluding Join | A − B | 左連接後篩 `B.Key IS NULL` |
| Right Excluding Join | B − A | 右連接後篩 `A.Key IS NULL` |
| OUTER JOIN／FULL OUTER JOIN／FULL JOIN | A ∪ B ∪ (A ∩ B)，即聯集 | `FULL OUTER JOIN` |
| Outer Excluding Join | (A − B) ∪ (B − A) | 全外連接後篩任一方鍵為 NULL |

圖中七段 SQL（`<select_list>` 是欲選欄位的占位符）：

```sql
-- Left Outer Join
SELECT <select_list>
FROM Table_A A
LEFT JOIN Table_B B ON A.Key = B.Key;

-- Right Outer Join
SELECT <select_list>
FROM Table_A A
RIGHT JOIN Table_B B ON A.Key = B.Key;

-- Inner Join
SELECT <select_list>
FROM Table_A A
INNER JOIN Table_B B ON A.Key = B.Key;

-- Left Excluding Join
SELECT <select_list>
FROM Table_A A
LEFT JOIN Table_B B ON A.Key = B.Key
WHERE B.Key IS NULL;

-- Right Excluding Join
SELECT <select_list>
FROM Table_A A
RIGHT JOIN Table_B B ON A.Key = B.Key
WHERE A.Key IS NULL;

-- Full Outer Join
SELECT <select_list>
FROM Table_A A
FULL OUTER JOIN Table_B B ON A.Key = B.Key;

-- Outer Excluding Join
SELECT <select_list>
FROM Table_A A
FULL OUTER JOIN Table_B B ON A.Key = B.Key
WHERE A.Key IS NULL OR B.Key IS NULL;
```

**ORM 關聯概念：**一對一以一個人對應一個身分證號碼為例；一對多以一個家庭有多個人為例，通常透過外鍵實作；多對多以學生可修多門課、每門課也有多名學生為例，通常以第三張關聯表實作。

**補充／限制：**這些集合圖是配對概念示意，SQL 結果仍會因一對多配對出現多列，不等同數學集合自動去重。`IS NULL` 的排除判斷宜使用確定非空的配對鍵。講義其他頁使用 MySQL；MySQL 並不直接支援圖中的 `FULL OUTER JOIN` 語法，不能原樣視為 MySQL 可執行語句。

<a id="p239"></a>

### P239｜完整關聯模型與資料庫遷移

[核對原講義第 239 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=239)

[本頁原圖（含完整畫面細節）](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=239)

**圖片：**頂端三組方框箭頭依序是「一個人 ↔ 一個身分證號」、「一個家庭 → 多個人」的三條箭頭，以及「學生 ↔ 課程」多條雙向箭頭。下方 `DBapp/models.py` 截圖把一對多、一對一、多對多放在同一個模型檔。

```python
from django.db import models

class students(models.Model):
    cID = models.AutoField(primary_key=True)
    cName = models.CharField(max_length=20, blank=False)
    cSex = models.CharField(max_length=1, blank=False, default='F')
    cBirthday = models.DateTimeField(auto_now_add=False)
    cEmail = models.CharField(max_length=100, blank=False)
    cPhone = models.CharField(max_length=50, blank=False)
    cAddr = models.CharField(max_length=255, blank=False)
    cHeight = models.IntegerField(blank=True, null=True)
    cWeight = models.IntegerField(blank=True, null=True)

# 一個學生有多個成績（one to many）（students to scorelist）
class scorelist(models.Model):
    id = models.AutoField(primary_key=True)
    cID = models.ForeignKey('students', on_delete=models.CASCADE, null=True)
    course = models.CharField(max_length=20, blank=False)
    score = models.IntegerField(blank=False)

# 一個學生有一個密碼與權限（one to one）（students to permissions）
class permissions(models.Model):
    id = models.AutoField(primary_key=True)
    cID = models.OneToOneField('students', on_delete=models.CASCADE, null=True)
    passwd = models.CharField(max_length=100, blank=False)
    level = models.CharField(max_length=2, blank=False)  # 0 管理者，1 一般使用者

class Book(models.Model):
    name = models.CharField(max_length=32)
    authors = models.ManyToManyField(to='Author')

class Author(models.Model):
    name = models.CharField(max_length=32)
```

- `students.cID` 是自動編號主鍵；其他基本資料含姓名、性別、生日、Email、電話、地址、身高、體重。
- `scorelist.cID` 是多對一外鍵：每筆成績屬於一名學生，同一學生可對應多筆成績。外鍵可為 NULL。
- `permissions.cID` 是一對一欄位：同一學生最多對應一筆權限記錄。圖中也設 `null=True`。
- 兩種關聯均用 `on_delete=models.CASCADE`：刪除被參照的學生時，Django 的刪除處理會連帶刪掉依附的成績／權限記錄。
- `Book.authors` 是多對多管理器，不是直接把多個作者姓名塞進 Book 的單一欄位；Django 會自動建立中介表。

原稿命令：

```sh
vim DBapp/models.py
sudo python3 manage.py makemigrations
sudo python3 manage.py migrate
```

`makemigrations` 建立模型變更的 migration 中介檔；`migrate` 將遷移套用至資料庫。

**補充／安全提醒：**原稿直接儲存 `passwd` 字串是教學模型，不應作正式密碼儲存方案；實際系統應使用 Django 認證與密碼雜湊機制。`blank` 關乎驗證、`null` 關乎資料庫空值，不是同一設定。使用虛擬環境通常不需 `sudo`，且實際遷移前應確認資料庫與備份。

<a id="p240"></a>

### P240｜phpMyAdmin 驗證四張資料表的實際結構

[核對原講義第 240 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=240)

[本頁原圖（含完整畫面細節）](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=240)

本頁幾乎全是 phpMyAdmin 截圖；位置列顯示伺服器 `127.0.0.1`、資料庫 `class`。操作是在左側點選資料表，再看「結構」頁，逐欄核對名稱、型別、NULL、主鍵及 AUTO_INCREMENT。文字欄位顯示 `utf8_unicode_ci` 定序。

**第一張：`dbapp_students`**

| 欄位 | 截圖型別 | 圖中意義 |
|---|---|---|
| cID | int(11) | 黃色主鍵圖示，AUTO_INCREMENT |
| cName | varchar(20) | 姓名 |
| cSex | varchar(1) | 性別 |
| cBirthday | datetime(6) | 生日日期時間 |
| cEmail | varchar(100) | 電子郵件 |
| cPhone | varchar(50) | 電話 |
| cAddr | varchar(255) | 地址 |
| cHeight | int(11) | 身高 |
| cWeight | int(11) | 體重 |

**第二張：`dbapp_scorelist`**：`id int(11)` 為自增主鍵；`cID_id int(11)` 為帶索引圖示的外鍵，可 NULL、預設 NULL；`course varchar(20)`；`score int(11)`。模型欄位叫 `cID`，實體欄位自動加 `_id` 變成 `cID_id`。

**第三張：`dbapp_permissions`**：`id int(11)` 自增主鍵、`passwd varchar(100)`、`cID_id int(11)`（可 NULL、預設 NULL、帶鍵圖示）、`level varchar(2)`。一對一在資料庫層的關鍵是對外鍵建立唯一限制，不能只從「也是整數欄位」判斷其關係。

**第四張：`dbapp_author`**：`id bigint(20)` 為自增主鍵；`name varchar(32)` 是作者姓名。模型沒明寫 `id`，Django 仍替它建立預設主鍵。

**圖片旁支資訊：**左側同時可見 Django 的 `auth_*`、`django_admin_log`、`django_content_type`、`django_migrations`、`django_session` 等表；右邊每欄有修改／刪除操作，這裡只是查看結構，不是要求點刪除。

**原稿疑點：**學生表截圖的 `cHeight`、`cWeight` 在 NULL 欄經局部放大確認均為「否」，與 P239 模型的 `null=True` 不一致，表示截圖與模型可能不是同一遷移狀態；不據此默改模型。Author 的 bigint 主鍵與前三個模型明定 AutoField 的 int 也不同，與預設自動主鍵設定相關。

<a id="p241"></a>

### P241｜Book 與多對多中介表、匯入後資料檢視

[核對原講義第 241 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=241)

[本頁原圖（含完整畫面細節）](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=241)

**圖片一：`dbapp_book` 結構。**`id bigint(20)` 為 AUTO_INCREMENT 主鍵；`name varchar(32)` 為書名，文字定序 `utf8_unicode_ci`。Book 本表沒有直接儲存作者清單的欄位。

**圖片二：自動產生的 `dbapp_book_authors`。**講義特別寫「自動增加的表格」。結構為 `id bigint(20)`（自增主鍵）、`book_id bigint(20)`、`author_id bigint(20)`；後兩者帶鍵圖示，三欄均不可 NULL。一筆中介記錄表示「這本書與這位作者有關聯」，因此一本書多作者、同作者多本書都以多筆關聯列表示。

**匯入資料表資料：**下半頁不是匯入精靈的步驟，而是匯入後的「瀏覽」結果。左側紅框指向要檢查的表。

- `dbapp_students`：執行 `SELECT * FROM dbapp_students`，綠色狀態列顯示共 10 筆，畫面只露出前 5 筆。欄位依序為 cID、cName、cSex、cBirthday、cEmail、cPhone、cAddr、cHeight、cWeight。可見學生 1–5 的性別依序 F、M、M、M、F；身高／體重依序 160／49、175／72、162／65、178／72、164／45。生日以帶時間的格式顯示，例如第 1 筆 `1987-04-04 00:00:00.000000`。Email、電話及地址作為學生基本資料範例，並不參與此頁的關聯計算。
學生截圖前五筆的其餘資料經局部放大轉錄如下（範例資料，不代表真實人物；生日均帶 `00:00:00.000000`）：

| cID | cName | cSex | cBirthday 日期部分 | cEmail | cPhone | cAddr | cHeight | cWeight |
|---:|---|---|---|---|---|---|---:|---:|
| 1 | 簡奉君 | F | 1987-04-04 | elven@superstar.com | 0922988876 | 台北市濟洲北路12號 | 160 | 49 |
| 2 | 黃靖輪 | M | 1987-07-01 | jinglun@superstar.com | 0918181111 | 台北市敦化南路93號5樓 | 175 | 72 |
| 3 | 潘四敬 | M | 1987-08-11 | sugie@superstar.com | 0914530768 | 台北市中央路201號7樓 | 162 | 65 |
| 4 | 賴勝恩 | M | 1984-06-20 | shane@superstar.com | 0946820035 | 台北市建國路177號6樓 | 178 | 72 |
| 5 | 黎楚寧 | F | 1988-02-15 | ivy@superstar.com | 0920981230 | 台北市忠孝東路520號6樓 | 164 | 45 |

地址第一筆依圖片可辨字樣轉錄；原圖小字／不常見路名不宜自行改成熟悉的街名，若需拿來建立逐字資料集應再對照原圖。

- `dbapp_permissions`：共 4 筆，資料如下。請注意畫面欄序是 `id, passwd, cID_id, level`，不是模型宣告順序。

| id | passwd（原稿明碼） | cID_id | level |
|---:|---|---:|---|
| 1 | 1234 | 1 | 1 |
| 2 | 3333 | 2 | 0 |
| 3 | 0000 | 4 | 1 |
| 4 | 444 | 3 | 1 |

由此可見學生表 10 筆、權限表只有 4 筆，並非每位學生已建立權限；後續跨表查詢會看到缺少關聯者的 NULL／None。主鍵 `id=3` 的權限對應的是學生 `cID=4`，不可把兩張表的自增 id 當成同一欄。

**補充／安全提醒：**本頁沒有提供匯入來源檔名、格式或點選匯入的完整步驟，不應自行補成原稿操作。圖示中的明碼密碼只用來說明關聯，不能照搬為正式帳號系統。

<a id="p242"></a>

### P242｜一對一關聯：先新增學生

[核對原講義第 242 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=242)

[本頁原圖（含完整畫面細節）](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=242)

**頁首圖片：**phpMyAdmin 的 `dbapp_scorelist` 瀏覽畫面，顯示共 30 筆、本頁顯示範圍 0–24；截圖露出的前 8 筆為國文成績，欄位是 `id, cID_id, course, score`，學生 1–8 的國文成績依序為 82、68、78、85、80、76、90、87。左側紅框強調選取成績表。

**模型圖片：**重列 P239 的 students 基本資料欄位，並用紅框標出 permissions 的一對一欄位。此頁關聯模型完整關鍵部分：

```python
class permissions(models.Model):
    id = models.AutoField(primary_key=True)
    cID = models.OneToOneField('students', on_delete=models.CASCADE, null=True)
    passwd = models.CharField(max_length=100, blank=False)
    level = models.CharField(max_length=2, blank=False)  # 0 管理者，1 一般使用者
```

**新增題目：**建立「王大明」、性別 M、生日 2020-08-20、Email `wang@yahoo.com.tw`、電話「099999」、地址新竹、身高 120、體重 40，另建立密碼「0000」、level「0」的權限資料。

原稿先建立學生，保留回傳物件到 `datas`：

```python
datas = students.objects.create(
    cName='王大明', cSex='M', cBirthday='2020-08-20',
    cEmail='wang@yahoo.com.tw', cPhone='09333333',
    cAddr='新竹', cHeight=120, cWeight=40
)
```

`create()` 同時建立、儲存物件，回傳的 `datas` 可供下一頁一對一關聯使用。此頁沒有把密碼直接放入學生表。

**原稿疑點：**題幹電話是 `099999`，程式卻是 `09333333`，兩者均保留、不默改。生日模型是 DateTimeField，但範例給日期字串；時區／時間處理在原稿未說明。

<a id="p243"></a>

### P243｜一對一新增、反向跨表查詢與連帶刪除

[核對原講義第 243 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=243)

[本頁原圖（含完整畫面細節）](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=243)

**承上新增權限：**圖中把 `cID=datas` 標成紅色，表示傳入前一頁建立的學生模型物件，不是字串姓名。

```python
permissions.objects.create(cID=datas, passwd='0000', level='0')
```

**查詢學生座號、姓名、密碼及 level：**`permissions__passwd` 與 `permissions__level` 透過反向關聯與雙底線跨到權限模型；`values()` 的每列是字典。

```python
datas = students.objects.values(
    'cID', 'cName', 'permissions__passwd', 'permissions__level'
)
for data in datas:
    print('%s %s %s %s' % (
        data['cID'], data['cName'],
        data['permissions__passwd'], data['permissions__level']
    ))
```

**輸出圖片：**列出座號 1–10，而不是只列出有權限的四名學生。前四名的密碼／level 是 `1234 1`、`3333 0`、`444 1`、`0000 1`；座號 5–10 均印出 `None None`。這正對應 P241 只有四筆 permissions 的資料狀態。圖中名單包括簡奉君、黃靖輪、潘四敬、賴勝恩，以及後六名學生；姓名只是結果辨識，查詢重點是缺關聯不會讓該學生從這個 values 查詢消失。

**刪除王大明的基本資料與權限資料：**兩種替代方式，不要連續執行成同一流程。

```python
# 第一種：取得單一物件後刪除
students.objects.get(cName='王大明').delete()

# 第二種：刪除所有符合條件的物件
students.objects.filter(cName='王大明').delete()
```

依 `CASCADE` 設定，刪學生也會清除其權限記錄；模型還有成績關聯，因此相關成績亦可能被連帶刪除。`get()` 要求恰好一筆，找不到或同名多筆會拋例外；`filter()` 是集合查詢，可匹配零筆、多筆。正式使用前要先核對目標主鍵，不以姓名唯一性作未驗證假設。

頁末開始「ORM(One-To-Many Relation)」，指示編輯 `DBapp/models.py`，模型圖片續於下一頁。

**原稿疑點：**查詢輸出截圖沒有新增的王大明，顯示它不是保證緊接前一頁操作後的同步結果；不把圖中十筆擅自增補成十一筆。

<a id="p244"></a>

### P244｜一對多：新增成績與依科目查詢

[核對原講義第 244 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=244)

[本頁原圖（含完整畫面細節）](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=244)

**模型圖片：**上半部再列 students 的所有基本欄位，下半部紅框圈出外鍵。關鍵模型完整如下：

```python
class scorelist(models.Model):
    id = models.AutoField(primary_key=True)
    cID = models.ForeignKey('students', on_delete=models.CASCADE, null=True)
    course = models.CharField(max_length=20, blank=False)
    score = models.IntegerField(blank=False)
```

學生是「一」的一方，成績是「多」的一方；`cID` 放在成績模型，將各筆成績指向學生。

**新增題目：**替姓名「黃靖輪」的學生新增地理成績。第一種寫法先找學生，直接建立成績：

```python
scorelist.objects.create(
    cID=students.objects.get(cName='黃靖輪'),
    course='地理', score=60
)
```

第二種先建 Python 物件再 `save()`；原稿實際改用「音樂」：

```python
data = scorelist(
    cID=students.objects.get(cName=' 黃靖輪'),
    course='音樂', score=60
)
data.save()
```

**原稿疑點：**第二種與題目／第一種不同，`course='音樂'` 並非地理；文字層第二種姓名字串還有前導空白，圖片亦有疏排空白，若真納入字串便可能查不到原姓名。此處保留文字層的前導空白並警示，不暗中修正；要執行時應先確認實際姓名值。

**查詢座號、姓名與國文成績：**先以反向關聯 `scorelist__course` 過濾，再取出基本資料與成績欄位。

```python
print(students.objects.filter(scorelist__course='國文').values(
    'cID', 'cName', 'scorelist__course', 'scorelist__score'
))
```

雙底線前段是關聯路徑，後段是被關聯模型欄位。這裡 `scorelist` 是查詢路徑名稱；後續從「物件」存取多筆成績會使用 `scorelist_set`，兩者位置不同，不可互換。

<a id="p245"></a>

### P245｜國文成績輸出與每位學生的聚合統計

[核對原講義第 245 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=245)

[本頁原圖（含完整畫面細節）](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=245)

頁首終端圖是 P244 查詢的原始 `<QuerySet [{...}, ...]>` 表示法：每筆字典含 `cID`、`cName`、`scorelist__course`、`scorelist__score`。接著示範用迴圈逐列格式化，而不是直接印整個 QuerySet。

```python
datas = students.objects.filter(scorelist__course='國文').values(
    'cID', 'cName', 'scorelist__course', 'scorelist__score'
)
for data in datas:
    print('%s %s %s %s' % (
        data['cID'], data['cName'],
        data['scorelist__course'], data['scorelist__score']
    ))
```

**圖片輸出表：**（依圖片文字轉錄）

| cID | 姓名 | 科目 | 分數 |
|---:|---|---|---:|
| 1 | 簡奉君 | 國文 | 82 |
| 2 | 黃靖輪 | 國文 | 68 |
| 3 | 潘四敬 | 國文 | 78 |
| 4 | 賴勝恩 | 國文 | 85 |
| 5 | 黎楚寧 | 國文 | 80 |
| 6 | 蔡中穎 | 國文 | 76 |
| 7 | 徐佳瑩 | 國文 | 90 |
| 8 | 林雨〔末字不確定〕 | 國文 | 87 |
| 9 | 林心儀 | 國文 | 78 |
| 10 | 王燕博 | 國文 | 65 |

**題目：列出全班每人的成績總分與平均。**

```python
from django.db.models import Sum, Count, Max, Min, Avg

print(students.objects.values_list('cID', 'cName').annotate(
    Sum('scorelist__score'), Avg('scorelist__score')
))
```

- `values_list('cID', 'cName')` 令每筆回傳 tuple，而不是 `values()` 的字典。
- `annotate()` 為每個學生分組補上聚合值；此處輸出欄序為座號、姓名、總分、平均。
- `Sum` 求和、`Avg` 求平均；原稿也匯入 `Count`（數量）、`Max`（最大）、`Min`（最小），但本例沒有使用後三者。
- 圖片中的 QuerySet 共有座號 1–10 的 tuple；總分與平均完整整理於 P246（同一資料的逐列輸出）。

**圖片操作：**終端畫面顯示開發伺服器 `http://127.0.0.1:8000/`、`Quit the server with CTRL-BREAK.`；另一小圖含 `GET /test/ HTTP/1.1` 的請求日誌。這表示教學把查詢結果 `print()` 到執行 Django 的終端，不代表結果已渲染進網頁。

**辨識註記：**小圖的個別人名字形可能因解析度混淆，姓名以可辨內容轉錄；查詢關鍵及數值均可直接辨讀。

<a id="p246"></a>

### P246｜總分／平均的 tuple 索引，依座號更新成績

[核對原講義第 246 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=246)

[本頁原圖（含完整畫面細節）](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=246)

承接前頁聚合範例，改成逐筆列印：

```python
from django.db.models import Sum, Count, Max, Min, Avg

datas = students.objects.values_list('cID', 'cName').annotate(
    Sum('scorelist__score'), Avg('scorelist__score')
)
for data in datas:
    print('%s %s %s %s' % (data[0], data[1], data[2], data[3]))
```

`data[0]` 是 cID、`data[1]` 是 cName、`data[2]` 是 Sum、`data[3]` 是 Avg。這與上一個 `values()` 例子用欄名字串當索引不同。

**終端圖片數值（照原圖，不重新計算／改寫精度）：**

| cID | 姓名 | 總分 | 平均 |
|---:|---|---:|---:|
| 1 | 簡奉君 | 236 | 78.6667 |
| 2 | 黃靖輪 | 207 | 69.0 |
| 3 | 潘四敬 | 242 | 80.6667 |
| 4 | 賴勝恩 | 233 | 77.6667 |
| 5 | 黎楚寧 | 207 | 69.0 |
| 6 | 蔡中穎 | 218 | 72.6667 |
| 7 | 徐佳瑩 | 193 | 64.3333 |
| 8 | 林雨〔末字不確定〕 | 195 | 65.0 |
| 9 | 林心儀 | 257 | 85.6667 |
| 10 | 王燕博 | 190 | 63.3333 |

**修改題目一：學號「03」的國文改為 60 分。**資料庫主鍵是整數，因此程式使用 `cID=3`，而非把顯示用的前導零寫入數值。

```python
# 第一種：先取一的一方，再從反向關聯管理器篩成績
datas = students.objects.get(cID=3)
datas.scorelist_set.filter(course='國文').update(score=60)

# 第二種：直接從成績表篩選，使用查到的學生主鍵
scorelist.objects.filter(
    course='國文', cID=students.objects.get(cID=3).cID
).update(score=60)
```

第一種的 `scorelist_set` 已限定為這名學生的所有成績，`filter(course='國文')` 再限縮科目。第二種同時比對 course 與外鍵 cID。`update()` 更新所有符合條件的成績列，若同一學生有多筆同科成績，並不只改一筆。

**修改題目二：簡奉君的國文改為 100。**本頁先取得學生，更新動作續在下一頁：

```python
datas = students.objects.get(cName='簡奉君')
```

**補充：**`update()` 是直接 QuerySet 更新，不等同逐一呼叫模型的 `save()`；在真實系統應先核對篩選結果及影響筆數。本筆記沒有執行更新。

<a id="p247"></a>

### P247｜依姓名更新／刪除，轉入多對多模型

[核對原講義第 247 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=247)

[本頁原圖（含完整畫面細節）](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=247)

**承 P246：簡奉君的國文改為 100，第一種完整流程：**

```python
datas = students.objects.get(cName='簡奉君')
datas.scorelist_set.filter(course='國文').update(score=100)
```

原稿說明：「先查尋多對一的一那方」，再查「多」的成績方並更新。

第二種以內層取得學生 cID，再把它作為成績表外鍵篩選值：

```python
scorelist.objects.filter(
    course='國文', cID=students.objects.get(cName='簡奉君').cID
).update(score=100)
```

**刪除題目：簡奉君的學生資料與全部成績一起刪除。**

```python
students.objects.get(cName='簡奉君').delete()
```

刪除學生時由先前 `ForeignKey(..., on_delete=models.CASCADE)` 連帶刪成績；同時也要留意一對一 permissions 的連带刪除。這是破壞性示例，未執行。

**多對多模型圖片：**編輯 `DBapp/models.py`，紅框圈住 `ManyToManyField`。

```python
class Book(models.Model):
    name = models.CharField(max_length=32)
    authors = models.ManyToManyField(to='Author')

class Author(models.Model):
    name = models.CharField(max_length=32)
```

一本書可有多個作者；一名作者也可寫多本書。資料分別存 Book、Author，`authors.add(...)` 新增的是中介表關聯。

**第一次新增作者「小虎」及「C++」「PHP」兩書，第一種：**

```python
Author_obj = Author.objects.create(name="小虎")
Book_obj = Book.objects.create(name="C++")
Book_obj.authors.add(Author_obj)
Book_obj = Book.objects.create(name="PHP")
# 下一頁承接此行
Book_obj.authors.add(Author_obj)
```

必須先有已儲存、具有主鍵的 Author 與 Book，再建立多對多關聯；只建立作者與書本，不會自動把它們連起來。

<a id="p248"></a>

### P248｜多對多新增：create 與 save、既有作者增添書籍

[核對原講義第 248 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=248)

[本頁原圖（含完整畫面細節）](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=248)

頁首 `Book_obj.authors.add(Author_obj)` 是上一頁 PHP 書的關聯，不是重複替 C++ 新增作者。

**第一次新增小虎、C++、PHP，第二種完整寫法：**

```python
Author_obj = Author(name="小虎")
Author_obj.save()

Book_obj1 = Book(name="C++")
Book_obj1.save()
Book_obj2 = Book(name="PHP")
Book_obj2.save()

Book_obj1.authors.add(Author_obj)
Book_obj2.authors.add(Author_obj)
```

**三張並排圖片：**左邊 `dbapp_book` 出現 `id=29, name=C++` 與 `id=30, name=PHP`；右邊 `dbapp_author` 是 `id=23, name=小虎`；中間 `dbapp_book_authors` 有兩筆：

| 中介 id | book_id | author_id |
|---:|---:|---:|
| 16 | 29 | 23 |
| 17 | 30 | 23 |

這些 id 是截圖當時的自增編號，不保證在新資料庫重跑時相同；關鍵是兩本書都指向同一位作者 23。

**既有作者小虎，再新增「JAVA」「Linux」，第一種：**

```python
Author_obj = Author.objects.get(name="小虎")
Book_obj = Book.objects.create(name="JAVA")
Book_obj.authors.add(Author_obj)
Book_obj = Book.objects.create(name="Linux")
Book_obj.authors.add(Author_obj)
```

這裡作者已存在，所以用 `get()` 重用，而不是再 `create()` 一名同名小虎。書名大小寫依原稿保留為 JAVA、Linux。

**補充：**第一種與第二種是替代示範，若都在同一資料庫照跑，會新增重複作者／書本；模型沒有對 name 設唯一性，之後 `get(name=...)` 可能出現多筆錯誤。

<a id="p249"></a>

### P249｜既有作者新增兩書的 save 寫法，一本書加入兩位作者

[核對原講義第 249 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=249)

[本頁原圖（含完整畫面細節）](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=249)

**承接 P248：小虎新增 JAVA、Linux，第二種：**

```python
Author_obj = Author.objects.get(name="小虎")

Book_obj1 = Book(name="JAVA")
Book_obj1.save()
Book_obj1.authors.add(Author_obj)

Book_obj2 = Book(name="Linux")
Book_obj2.save()
Book_obj2.authors.add(Author_obj)
```

**三張並排結果圖：**Book 表有 `29 C++`、`30 PHP`、`33 JAVA`、`34 Linux`；Author 表仍僅 `23 小虎`；中介表變成四列：

| id | book_id | author_id |
|---:|---:|---:|
| 16 | 29 | 23 |
| 17 | 30 | 23 |
| 20 | 33 | 23 |
| 21 | 34 | 23 |

圖片表明新增書與關聯不需要複製作者。中介自增編號有跳號，原稿未解釋原因，不假設是連續新建資料庫。

**新題目：小明、大雄均為 C# 的作者。第一種：**

```python
Author_obj1 = Author.objects.create(name="小明")
Author_obj2 = Author.objects.create(name="大雄")
Book_obj = Book.objects.create(name="c#")
Book_obj.authors.add(Author_obj1, Author_obj2)
```

`add()` 可以一次傳入多個作者物件，在同一本書下建立兩筆多對多關聯。它不會把作者名合成一個字串。

**第二種在本頁先建立小明，接續下一頁：**

```python
Author_obj1 = Author(name="小明")
Author_obj1.save()
```

**原稿疑點：**題目是大寫 `C#`，新增程式實際使用小寫 `c#`。後續查詢與刪除又寫 `C#`；大小寫是否視為相同取決於資料庫與欄位定序，不應默認跨資料庫都一樣。

<a id="p250"></a>

### P250｜一書多作者的結果、依書名與作者查詢

[核對原講義第 250 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=250)

[本頁原圖（含完整畫面細節）](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=250)

**承 P249，第二種完整新增流程：**

```python
Author_obj1 = Author(name="小明")
Author_obj1.save()
Author_obj2 = Author(name="大雄")
Author_obj2.save()
Book_obj = Book(name="c#")
Book_obj.save()
Book_obj.authors.add(Author_obj1, Author_obj2)
```

**三表圖片：**Book 為 `id=37, name=c#`；Author 為 `id=34, name=小明`、`id=35, name=大雄`；中介表是 `(id=26, book_id=37, author_id=34)` 與 `(id=27, book_id=37, author_id=35)`。同一個 book_id 出現兩次，對應不同 author_id，正是一本書多位作者。

**查詢一：「C#」有哪些作者？**

```python
print(Book.objects.filter(name="C#").values('name', 'authors__name'))
```

原圖終端回傳：

```text
<QuerySet [{'name': 'c#', 'authors__name': '小明'},
           {'name': 'c#', 'authors__name': '大雄'}]>
```

同一本書因關聯到兩位作者，會展開為兩筆結果；不是回傳 `authors__name` 為 Python 清單。原稿圖中大寫條件查到了小寫書名，與先前 `utf8_unicode_ci` 不區分大小寫定序相符，但不適用於所有資料庫設定。

**查詢二：「小虎」出版哪些書？第一種用作者物件篩：**

```python
print(Book.objects.filter(
    authors=Author.objects.get(name="小虎")
).values('name', 'authors__name'))
```

**第二種沿關聯直接篩作者姓名：**

```python
print(Book.objects.filter(authors__name="小虎").values(
    'name', 'authors__name'
))
```

第一種先要求作者姓名恰好匹配一筆；第二種不使用 `get()`，直接以跨表條件過濾。第三種主鍵寫法及結果續 P251。

<a id="p251"></a>

### P251｜使用作者 id 查詢，多對多刪除的邊界

[核對原講義第 251 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=251)

[本頁原圖（含完整畫面細節）](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=251)

**查小虎的書，第三種：**

```python
authors_id = Author.objects.get(name="小虎").id
print(Book.objects.filter(authors=authors_id).values('name', 'authors__name'))
```

此處 `authors_id` 是程式變數名稱，並非自動生成的多對多模型欄位；先取得作者 id，再傳入 `authors=` 作為關聯篩選值。

**結果圖片：**QuerySet 中有四筆：`C++／小虎`、`PHP／小虎`、`JAVA／小虎`、`Linux／小虎`，對應 P249 的四筆中介關聯。

**刪除書名 C# 的資料，保留 Author：**

```python
Book.objects.get(name="C#").delete()
```

刪除該 Book 與它的中介關聯，不刪小明、大雄兩個 Author 物件。原稿「Author 資料表保留」指作者資料仍保留，不是只保留空表架構。

**刪除作者小虎，保留 Book：**

```python
Author.objects.get(name="小虎").delete()
```

刪小虎及其中介關聯，但 C++、PHP、JAVA、Linux 的 Book 記錄仍在；書可能變成沒有作者關聯。這兩種刪除都是刪模型物件，不只是解除一筆關聯。

**補充／安全提醒：**若只想解除作者與書的關聯，應考慮關聯管理器的 `remove()`／`clear()`，而不是刪 Book／Author；這是補充用法，非本頁原稿範例。原稿 `get(name=...)` 仍有找不到或多筆的例外風險。所有刪除指令在本筆記中未執行。

**原稿列出的參考文獻（僅轉錄，未另取代本頁內容）：**

- https://notes.andywu.tw/2018/%E8%B3%87%E6%96%99%E5%BA%AB-%E9%97%9C%E8%81%AF%E4%BB%8B%E7%B4%B9-%E4%B8%80%E5%B0%8D%E4%B8%80%E3%80%81%E4%B8%80%E5%B0%8D%E5%A4%9A%E3%80%81%E5%A4%9A%E5%B0%8D%E5%A4%9A/
- https://www.runoob.com/django/django-orm-2.html
- https://www.cnblogs.com/pythonxiaohu/p/5814247.html

<a id="p252"></a>

### P252｜MySQL 的 JOIN UPDATE 與多表 DELETE

[核對原講義第 252 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=252)

[本頁原圖（含完整畫面細節）](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=252)

本頁用紅字標記 SQL 關鍵字，示範在原始 SQL 層完成與 ORM 相似的更新、刪除。這些是 MySQL 風格語法，並非所有 SQL 引擎通用。

**UPDATE 使用 INNER JOIN／LEFT JOIN 的格式：**

```sql
UPDATE T1
[INNER JOIN | LEFT JOIN] T2 ON T1.C1 = T2.C1
SET T1.C2 = T2.C2,
    T2.C3 = expr
WHERE condition
```

方括號與直線表示語法選項，不是可直接執行的 SQL 字元。`ON` 指定兩表配對條件，`SET` 指定更新欄位／運算式，`WHERE` 限定哪些匹配列可更新。

**例一：cID「03」的國文改 60。原稿：**

```sql
UPDATE `scorelist` SET `score`=60 WHERE `cID`=3 AND `course`=’國文’
```

這個例子已知道成績表外鍵，不需要 JOIN。

**例二：姓名簡奉君的國文改 100。原稿排版整理如下；姓名疏排空白另見疑點：**

```sql
UPDATE `students`
INNER JOIN `scorelist` ON `students`.`cID`=`scorelist`.`cID`
SET `scorelist`.`score`='100'
WHERE `students`.`cName`=' 簡 奉 君 ' AND `scorelist`.`course`='國文'
```

由學生表依姓名選到學生，再透過 cID 連到成績表，最後只更新國文列。`'100'` 在原稿是加引號的值，即使 score 是整數型別也照錄；適當型別與轉換要由真正資料庫確認。

**DELETE 使用 INNER JOIN 的格式：**

```sql
DELETE T1, T2
FROM T1
INNER JOIN T2 ON T1.key = T2.key
WHERE condition;
```

`DELETE` 後面列出的表是刪除目標；`FROM ... JOIN ...` 是用來辨認該刪哪些列的配對條件。

**例：把簡奉君的學生資料與所有成績刪掉：**

```sql
DELETE `students`, `scorelist`
FROM `students`
INNER JOIN `scorelist` ON `students`.`cID`=`scorelist`.`cID`
WHERE `students`.`cName`="簡奉君"
```

**原稿疑點／執行限制：**

1. 本頁使用 `students`、`scorelist` 與 `scorelist.cID`，但 P240 的 Django 實體表是 `dbapp_students`、`dbapp_scorelist`，外鍵欄位 `cID_id`。這是不同命名的 SQL 範例，不能直接當作 P240 資料庫的可執行命令。
2. 第一例科目字串用了彎引號 `’`；第二例姓名的空白可能來自排版疏排，若真作字串會改變比對。上述先保留原稿，不能未核對就「修好」後執行。
3. 內連接只會選到有成績配對的學生；沒有成績的同名學生，不會由此 INNER JOIN 例子選中刪除。
4. ORM 的 `on_delete=models.CASCADE` 不等同於可以任意直接 SQL 多表刪除而不顧資料庫外鍵；還有 permissions 等關聯需考量。真實資料庫可能因外鍵約束阻擋，不能保證本 SQL 與 ORM 刪除完全相同。
5. 更新、刪除前應以相同 JOIN／WHERE 做只讀核對，確認範圍與備份；本次沒有連接或改動真實資料庫。

**原稿參考：**http://www.mysqltutorial.org/mysql-update-join/ 及 https://www.yiibai.com/mysql/update-join.html。

<a id="p253"></a>

### P253｜3-14 Cookies 與 Sessions：為什麼網站需要保存狀態

[核對原講義第 253 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=253)

[本頁原圖（含完整畫面細節）](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=253)

**原稿觀念：**使用者送出需求、伺服器處理並回傳頁面後，下一次取新資料仍需再送需求或重新載入。網站若要「記得」目前登入的會員，或購物車內尚未結帳的商品，就需要跨請求保存狀態的機制。

- Cookie：在使用者電腦／瀏覽器端保存資料。
- Session：原稿以在伺服器記憶體產生儲存空間來說明，讓網站記得登入資訊。
- 登入後，各頁讀取相應的 Cookie／Session 檢查並維持登入；離開或登出時清除相應狀態。

**示意圖片：**左邊電腦標示「客戶瀏覽器」，上方氣泡寫 Cookie；右邊機櫃標示「網站伺服器」，上方氣泡寫 Session；兩條相反方向的箭頭表示雙向請求／回應。圖的重點是存放位置不同，不是 Cookie 與 Session 完全互斥。

**建立環境的原稿命令：**

```sh
cd ~/dvds
source ./dvds/dvdsenv/bin/activate
django-admin startproject CookieSession
```

原稿註解分別為啟動虛擬環境、建立「project1」專案；實際命令名稱卻是 `CookieSession`。

**關於 Cookie：**Cookie 可識別使用者或保存相關資訊；講義以購物車為例，使用者中途離開甚至關閉瀏覽器後，下次回來仍可調出未結帳商品。它之所以能跨時間使用，還取決於是否設置適當的持續時間（續 P254）。

**原稿疑點與補充（與原稿敘述分開）：**

1. 原稿把每次回應後的「無狀態」描述為連線已結束。HTTP 無狀態指每個請求不自帶應用登入記憶，不等於底層 TCP／HTTP 連線必然立即關閉；持續連線不會自動解決登入狀態。
2. Session 不必只存記憶體；Django 可用資料庫、快取等儲存後端。Cookie 和 Session 常是搭配使用：Cookie 保存 session 識別值，伺服器用它找狀態。
3. 本頁 `source ./dvds/dvdsenv/bin/activate` 要以實際所在目錄核對，不能保證從 `~/dvds` 出發就一定存在這條相對路徑；不擅自改成其他環境名稱。
4. `startproject CookieSession` 旁的「project1」是原稿註解不一致。後面範例已出現 `CookieSessionApp`，但本頁沒有展示建立該 app 的命令，不把未展示步驟當作原稿。
5. Cookie 不應直接作為可信的「已登入」宣告，因為用戶端可修改；正式認證需要伺服器驗證。

<a id="p254"></a>

### P254｜Cookie 限制、Session 敘述與 set_cookie 基本參數

[核對原講義第 254 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=254)

[本頁原圖（含完整畫面細節）](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=254)

Cookie 在尚未過期且未被清除時可保留資訊，避免重複輸入；例如重新開啟會員頁面仍維持登入。講義列出的限制完整如下：

| 原稿項次 | 原稿所述限制 |
|---:|---|
| 1 | 每個瀏覽器最多儲存 300 個 Cookie |
| 2 | 對單一網站只能儲存 20 個 Cookie |
| 3 | 每個 Cookie 最多約 4k Bytes |
| 4 | 用戶端把 Cookie 關閉後便無法使用 |

**安全提醒（原稿）：**Cookie 放在使用者電腦，可被取得並不當利用，因此帳號密碼、信用卡卡號等機密資訊不適合直接存放其中。

**關於 Session（原稿說法）：**進入網站並開啟 Session 時記錄使用者資訊，描述為關閉瀏覽器便結束；原稿認為 Session 存在伺服器端較不易被利用，並寫即使瀏覽器停用 Cookie，Session 仍可正常運作。

**Cookie 的使用範圍：**可設定要保存的資料、有效時間、存放路徑與有效網域。基本 API 格式：

```python
set_cookie(key, value='', max_age=None, expires=None)
```

| 參數 | 講義說明 |
|---|---|
| key | 變數名稱／Cookie 名稱 |
| value | 值 |
| max_age | 持續時間，單位為秒 |
| expires | 到期時間（表格接 P255） |

**原稿疑點／補充：**

- 300／20 是講義列出的歷史式數量限制，不能當成所有瀏覽器固定不變的共同規範；4 KB 是常見單個 Cookie 容量級別，實際限制還要依瀏覽器實作，不能以此保證一定可存滿。
- 原稿第 4 點是「停用 Cookie 功能」，不是指一關閉瀏覽器所有 Cookie 都一定消失；有到期時間的持久 Cookie 可能仍保留。
- Session 的到期與是否在關閉瀏覽器後結束，取決於 Cookie 與伺服器的期限設定；不是一律關閉即刪伺服器資料。
- Django 一般用 Cookie 傳 Session ID；停用該 Cookie 後通常無法跨請求識別同一 Session。原稿「停用 Cookie 仍正常」不適合作 Django 預設行為，且與 P262 以 Cookie 傳 SessionID 的說明互相衝突。
- 伺服器端 Session 也不是絕對安全；Session ID 若被竊取仍可能導致會話劫持，需 HTTPS、Cookie 安全屬性等保護。

<a id="p255"></a>

### P255｜完整 Cookie API 圖片、UTC、讀取語法與路由

[核對原講義第 255 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=255)

[本頁原圖（含完整畫面細節）](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=255)

本頁先補上參數表的 `expires：到期時間`。文档截圖的完整簽名為：

```python
HttpResponse.set_cookie(
    key, value='', max_age=None, expires=None,
    path='/', domain=None, secure=False, httponly=False, samesite=None
)
```

**圖片英文文件逐項要義：**此方法設定 Cookie，參數與 Python 標準函式庫的 Morsel Cookie 物件相同。`max_age` 是整數秒；預設 None 表示只維持到瀏覽器會話結束。如果未指定 expires，會據其計算。`expires` 可以是格式 `Wdy, DD-Mon-YY HH:MM:SS GMT` 的字串，或 UTC 的 `datetime.datetime` 物件；若提供 datetime，則計算 max_age。圖中用紅框圈住 **UTC**。

| 完整簽名中其餘參數 | 補充解釋（圖中只列參數名，未逐項敘述） |
|---|---|
| path='/' | Cookie 適用 URL 路徑；`/` 表示全站路徑 |
| domain=None | 適用的網域範圍；未指定時為 host-only Cookie |
| secure=False | 若設 True，瀏覽器只在安全傳輸條件下傳送；正式 HTTPS 網站通常應啟用 |
| httponly=False | 若設 True，限制前端 JavaScript 透過 Cookie API 讀取；不能取代其他 XSS 防護 |
| samesite=None | 控制跨站請求的 Cookie 傳送政策；Python 的 None 與字串 `'None'` 不同，不能混同 |

UTC 是 Coordinated Universal Time（世界協調時間）；原稿說它在時刻上盡量接近格林威治標準時間。expires 的 HTTP 日期不可把任意本地時間直接標成 GMT。

**原稿兩個簡例（原樣保留其疑點）：**

```text
from django.http import HttpResponse
response = HttpResponse('TestCookie')
response.set_cookie(TestCookie,”這是cookie 內容”)

from django.http import HttpResponse
response = HttpResponse('TestCookie')
response.set_cookie(TestCookie,”這是cookie 內容”, max_age=3600)
```

第二段意圖是持續一小時，`max_age=3600`。原稿的 `TestCookie` 沒有引號，會被當變數；且值使用彎引號，不能直接當 Python 字串分隔符。**補充修正版示意**（不是無聲改寫原稿）：

```python
from django.http import HttpResponse
response = HttpResponse('TestCookie')
response.set_cookie('TestCookie', '這是cookie 內容', max_age=3600)
```

**讀取：**原稿寫 `Request.COOKIES[“名稱”]`；在下面 view 的實際參數名稱是小寫 `request`，所以通常以 `request.COOKIES['名稱']` 存取。大小寫是 Python 變數名稱的一部分，鍵不存在時直接索引會拋 KeyError。

**範例：儲存並顯示 Cookie 值。**編輯 `CookieSession/urls.py`，圖片紅框先匯入 app 的 views，再加路由：

```python
from django.contrib import admin
from django.urls import path
from CookieSessionApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('set_cookie/<str:key>/<str:value>', views.set_cookie),
]
```

`<str:key>`、`<str:value>` 把 URL 的兩段內容轉成字串傳給 view；範例路由尾端沒有 `/`，應照原樣辨識。頁末標示接著新增 view functions，完整內容在 P256。

<a id="p256"></a>

### P256｜set_cookie view 與 Chrome 開發人員工具驗證

[核對原講義第 256 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=256)

[本頁原圖（含完整畫面細節）](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=256)

編輯 `CookieSessionApp/views.py`。程式圖片的紅框圈出 HttpResponse 匯入；完整可见程式如下：

```python
from django.shortcuts import render
from django.http import HttpResponse

def set_cookie(request, key=None, value=None):
    # print(key)
    # print(value)
    # return HttpResponse("ok")
    response = HttpResponse('Cookie 儲存完畢!')
    response.set_cookie(key, value)
    return response
```

步驟是建立回應 → 在該回應上設定 Cookie → 回傳同一個 response。`request.COOKIES` 是本次收到的 Cookie；`response.set_cookie()` 是告訴瀏覽器接收回應後保存，所以不會直接改寫本次 request 物件。此例未設 max_age／expires，是會話 Cookie。

原稿測試命令：

```sh
sudo python3 manage.py runserver 0.0.0.0:8080
```

**圖片操作完整路徑：**

1. 在瀏覽器開範例網址，圖中為 `http://192.168.57.236:8080/set_cookie/aa/bb`；URL 紅框強調 aa 是 key、bb 是 value。
2. 頁面顯示「Cookie 儲存完畢!」。
3. 按 F12 開開發人員工具；第一張圖也展示右上角三點選單 →「更多工具」→「開發人員工具」，並標示快捷鍵 Ctrl+Shift+I。
4. 切到 **Application** 分頁（紅框），在左側 Storage 下展開 **Cookies**，選取目前網站 `http://192.168.57.236:8080`（紅框）。
5. 右側表格紅框看到 `Name=aa`、`Value=bb`；Path 為 `/`、Expires 欄顯示 Session。另有 `csrftoken` 是其他 Cookie，不要誤認為這個 view 只建立 aa 之外所有列。
6. 表格也提供 Domain、Path、Expires、Size、HttpOnly、Secure、SameSite、Priority 等欄，方便核對 Cookie 的作用範圍與安全屬性。

**補充／安全提醒：**`0.0.0.0` 是伺服器監聽所有網路介面，不是客戶端一般輸入的目標主機位址；圖中用的是該主機區網 IP。開發伺服器不應公開作正式服務。讓任意 URL 值直接設定任意 Cookie 名稱僅供練習，正式站應限制名稱、值與權限；URL 也會進入歷史／日誌，不要放密碼或敏感識別資訊。

<a id="p257"></a>

### P257｜取得單一 Cookie，處理不存在的鍵

[核對原講義第 257 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=257)

[本頁原圖（含完整畫面細節）](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=257)

編輯 `CookieSession/urls.py`，本頁圖片在原有設定 Cookie 路由旁新增讀取路由，紅框圈住 get_cookie：

```python
from django.contrib import admin
from django.urls import path
from CookieSessionApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('set_cookie/<str:key>/<str:value>', views.set_cookie),
    path('get_cookie/<str:key>', views.get_cookie),
]
```

編輯 `CookieSessionApp/views.py`，新增：

```python
def get_cookie(request, key=None):
    if key in request.COOKIES:
        return HttpResponse('%s : %s' % (key, request.COOKIES[key]))
    else:
        return HttpResponse('Cookie 不存在!')
```

`key in request.COOKIES` 先檢查鍵是否存在，避免不存在時直接索引觸發 KeyError；存在時回傳「鍵 : 值」，否則顯示錯誤提示文字。`HttpResponse` 的 import 沿用 P256。

**測試圖片：**使用 `sudo python3 manage.py runserver 0.0.0.0:8080`。

- `http://192.168.57.236:8080/get_cookie/aa` 顯示 `aa : bb`，承接 P256 已設定的 Cookie。
- `http://192.168.57.236:8080/get_cookie/cc` 顯示 `Cookie 不存在!`，測到未設定鍵的分支。

頁末引出 Cookie 字典：從 `request.COOKIES.items()` 可在迴圈中同時取得 key、value，完整程式續 P258。

**補充／安全提醒：**Cookie 值是用戶端輸入，不可信。原稿直接拼入 HttpResponse 的 HTML 內容，若值含 HTML 標記可能被瀏覽器解讀；正式顯示應使用自動跳脫模板、明確文字 Content-Type 或正確 escaping，不能把這個展示端點公開給不受信任輸入。

<a id="p258"></a>

### P258｜列出全部 Cookie 與會話 Cookie 有效期

[核對原講義第 258 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=258)

[本頁原圖（含完整畫面細節）](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=258)

**新增路由：**`CookieSession/urls.py` 的圖中保留 admin、set_cookie、get_cookie，新增帶尾端斜線的 `get_allcookies/`：

```python
from django.contrib import admin
from django.urls import path
from CookieSessionApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('set_cookie/<str:key>/<str:value>', views.set_cookie),
    path('get_cookie/<str:key>', views.get_cookie),
    path('get_allcookies/', views.get_allcookies),
]
```

**圖片中的完整 view：**

```python
def get_allcookies(request):
    if request.COOKIES != None:
        strcookies = ""
        for key1, value1 in request.COOKIES.items():
            strcookies = strcookies + key1 + ":" + value1 + "<br>"
        return HttpResponse('%s' % (strcookies))
    else:
        return HttpResponse('Cookie 不存在!')
```

逐行意義：先準備累積字串，用 `items()` 逐組解包 Cookie 名值，組成 `key:value<br>`；`<br>` 讓瀏覽器逐行顯示，最後一次回傳整個字串。

**測試圖片：**啟動命令仍為 `sudo python3 manage.py runserver 0.0.0.0:8080`；瀏覽 `http://192.168.57.236:8080/get_allcookies/`，畫面可見：

```text
t2:bill
csrftoken:（圖中有一長串 token）
counter:14
name:tony
```

圖片中的 csrftoken 是該瀏覽器當時的反 CSRF Cookie 值；需要理解這是任意 token 字串，不必把它當作固定值複製使用。畫面也證明「列出全部」會包含其他功能建立的 Cookie，並不只列這幾頁新增的 aa。

**原稿疑點／補充：**Django 的 `request.COOKIES` 一般是字典，沒有 Cookie 時通常是空字典 `{}`，並非 None。因此這個 `!= None` 檢查仍會進入第一分支，迴圈不執行後回傳空內容；不能保證出現「Cookie 不存在!」。若要判斷有沒有任何 Cookie，通常用字典真值測試；這是補充，不默改原稿。

**安全提醒：**此 view 將所有 Cookie 未經跳脫直接輸出 HTML，有 XSS 與敏感資訊暴露風險；HttpOnly 的 Cookie 雖不能被前端 JS 直接讀，但若伺服器把值回顯在頁面上，會破壞這項保護的目的。僅作本機教學觀察。

**有效時間（本頁原稿）：**關閉瀏覽器再打開，原本未設定期限的 Cookie 會消失，需要重新加入；若要保留，需設定持續時間。**補充限制：**瀏覽器的會話還原可能保留會話 Cookie，因此「關閉即消失」並非所有設定下都可保證；重點是區別會話 Cookie 與明確設期限的持久 Cookie。

<a id="p259"></a>

### P259｜max_age、明日零時 expires、刪除 Cookie 與新增路由

[核對原講義第 259 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=259)

[本頁原圖（含完整畫面細節）](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=259)

**一小時持續時間：**原稿採彎引號排版；以下標為排版引號轉成 ASCII 的同義抄錄，不更動字串值或參數：

```python
response.set_cookie("TestCookie", "內容", max_age=3600)
```

**設定到期時間：**原稿先取現在加一天，將時分秒改為零，再格式化 GMT 字串：

```python
tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
tomorrow = datetime.datetime.replace(tomorrow, hour=0, minute=0, second=0)
expires = datetime.datetime.strftime(tomorrow, "%a, %d-%b-%Y %H:%M:%S GMT")
response.set_cookie("counter", counter, expires=expires)
```

- `timedelta(days=1)` 用來取下一日；`replace(...)` 把時分秒歸零，意圖為隔日零時。
- `%a` 是星期縮寫、`%d` 日、`%b` 月縮寫、`%Y` 四位年、`%H:%M:%S` 時分秒，尾端加 GMT。
- 這是一段片段，`datetime` 與 `counter` 必須由其他程式先準備；完整計數器例見 P261。

**原稿疑點：**`datetime.datetime.now()` 是未指定時區的本地時間，最後只加 GMT 字樣並不會做 UTC 轉換；若主機本地時間不是 UTC，到期時刻會偏差。另 `replace` 沒把 microsecond 歸零，雖此處格式化省略微秒，仍應明白它是格式化後才不顯示。星期／月份縮寫亦受執行環境 locale 影響，不能假設一定符合英文 HTTP 日期。

**刪除 Cookie：**原稿概括語法寫 `delete_cookie[名稱]`，但實際範例使用的是方法呼叫小括號：

```python
from django.http import HttpResponse
response = HttpResponse('Delete Cookie')
response.delete_cookie('TestCookie')
```

**原稿疑點：**`delete_cookie[名稱]` 不能當正確 Python 呼叫，應以此頁示例的 `response.delete_cookie(...)` 為準。刪除也是透過回應告知瀏覽器過期，view 仍需回傳 response；若原 Cookie 有特定 path／domain，刪除時需匹配，否則不一定刪到同一 Cookie。

**範例：設定 Cookie 持續時間。**`CookieSession/urls.py` 截圖增加 `set_cookie2`、`delete_cookie`，本頁完整可見設定如下（此張圖未列前頁 get_allcookies）：

```python
from django.contrib import admin
from django.urls import path
from CookieSessionApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('set_cookie/<str:key>/<str:value>', views.set_cookie),
    path('get_cookie/<str:key>', views.get_cookie),
    path('set_cookie2/<str:key>/<str:value>', views.set_cookie2),
    path('delete_cookie/<str:key>', views.delete_cookie),
]
```

紅框圈住最後兩條路由。頁末指示編輯 `CookieSessionApp/views.py`，程式本體在 P260。

<a id="p260"></a>

### P260｜一小時 Cookie view、delete_cookie view 與測試不一致處

[核對原講義第 260 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=260)

[本頁原圖（含完整畫面細節）](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=260)

**圖片完整程式：**

```python
def set_cookie2(request, key=None, value=None):
    response = HttpResponse('Cookie 有效時間1小時!')
    response.set_cookie(key, value, max_age=3600)
    return response


def delete_cookie(request, key=None):
    if key in request.COOKIES:
        response = HttpResponse('Delete Cookie: ' + key)
        response.delete_cookie(key)
        return response
    else:
        return HttpResponse('No cookies:' + key)
```

第一個 view 與 P256 最大差別是 `max_age=3600`。第二個 view 先檢查本次請求是否帶有該 Cookie；若存在，設定刪除回應並回傳，否則只回覆找不到。

**圖片測試步驟：**

1. 用 `sudo python3 manage.py runserver 0.0.0.0:8080` 啟動。
2. 開 `http://192.168.57.236:8080/set_cookie2/name/tony`，網頁顯示「Cookie 有效時間1小時!」。Application 的 Cookies 表出現 `name=tony`，Expires 不再顯示 Session，而是具體時間。圖中另有 counter=14、t2=bill、csrftoken 等既存列。
3. 開 `http://192.168.57.236:8080/get_cookie/name`，畫面顯示 `name : tony`。
4. 原稿接著說關閉瀏覽器、再開此頁，Cookie 的 name 仍在，用來驗證設定持續時間後能跨瀏覽器重新開啟保留。
5. 最下圖在 Application → Cookies → 該站台以紅框圈出 `name=tony`，但網址列實際是 `/delete_cookie/name`，左側內容卻仍是 `name : tony`。

**重要原稿疑點：**最後一張圖的刪除 URL、頁面讀取結果與 Cookie 仍存在互相矛盾。依本頁 delete_cookie view，真正執行刪除應回應 `Delete Cookie: name`，並要求瀏覽器清除該 Cookie；此圖不能拿來證明已成功刪除，也不能自行宣稱作者操作一定已完成。它可能是尚未送出新網址或畫面時間點不同，原因原稿未提供。

**補充／安全提醒：**兩個 view 都是可改狀態的示範，不宜在正式系統透過無驗證 GET 任意設定／刪除敏感 Cookie。`key=None` 的預設值若在非路由呼叫中真的為 None，`'No cookies:' + key` 還會有型別問題；正常此路由要求 `<str:key>` 因而會傳字串。

<a id="p261"></a>

### P261｜Cookie 刪除確認圖與每日瀏覽次數計數器

[核對原講義第 261 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=261)

[本頁原圖（含完整畫面細節）](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=261)

**頁首承接 P260 的刪除結果：**瀏覽器網址 `http://192.168.57.236:8080/delete_cookie/name`，這次左側確實顯示 `Delete Cookie: name`。Application → Cookies 的表格中只看到 csrftoken，name 列已不在。這是原稿真正呈現的刪除後畫面，與 P260 末圖的狀態不同；可以用前後圖辨識「輸入網址」與「真正收到刪除回應」的差別，但原稿未交代中間時間點。

**新範例：顯示使用者今天瀏覽本頁面的次數。**`CookieSession/urls.py` 圖中仍匯入 admin、path、`CookieSessionApp.views`，並在 urlpatterns 新增以下兩列：

```python
path('', views.index),
path('index/', views.index),
```

根路徑與 `/index/` 都交給同一 view，會共用同名 counter Cookie。

**`CookieSessionApp/views.py` 圖片完整程式：**

```python
import datetime

def index(request):
    if "counter" in request.COOKIES:
        counter = int(request.COOKIES["counter"])
        counter += 1
    else:
        counter = 1
    response = HttpResponse('今日瀏覽次數：' + str(counter))
    tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
    tomorrow = datetime.datetime.replace(tomorrow, hour=0, minute=0, second=0)
    expires = datetime.datetime.strftime(tomorrow, "%a, %d-%b-%Y %H:%M:%S GMT")
    response.set_cookie("counter", counter, expires=expires)
    return response
```

`HttpResponse` 沿用前頁 import。程式流程：

1. 有 counter 就把 Cookie 字串轉整數，加一；沒有則從 1 開始。
2. 以最新 counter 建立「今日瀏覽次數」回應文字。
3. 取明天的日期、把時分秒設零，格式化 expires。
4. 把更新後計數回寫成 counter Cookie，並回傳 response。
5. 期限到後瀏覽器不再傳回該 Cookie，下次走初始值分支。原稿意圖是在一天結束時歸零，不是每次造訪後延長一整天。

測試仍執行：

```sh
sudo python3 manage.py runserver 0.0.0.0:8080
```

結果圖片續 P262。

**原稿疑點／補充：**此計數只是特定瀏覽器的可修改 Cookie，不是可信全站統計、獨立訪客數或安全限流依據。使用者可刪除／修改 counter；非整数字串會使 `int()` 拋 ValueError；並行請求也可能覆寫同一計數。日期程式仍有 P259 的本地時間冒充 GMT 問題，因此「今日」須先定義時區，不能保證所有主機都在預期的本地午夜歸零。此處保留原例、未將之偽裝成健全的正式計數器。

<a id="p262"></a>

### P262｜計數器測試、Session ID 原理與啟用設定

[核對原講義第 262 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=262)

[本頁原圖（含完整畫面細節）](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=262)

**頁首兩張圖片承接 P261：**

- 瀏覽 `http://192.168.57.236:8080`，頁面顯示「今日瀏覽次數：14」。
- 開啟 Application → Cookies，`counter` 的 Value 是 `14`，同時可見 `t1=bill` 與 csrftoken。counter 有具體到期時間而非 Session；圖中滑鼠提示顯示午夜附近的 UTC 時間字串，說明 expires 已寫入瀏覽器。這是原稿截圖，不是本次實際執行計數器的結果。

**Session 的使用（原稿）：**Session 是瀏覽者與伺服器工作期間維持的狀態；進入啟用 Session 機制的網站後開始使用，尚未到期時再次回到網站仍然有效。

**紅字運作原理：**原稿說網站派發 SessionID，網站程式依此區分使用者並處理各自保存的狀態；在預設狀態下，把 SessionID「加密處理後」用 Cookie 保存於用戶端，同站不同頁面透過同一 Cookie 維持同一 SessionID。

**安裝／啟用 Session app：**編輯原稿路徑 `CookieSession/CookieSession/settings.py`。圖片的第一個紅框是 `INSTALLED_APPS` 中的 sessions：

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'CookieSessionApp',
]
```

第二個紅框是中介軟體的 SessionMiddleware。圖片可見列表前四項如下；原稿截圖在 CsrfViewMiddleware 這一行結束，未展示全部後續項目，這是**節錄**，不是要求以四項覆蓋完整 MIDDLEWARE：

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # 圖片下緣截斷，後續既有項目未展示
]
```

SessionMiddleware 負責在請求／回應流程掛載與處理 Session；僅把 app 加到 INSTALLED_APPS 並不代表能忽略 middleware。

**存取資料：**頁末原稿寫「使用 request 物件的 sesson() 函式，以字典方式存取 session 資料」。

**原稿疑點／補充（不冒充原頁續文）：**

1. `sesson()` 是拼字／API 描述錯誤；Django 常用的是 `request.session`，以類字典方式存取，而不是呼叫 `request.sesson()`。示意為 `request.session['key'] = value`、`request.session.get('key')`；具體 Session 讀寫範例不在這次 P238–P262 範圍內，不延伸抄錄後頁。
2. 「SessionID 加密後存在 Cookie」不精確：常見伺服器端 Session 後端的 Cookie 保存不透明識別鍵，並不是每次都先把 Session ID 加密。若改用 signed-cookie 後端，資料的簽署也不等於加密，不能把它描述為客戶端看不到內容。
3. 不一定每個純讀網頁請求都立刻建立、儲存新 Session；Session 是否建立與更新、後端及設定有關。Cookie 只作識別值時，真正狀態保存在伺服器所選後端。
4. 圖中沒有展示 `migrate` 或資料表建立步驟；若採 Django 資料庫 Session 後端，仍要確保相應遷移已套用。此為補充前提，不是原圖已有命令。
5. P254 說停用 Cookie 仍可使用 Session，與這頁以 Cookie 維持 SessionID 的機制矛盾；預設 Django 會話識別通常依賴 Cookie。



---

## P263–P286｜Session、使用者驗證與會員註冊（逐頁完整知識筆記）

> 來源：指定講義 PDF 第 263–286 頁，對照文字層及每頁圖片。程式碼由圖片辨識整理，**未執行講義專案**；畫面結果皆為「講義展示」，不是本次測試。原稿錯字、版本差異及安全補充另列，不偷偷改寫原碼。截圖 IP、帳密只是課堂示例。

<a id="p263"></a>

### P263｜以 Session 儲存與讀取資料

[核對原講義第 263 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=263)

- 寫入：`request.session[名稱] = 值`；讀取：`變數 = request.session[名稱]`。Session 提供類字典存取介面。
- 專案路由檔：`sudo vim CookieSession/urls.py`。圖中匯入 `from django.contrib import admin`、`from django.urls import path`、`from CookieSessionApp import views`，新增：
  ```python
  path('set_session/<str:key>/<str:value>', views.set_session),
  path('get_session/', views.get_session),
  ```
  `str` 轉換器把 URL 的 `key`、`value` 當字串傳給 view；寫入路由沒有結尾斜線。
- view 檔：`sudo vim CookieSessionApp/views.py`，圖片程式：
  ```python
  def set_session(request, key=None, value=None):
      response = HttpResponse('Session 儲存完畢!')
      request.session[key] = value
      return response

  def get_session(request, key=None):
      if key in request.session:
          return HttpResponse('%s : %s' % (key, request.session[key]))
      else:
          return HttpResponse('Session 不存在!')
  ```
  `key=None`、`value=None` 是 Python 預設引數；存在測試避免直接讀取不存在的 key。`HttpResponse` 是 HTTP 回應，Session 寫入由 Django 的 session 機制處理，而非把資料附加在該回應字串。
- 啟動命令：`sudo python3 manage.py runserver 0.0.0.0:8080`。圖中實際瀏覽 `192.168.57.236:8080/set_session/who/student`，文字顯示「Session 儲存完畢!」。Chrome 開發者工具開啟 **Application → Cookies**，可見 `counter`、`sessionid`、`csrftoken`，紅框標記 URL，藍色選取 `sessionid` 列。`who=student` 不以同名 cookie 明文列出。
- **原稿疑點**：本頁的 `get_session/` 未捕捉 `key`，會沿用 `None`；下一頁改成 `get_session/<str:key>`，才吻合 `/get_session/who` 的結果。
- **補充／安全**：GET URL 寫入狀態是教學捷徑；正式系統應使用適當的 POST、CSRF 防護及授權。不要使用開發伺服器公開部署，也不需一律用 `sudo` 啟動。這些改善不是原稿已實作的功能。

<a id="p264"></a>

### P264｜sessionid Cookie 與列出 Session 字典

[核對原講義第 264 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=264)

- 原稿說明：伺服器派發 SessionID，以名為 `sessionid` 的 Cookie 存於用戶端，內容為編碼字串；原文使用「加密處理」一詞。
- 上方結果圖：瀏覽 `/get_session/who`，顯示 `who : student`，驗證前頁儲存的 key/value 可於後續請求讀取。
- 路由檔仍為 `CookieSession/urls.py`，圖片完整三條路由：
  ```python
  path('set_session/<str:key>/<str:value>', views.set_session),
  path('get_session/<str:key>', views.get_session),
  path('get_allsessions/', views.get_allsessions),
  ```
  新增 `get_allsessions/` 以紅框指出；同時看得出 `get_session` 已加入 key 參數。
- 原稿把 Session 稱作字典，使用 `request.session.items()` 逐項取得 key/value。`CookieSessionApp/views.py`：
  ```python
  def get_allsessions(request):
      if request.session != None:
          strsessions = ""
          for key1, value1 in request.session.items():
              strsessions = strsessions + key1 + ":" + str(value1) + "<br>"
          return HttpResponse(strsessions)
      else:
          return HttpResponse('Session 不存在!')
  ```
  `str(value1)` 使數字、布林等值可串接；`<br>` 讓各項分行；結果續於 P265。
- **原稿疑點與補充**：Session 是類字典的 session store，不等於純 `dict`；`request.session != None` 不是判斷「有沒有內容」的可靠方式，空 session 仍通常有 store 物件，因此可能回傳空字串。一般伺服器端 session 的 cookie 是不透明 session key，不宜將「編碼」直接等同「加密」；不同 session backend 的儲存方式不同。此處未據此改寫原文。
- **安全補充**：列印全部 Session 可能外洩登入資訊；原碼以未轉義字串組 HTML，若 key/value 可受使用者控制也有 HTML 注入風險，實務宜用模板自動轉義，並避免提供公開的 session 檢視端點。

<a id="p265"></a>

### P265｜Session 全項目結果與簡易防重複投票

[核對原講義第 265 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=265)

- 頁首承 P264，使用相同 `runserver 0.0.0.0:8080` 命令。瀏覽 `/get_allsessions/` 的截圖分兩行呈現 `who:student`、`cat:coco`；這是圖片額外提供的第二組 Session 資料。
- 防灌票概念：在同一 Session 記住已投票；重整或重新開啟瀏覽器時，只要原 Session 仍有效，不持續累加。此頁程式沒有票數資料庫，只示範記號與提示。
- `CookieSession/urls.py` 加入 `path('vote/', views.vote),`；`CookieSessionApp/views.py`：
  ```python
  def vote(request):
      if not "vote" in request.session:
          request.session["vote"] = True
          msg = "您第一次投票!"
      else:
          msg = "您已投過票!"
      response = HttpResponse(msg)
      return response
  ```
  檢查的是 `vote` 鍵是否存在，不是其值是否為 `True`；第一次存入布林 `True`，後續走 else。
- 圖中紅框延續標示 `from CookieSessionApp import views`；新 URL 對應 `views.vote`，而非在模板執行判斷。測試命令仍為 `sudo python3 manage.py runserver 0.0.0.0:8080`。
- **安全補充**：Session 只能阻擋同一有效 Session 的重複操作，清除 cookie、換瀏覽器或到期後可取得新 Session，不能單獨保證「一人一票」。正式投票需帳號／資格驗證、資料庫唯一限制、並行安全與 POST/CSRF。

<a id="p266"></a>

### P266｜Session 有效時間、Cookie 壽命與刪除語法

[核對原講義第 266 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=266)

- 頁首兩張 `/vote/` 瀏覽器截圖分別顯示「您第一次投票!」、「您已投過票!」，具體展示前頁 if/else 的分支。
- 設定表逐項：
  | 設定 | 原稿意義 | 原稿預設值 |
  |---|---|---|
  | `SESSION_EXPIRE_AT_BROWSER_CLOSE` | 是否於瀏覽器關閉時結束 Session；`True` 表示關閉後結束 | `False` |
  | `SESSION_COOKIE_AGE` | Session Cookie 的有效時間，單位為秒 | `1209600` 秒，即兩週 |
- 原稿提醒：**先刪除 Cookie 才測試設定效果**。範例：`SESSION_EXPIRE_AT_BROWSER_CLOSE=True`；`SESSION_COOKIE_AGE=1440`，標示為 24 分鐘。
- 逐一 Session 的期限範例原文是「設定 Session 持續時間為 5 分」配 `Request.session.set_expiry(50*60)`。
- 刪除指定項目的原稿：`del request.session[名稱]`；刪除所有 Session 的原稿：`del request.clear()`。頁末開始「設定 Session 持續時間」範例，程式在 P267。
- **原稿疑點（不默改）**：`50*60` 實際為 3000 秒、50 分鐘，不是 5 分鐘；5 分鐘應是 `5*60`（300 秒）。`Request` 大寫與一般 view 參數 `request` 不符。`del request.clear()` 既不是正確 Session API，也不能用 `del` 刪除函式呼叫結果；清除內容應討論 `request.session.clear()`，完整失效可用 `request.session.flush()`，兩者目的不同。以上數值換算已用 Python 核對，並非執行 Django 範例。
- **補充**：`set_expiry()` 設定的是整個 Session 的期限，不是只替某一 key 設 TTL；瀏覽器工作階段恢復功能也會影響「關閉即結束」的實際觀察。清除字典內容與刪除 session key/cookie 不應混為一談。

<a id="p267"></a>

### P267｜30 秒 Session 與指定 key 刪除 view

[核對原講義第 267 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=267)

- 路由檔 `CookieSession/urls.py`，仍匯入 `CookieSessionApp.views`：
  ```python
  path('set_session2/<str:key>/<str:value>', views.set_session2),
  path('delete_session/<str:key>', views.delete_session),
  ```
- 原稿 view 編輯路徑寫 `CookieSessionAPP/views.py`（與前文 `CookieSessionApp` 大小寫不同）。圖片程式：
  ```python
  def set_session2(request, key=None, value=None):
      response = HttpResponse('Session 儲存完畢!')
      request.session[key] = value
      request.session.set_expiry(30)  # 設持續的時間為30秒
      return response

  def delete_session(request, key=None):
      if key in request.session:
          response = HttpResponse('Delete Session: ' + key)
          del request.session[key]
          return response
      else:
          return HttpResponse('No Session:' + key)
  ```
- `set_session2` 在寫入後設 30 秒期限；`delete_session` 先確認 key 存在，才執行 `del`，不存在則回應 `No Session:`。URL 保證傳入字串 key；若繞過路由以預設 `None` 呼叫，字串串接不一定成立。
- 測試命令：`sudo python3 manage.py runserver 0.0.0.0:8080`。截圖使用 `127.0.0.1:8080/set_session2/mysession/cat`，回應「Session 儲存完畢!」，因此儲存的是 `mysession → cat`。
- **原稿疑點／安全補充**：Linux 路徑大小寫有別，`APP` 與 `App` 應以實際專案目錄為準；圖片並未交代重新命名。刪除狀態的 GET 端點也只是示範，不是安全的正式介面。

<a id="p268"></a>

### P268｜期限前後與新增再刪除的完整畫面序列

[核對原講義第 268 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=268)

本頁沒有新增程式，主要資訊全在五張瀏覽器截圖：

1. `/get_session/mysession` 顯示 `mysession : cat`：承接 P267 的 30 秒 Session，期限內可讀取。
2. 「30 秒後就自動消失」下方同一 URL 顯示「Session 不存在!」：到期後再請求，進入缺少 key 的分支；不是網頁上的既有文字會自行計時變更。
3. 原文「新增一個 seesion，再將 seesion 刪除」：瀏覽 `/set_session/name/bill`，回應「Session 儲存完畢!」。`seesion` 為原文拼字。
4. `/get_allsessions/` 顯示 `name:bill`，確認剛新增的 key/value。
5. `/delete_session/name` 顯示 `Delete Session: name`，對應前頁刪除函式。

- 圖片主機均為 `127.0.0.1:8080`；新增 `name` 用的是原本的 `set_session`，不是另行呼叫 30 秒版本 `set_session2`。
- 刪除後再次列出全部 Session 的畫面在 P269 頁首；不要把本頁的回應字串單獨當成資料庫刪除驗證。

<a id="p269"></a>

### P269｜手動 Session 會員登入

[核對原講義第 269 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=269)

- 頁首承接刪除示例：`/get_allsessions/` 的瀏覽器內容區空白，對應 session store 仍存在、但無項目可串接的情形。
- 本頁尚未使用 Django Auth；只是手動用 `username` Session 鍵維持登入狀態。`CookieSession/urls.py`：
  ```python
  path('login/', views.login),
  path('logout/', views.logout),
  ```
- view 的文字路徑為 `CookieSessionAPP/views.py`。圖片程式整理如下：
  ```python
  def login(request):
      # 預設帳號密碼
      username = "tony"
      password = "1234"
      if request.method == 'POST':
          if not 'username' in request.session:
              if request.POST['username'] == username and request.POST['password'] == password:
                  request.session['username'] = username  # 儲存Session
                  message = username + " 您好，登入成功！"
                  status = "login"
              else:
                  message = "密碼或帳號錯誤"
      else:
          if 'username' in request.session:
              if request.session['username'] == username:
                  message = request.session['username'] + " 您已登入過了！"
                  status = "login"
      return render(request, 'login.html', locals())
  ```
- 流程逐項：POST 先檢查 Session 無 `username` 才比對帳密；成功存 Session、設 `message` 與 `status='login'`；失敗只設錯誤訊息。非 POST 時，若 Session 中已有指定使用者，顯示已登入提示。`render()` 把本地變數交給 `login.html`。
- **原稿缺口**：P269–270 未展示這個手動 Session 版本的 `login.html` 原始碼，只有輸出畫面，故不能假造其條件、CSRF token 或表單 action。若 POST 時已有 `username`，原碼没有指定新的 `status/message`；變數也非所有分支均初始化。
- **安全補充**：硬編碼 `tony/1234` 僅供示例，不能用作正式憑證管理；`locals()` 會把本地 `password` 也傳進模板 context，宜明確列出允許輸出的 context。直接比較明文、缺少驗證限速、未輪替 session key，均不應取代 Django Auth。

<a id="p270"></a>

### P270｜手動 Session 登出與四種登入畫面

[核對原講義第 270 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=270)

- 延續 `views.py` 的 `logout`：
  ```python
  def logout(request):
      if 'username' in request.session:
          message = request.session['username'] + ' 您已登出!'
          del request.session['username']  # 刪除Session
      return render(request, 'login.html', locals())
  ```
  實際刪除的是 Session 裡的 `username` 項目，並不是清除全部 Session。未登入時不建立 `message`，仍渲染同一模板。
- 測試命令：`sudo python3 manage.py runserver 0.0.0.0:8080`。
- 圖片四種狀態：
  1. 帳號／密碼與「登入」按鈕；帳號欄已填 `tony`，密碼以圓點遮蔽，URL 是 `/logout/`。
  2. `/login/` 保留表單，下方紅字「密碼或帳號錯誤」。
  3. `/login/` 成功時，表單改成「登出系統」連結，下方紅字 `tony 您好，登入成功！`。
  4. `/logout/` 再度顯示空白登入表單，紅字 `tony 您已登出!`。
- 由畫面能確定模板會切換登入與登出介面、用紅字呈現訊息；不能由截圖證明密碼安全儲存或伺服器端授權已完整實作。

<a id="p271"></a>

### P271｜3-15 使用者管理：內建 Auth 與查詢使用者路由

[核對原講義第 271 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=271)

- `django.contrib` 的 `auth` 應用程式提供內建使用者模型／資料表，可儲存使用者資訊。原稿以 `is_authenticated` 區分：User 為 true、AnonymousUser 為 false。
- 登入函式接受 `request`、`user`；成功後藉 Session 跨頁維持狀態；登出清除原 Session。原文誤拼 `auth.lgoin()`，正確名稱在後頁是 `auth.login()`。
- 建立環境的原稿命令（保留相對路徑）：
  ```bash
  cd ~/dvds
  source ./dvds/dvdsenv/bin/activate
  django-admin startproject login
  ```
  說明分別為切換目錄、啟動虛擬環境、建立 `login` 專案。**疑點**：已 `cd ~/dvds` 後再用 `./dvds/...`，是否真的存在該層巢狀目錄需自行確認；此頁未列 `startapp loginapp` 或 migration 步驟。
- 讀取 Auth User：使用 model manager 的 `objects.get()` 取單筆、`objects.all()` 取全部；接著做「輸入會員姓名，判斷是否為使用者用戶」示例，但實際路由參數及下頁查詢欄位是 username。
- `sudo vim login/urls.py`，圖中：
  ```python
  from django.contrib import admin
  from django.urls import path
  from loginapp import views

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('search_name/<str:name>', views.search_name),
  ]
  ```
- 下一檔是 `sudo vim loginapp/views.py`，具體程式續於 P272。檔案關係：專案的 `urls.py` 收請求 → `loginapp.views.search_name` → Auth 的 User 模型 → `HttpResponse`，不需模板即可回覆查詢結果。
- **補充**：只有「User 實體」並不證明目前 HTTP 請求已登入；判斷應使用經 AuthenticationMiddleware 建立的 `request.user.is_authenticated`。原文是入門簡化敘述。

<a id="p272"></a>

### P272｜查詢 User 的 view、查詢畫面與 request.user

[核對原講義第 272 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=272)

- `loginapp/views.py` 圖片完整內容：
  ```python
  from django.shortcuts import render
  from django.contrib.auth.models import User
  from django.http import HttpResponse

  def search_name(request, name=None):
      try:
          # print(name)
          user = User.objects.get(username=name)
          # print(dir(user))
          print(user.username)
          print(user.email)
          return HttpResponse('存在')
      except:
          return HttpResponse('不存在!')
  ```
  註解的 `print(name)` 用來看 URL 參數；`dir(user)` 可探索物件屬性；實際兩個 `print` 輸出到伺服器終端，不是瀏覽器。查詢 `username` 成功才回「存在」。
- 測試命令同前。兩張圖分別為 `/search_name/t01` →「存在」，`/search_name/aaa` →「不存在!」。這是講義當時資料庫的內容，不代表本次環境有這些帳號。
- `HttpRequest.user`：原稿說明請求的 `user` 屬性可取得具名 User 或匿名 AnonymousUser，用來判斷登入。圖中條件：
  ```python
  if request.user.is_authenticated:
      ...  # Do something for logged-in users.
  else:
      ...  # Do something for anonymous users.
  ```
- **補充／疑點**：裸 `except:` 會把資料庫故障等全部變成「不存在」，宜只捕捉 `User.DoesNotExist`。公開查詢介面會洩漏帳號存在與否；終端列出 email 也有個資紀錄風險。自訂 User 專案不要照搬固定 `django.contrib.auth.models.User`，應依可替換模型機制取得 User（後頁介紹）。

<a id="p273"></a>

### P273｜User 常用屬性與方法逐項對照

[核對原講義第 273 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=273)

原稿屬性表完整列出下列項目：

| 屬性 | 講義說明與使用意義 |
|---|---|
| `username` | 使用者帳號；原稿說由字母、數字、底線組成。 |
| `is_anonymous` | User 永遠為 `False`；AnonymousUser 永遠為 `True`，用來辨別匿名身份。 |
| `is_authenticated` | User 永遠為 `True`；AnonymousUser 永遠為 `False`。應從 `request.user` 判斷請求登入狀態，不能拿任意查到的 User 當成驗證成功。 |
| `first_name` | 名字。 |
| `last_name` | 姓氏。 |
| `email` | 電子郵箱。 |
| `password` | 原稿稱「加密（經編碼）過後的密碼」；不能直接與使用者輸入的明文比較。 |
| `is_staff` | 布林值；原稿說 True 可以登入 admin 後端。不是所有模型權限的保證。 |
| `is_active` | 布林值；原稿說 True 可登入，False 表示帳號停用。 |
| `is_superuser` | 布林值；原稿說 True 擁有全權限。 |
| `last_login` | 上一次登入的日期與時間。 |
| `date_joined` | 建立帳號的日期與時間。 |

- 原稿特別提醒：`is_active=False` 時，預設 `auth.authenticate()` 即使帳密正確仍回 `None`；不再使用的帳號建議停用，不直接刪除，以保留關聯紀錄。

| 方法 | 引數、結果與注意事項 |
|---|---|
| `get_username()` | 不需額外引數，取得帳號。 |
| `get_full_name()` | 取得完整姓名。 |
| `get_short_name()` | 只取得名字。 |
| `set_password(password)` | 把輸入密碼按密碼儲存機制編碼／雜湊；**不包含 User 物件存檔**，還需 `user.save()`。 |
| `check_password(password)` | 驗證輸入密碼，正確回 `True`；由框架使用相同的密碼驗證機制處理，不是直接明文字串比較。 |

- **精確性補充，與原稿分開**：Django password 應稱帶演算法參數與鹽值的密碼雜湊格式，非可逆「加密」。username 可接受字元由 User 模型及 validator 決定，原稿列舉非完整規格。admin 通常同時要求 active/staff；active/superuser 對驗證及權限的效果亦取決於 backend，不宜把布林欄位看成所有設定下的通用保證。
- **API 年代註記**：本頁圖片使用 `is_authenticated`、`is_anonymous` 屬性形式（不加括號），屬於較新於舊式方法呼叫的寫法；請不要把舊教學 `is_authenticated()` 暗混進這份原碼。講義未註明 Django 精確版本。

<a id="p274"></a>

### P274｜create_user 新增帳號、設定屬性與導向 admin

[核對原講義第 274 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=274)

- `login/urls.py` 圖中除 `admin/`、`search_name/<str:name>` 外，有 `path('index/', views.index),`，紅框新增 `path('adduser/', views.adduser),`。
- `loginapp/views.py` 新增匯入 `from django.shortcuts import redirect`，程式：
  ```python
  def adduser(request):
      try:
          user = User.objects.get(username="test1")
      except:
          user = None

      if user != None:
          message = user.username + " 帳號已建立!"
          return HttpResponse(message)
      else:  # 建立 test 帳號
          user = User.objects.create_user("test1", "test1@test.com.tw", "aa123456")
          user.first_name = "wen"  # 姓名
          user.last_name = "lin"   # 姓氏
          user.is_staff = True     # 工作人員狀態
          user.save()
          return redirect('/admin/')
  ```
- `create_user()` 三個位置引數依序為 username、email、password；透過 manager 建立 User，會依框架規則處理密碼。後續指定 first/last name 及 staff，再 `save()` 保存更動。成功後是 redirect，瀏覽器發出新請求至 `/admin/`；不是直接渲染 admin 模板。
- 圖中文字的測試命令為 `sudo python3 manage.py runserver 0.0.0.0:8080`，並寫「登入 `127.0.0.1:8080/useradd/`」。
- **原稿疑點**：路由及函式皆為 `adduser`，但操作文字倒寫成 `useradd/`；應辨別，不直接視為可用路徑。`views.index` 的實作在 P276。此處 `except:` 過廣，查無與連線錯誤混為一談；先查再建也未處理同時請求的競爭。
- **安全補充**：公開 GET 即建立固定密碼的 staff 帳號非常危險；實務需授權、POST/CSRF、使用者輸入驗證及安全密碼規則。`is_staff=True` 不等於已授予管理所有資料表的權限。

<a id="p275"></a>

### P275｜新增使用者畫面、authenticate 與 login 的差別

[核對原講義第 275 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=275)

- 頁首 admin 使用者清單截圖顯示 `root`、`t01`、`test`、`test1`、`test2`；紅框實際圈在 `test2` 一列，並非上一頁程式的 `test1`。清單有電子郵件、名字、姓氏與狀態圖示；`test1/test2` 圖中皆可見 `wen`、`lin`。**疑點**：截图可能來自不同示範操作，不應推論前頁同一段程式會建立 test2。
- 「再重新整理」的 `/adduser/` 圖顯示 `test1 帳號已建立!`，對應查到使用者後不再建立的分支。
- 驗證：`user = auth.authenticate(username=帳號, password='密碼')`。成功回傳 User；密碼錯誤／帳號無效時回 `None`；預設 backend 對 `is_active=False` 亦拒絕。
- 圖片中的 API 說明有 `authenticate(request=None, **credentials)`：`request` 是可選的 HttpRequest，可傳至驗證 backend；`username`、`password` 是 credentials，框架交由驗證 backend 檢查。有效則回 User，未被 backend 驗證或 backend 拒絕（圖文提及 `PermissionDenied`）則回 `None`。
- 文件截圖示例：
  ```python
  from django.contrib.auth import authenticate
  user = authenticate(username='john', password='secret')
  if user is not None:
      # A backend authenticated the credentials
      ...
  else:
      # No backend authenticated the credentials
      ...
  ```
  此處 `...` 是筆記為了顯示分支所加的佔位，不是講義已提供的業務實作；原圖片分支內只有說明註解。
- 登入另用 `auth.login(request, user)`：`authenticate` 負責驗證，`login` 才把成功身份記到 Session 供後續請求使用，兩者不可混淆。

<a id="p276"></a>

### P276｜Auth Session、登入／登出路由及首頁 view

[核對原講義第 276 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=276)

- 原文說登入後產生 Session，使登入者跨頁保持狀態，登出再清除。示意原文為：
  ```text
  If user.is_active:
      auth.login(request, user)
  ```
  **原稿疑點**：Python 關鍵字應是小寫 `if`；呼叫前須先排除 `user is None`。此外登入狀態也可能因到期、伺服器清除等原因失效，不是只會在主動登出時結束。
- 登出：`auth.logout(request)`；文字先以 `auth.logout()` 泛稱，具體呼叫仍需 request。與 P270 手動只刪 `username` 不同，Auth 會清理整個目前 Session。
- `login/urls.py` 圖中路由保留 `admin/`、`search_name/<str:name>`、`adduser/`，紅框新增三條：
  ```python
  path('index/', views.index),
  path('login/', views.login),
  path('logout/', views.logout),
  ```
- `loginapp/views.py` 圖中首頁：
  ```python
  def index(request):
      # 判斷用戶是否認證過
      if request.user.is_authenticated:
          name = request.user.username
      return render(request, "index.html", locals())
  ```
  已登入時把 username 放入 `name`；未登入則仍渲染首頁，但 `name` 不會由此分支賦值。畫面是否登入由模板判斷，模板在 P278。

<a id="p277"></a>

### P277｜完整 Auth 登入／登出 view 與允許停用帳號驗證的 backend

[核對原講義第 277 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=277)

- `loginapp/views.py` 程式圖片：
  ```python
  from django.contrib import auth

  def login(request):
      if request.method == 'POST':
          name = request.POST['username']
          password = request.POST['password']
          # 利用auth物件內的authenticate方法，可以完成使用者登入驗證
          user = auth.authenticate(username=name, password=password)
          if user is not None:
              if user.is_active:
                  auth.login(request, user)
                  message = '登入成功!'
              else:
                  message = '帳號尚未啟用!'
          else:
              message = '登入失敗!'
          return render(request, "index.html", locals())
      else:
          return render(request, "login.html", locals())

  def logout(request):
      auth.logout(request)
      return redirect('/index/')
  ```
- POST 從表單的 `username/password` 取值，先驗證是否有 User，再看 active；登入成功才呼叫 `auth.login`。POST 的成功、停用、失敗都渲染 `index.html`；非 POST 則顯示 `login.html`。logout 清 Session 後導回 `/index/`。
- 黃底重點：預設 `authenticate()` 對帳密錯誤與停用帳號都回 `None`，因此上方「帳號尚未啟用」分支在預設 backend 下難以到達。原稿要求 `sudo vim login/settings.py` 新增：
  ```python
  AUTHENTICATION_BACKENDS = [
      'django.contrib.auth.backends.AllowAllUsersModelBackend'
  ]
  ```
  此 backend 可回傳帳密正確但 inactive 的 User，再由 view 的 `if user.is_active` 禁止登入，以區分錯誤原因。
- 圖片額外資訊：settings 編輯器可見 `DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'` 及 `https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field` 註解，因此至少這段專案截圖屬 **Django 3.2 時期樣式**，不是所有頁都保證同版本。紅框圈出 `AUTHENTICATION_BACKENDS` 單行設定。
- 原稿參考文獻：<https://www.cnblogs.com/yoyoketang/p/13192138.html>（只記錄講義引用，未宣稱本次開啟驗證）。
- **安全補充**：此設定替換整份 backend 清單，其他登入流程若只相信 authenticate 非空、未檢查 active，可能讓停用帳號登入；不能為了錯誤提示盲目照改。區別「帳號停用」亦可能增加帳號狀態洩漏。`locals()` 仍包含 password，不建議用於正式模板 context；POST 後直接 render 而非 redirect，也可能讓重新整理重送表單。

<a id="p278"></a>

### P278｜Auth 專案的 index.html 與 login.html

[核對原講義第 278 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=278)

- `sudo vim templates/index.html`：圖片顯示 HTML 文件骨架、UTF-8 Content-Type meta、`<title>首頁</title>`。body 的完整功能內容：
  ```html
  <h2>文淵閣首頁</h2>
  {% if request.user.is_authenticated %}
      歡迎光臨:{{name}}
      <p><a href="/logout/">登出</a></p>
  {% else %}
      <p>您尚未登入喔~</p>
      <a href="/login/">登入</a>
  {% endif %}
  <span style="color:red">{{message}}</span>
  ```
  模板條件直接使用請求上的驗證狀態；`{{name}}` 來自 index/login view；`{{message}}` 顯示成功、失敗或停用訊息。登入與登出 URL 是寫死的絕對路徑。
- `sudo vim templates/login.html`，圖中內容：
  ```html
  <html>
  <form action="." method="POST" name="form1">
      {% csrf_token %}
      <div>帳號：<input type="text" name="username" id="username" autocomplete="off"/></div>
      <div>密碼：<input type="password" name="password" id="password"/></div>
      <div>
          <input type="submit" name="button" id="button" value="登入"/>
      </div>
      <span style="color:red">{{message}}</span>
  </form>
  </html>
  ```
  `action="."` 在 `/login/` 位置把表單送回目前路徑；POST 欄位 `name` 必須與 P277 的 `request.POST['username']`、`['password']` 一致。`id` 用於 HTML 識別，並不是 POST key；`autocomplete="off"` 關閉帳號欄建議；password type 遮蔽畫面輸入，不代表網路加密。`{% csrf_token %}` 產生 CSRF 隱藏欄位。
- 測試仍用 `sudo python3 manage.py runserver 0.0.0.0:8080`。本頁只展示模板，成果在 P279。
- **檔案與請求關係總串接**：`login/urls.py` → `loginapp/views.py` 的 index/login/logout → Auth backend 驗證 User → Session 記住使用者 → `templates/index.html` 根據 request.user 呈現登入或登出；`templates/login.html` POST 回 login view。`login/settings.py` 控制 backend 與模板搜尋路徑；此頁未展示完整 TEMPLATES、middleware 或 context processor 設定，不能宣稱已具備所有專案檔。
- **安全／版本補充**：登入表單有 CSRF token，但登出用 GET 超連結，是這份手寫 view 的設計；不等同各版本內建 LogoutView 的允許方法。正式登出宜用 POST/CSRF，傳輸密碼須 HTTPS。模板是否能使用 `request` 亦需相應 context processor。

<a id="p279"></a>

### P279｜Auth 成功、失敗、停用的展示與 Registration 專案引入

[核對原講義第 279 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=279)

- 本頁上方五張圖片依次展示：
  1. `/index/` 的「會員系統首頁」，顯示「您尚未登入喔~」及「登入」連結。
  2. `/login/` 輸入帳號 `test2` 與遮蔽密碼，按鈕「登入」。
  3. `/index/` 成功畫面：「會員系統首頁」、「歡迎光臨:test2」與「登出」連結。
  4. `/login/` 保留帳密輸入表單，下方紅字「登入失敗！」。
  5. `/login/` 顯示首頁布局、「您尚未登入喔~」、「登入」連結，以及紅字「帳號尚未啟用！」。
- **圖文不一致需保留**：P278 模板 h2 寫「文淵閣首頁」，本頁截圖則為「會員系統首頁」；P277 所示失敗 POST 應 render index.html，而本頁失敗图仍是登入表單；成功 POST 原碼亦直接 render，圖中卻出現 `/index/`。這些可能是修改過的版本或另行導覽結果，不能當作完全相同程式的一致執行證據。
- 頁末引入 **Registration 小專案（會員註冊與登入）**，寫「結果如下」，實際新版 UI 展示在 P280–281。此處不是完整新專案碼，也沒有列出註冊驗證函式。

<a id="p280"></a>

### P280｜Registration 新版首頁與完整註冊欄位（圖片頁）

[核對原講義第 280 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=280)

本頁文字層幾乎只有頁碼，主要內容是兩張網站結果截圖，逐項如下：

- **首頁** `/index/`：藍色整頁背景，中央白色圓角大卡片；標題「會員系統首頁」，主訊息「您尚未登入」，下方「已有帳號？登入」及「尚未申請帳號？加入會員」。登入與加入會員是兩個不同入口。
- **註冊頁** `/useradd/`：同樣藍底，狹長白色置中卡片，標題「會員註冊」。欄位自上而下：
  | 標籤 | 圖片提示／控件 |
  |---|---|
  | 帳號 | 「請輸入使用者帳號」文字框 |
  | 密碼 | 「請輸入密碼」 |
  | 確認密碼 | 「請重複輸入密碼」 |
  | 手機號碼 | 「請輸入您的手機號碼」 |
  | 電子信箱 | 「請輸入您的信箱」 |
  | 生日 | `年/月/日` 格式提示，右側有日期選擇器圖示 |
- 表單底部為橫跨內容寬度的綠色「註冊」按鈕，再下方是「已有帳號了？登入」。圖中滑鼠游標位於註冊按鈕。
- **與前例區分**：本 Registration 成果路徑確實是 `/useradd/`；P274 的原型是 `/adduser/`。本頁不展示 routes、view、模板原碼，不能把新介面自行倒推出已存在的檔案內容。
- **知識連結／補充**：手機與生日並非前面 User 表列的標準欄位，需另行擴充模型或關聯 profile；後頁介紹自訂 User。確認密碼屬輸入驗證，通常不另存第二份密碼；截圖無法證明其伺服器端驗證、安全 hash、email 格式檢查或生日欄位已實作。

<a id="p281"></a>

### P281｜註冊成功提示與新版會員登入（圖片頁）

[核對原講義第 281 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=281)

- 上方圖是瀏覽器 JavaScript 風格提示視窗，標頭「127.0.0.1:8080 顯示」，內容「註冊成功，請登入」，有「確定」按鈕。背景為藍色頁面，瀏覽器分頁標題「會員登入」。
- URL 可辨識 `/userlogin/?useradd_success_sta...`，尾端被瀏覽器省略；**不可據此猜成完整參數名稱或值**。這表示成果展示中有註冊後導向登入並帶查詢字串的流程，但本頁沒給其產生或判讀程式。
- 下方登入畫面：藍底、中央白色圓角卡片、標題「會員登入」，「帳號」欄輸入 `a2`、「密碼」欄為圓點遮蔽；綠色全寬「登入」按鈕，下方「註冊新帳號」連結。
- **與舊版比較**：此專案用 `/userlogin/`，不是 P276 的 `/login/`；圖只證實 UI 和操作順序，不能假稱已檢查後端帳號建立、資料保存或 JavaScript 實作。

<a id="p282"></a>

### P282｜登入後首頁、page1 連結與版型參考

[核對原講義第 282 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=282)

- 上圖：`127.0.0.1:8080/index/`，藍底白色卡片，標題「會員系統首頁」，顯示「歡迎光臨：a2」。有「連接到page1」與「登出」連結。滑鼠在 page1 上，瀏覽器左下狀態列顯示 `127.0.0.1:8080/page1/`。
- 下圖：瀏覽 `/page1/`，分頁名 `Document`，簡單白頁左上只顯示 `page1` 後接一串點號。它展示登入後跨頁導覽；**沒有展示 page1 的登入保護程式**，不能由先登入再點連結推論匿名請求一定被禁止。
- Layout 參考逐項保留：
  1. 「HTML/CSS 寫的簡單的註冊頁面」：<https://www.796t.com/content/1545570916.html>。
  2. 「Registration form Bootstrap 5 Registration form componen」：<https://mdbootstrap.com/docs/standard/extended/registration/#docsTabsOverview>。原標題的 `componen` 缺字照錄，不替原稿補出完整英文。
- 頁末新問題：**How to add phone number to django user model?**，接續下一頁的 AbstractUser 擴充。
- **版本補充**：此處版型參考寫 Bootstrap 5，P285 卻明確講 Bootstrap 4 utility，應區分來源與實際採用版本，不能假設兩版 class 完全相容。

<a id="p283"></a>

### P283｜擴充 AbstractUser、AUTH_USER_MODEL 與 view 匯入

[核對原講義第 283 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=283)

- 頁首網頁截圖章節「3. 繼承自 AbstractUser」；圖片原文說明：不想修改原有 User 欄位而想加新欄位，可繼承 `django.contrib.auth.models.AbstractUser`，這也是內建 User 的父類；例子新增 `telephone` 與 `school`。圖頂端還保留上一段殘句「會建立一個 UserExtension 和 User 進行綁定」，但其完整方案不在本頁，不能補造。
- 對原 PDF 局部重繪放大確認後，示例碼為：
  ```python
  from django.contrib.auth.models import AbstractUser

  class User(AbstractUser):
      telephone = models.CharField(max_length=11, unique=True)
      school = models.CharField(max_length=100)

      # 指定telephone作為USERNAME_FIELD，以後使用authenticate
      # 函數驗證時可根據telephone，而非原來的username
      USERNAME_FIELD = 'telephone'
      REQUIRED_FIELDS = []
  ```
  `max_length=11` 限制電話欄字串長度，`unique=True` 要求唯一；學校欄長度上限 100。`USERNAME_FIELD` 改變主要身份欄位。`REQUIRED_FIELDS=[]` 在這個片段留空。
- **片段限制／補充**：圖片未列 `from django.db import models`；`REQUIRED_FIELDS` 主要參與 `createsuperuser` 額外詢問，不等同所有欄位都可空白，也不自動免除表單／資料庫驗證。更換 USERNAME_FIELD 尚須讓 manager、建立使用者流程及表單配合；截圖不等於可直接覆蓋任意專案的完整模型。
- 原稿來源完整網址：<http://139.155.2.227/di-qi-zhang-ff1a-zhong-jian-jian-he-zi-kuang-jia/di-er-jie-ff1a-yong-hu-mo-xing.html>。
- 原稿強調自訂 User 後還要修改兩處；下方是另一個 `UserCreationForm01` 專案的具體截圖，不要與上方類名 `User` 混為同一完整程式：
  1. `UserCreationForm01/settings.py`：在 `ROOT_URLCONF = 'UserCreationForm01.urls'` 附近加入紅框設定：
     ```python
     AUTH_USER_MODEL = 'myapp.CustomUser'
     ```
     字串是 app label 加模型類名，告訴 Auth 使用哪張自訂使用者表。
  2. `myapp/views.py`：紅框把內建 User 匯入註解，換成自訂模型別名：
     ```python
     # from django.contrib.auth.models import User
     from myapp.models import CustomUser as User
     ```
     圖中同時可見 `from django.shortcuts import render`、`from django.http import HttpResponse`、`from datetime import datetime`。之後 view 內既有 `User` 名称會指向 `CustomUser`。
- **檔案關係**：`myapp/models.py` 定義 CustomUser → settings 指向 `myapp.CustomUser` → migration 建表 → views 匯入同一模型 → 註冊／登入處理資料。正式可重用程式也可用 `get_user_model()`，模型關聯則依 `settings.AUTH_USER_MODEL`，此為補充，不是原稿的匯入寫法。
- **重要限制**：指定範圍內沒有 `CustomUser` 的完整定義，也未給手機／生日的最終模型碼。不能拿頁首電話與學校示例，冒充 Registration 成品的手機與生日模型。

<a id="p284"></a>

### P284｜變更使用者模型：欄位改名、非空欄位與重建示例

[核對原講義第 284 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=284)

- 標題「Django 變更模型（Models）過程中易出現的問題及解決方案」，子題「Adding custom fields to users in Django」。
- 首張終端截圖（已局部重繪核對）：
  ```text
  (dvds) c:\dvds\UserCreationForm01>python manage.py makemigrations myapp
  Did you rename customuser.phone to customuser.tel (a CharField)? [y/N] y
  You are trying to add a non-nullable field 'cBirthday' to customuser without a default;
  we can't do that (the database needs something to populate existing rows).
  Please select a fix:
   1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
   2) Quit, and let me add a default in models.py
  Select an option:
  ```
  圖中已用 `y` 確認 `phone → tel` 改名；下一個問題是新增不可為 NULL 的 `cBirthday`，舊資料列沒有值可填，需一次性 default 或回模型定義 default。此圖沒有顯示最後選哪個選項。
- 中間 VS Code 圖：專案 `USERCREATIONFORM01`，左側 `myapp/migrations` 被紅框標示，`0001_initial.py` 也被框選，滑鼠右鍵選單停在 **Delete**。圖片有 `__init__.py` 與 cache 項目，但明確被選取的是 initial migration 檔；不應延伸成無差別刪除整個資料夾的指令。
- 原稿文字「刪除資料庫，再用以下指令重建」。下方命令與展示輸出：
  ```text
  python manage.py makemigrations myapp
  Migrations for 'myapp':
    myapp\migrations\0001_initial.py
      - Create model CustomUser

  python manage.py migrate
  Operations to perform:
    Apply all migrations: admin, auth, contenttypes, myapp, sessions
  Running migrations:
    No migrations to apply.
  ```
- **原稿重大疑點**：聲稱刪除資料庫重建，卻展示 `No migrations to apply.`，該輸出只代表當下沒有待套用的 migration，不足以证明新資料庫與新欄位已建立。它可能是不同狀態的截圖，不能當成完整成功紀錄。
- **安全補充（與原稿做法分開）**：刪資料庫會永久失去資料，刪 migration 會破壞歷史與團隊依賴；只能在可丟棄、已確認不需資料的教學環境考慮重建，正式環境先備份及設計資料遷移。既有資料通常應保留正確 RenameField，依需求提供合理 default，或先允許空值→補資料→再加非空限制。自訂 User 最好於初始 migration 前決定；專案中途替換使用者模型不是只改設定即可。
- 本次只閱讀上述圖片與命令，**沒有刪除任何資料庫／migration，也沒有執行專案 migration**。

<a id="p285"></a>

### P285｜UserCreationForm01 的檔案結構、路由與 Bootstrap 4 類別

[核對原講義第 285 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=285)

- 頁首 VS Code 截圖黃色標籤明寫「範例：專案 UserCreationForm01」。檔案總管可見應用程式檔 `admin.py`、`apps.py`、`models.py`、`tests.py`、`views.py`，`static` 目錄，`templates` 下列四檔：
  - `index.html`：首頁模板。
  - `useradd1.html`：第一版註冊模板。
  - `useradd2.html`：第二版註冊模板。
  - `userlogin.html`：登入模板。
  專案套件 `UserCreationForm01` 下可見 `__pycache__`、`__init__.py`、`asgi.py`、`settings.py`、`urls.py`。圖中沒展開 static 內容，也沒有上述模板全文；命名可辨識角色，但兩個註冊版本差異不能憑名稱臆測。
- 編輯器所開是專案的 `urls.py`，圖片可見的實質程式完整如下（頂部保留 Django 標準 URLconf 說明註解片段）：
  ```python
  from django.contrib import admin
  from django.urls import path
  from myapp import views

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('useradd1/', views.useradd1),
      path('useradd2/', views.useradd2),
      path('userlogin/', views.userlogin),
      path('index/', views.index),
      path('userlogout/', views.userlogout),
  ]
  ```
- **全專案關係，限已見資訊**：`UserCreationForm01/urls.py` 把註冊兩版本、登入、首頁、登出派給 `myapp/views.py`；views 應按各功能讀写 `myapp.models.CustomUser`，並選用 templates 裡相應 HTML。P283 明示模型匯入及 `AUTH_USER_MODEL`；P284 明示 `myapp/migrations/0001_initial.py` 與 CustomUser 建模。`static` 放前端資源的角色為一般 Django 知識，圖片未提供實際 CSS/JS 檔。本範圍沒有 `useradd1/useradd2/userlogin/userlogout` 的完整 view，因此不假造註冊、登入與登出邏輯。
- **注意不同版本的路由**：P280 成果用 `/useradd/`，本圖路由是 `/useradd1/` 與 `/useradd2/`；P282 有 `/page1/`，本圖未列它。應視為不同示例／階段，不可合併宣稱一份完整、可直接執行的 URLconf。
- 頁面接著標 **Bootstrap 4**，顏色文件：<https://getbootstrap.com/docs/4.0/utilities/colors/>。以下說明被放在 Django `{% comment %}` 與下一頁 `{% endcomment %}` 之間，表示模板多行註解，不會直接輸出至瀏覽器。
- 原稿 CSS class 逐項：
  | 類別 | 原稿說明 | 精確性補充 |
  |---|---|---|
  | `mt-4` | margin-top | 設上外距；4 是 Bootstrap spacing 等級，不是 4px。 |
  | `mb-5` | margin-bottom | 設下外距；5 是 spacing 等級，不是 5px。 |
  | `text-uppercase` | 把本文英文字母轉大寫 | 是顯示上的 text-transform，不改資料庫內容。 |
  | `text-muted` | 文字灰色 | 弱化文字的主題樣式，實際色碼依樣式表。 |
  | `d-flex` | 使用 Flexbox，做彈性布局 | 設定 display:flex。 |
  | `justify-content-center` | 原稿說 Flexbox 水平置中 | 精確說為沿主軸置中；預設 row 是水平，改 column 時則非水平。 |
  | `bg-danger` | danger 主題背景，紅色 | 只設定背景主題色，不自動代表驗證或錯誤處理。 |

<a id="p286"></a>

### P286｜Bootstrap 4 按鈕與文字類別續表

[核對原講義第 286 頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Python%20and%20Django%28%E6%9C%80%E6%96%B0%E7%89%88%29P.pdf#page=286)

- 本頁上半部延續前頁註解方框，沒有新程式或網站截圖；下半頁留白。完整類別：
  | 類別 | 講義內容與作用 |
  |---|---|
  | `btn` | 按鈕基礎類別，套用 Bootstrap 按鈕視覺樣式。 |
  | `btn-success` | 使用 success 主題，原稿說明為綠色。 |
  | `btn-block` | 以塊級形式顯示按鈕，占滿容器寬度，以適應不同螢幕尺寸。 |
  | `btn-lg` | 大號（large）按鈕樣式。 |
  | `text-body` | 原稿說採用預設文字顏色與大小，通常黑色及 16px。 |
- 方框末尾為 `{% endcomment %}`，結束 P285 的多行模板註解。
- **原稿精確性補充**：`btn` 是 CSS 樣式，不会讓任意元素自動具有真正 button 的語意與行為；應搭配合適 `<button>`、`<input>` 或連結元素。`text-body` 主要設定 body 文字顏色，並不保證或專門設定字體大小 16px；實際字型大小受其他樣式繼承或覆寫。
- **版本註記**：本組以原稿標示的 Bootstrap 4 理解，尤其 `btn-block` 是 Bootstrap 4 的典型用法；不要因 P282 的 Bootstrap 5 參考網址，就把此處 classes 視為同一版本。若移植其他版本，應另核對該版本文件，本筆記沒有暗自把原稿改成新版。

#### 本範圍閱讀界線與可重現性

- 已逐頁區分：Session 原型（CookieSession）、Auth 原型（login）、新版 Registration 成果、UserCreationForm01 片段；保留各自檔名、路由與畫面差異。
- 所有展示命令與結果均出自講義；本次只做閱讀、圖片放大與筆記結構核對，未聲稱 Django 專案已可執行。缺少的完整設定、模型、模板及新註冊 view 已在所屬頁標註，不以猜測補成「原碼」。





---

## 補充講義：Django平台建置(windows) by venv(P).pdf（17頁）

## ENV｜Django 平台建置（Windows／venv）逐頁詳細知識筆記

來源：`Django平台建置(windows) by venv(P).pdf`，共17頁。本筆記逐頁核對文字層與頁圖；「原稿」記錄講義實際展示，「補充／勘誤」是閱讀時的技術說明，並非講義原文。所有安裝、執行原則與伺服器命令僅抄錄，未在系統執行。圖上的 `#` 是講義列命令的符號，實際輸入時不要照抄；命令內使用半形 ASCII `-`。頁面皆有 PDNob 浮水印，非 Django 操作內容。

<a id="env-p001"></a>

### ENV-P001｜安裝 Windows Python、PATH 與多版本辨識

[原講義《Django平台建置(windows) by venv(P).pdf》第1頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Django%E5%B9%B3%E5%8F%B0%E5%BB%BA%E7%BD%AE%28windows%29%20by%20venv%28P%29.pdf#page=1)

**原稿與圖中操作**

- 章名「3-1 Django 平台建置(windows)」。瀏覽器開啟 `python.org/downloads/windows/`。
- 下載頁截圖包含 `Python 3.8.10 - May 3, 2021`，下方有 Windows embeddable package（32-bit／64-bit）、Windows help file、Windows installer（32-bit／64-bit）連結；游標指向 `Download Windows installer (64-bit)`。
- 另可見 `Python 3.9.4 - April 4, 2021`。頁面註記 Python 3.8.10 不能用於 Windows XP 或更早版本，Python 3.9.4 不能用於 Windows 7 或更早版本。
- 安裝器截圖特別框出已勾選的 **Add Python 3.6 to PATH**；另有 `Install launcher for all users (recommended)` 與 `Cancel`。重點是把 Python 加入 PATH，不是要求安裝3.6。
- 兩個版本都加入環境變數時，直接打 `python` 用哪個版本由 Windows 的 PATH 搜尋結果決定。

```bat
python --version
python -V
py -0
py -V
```

圖中命令提示字元在 `C:\Users\tony>`；`python -V`、`python --version` 均輸出 `Python 3.14.0`。`py -0` 的版本清單為：

```text
-V:3.14 *       Python 3.14 (64-bit)
-V:3.9          Python 3.9 (64-bit)
```

星號表示 Launcher 選定的預設版本。原稿說 `py -V` 由 Python Launcher（`C:\Windows\py.exe`）控制，可用 `py.ini` 設定預設版本。

**補充／勘誤**

- 同頁混用3.6安裝畫面、3.8／3.9下載頁及3.14終端機，是跨版本示範，不是一套一致的版本需求。
- `python -V` 與 `py -V` 不必相同：前者主要受 PATH／啟用中的虛擬環境影響，後者涉及 Launcher 的選版規則。
- 文字層曾把減號抽成長短破折號，應依截圖使用 `--version`、`-V`、`-0`，其中 `-0` 是數字零。
- `tony` 是講義使用者名稱；實際路徑需代入自己的帳戶。此處是在說傳統 Windows Python Launcher；不能把歷史安裝畫面的版本當作現在應採用的版本。

<a id="env-p002"></a>

### ENV-P002｜以明確版本或 py.ini 設定 Python Launcher

[原講義《Django平台建置(windows) by venv(P).pdf》第2頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Django%E5%B9%B3%E5%8F%B0%E5%BB%BA%E7%BD%AE%28windows%29%20by%20venv%28P%29.pdf#page=2)

**原稿：兩種選版方法**

1. 每次指定版本（原稿稱「最簡單，推薦」）：
   ```bat
   py -3.9
   ```
   此命令直接啟動已安裝的 Python 3.9 直譯器；若後面再接檔名或 `-m`，則交由該版本執行。
2. 修改 Launcher 預設版本：新增 `C:\Users\tony\AppData\Local\py.ini`，內容為：
   ```ini
   [defaults]
   python=3.14
   ```
   再執行 `py -V` 檢查。

**圖像細節**

- 檔案總管麵包屑為「本機 > 本機磁碟 (C:) > 使用者 > tony > AppData > Local」，清單選取 `py.ini`，類型為「組態設定」。這不是放在專案內的設定檔。
- Notepad++ 標題是 `C:\Users\tony\AppData\Local\py.ini - Notepad++`；檔案只有兩行 `[defaults]`、`python=3.14`。狀態列顯示 Windows (CR LF)、UTF-8、INS。
- 圖中的其他 Local 資料夾（如 speech、SquirrelTemp、TechSmith、Temp、Tracker Software、VirtualStore、VMware）只是定位路徑的背景，無須建立或修改。

**補充**

- 必須真的安裝指定的 Python；設定檔不會自行下載直譯器。
- 注意檔名不要存成 `py.ini.txt`。設定 Launcher 預設版不等於修改 PATH 中 `python` 的指向。

<a id="env-p003"></a>

### ENV-P003｜建立 venv、指定基底 Python 並啟用 venv1

[原講義《Django平台建置(windows) by venv(P).pdf》第3頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Django%E5%B9%B3%E5%8F%B0%E5%BB%BA%E7%BD%AE%28windows%29%20by%20venv%28P%29.pdf#page=3)

**原稿與截圖**

頁首承接前頁驗證：在 `C:\Users\tony>` 執行 `py -V`，輸出 `Python 3.14.0`。

建立虛擬環境方法一，使用當下 `python`：

```bat
python -m venv venv1
```

- `python`：呼叫 Python 直譯器。
- `-m venv`：執行 Python 的 `venv` 模組。
- `venv1`：將建立的資料夾名稱。

方法二，先列版本，再明確指定3.9：

```bat
py -0
py -3.9 -m venv venv2
```

`C:\>` 的版本清單仍是3.14（星號）及3.9，皆64-bit。啟用 `venv1`：

```bat
cd c:\venv1
Scripts\activate
```

圖中拆成 `cd c:\`、`cd venv1`，再於 `C:\venv1>` 執行 `Scripts\activate`。成功後提示字元有 `(venv1)`：

```text
(venv1) c:\venv1>python -V
Python 3.14.0

(venv1) c:\venv1>pip list
Package Version
------- -------
pip     25.2
```

**補充／容易誤會處**

- `venv1` 是相對於建立命令執行位置的資料夾；只有在 `C:\` 建立，才會位於 `C:\venv1`。本頁示例後續假設環境在C槽根目錄。
- 啟用是調整目前終端機工作階段的環境，並非重新安裝 Python。不同 venv 的第三方套件互相隔離；版本由建立它的基底 Python 決定。
- 圖中是 CMD 寫法；PowerShell 通常使用 `.\Scripts\Activate.ps1`，執行原則問題另見P010。虛擬環境提示前綴是辨識線索，也應同時檢查 `python -V`。

<a id="env-p004"></a>

### ENV-P004｜離開與切換環境、開始 Django 開發流程

[原講義《Django平台建置(windows) by venv(P).pdf》第4頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Django%E5%B9%B3%E5%8F%B0%E5%BB%BA%E7%BD%AE%28windows%29%20by%20venv%28P%29.pdf#page=4)

**原稿與圖中命令**

用 `deactivate` 離開目前虛擬環境。原稿括號「離開虛擬環境」是說明，不能一併輸入。接著示範切到 `venv2`：

```bat
cd c:\
cd venv2
Scripts\activate
python -V
pip list
```

- CMD 標頭為 Microsoft Windows `[版本 10.0.19045.4894]`。
- 提示字元變成 `(venv2) c:\venv2>`，`python -V` 輸出 `Python 3.9.7`。
- `pip list` 列出 `pip 21.2.3`、`setuptools 57.4.0`。
- 黃色警告原意：正在使用 pip 21.2.3，另有26.0.1可用；畫面建議透過 `c:\venv2\Scripts\python.exe -m pip install --upgrade pip` 升級。這是該截圖當時的提示，並非本筆記查得的最新版，也不保證新版本仍適用舊Python。
- 再次輸入 `deactivate` 可離開 `venv2`。

下半部「開發 django 流程」回到 `venv1`：

```bat
python -m venv venv1
cd c:\venv1
Scripts\activate
```

附圖的實際切目錄順序仍是 `cd c:\` → `cd venv1` → `Scripts\activate`。

**補充**

- 本頁的3.9.7與前頁的3.14.0，示範兩個虛擬環境各自綁定不同版本。
- `deactivate` 不會刪除環境或移除套件，只還原目前 shell 的環境設定。建立既有環境不是每次開發都需要做的動作；日常開發只需進入正確目錄並啟用它。

<a id="env-p005"></a>

### ENV-P005｜安裝 Django、建立 project 與 app、準備前端目錄

[原講義《Django平台建置(windows) by venv(P).pdf》第5頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Django%E5%B9%B3%E5%8F%B0%E5%BB%BA%E7%BD%AE%28windows%29%20by%20venv%28P%29.pdf#page=5)

**原稿命令與解釋**

本頁先確認 `(venv1) c:\venv1>` 裡的 `python -V` 為3.14.0；安裝前 `pip list` 只有 pip 25.2。安裝 Django：

```bat
pip install Django
pip list
```

`pip` 是下載／管理Python套件的工具，`install` 執行安裝，`list` 列出目前環境套件。安裝後截圖的清單完整如下：

| Package | Version |
|---|---|
| asgiref | 3.12.1 |
| Django | 6.0.7 |
| pip | 25.2 |
| sqlparse | 0.5.5 |
| tzdata | 2026.3 |

建立專案與應用程式：

```bat
Django-admin startproject project1
cd project1
python manage.py startapp myapp
mkdir templates
mkdir static
```

- `Django-admin`：原稿大寫D；Django全域管理指令，能建立專案、處理管理工作。一般文件慣用小寫 `django-admin`，本處保留原稿。
- `startproject project1`：建立名為 `project1` 的專案，參數同時決定生成目錄／專案名稱。
- `cd project1`：把工作目錄切到新專案，後續命令需找得到 `manage.py`。
- `python manage.py`：由目前環境的Python執行專案管理入口；`startapp myapp` 建立名為 `myapp` 的應用程式。
- `templates`：放網頁模板，如 `.html`。
- `static`：放網站靜態檔案，例如 CSS、JavaScript、圖片；後續仍要設定搜尋路徑。

**補充／版本注意**

- 以上版本只是圖中安裝結果。`pip install Django` 未鎖版本，在另一時間／Python版本執行，得到的版本可能不同。
- 為避免叫錯另一套Python的pip，可用 `python -m pip install Django`、`python -m pip list`；這是補充寫法，非原稿命令。
- Project 管整站設定與路由；App 是站內功能模組。建立App之後還要放進 `INSTALLED_APPS`（P007）。

<a id="env-p006"></a>

### ENV-P006｜在 VS Code 開啟 venv1 與 Workspace Trust

[原講義《Django平台建置(windows) by venv(P).pdf》第6頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Django%E5%B9%B3%E5%8F%B0%E5%BB%BA%E7%BD%AE%28windows%29%20by%20venv%28P%29.pdf#page=6)

**原稿：命令實際所在目錄**

圖中依序執行，未顯示錯誤輸出：

```text
(venv1) c:\venv1>Django-admin startproject project1
(venv1) c:\venv1>cd project1
(venv1) c:\venv1\project1>python manage.py startapp myapp
(venv1) c:\venv1\project1>mkdir templates
(venv1) c:\venv1\project1>mkdir static
```

原稿標題「利用 vscode 開啟與修改 settings.py」，但本頁圖實際先展示開資料夾及信任設定，尚未顯示 `settings.py` 內容。

VS Code Explorer 根目錄為 `VENV1`，可見：

```text
VENV1/
├─ Include/
├─ Lib/
├─ project1/
├─ Scripts/
├─ .gitignore
└─ pyvenv.cfg
```

上方出現 Restricted Mode 提示「…Trust this folder to enable all features」，紅框標示 **Manage**，另有 Learn More。點 Manage 可進入 Workspace Trust 頁，標題 `You are in Restricted Mode`。

**Workspace Trust 圖中兩欄（已局部放大核對）**

| Trusted Folder（信任作者） | Restricted Mode（不信任作者） |
|---|---|
| Tasks are allowed to run | Tasks are not allowed to run |
| Debugging is enabled | Debugging is disabled |
| All workspace settings are applied | 94 workspace settings are not applied |
| All enabled extensions are activated | 19 extensions are disabled or have limited functionality |

- 左欄有 **Trust** 按鈕，快捷鍵 `Ctrl+Enter`。
- 底部 `Trusted Folders & Workspaces` 表示信任項目及子目錄／workspace檔；欄位為 Host、Path。截圖背景列出 Local `D:\backup`、Local `D:\git_temp`，以及 `SSH: 192.168.57.227` 的 `/home`，另有 **Add Folder**。這些是講師既有信任記錄，不是本專案必須添加的路徑。

**補充／安全注意**

- 只有在確認來源可信且理解程式會做什麼時才按 Trust；信任工作區會允許任務／除錯與擴充功能執行，不是純粹關掉提示。
- 講義把專案放在虛擬環境 `C:\venv1` 裡。可照此理解後續路徑，但實務也常把可重建的 `.venv` 與原始碼分開管理，避免刪環境時誤刪專案。

<a id="env-p007"></a>

### ENV-P007｜允許主機名稱與註冊 myapp

[原講義《Django平台建置(windows) by venv(P).pdf》第7頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Django%E5%B9%B3%E5%8F%B0%E5%BB%BA%E7%BD%AE%28windows%29%20by%20venv%28P%29.pdf#page=7)

**原稿與圖像**

頁首的 Workspace Trust 已顯示 `You trust this folder`，紅框指向右上角關閉控制（提示 `Close ... (Escape)`）；接續開始編輯專案的 `settings.py`。

```python
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
]
```

- 原稿把 `ALLOWED_HOSTS = ['*']` 解釋為「允許任何網域或IP位址的電腦連線參觀」。截圖紅框是第28行；同時可見 `DEBUG = True`，上方 `SECRET_KEY` 只顯示開頭 `django-insecu...`，右側已裁切，不能重建完整金鑰。
- `INSTALLED_APPS` 是已安裝應用程式清單；新增的 `'myapp',` 用紅字強調，需保留清單內的引號與逗號。
- VS Code截圖根目錄此處改成 `DVDS`，不再是前頁的 `VENV1`；可見 `Lib`、外層 `project1`、其下 `myapp` 與內層 `project1`，內層有 `__pycache__`、`__init__.py`、`asgi.py`、`settings.py`、`urls.py`。編輯麵包屑為 `project1 > project1 > settings.py`。

**補充／安全與概念勘誤**

- `ALLOWED_HOSTS` 驗證請求的 Host 主機名稱，不是依「連線者的IP」做存取白名單；`'*'` 接受任意Host，**不應直接當成正式部署的安全設定**。它也不會替你開放防火牆或開始監聽網路。
- `DEBUG = True` 適合開發，不適合公開正式服務。`SECRET_KEY` 不應外洩或當成通用常數分享。
- 內建App用途：`admin` 管理後台；`auth` 使用者／群組／權限；`contenttypes` 模型內容類型；`sessions` 工作階段；`messages` 暫存提示訊息；`staticfiles` 靜態檔案搜尋與收集；`myapp` 是自建功能。
- 編輯的是內層 `project1/settings.py`，不是App裡的檔案。原稿截圖混用不同工作區名稱，需以自己的實際路徑為準。

<a id="env-p008"></a>

### ENV-P008｜設定模板引擎與 templates 搜尋目錄

[原講義《Django平台建置(windows) by venv(P).pdf》第8頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Django%E5%B9%B3%E5%8F%B0%E5%BB%BA%E7%BD%AE%28windows%29%20by%20venv%28P%29.pdf#page=8)

**圖中承接：確認App已加入**

上方 VS Code 紅框標示內層 `project1/settings.py` 及第40行 `'myapp',`，第33–41行為前頁完整 `INSTALLED_APPS`。Explorer仍為 `DVDS`，目錄結構與P007相同。

**原稿完整設定**

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

- 原稿稱 `TEMPLATES` 為「Django設定網頁外觀的大字典」；實際語法是**列表裡放字典**，一個字典描述一個模板後端。
- `BACKEND` 指向Django模板引擎。
- `DIRS` 是模板目錄列表，本頁新增重點為 `[BASE_DIR / 'templates']`。藍字標出 `BASE_DIR` 是專案根目錄、`templates` 是資料夾名稱。
- `APP_DIRS = True`：也讓模板載入器搜尋已安裝App中的模板目錄。
- `OPTIONS/context_processors`：模板情境處理器設定。原稿列出 debug、request、auth、messages 四個點分模組路徑，並不是四個HTML檔案。

**補充**

- `BASE_DIR / 'templates'` 是 `pathlib.Path` 的路徑串接，不是字串除法。依講義布局通常指 `C:\venv1\project1\templates`，即 `manage.py` 同層的模板資料夾。
- `request` 可將請求放入模板情境；`auth` 提供登入使用者／權限；`messages` 提供訊息；`debug` 與偵錯資訊有關。實際可用內容仍受請求、設定及渲染方式影響。
- 不同Django版本自動產生的預設清單可能不同；本頁是原稿範例，不表示所有版本都必須手動加上完全相同的預設項。

<a id="env-p009"></a>

### ENV-P009｜語系、時區與靜態檔案設定

[原講義《Django平台建置(windows) by venv(P).pdf》第9頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Django%E5%B9%B3%E5%8F%B0%E5%BB%BA%E7%BD%AE%28windows%29%20by%20venv%28P%29.pdf#page=9)

**原稿圖中模板確認**

上方程式截圖第53行是 `ROOT_URLCONF = 'project1.urls'`；第55–69行重現P008的 `TEMPLATES`，第58行 `DIRS` 被紅框圈出，值為 `[BASE_DIR / 'templates']`，其餘後端、APP_DIRS與四個context processors保持前頁設定。

**原稿語系及時區**

```python
LANGUAGE_CODE = 'zh-Hant'
TIME_ZONE = 'Asia/Taipei'
USE_I18N = True
USE_TZ = True
```

- 文字指出 `LANGUAGE_CODE` 是網站預設語言環境參數，`zh-Hant` 代表繁體中文。
- `TIME_ZONE` 是管理日期與時間的設定，使用臺北時區。
- 截圖第107、109行分別是語系／時區，第111及113行還可見 `USE_I18N = True`、`USE_TZ = True`；這兩行不是文字層正文列出的，但圖中確實存在。

**原稿靜態檔案**

```python
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

- `STATICFILES_DIRS` 是「靜態檔案搜尋路徑清單」；`BASE_DIR` 仍是專案根目錄，`static` 是P005建立的資料夾。

**補充／區別**

- `STATIC_URL` 是產生靜態資源URL時使用的前綴，`STATICFILES_DIRS` 是磁碟搜尋目錄，兩者不可混為一談。
- `LANGUAGE_CODE` 設定不會自動翻譯自己寫的所有內容。Django慣用語言碼常見小寫 `zh-hant`；這裡忠實保留原稿大小寫 `zh-Hant`。
- `USE_I18N` 啟用國際化；`USE_TZ` 啟用時區感知時間處理。時區設定與作業系統時鐘不是同一回事，啟用時區支援時不能把資料庫保存時刻一概理解為臺北本地無時區時間。
- 開發期靜態檔案服務不等於正式部署；正式站通常還需要 `STATIC_ROOT`、收集及Web伺服器設定，本頁未教這些步驟。

<a id="env-p010"></a>

### ENV-P010｜開啟整合終端機與 PowerShell 執行原則

[原講義《Django平台建置(windows) by venv(P).pdf》第10頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Django%E5%B9%B3%E5%8F%B0%E5%BB%BA%E7%BD%AE%28windows%29%20by%20venv%28P%29.pdf#page=10)

**原稿圖中確認設定**

首圖 `settings.py` 第119–122行確認P009的 `STATIC_URL = 'static/'` 與 `STATICFILES_DIRS = [BASE_DIR / 'static']`。註解連到 `https://docs.djangoproject.com/en/4.1/howto/static-files...`，右側裁切；這顯示使用了Django4.1時期截圖，不能與P005的6.0.7直接視為同一版本畫面。

VS Code 選單 **View → Terminal**，快捷鍵顯示 `Ctrl+反引號`。同張圖展示完整專案層次：

```text
PROJECT1/
├─ myapp/
│  ├─ migrations/
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ models.py
│  ├─ tests.py
│  └─ views.py
├─ project1/
│  ├─ __pycache__/
│  ├─ __init__.py
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
├─ static/
├─ templates/
└─ manage.py
```

圖中View選單另列 Command Palette（Ctrl+Shift+P）、Open View、Appearance、Editor Layout、Explorer（Ctrl+Shift+E）、Search（Ctrl+Shift+F）、Source Control（Ctrl+Shift+G）、Run（Ctrl+Shift+D）、Extensions（Ctrl+Shift+X）、Problems（Ctrl+Shift+M）、Output（Ctrl+Shift+U）、Debug Console（Ctrl+Shift+Y）、Word Wrap（Alt+Z）、Sticky Scroll；本頁實際要選的是 Terminal。

**原稿：以系統管理員身分執行 PowerShell 或 VS Code**

Windows搜尋結果選 Windows PowerShell，右鍵選「以系統管理員身分執行」（另有「開啟檔案位置」），接著原稿列：

```powershell
set-executionpolicy remotesigned
get-executionpolicy -list
```

- `Set-ExecutionPolicy` 修改PowerShell執行原則。
- `RemoteSigned`：原稿說明為遠端下載的腳本需數位簽署，本機寫的腳本可執行。
- `Get-ExecutionPolicy -List`：列出各作用域的原則。原稿文字要求調整後 LocalMachine（整台電腦）、CurrentUser（目前使用者）都變 RemoteSigned；**此頁並未展示該表格實際輸出**。

**補充／高影響命令勘誤**

- 不指定 `-Scope` 的 `Set-ExecutionPolicy` 預設針對 LocalMachine，需要提升權限，**不會自動同時把CurrentUser也設成RemoteSigned**。原稿對兩層都要變更的說法過度簡化。
- 不必為一般Django開發把整個VS Code長期以系統管理員開啟，也不一定需修改全機原則。若確有需求，可考慮較小範圍的 `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`；若只想暫用，Process作用域只影響目前行程。這些是安全補充，不是要求讀者立即執行。
- 群組原則可能優先覆蓋設定；執行原則不是完整安全邊界。RemoteSigned針對帶有網際網路來源標記的腳本有特定行為，不能簡化成「所有下載檔都安全」或「本機腳本都可信」。本筆記未修改任何執行原則。

<a id="env-p011"></a>

### ENV-P011｜確認執行原則變更、建立與套用資料庫遷移

[原講義《Django平台建置(windows) by venv(P).pdf》第11頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Django%E5%B9%B3%E5%8F%B0%E5%BB%BA%E7%BD%AE%28windows%29%20by%20venv%28P%29.pdf#page=11)

**原稿參考連結**

原頁將網址折成數行，連續網址為：
<https://learn.microsoft.com/zh-tw/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.4>

**PowerShell圖中操作**

視窗標題「系統管理員: Windows PowerShell」，提示為 `PS C:\Windows\system32>`：

```powershell
set-executionpolicy remotesigned
```

畫面出現「執行原則變更」警告：變更原則可能有安全風險，詢問是否要變更；選項含 `[Y] 是`、`[A] 全部皆是`、`[N] 否`、`[L] 全部皆否`、`[S] 暫停`、`[?] 說明`，預設N。截圖在提示後輸入 `y`，然後回到命令提示字元；這只證明圖中答應變更，沒有展示 `Get-ExecutionPolicy -List` 的結果。

**原稿遷移命令**

```bat
python manage.py makemigrations myapp
python manage.py migrate
```

- `makemigrations myapp`：把模型程式裡的表格結構變動，轉成放在 `myapp/migrations/` 的migration檔；原稿稱「施工藍圖」。
- `migrate`：把遷移藍圖套用到資料庫，更新結構；不是只儲存Python檔案。

**CMD截圖完整遷移項目**

提示為 `(dvds) c:\dvds\project1>python manage.py migrate`。輸出 `Operations to perform:` → `Apply all migrations: admin, auth, contenttypes, sessions`，然後 `Running migrations:`。以下每行均為 `Applying <名稱>... OK`：

```text
contenttypes.0001_initial
auth.0001_initial
admin.0001_initial
admin.0002_logentry_remove_auto_add
admin.0003_logentry_add_action_flag_choices
contenttypes.0002_remove_content_type_name
auth.0002_alter_permission_name_max_length
auth.0003_alter_user_email_max_length
auth.0004_alter_user_username_opts
auth.0005_alter_user_last_login_null
auth.0006_require_contenttypes_0002
auth.0007_alter_validators_add_error_messages
auth.0008_alter_user_username_max_length
auth.0009_alter_user_last_name_max_length
auth.0010_alter_group_name_max_length
auth.0011_update_proxy_permissions
auth.0012_alter_user_first_name_max_length
sessions.0001_initial
```

頁尾有 `or`，表示下一頁提供VS Code終端機的另一組示例。

**補充**

- `makemigrations` 偵測模型狀態變更，不是把現有資料庫自動倒推成模型；若App尚未定義模型，沒有變更可產生是合理的。
- `migrate` 也會套用Django內建App的遷移。這張圖清單沒有myapp遷移，不能聲稱已建立自訂資料表。
- 這是會修改資料庫的指令；對重要資料庫操作前應確認環境與備份。本任務未執行命令。

<a id="env-p012"></a>

### ENV-P012｜VS Code 中套用遷移並啟動開發伺服器

[原講義《Django平台建置(windows) by venv(P).pdf》第12頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Django%E5%B9%B3%E5%8F%B0%E5%BB%BA%E7%BD%AE%28windows%29%20by%20venv%28P%29.pdf#page=12)

**VS Code PowerShell圖中流程**

```powershell
# 提示字元：PS C:\venv1\project1>
..\Scripts\activate
python manage.py makemigrations myapp
python manage.py migrate
```

- 由於工作目錄是 `project1`，啟用腳本在上一層的 `Scripts`，所以使用 `..\Scripts\activate`；成功後前綴為 `(venv1)`。
- `makemigrations myapp` 實際輸出 `No changes detected in app 'myapp'`。
- `migrate` 的 `Apply all migrations` 仍是 admin、auth、contenttypes、sessions；逐項名稱、順序與P011完整清單相同，每項皆 `OK`。執行後回到 `(venv1) PS C:\venv1\project1>`。

**原稿啟動命令**

```bat
python manage.py runserver 0.0.0.0:8080
```

原稿註解：runserver「把網站跑在本地端」；`0.0.0.0`「對所有網路開放」；8080提供服務、避免與其他程式衝撞。

**兩組截圖輸出，保留版本差異**

1. 舊CMD示例，`(dvds) c:\dvds\project1>`：
   ```text
   Watching for file changes with StatReloader
   Performing system checks...
   System check identified no issues (0 silenced).
   June 11, 2021 - 16:01:42
   Django version 3.2.4, using settings 'project1.settings'
   Starting development server at http://0.0.0.0:8080/
   Quit the server with CTRL-BREAK.
   ```
2. 新PowerShell示例，`(venv1) PS C:\venv1\project1>`：同樣使用StatReloader、通過系統檢查，時間為 `July 24, 2026 - 16:47:30`，版本為 `Django version 6.0.7`，設定模組 `project1.settings`，監聽 `http://0.0.0.0:8080/`，同樣提示 `CTRL-BREAK`。
   - 黃字警告：`WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.`
   - 部署文件：`https://docs.djangoproject.com/en/6.0/howto/deployment/`
   - 請求日誌：`[24/Jul/2026 16:47:37] "GET / HTTP/1.1" 200 11995`，表示首頁GET回應200，圖中記錄的回應大小11995。

**補充／網路安全與版本**

- `0.0.0.0` 代表綁定所有IPv4網路介面，不等於自動穿越防火牆、NAT或路由，也不是給使用者瀏覽的具體目的IP。瀏覽自己的站用 `127.0.0.1`，其他電腦使用主機實際可達IP。
- 8080也可能被其他程式占用；選8080不能保證一定不衝撞。只需本機學習時，綁 `127.0.0.1:8080` 範圍較小。
- `runserver` 是開發工具，尤其搭配 `DEBUG=True`、`ALLOWED_HOSTS=['*']` 時不應當成公開正式架站方案。
- 本頁明確混用2021年Django3.2.4與2026年6.0.7截圖；日期與版本均是原稿內容，非本次執行結果。

<a id="env-p013"></a>

### ENV-P013｜瀏覽安裝成功頁與手動選擇 VS Code Python 環境

[原講義《Django平台建置(windows) by venv(P).pdf》第13頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Django%E5%B9%B3%E5%8F%B0%E5%BB%BA%E7%BD%AE%28windows%29%20by%20venv%28P%29.pdf#page=13)

**原稿瀏覽驗證**

- 藍字提示 `ipconfig` 可查詢IP；該行部分文字被浮水印／破碎字形干擾，但命令及「查詢ip」可辨。
- `127.0.0.1:8080`：原稿稱「自己電腦關起門來自己看」。
- `實體IP:8080`：原稿稱「模擬外部連線」。
- 瀏覽器網址列為 `127.0.0.1:8080`，Django火箭成功頁顯示 `View release notes for Django 3.2` 及 `The install worked successfully! Congratulations!`。
- 下面說明：`You are seeing this page because DEBUG=True is in your settings file and you have not configured any URLs.` 此處代表Django預設成功頁，不是已完成自訂功能網站。

**原稿：設定 VS Code 要啟用哪個虛擬環境，方法一（手動）**

點右下角Python環境狀態 `venv1 (3.14.0.final.0)`，開啟 `Select a Python Environment`，紅箭頭指向 `Browse...`。選單還有 `Create Virtual Environment...`。下列候選清單已放大核對：

| 顯示名稱 | 圖中路徑 | 類型／標示 |
|---|---|---|
| venv1 (3.14.0.final.0) | `C:\venv1\Scripts\python.exe`（部分被箭頭覆蓋，P014完整路徑可交叉核對） | Recommended |
| Python 3.14 (64-bit) | `C:\Users\tony\AppData\Local\Programs\Python\Python314\python.exe` | Global |
| Python 3.9 (64-bit) | `C:\Users\tony\AppData\Local\Programs\Python\Python39\python.exe` | 此行右欄未見明確文字 |
| dvds (3.9.7.final.0) | `D:\backup\dvds\Scripts\python.exe` | venv |
| pyenv (3.9.7) | `C:\Users\tony\.pyenv\pyenv-win\versions\3.9.7` | PyEnv |
| pyenv (2.7.18) | `C:\Users\tony\.pyenv\pyenv-win\versions\2.7.18` | 此行右欄未見明確文字 |

終端機除P012的正常啟動／GET首頁紀錄外，還出現：

```text
Not Found: /favicon.ico
[24/Jul/2026 16:47:38] "GET /favicon.ico HTTP/1.1" 404 2215
```

**補充**

- 瀏覽器自動請求小圖示，缺少favicon的404不等於首頁失敗；首頁前一行仍是200。
- 從本機用自身區網IP測試，並不能證明網際網路其他人已可連入；還須考慮監聽介面、路由、防火牆及ALLOWED_HOSTS。
- 選中VS Code直譯器能對齊執行／除錯與分析工具，但既有終端機未必立刻切換；需確認終端機實際使用的環境。

<a id="env-p014"></a>

### ENV-P014｜瀏覽指定 venv1 的 python.exe

[原講義《Django平台建置(windows) by venv(P).pdf》第14頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Django%E5%B9%B3%E5%8F%B0%E5%BB%BA%E7%BD%AE%28windows%29%20by%20venv%28P%29.pdf#page=14)

**原稿檔案選擇器**

承接上一頁Browse，對話框標題為 **Select Python Executable**，麵包屑「本機 > 本機磁碟 (C:) > venv1 > Scripts」。選取的檔案是 `python.exe`，所以目標是：

```text
C:\venv1\Scripts\python.exe
```

同目錄清單可見：

```text
django-admin.exe
pip.exe
pip3.14.exe
pip3.exe
python.exe
pythonw.exe
sqlformat.exe
```

這些類型均顯示「應用程式」。`python.exe`、`pythonw.exe` 的修改日期為 `2025/10/7 上午11:17`；其餘套件工具在2026/7/24，這些是檔案畫面資料，不是選直譯器的版本判據。

**VS Code選完後畫面**

- 右下角紅框為 `venv1 (3.14.0.final.0)`，用來確認所選環境。
- 左側PROJECT1下可見 `myapp`、`project1`；編輯頁為 `myapp/views.py`，首行可見Django shortcuts的import，頁圖上方部分程式被終端機遮住，不把它當成新增程式碼範例。
- 終端機仍有P012–P013相同的遷移成功、runserver 6.0.7、首頁 `200 11995` 及favicon `404 2215`，最後回到 `(venv1) PS C:\venv1\project1>`。重複畫面是環境選取的操作證據，不是新的部署結果。
- 頁尾開始下一方法：「方法二（新增環境變數）」，真正的表單在P015。

**補充**

- 應選虛擬環境內的 `python.exe`，不是 `pip.exe`、`django-admin.exe` 或 `pythonw.exe`。`pythonw.exe` 是Windows不顯示一般主控台視窗的啟動器，這裡不拿它當標準除錯直譯器。
- 檔案存在不代表Django已裝在其中，仍應核對套件是否在同一環境。本次僅閱讀截圖，未測試該Windows路徑。

<a id="env-p015"></a>

### ENV-P015｜PATH方法的限制與新增 Python 除錯組態

[原講義《Django平台建置(windows) by venv(P).pdf》第15頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Django%E5%B9%B3%E5%8F%B0%E5%BB%BA%E7%BD%AE%28windows%29%20by%20venv%28P%29.pdf#page=15)

**原稿：編輯環境變數表單**

視窗標題「編輯環境變數」，圖中紅框新增兩列 `C:\venv1` 與 `C:\venv1\Scripts`。可見清單自上而下為：

```text
C:\Users\tony\AppData\Local\Programs\Python\Python314\Scripts\
C:\Users\tony\AppData\Local\Programs\Python\Python314\
C:\Users\tony\.pyenv\pyenv-win\bin
C:\Users\tony\.pyenv\pyenv-win\shims
C:\Users\tony\.pyenv\pyenv-win\bin
C:\Users\tony\.pyenv\pyenv-win\shims
C:\Users\tony\.pyenv\pyenv-win\bin
C:\Users\tony\.pyenv\pyenv-win\shims
C:\Users\tony\AppData\Local\Programs\Python\Python39\Scripts\
C:\Users\tony\AppData\Local\Programs\Python\Python39\
C:\Users\tony\AppData\Local\Microsoft\WindowsApps
C:\Users\tony\AppData\Local\Programs\Microsoft VS Code\bin
D:\backup\dvds\Scripts\
C:\Program Files\Tesseract-OCR\
C:\venv1
C:\venv1\Scripts
```

- pyenv的bin／shims三組重複是截圖本來就有，並非要求照抄三次。
- 右側按鈕為「新增(N)」「編輯(E)」「瀏覽(B)…」「刪除(D)」「上移(U)」「下移(O)」「編輯文字(T)…」；底部「確定」「取消」。圖中未顯示外層表單，因此無法由此圖確定正在編輯使用者Path或系統Path。

**補充／不建議直接照搬**

- 將venv Scripts加到PATH，不等於啟用虛擬環境，也不保證VS Code會改選該直譯器。截圖把它加在最後，前面的全域Python仍可能先被找到。
- 永久把某個專案venv塞進全域PATH容易混用不同專案套件；優先採明確選直譯器與每個終端機啟用環境的方式。
- `C:\venv1` 根目錄一般不是 `python.exe` 所在處；本示範真正直譯器位於 `Scripts`。不得直接複製講師所有其他工具路徑。

**原稿：新增組態**

文字寫「新增組態（目的讓vscode知道使用什麼平台）」。實際操作是 **Run → Add Configuration...**，建立除錯啟動設定。

- Run選單同時可見 Start Debugging（F5）、Run Without Debugging（Ctrl+F5）、Stop Debugging（Shift+F5）、Restart Debugging（Ctrl+Shift+F5），紅框指向Add Configuration。
- 隨後的 `Select debugger` 選單選 **Python Debugger**（Suggested）。其他項目可見 More Node.js options...、More Python Debugger options...、Install an extension for Python...。
- 下方背景為 `views.py`，可見 `from django.shortcuts` 開頭，右側被選單覆蓋。這裡不是要求改寫view。

**補充**

- 這個「平台」比較精確地說是除錯器類型及啟動方式，不是在設定作業系統；後續會選Django範本。

<a id="env-p016"></a>

### ENV-P016｜Django 除錯範本、launch.json 與 F5 啟動

[原講義《Django平台建置(windows) by venv(P).pdf》第16頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Django%E5%B9%B3%E5%8F%B0%E5%BB%BA%E7%BD%AE%28windows%29%20by%20venv%28P%29.pdf#page=16)

**原稿選單流程（已局部放大）**

1. `Select a debug configuration` 選擇 **Django — Launch and debug a Django web application**。
   - 同選單還有 Python File（除錯目前檔案）、Python File with Arguments（帶參數）、Module（用 `-m` 執行模組）、Remote Attach（附加遠端除錯伺服器）、Attach using Process ID（附加本機行程）、FastAPI、Flask、Pyramid。
   - 圖中Django項目的浮動說明壓到下一列FastAPI附近，**不能把顯示的Django說明解讀成FastAPI也是Django**。
2. `Debug Django` 提示輸入manage.py路徑或從清單選擇；列表是 `manage.py ${workspaceFolder}\manage.py`，另有 `Browse files...`。選擇本工作區的manage.py。
3. 產生 `.vscode/launch.json`。左側PROJECT1新增 `.vscode` 及其內 `launch.json`；其餘有myapp、project1、static、templates、`db.sqlite3`、`manage.py`。這裡工作區根就是manage.py所在的外層project1。

**原稿 launch.json 設定完整重錄**

圖中最上面有IntelliSense與Hover的預設註解，以及一行Microsoft說明網址；網址右側被截掉，不猜完整URL。以下去除非功能性註解，保留全部可見有效欄位與數值：

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger: Django",
            "type": "debugpy",
            "request": "launch",
            "args": [
                "runserver", "0.0.0.0:8080"
            ],
            "django": true,
            "autoStartBrowser": false,
            "program": "${workspaceFolder}\\manage.py"
        }
    ]
}
```

- 第12行紅框強調參數：`"runserver", "0.0.0.0:8080"`。兩項是分開的字串，不是一個整串shell命令。
- `version` 是啟動設定格式版本，不是Python或Django版本。
- `configurations` 可以含多套啟動設定；本圖只有一套。
- `name` 是UI顯示名稱；`type = debugpy` 指定Python除錯器；`request = launch` 是啟動新程式而不是attach已存在行程。
- `program` 指向工作區根目錄中的 `manage.py`，JSON中兩個反斜線 `\\` 表示Windows路徑中的一個反斜線；已放大核對，不可漏掉跳脫。
- `django = true` 啟用Django除錯支援；`autoStartBrowser = false` 表示此範本不自動開啟瀏覽器。

**原稿啟動動作**

文字說在VS Code按綠色播放鍵或除錯按鈕，即可自動執行開機指令。底圖選 **Run → Start Debugging**，快捷鍵 **F5**；下方可見 **Run Without Debugging**（Ctrl+F5）及停用中的Stop Debugging（Shift+F5）。

**補充／路徑與風險**

- 這套設定等價於讓所選Python透過除錯器執行 `manage.py runserver 0.0.0.0:8080`；仍是Django開發伺服器，沒有升級成正式服務。
- `${workspaceFolder}` 取決於VS Code實際開啟的資料夾。若開的是 `C:\venv1` 而不是 `C:\venv1\project1`，本圖的program路徑便會指錯，必須調整工作區或路徑。
- 只需自己測試時，可把參數改成 `127.0.0.1:8080`（補充建議，原稿是0.0.0.0）。若前一個runserver還在占用8080，需先停止或換埠，不能重複啟動後假定成功。
- 此頁未展示除錯器終端機的成功日誌；能確認的是設定內容及按鍵操作，不可杜撰新的執行輸出。

<a id="env-p017"></a>

### ENV-P017｜最後驗證：Django 預設成功頁

[原講義《Django平台建置(windows) by venv(P).pdf》第17頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/Django%E5%B9%B3%E5%8F%B0%E5%BB%BA%E7%BD%AE%28windows%29%20by%20venv%28P%29.pdf#page=17)

**原稿全頁圖像**

本頁沒有新增命令、程式碼或文字正文；唯一主要內容是與P013一致的瀏覽器成功頁：

- 網址列：`127.0.0.1:8080`。
- 分頁標題：`The install worked successfully!`。
- 頁首Django標誌、`View release notes for Django 3.2`。
- 中間綠色火箭／雲朵圖，標題 `The install worked successfully! Congratulations!`。
- 原文說明：`You are seeing this page because DEBUG=True is in your settings file and you have not configured any URLs.`
- 瀏覽器書籤列可見 `192.168.57.236`、MSN、Outlook、Gmail；那個IP是書籤，不是此頁實際網址或新教學指令。

**如何解讀這個結果（補充）**

- 代表該截圖中的本機8080曾成功回應Django預設首頁，開發平台的基本安裝／啟動已可運作。
- 不代表已寫好myapp的模型、視圖、模板、URL或正式部署，也不代表外部連線／安全設定已通過驗證。
- 最後頁仍使用Django3.2的歷史畫面，而P016的設定流程與前面6.0.7環境混排；驗收應看自己的網址、終端實際版本和錯誤，而不是強求畫面版本完全一樣。
- 讀圖只證實講義展示此結果；本次閱讀任務沒有安裝Django、改Windows設定或真的架設網站。









---

## 補充講義：PowerShell更改執行原則.pdf（1頁）

<a id="ps-p001"></a>

### PS-P001｜PowerShell 更改執行原則與虛擬環境啟動前提

[原講義《PowerShell更改執行原則.pdf》第1頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/PowerShell%E6%9B%B4%E6%94%B9%E5%9F%B7%E8%A1%8C%E5%8E%9F%E5%89%87.pdf#page=1)

來源：《PowerShell更改執行原則.pdf》唯一一頁。已同時核讀文字與 Windows 操作截圖。本節記錄操作，不代表本次已對你的電腦變更設定。

#### 老師原文與白話意思

原文：「進入虛擬環境(PowerShell):」「以系統管理身分執行(PowerShell or VScode)」，接著列：

```powershell
# 原稿每行前有 #；以下移除排版提示字元，保留實際指令
set-executionpolicy remotesigned
get-executionpolicy -list
```

白話：講義處理的是 PowerShell 是否允許執行腳本，讓虛擬環境的 PowerShell 啟動腳本能在符合原則的情況下執行。**這兩個指令本身不是建立或啟動虛擬環境的指令。** 此頁沒有展示 `Activate.ps1` 的路徑，也沒有虛擬環境啟動後的終端輸出，不應補稱本頁已操作成功。

#### 圖片中的操作

1. Windows 搜尋結果顯示藍底、白色 `>_` 圖示的 **Windows PowerShell**，下方標示「桌面應用程式」。
2. 右方操作選單有帶盾牌的「**以系統管理員身分執行**」；其下是「開啟檔案位置」。老師要選前者，不是後者。
3. 圖片後方露出 Visual Studio Code，文字也允許以管理員身分啟動 VS Code，但截圖沒有完整展示 VS Code 的選單流程。
4. 頁面沒有顯示執行原則變更確認提示或 `get-executionpolicy -list` 的結果表，不能說原圖已選 Y 或已顯示 RemoteSigned。

#### 指令逐項解釋與必要補充

| 項目 | 意義 | 來源層次 |
|---|---|---|
| `Set-ExecutionPolicy` | 變更 PowerShell 執行原則 | 原稿指令；用途由官方說明核對 |
| `RemoteSigned` | 本機撰寫的腳本不必簽署；標記為網際網路下載的腳本一般需要受信任發行者的簽署，已解除封鎖者另論 | 官方補充，不是原頁已有的完整定義 |
| 未指定 `-Scope` | 預設作用範圍為 `LocalMachine`，影響本機所有使用者；變更此範圍需管理員權限 | 解釋原稿為何要求管理員 |
| `Get-ExecutionPolicy -List` | 列出不同範圍的原則，不是變更原則 | 原稿第二條指令 |
| `Get-ExecutionPolicy` | 不帶 `-List` 時查詢目前有效原則 | 官方補充 |

上述原則、範圍與權限已對照 Microsoft 官方文件。[4]

補充的範圍優先順序是 `MachinePolicy → UserPolicy → Process → CurrentUser → LocalMachine`；群組原則可以覆寫其他範圍。變更命令成功，不代表最後有效原則一定採用該值。`Process` 只限目前工作階段，`CurrentUser` 只影響目前使用者，`LocalMachine` 影響整台電腦，不能把所有變更都當成僅影響當前視窗。[4]

**安全與使用界線：**執行原則不是完整的安全邊界；`RemoteSigned` 也不保證脚本安全。此處忠實保留老師的管理員流程，但不表示所有情況都必須提升權限、修改整台電腦的設定，更不應為了啟動環境就一律改成 `Bypass` 或 `Unrestricted`。[4]

#### 與另一份讲義的關係

搭配《Django平台建置(windows) by venv(P).pdf》閱讀：建立 venv、啟動 venv 與調整 PowerShell 執行原則是不同步驟。CMD 與 PowerShell 的啟動方式也要分清楚，不能只看到 Windows 終端畫面就把指令混用。

原稿參考網址（已取回正文核讀）：
https://learn.microsoft.com/zh-tw/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.4




---

## 補充講義：網頁語言簡介P.pdf（1頁）

<a id="web-p001"></a>

### WEB-P001｜網頁技術全貌：前端、後端、資料庫與伺服器

[原講義《網頁語言簡介P.pdf》第1頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E7%B6%B2%E9%A0%81%E8%AA%9E%E8%A8%80%E7%B0%A1%E4%BB%8BP.pdf#page=1)

來源：《網頁語言簡介P.pdf》唯一一頁。這頁雖能抽出文字，知識重點仍在左右位置、箭頭與分類，已實際看過完整圖面。

#### 圖中整體結構

左側「前端」與中央「後端」之間有藍色垂直虛線；跨越虛線的紅色**雙向箭頭**表示前後端互動。後端與右側 `Database` 間另有紅色雙向箭頭，其下標示 **SQL指令、ORM**。底部左側列瀏覽器，中央列 Web Server，右下寫 MVC、ORM 全名。

將圖轉成文字流程：

```text
瀏覽器解析前端（HTML + CSS + JavaScript）
          ↕ 請求／回應（補充：實際通常以HTTP往返）
後端應用程式（PHP、C#、Java、Python、JavaScript等）
          ↕ SQL指令或ORM
資料庫（關聯式資料庫、圖中另列NoSQL與第三方服務）
```

#### 前端：每種技術負責什麼

| 原圖項目 | 原圖定義／標註 | 白話解釋 |
|---|---|---|
| HTML | 定義網頁內容；黃色底色 | 頁面有哪些標題、文字、表單、連結等結構與內容 |
| JavaScript | 定義網頁行為 | 互動、事件、動態處理等程式行為 |
| VBScript | IE | 原稿列出的舊瀏覽器相關腳本技術，不宜當作跨瀏覽器網頁標準做法 |
| CSS | 定義網頁外觀；黃色底色 | 文字、顏色、大小、間距及版面的樣式 |

「解析前端」的是瀏覽器。原圖列 `chrom`、`edge`、`ie`、`safari`；`chrom` 應是 Chrome 的拼字省漏，前三者與 Safari 並非每一種都能執行 VBScript。圖中 Chrome 以紅字標示。

#### 後端：語言與框架並列

| 原圖文字 | 拆解閱讀 |
|---|---|
| `PHP, Laravel MVC (PHP)` | PHP 為語言；Laravel 為 PHP 框架，圖以 MVC 標示 |
| `ASP.NET, ASP MVC (C#)` | 微軟網站開發技術／框架，圖以 C# 配對 |
| `JSP/Servlet, Spring MVC(JAVA)` | Java 網站技術與 Spring MVC 框架 |
| `Flask, Django MVT (Python)` | Flask、Django 為 Python 網站框架；黃色底色特別強調此列 |
| `Javacript` | 原圖拼字如此，指 JavaScript；可在後端執行，相關環境於下方列 Node.js |

白話：前端把頁面顯示給人看並接收操作；後端負責處理請求與應用邏輯，視需要存取資料庫，再回傳結果。並非每一個網站都必須同時使用表中所有技術。

#### 資料庫與服務分類——保留原稿標籤

| 原圖資料庫 | 原圖規模標籤 | 原圖平台標籤 |
|---|---|---|
| Access | 小型 | Windows |
| SQLite | 小型 | Linux |
| MySQL | 中型 | Linux、Windows |
| MS-SQL | 中型 | Windows Server |
| Oracle | 大型 | Linux |

SQLite、MySQL 兩列以黃色底色強調；MySQL 名稱另用紅字。下方以虛線隔出 `NoSQL`，再以虛線隔出「第三方服務」，列 **Thingspeak**、**firebase**。

**補充／辨析：**上表是老師示意的配對，不是平台支援的完整清單，也不是硬性容量分級；例如 SQLite 不只 Linux 可用。NoSQL 是一類資料庫取向，不是特定一套軟體；ThingSpeak、Firebase 在此被列成第三方服務，不能與上面五個資料庫產品完全等同。

#### Web Server 區塊逐項保留

原圖由上而下列：

- `Node.js (Javacript)`
- `Apache or Nginx(PHP)`
- `IIS(C#)`
- `Tomact(JAVA)`
- `Flask`
- `Django`

其中 Apache、Django 以紅字強調。`Javacript` 是 JavaScript 拼字錯誤，`Tomact` 是 Tomcat 拼字錯誤。

**補充／辨析：**圖為教學簡化，混列執行環境、Web Server、容器與框架。Node.js 是 JavaScript 執行環境；Flask、Django 是框架，不能因為出現在 Web Server 清單就把開發伺服器當成完整正式部署方案。Apache/Nginx 也不只服務 PHP，IIS 與 C#、Tomcat 與 Java 等是常見搭配，不是排他限制。

#### MVC、MVT 與 ORM

- 原圖：`MVC模式:Model–view–controller`，即 Model（資料模型）、View（呈現）、Controller（控制／協調）。
- Django 列標示 `MVT`；與主講義P112–113的 Model/View/Template 分工互相對照，不能把 MVC 的 View 與 Django 的 View 直接当作同一角色。
- 原圖：`ORM: Object Relational Mapping`，物件關聯映射。白話是以程式物件、模型和方法表達資料操作，再由 ORM 對應到資料庫；不是完全不需要理解 SQL 或資料表。
- 圖中 `SQL指令` 與 `ORM` 並列，說明資料存取可直接用 SQL，也可透過 ORM；主講義的原生 SQL CRUD 與 ORM CRUD 即是兩種教法。

本頁只提供知識架構，沒有專案檔、程式碼或安裝指令，不能把它擴寫成老師已要求完成某個專案。




---

## 補充講義：api.pdf（3頁）

<a id="api-p001"></a>

### API-P001｜Client → Web Server → MySQL 的 API 資料流程

[原講義《api.pdf》第1頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/api.pdf#page=1)

來源：《api.pdf》第1頁。全頁是圖表：左側藍色矩形為 Client、右上藍色星形為 Web Server、右下藍色圓柱為 Database。已看過所有箭頭與標籤；文字擷取沒有保留的相對位置在此補回。

#### Client 的六種例子

圖中由上而下列 `Android app`、`App inventor`、`Pi`、`HTML`、`Postman`、`Arduino`。共同角色是請求網站服務的客戶端；不表示它們必須同時存在。**補充：**HTML 是標記語言，這裡可理解為「使用網頁的客戶端」的簡寫，而不是 HTML 本身獨立發送所有請求。

#### 圖中四組箭頭

| 箭頭 | 圖中文字 | 白話意思 |
|---|---|---|
| Client → WEB Server | `url request`、`POST or GET` | 客戶端透過網址，以 GET 或 POST 送出請求 |
| WEB Server → Client | `json decode` | 伺服器送回資料後，客戶端解讀 JSON |
| WEB Server → Database | `insert`、`update`、`delete` | 伺服器處理新增、更新、刪除資料的工作 |
| Database → WEB Server | `select`、`json_encode` | 圖中表示查詢資料回到伺服器，再編碼為 JSON |

Web Server 標為 `Apache or flask`，資料庫標為 `MySQL`。

**重要辨析：**圖中的 `select/json_encode` 放在向上箭頭旁，不表示 MySQL 會自動替所有 API 做 PHP 的 `json_encode()`。較完整的理解是「應用程式發出查詢 → 取得資料庫結果 → 應用程式編碼 JSON → 回傳客戶端 → 客戶端 decode」。圖也把 Apache 與 Flask 並列做示意；前者是 Web Server 軟體，後者是 Python 框架，並非同一層級的產品。

#### 串成完整旅程

1. 客戶端準備 URL 與必要參數，發出 GET／POST。
2. 伺服器端程式判斷請求的功能，必要時對 MySQL 做 `SELECT` 或 `INSERT/UPDATE/DELETE`。
3. 將處理結果整理成 JSON 格式回應。
4. 客戶端解析 JSON，再顯示或進行後續操作。

補充：GET／POST 是 HTTP 方法，不與某一條 SQL 一對一綁定；JSON 是資料交換格式，不是 SQL，也不是加密。實務需另外考慮驗證、授權、輸入檢查、HTTPS及錯誤回應，這些未在原圖實作。本頁沒有提供 endpoint、參數規格、JSON範例、HTTP狀態碼或可執行程式，不能補造後宣稱來自講義。

<a id="api-p002"></a>

### API-P002｜PC 資料服務與 Raspberry Pi＋Python 控制端

[原講義《api.pdf》第2頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/api.pdf#page=2)

來源：《api.pdf》第2頁。此頁把抽象的 Client 換成具體硬體配置。

#### 裝置與部署位置

| 區域 | 圖中元件／位址 | 所扮演角色 |
|---|---|---|
| 右側紅框 | `PC(192.168.58.106)` | 同一台PC內放 Web Server 和 MySQL |
| 紅框上方星形 | `WEB Server (Apache or flask)` | 應用服務 |
| 紅框下方圓柱 | `Database (MySQL)` | 資料庫 |
| 左側大矩形 | `Client PI+Python`，下方 `PI(192.168.58.40)` | Pi 上用Python作為客戶端 |
| 最左小圖示 | `realy` | 與Pi相連的外部設備；原拼字疑應為 relay（繼電器） |

圖片的線條是小圖示與 Pi 相連，沒有標 GPIO 腳位、電壓、負載或接線安全規格；不能將圖當成可直接照接的電路圖。

#### 可見資料方向

- MySQL 向上到 Web Server 的箭頭旁仍是 `select`、`json_encode`。
- Web Server 向左下送回 Pi 的箭頭旁為 `json decode`，表示 Pi 取得資料後解讀 JSON。
- **此頁未畫出 Pi → Server 的請求箭頭。** 可以用第1頁解釋一般請求流程，但不能說本頁已展示輪詢週期、推播或完整双向通訊程式。

依圖合理理解的用途是「Pi 讀取服務提供的資料後，用程式連接／操作外部設備」；具體資料欄位、開關判定與 relay 控制碼並未提供，屬未展示部分。

兩個 IP 是老師架構圖的例子，不是你電腦的位址。圖沒有子網路遮罩，不能僅憑前三段相同就宣稱實際網路設定或防火牆已正確。

<a id="api-p003"></a>

### API-P003｜加入 Android 與 PHP 管理端的多客戶端架構

[原講義《api.pdf》第3頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/api.pdf#page=3)

來源：《api.pdf》第3頁。保留第2頁的 PC、MySQL、Pi及左側 `realy` 連線，再加入 Android 與 PHP+MySQL 客戶端。

#### 所有元件與位置

- PC紅框仍標 `PC(192.168.58.106)`；框內有三個元件：上方 `WEB Server WEB API (Apache)`、下方 `Database (MySQL)`、右側 `Client PHP+MySQL`。
- 左上為 `Client PI+Python`、`PI(192.168.58.40)`，連到最左側 `realy` 圖示。
- 左下新增 `Client Android`，下方標 `手機(192.168.58.x)`。`x` 是示意佔位符，不是可直接使用的 IPv4 位址。

#### 箭頭逐一閱讀

1. **Android → Web API**：斜向右上箭頭，文字 `url request / POST or GET`，表示手機呼叫服務。
2. **Web API → Android**：斜向左下箭頭，文字 `json decode`，表示 Android 端解析收到的資料。
3. **Web API → Pi**：斜向左下箭頭，旁寫 `json decode`，表示 Pi 端也能消費同一類服務資料。
4. **MySQL → Web API**：垂直向上，標 `select / json_encode`，表示查詢結果供 API 組回應；編碼責任的辨析同第1頁。
5. **MySQL → 右側 Client PHP+MySQL**：斜向右上，標 `select`，表示此管理／操作端可讀資料。
6. **右側 Client PHP+MySQL → MySQL**：斜向左下，標 `add`，表示此端可新增資料。
7. Pi仍連到外部 `realy`，但沒有新增控制線細節。

#### 此頁新增的知識

- 同一個資料庫與 Web API 可以服務不只一種客戶端，例如 Android、Pi上的Python。
- PHP+MySQL端在圖中位於PC紅框內，與MySQL直接有讀取／新增箭頭；不要錯寫成圖上所有客戶端都必須先經同一條 API 箭頭。
- 可將「資料來源／管理端」與「讀取資料／裝置控制端」分工：PHP端新增資料，API從資料庫查詢後供手機或Pi使用。這是圖的資料流解讀，原稿未提供實際的時序、同步方式或更新頻率。
- `Client` 是相對角色，PHP程式可相對資料庫扮演客戶端；不代表它一定執行於使用者瀏覽器。
- 此圖沒有 Django 程式碼，不能因它被放在 Django 講義資料夾，就把 Apache/PHP 範例默默改成 Django 已完成的專案。

#### 三頁連貫比較

| 頁碼 | 本頁重點 | 新增資訊 |
|---|---|---|
| API-P001 | 一般 API 流程 | 六種Client、GET/POST、JSON與資料庫CRUD |
| API-P002 | 具體PC與Pi架構 | PC/Pi IP、Pi＋Python、外部relay示意 |
| API-P003 | 多客戶端共享服務 | Android手機、PHP+MySQL端的select/add與共同資料庫 |

全份講義提供的是架構與資料流，沒有可重建完整系統的程式、API契約、資料表定義、硬體接線或認證設定。本筆記保留此界線，不虛構「完成後應出現某畫面」。




---

## 補充講義：資料庫正規化.pdf（53頁）

## 資料庫正規化：第 1–27 頁逐頁詳細筆記

> 來源：`資料庫正規化.pdf`，以 PDF 實際頁序標示。每頁均對照文字層及頁圖閱讀；「原稿」代表講義內容，「補充／勘誤」則為釐清概念，不混作原稿。圖內範例保留原值；未明示的鍵與限制會另外標示推論。本範圍止於第 27 頁。

<a id="db-p001"></a>

### DB-P001｜第四章：資料庫正規化

[原講義《資料庫正規化.pdf》第1頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=1)

- **原稿內容**：章名為「第四章　資料庫正規化」；課程名稱是「資料庫系統」。
- **圖像閱讀**：封面中央為章名，下方「資料庫系統」帶底線。左側圓形與直線、右下角標誌屬投影片版面裝飾，不是實體關係圖或相依性符號。本頁沒有表格、例題、PK／FK 或資料相依箭頭。
- **學習定位**：本章處理關聯式資料庫的資料表結構設計與正規化，不是數值縮放或機器學習的 normalization。

<a id="db-p002"></a>

### DB-P002｜本章學習目標

[原講義《資料庫正規化.pdf》第2頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=2)

**原稿兩項目標**：
1. 讓讀者瞭解資料庫正規化的概念及目的。
2. 讓讀者瞭解資料庫正規化（Normalization）程序及規則。

**讀法補充**：前者回答「為什麼要做」，後者回答「依什麼條件、用什麼步驟來做」。學習時應同時掌握資料重複與異常的成因，以及拆表時的相依性依據，不能只背正規形式名稱。

**圖像閱讀**：本頁僅有標題及編號 1、2 的兩段文字，沒有圖表或隱藏的範例資料。

<a id="db-p003"></a>

### DB-P003｜本章內容與概念順序

[原講義《資料庫正規化.pdf》第3頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=3)

|原稿節次|主題|閱讀重點（補充）|
|---|---|---|
|4-1|正規化的概念|了解這是一種資料模式設計與檢查技術。|
|4-2|正規化的目的|降低資料重複，避免新增、修改、刪除異常。|
|4-3|功能相依（Functional Dependence; FD）|分析哪些屬性可決定哪些屬性。|
|4-4|資料庫正規化（Normalization）|依規則分解關聯，保留重建資訊的能力。|

- **圖像閱讀**：原頁為四行章節目錄，無箭頭、表格或 PK／FK 圖示。以上表格是筆記重排，不是原稿原有表格。
- **術語補充**：Functional Dependence 與 Functional Dependency 在教材語境均指功能相依；縮寫 FD。

<a id="db-p004"></a>

### DB-P004｜前言：不能把全部資料混存或憑直覺拆表

[原講義《資料庫正規化.pdf》第4頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=4)

**原稿論述**：初學者可能以為一張表就能儲存全部資料，或未經完整規劃，僅依直覺把資料任意切成很多小表。這兩種作法都可能浪費儲存空間、造成資料不一致，增加 DBA（原稿稱「資料庫管理師」）的維護困難。因此原稿強調在關聯式資料庫設計前先完成正規化。

**圖像閱讀**：整頁是文字敘述；「DBA（資料庫管理師）」帶底線，末段「正規化（Normalization）」以大字強調，無流程圖或資料表。

**補充／措辭釐清**：原稿說正規化是避免問題的「唯一的方法」，語氣過強。正規化是邏輯資料設計的重要方法，但資料一致性還需要主鍵、外鍵、唯一性與其他約束、交易及正確的應用程式配合。需求分析、綱要設計與正規化通常反覆修正，不必理解為三個完全不可交錯的階段。

<a id="db-p005"></a>

### DB-P005｜4-1 正規化的概念與 Database Schema

[原講義《資料庫正規化.pdf》第5頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=5)

- **資料庫綱要（Database Schema）**：原稿指出，資料庫用來存放資料，因此必須妥善規劃資料庫綱要，且綱要要配合實務需要；設計完成後以正規化的方法論檢視設計是否良好。
- **正規化（Normalization）**：原稿定義為結構化分析與設計中，建構「資料模式」所運用的一項技術。
- **核心目的**：降低資料「重覆性」，避免「更新異常」；原稿進一步列出新增異常、刪除異常與修改異常。
- **圖像閱讀**：本頁全為文字，特別將「資料庫綱要」與「結構化分析與設計」加底線，沒有表格或相依箭頭。

**補充**：綱要描述表、欄位、型別、鍵及約束等結構，不等於某一時刻的實際資料列。原稿的「將重複性的資料剔除」不是任意刪掉同值的資料列，而是讓同一項事實放到適當的表中儲存；仍需保留關聯所用的鍵。重複的欄位值未必是設計錯誤，例如多名學生選同一門課，其課號自然會重複。

<a id="db-p006"></a>

### DB-P006｜4-2 正規化的兩項目的

[原講義《資料庫正規化.pdf》第6頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=6)

**原稿**：正規化的精神，是讓資料庫中重複的欄位資料減到最少，並能快速找到資料，提高關聯式資料庫效能。明列兩項目的：
1. 降低資料重複性（Data Redundancy）。
2. 避免資料更新異常（Anomalies）。

**圖像閱讀**：標題下是一段說明及「【目的】」編號清單；沒有資料表、數據或箭頭。

**補充／效能釐清**：正規化主要改善資料的邏輯一致性與可維護性，不保證每一種查詢都更快。拆表可能增加 JOIN 成本；實際效能仍受索引、資料量、查詢方式與工作負載影響。「重複減少」也不代表所有相同值都應消失。

<a id="db-p007"></a>

### DB-P007｜降低資料重複性：校務系統的學籍資料

[原講義《資料庫正規化.pdf》第7頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=7)

**原稿情境**：校務系統把相同的「學籍資料」分別存於「教務處」與「學務處」。這不僅重複儲存而浪費空間，也使姓名變更時必須同步更改兩處；若有一處漏改，就發生資料不一致。未先規劃正規化，會增加應用系統撰寫難度與資料庫處理負擔，因此降低資料重複性是正規化的重要工作。

**圖像閱讀**：本頁只有完整情境敘述，校務系統、兩處學籍資料等文字帶底線；實際拆表圖在下一頁。

**理解補充**：問題不是教務處、學務處不能共用學生資料，而是「同一學生姓名」不應由兩張業務表各自維護一份事實。共享學籍表後，兩處仍可各自維護其專屬成績欄位。

<a id="db-p008"></a>

### DB-P008｜將兩張表整理為三張表：學籍 PK 與業務表 FK

[原講義《資料庫正規化.pdf》第8頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=8)

**原稿方法**：將教務處與學務處相同的資料項抽出，組成「學籍資料表」；圖中字句是「重複項取出，保留關聯必要欄位」。

**正規化前：教務處資料表**

|學號|姓名|學業成績|
|---|---|---|
|96001|張三|60|
|96002|李四|70|
|96003|王五|80|
|96004|李安|90|

**正規化前：學務處資料表**

|學號|姓名|操行成績|
|---|---|---|
|96001|張三|80|
|96002|李四|93|
|96003|王五|75|
|96004|李安|60|

**正規化後：教務處資料表**

|序號|學號|學業成績|
|---|---|---|
|1|96001|60|
|2|96002|70|
|3|96003|80|
|4|96004|90|

**正規化後：學籍資料表**

|學號|姓名|
|---|---|
|96001|張三|
|96002|李四|
|96003|王五|
|96004|李安|

**正規化後：學務處資料表**

|序號|學號|操性成績（圖中下表原字）|
|---|---|---|
|1|96001|80|
|2|96002|93|
|3|96003|75|
|4|96004|60|

**圖與箭頭逐項解讀**：
- 上方兩張原始表並排，兩表的「學號、姓名」被粗框圈出，表示重複資料項。
- 兩條向下斜箭頭，分別從原表的重複區塊指向下方中央「學籍資料表」，表示抽出共同學生資訊。
- 下方排列為左「教務處資料表」、中「學籍資料表」、右「學務處資料表」。左右業務表移除姓名、保留學號，各增加圖示中的序號欄。
- 圖底的兩條折線箭頭由左右業務表連至中間學籍表，左右標「外鍵」，中央標「主鍵」。亦即 `教務處.學號（FK）→ 學籍.學號（PK）`、`學務處.學號（FK）→ 學籍.學號（PK）`。
- 正規化結果是原稿所稱「將兩個表格切成三個資料表」，不是分割資料列，而是重新安排屬性與事實。

**補充與原稿字樣差異**：上方原表寫「操行成績」，下方小表顯示「操性成績」，應是同一欄位的文字誤植；此處保留差異。圖並未明確標出兩張業務表「序號」是否為主鍵，不把它自行認定為 PK。關聯箭頭也沒有標一對一或一對多，不能單憑這四筆資料推定完整基數限制。

<a id="db-p009"></a>

### DB-P009｜三種資料更新異常的定義

[原講義《資料庫正規化.pdf》第9頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=9)

|種類|原稿說明|概念釐清（補充）|
|---|---|---|
|新增異常（Insert Anomalies）|新增某些資料時必須同時新增其他資料；另一實體資料尚未插入前，無法插入目前實體。|本來可獨立存在的事實，被不當綁在其他實體或事件上。|
|修改異常（Update Anomalies）|修改某些資料時必須一併修改其他資料，否則發生異常。|同一事實散在多列，漏改其中一份便互相矛盾。|
|刪除異常（Delete Anomalies）|原稿先說「刪除某些資料時必須同時刪除其他的資料」，再說刪除單一資料列造成多個實體資訊遺失。|重點是刪除某一事實時，非預期地連帶失去仍應保留的另一項事實。|

**圖像閱讀**：本頁為三段文字定義，無表格與範例。上述表格是筆記重排。

**勘誤式釐清**：「刪除異常」不等於忘記同步刪除其他資料；以原稿後一句「資訊遺失」及第 13 頁案例理解較準確。這裡「資料更新異常」是廣義總稱，涵蓋新增、修改、刪除，不只 SQL 的 UPDATE。

<a id="db-p010"></a>

### DB-P010｜學員課程收費表：只有三個欄位也可能設計不良

[原講義《資料庫正規化.pdf》第10頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=10)

**原稿情境**：某國立大學開設「網路碩士學分班」，其「學員課程收費表」如下。

|學號|課號|學分費|
|---|---|---|
|S0001|C001|3000|
|S0002|C002|4000|
|S0003|C001|3000|
|S0004|C003|5000|
|S0005|C002|4000|

**原稿選課需知／業務規則**：
1. 每一位學員只能選修一門課程。
2. 每一門課程均有收費標準：C001 為 3000 元、C002 為 4000 元、C003 為 5000 元。

**原稿分析**：表格雖僅有三個欄位，仍不是良好儲存結構，因為同一課程費用在多位學員身上重複出現；例為 S0001 與 S0003、S0002 與 S0005。這會造成錯誤或不一致的異常（Anomalies），下頁起分別分析。

**圖像閱讀**：左側為上表，右側為選課需知，下方是說明、例如及「分析：從下一頁開始」。本頁沒有 PK／FK 標記。

**依業務規則的補充推導**：`學號 → 課號`，`課號 → 學分費`，故 `學號 → 學分費`。重複的是「某課號的標準學分費」，不是不同學員各自選課的事實。學號可作本例資料列識別鍵，但這是依規則推導，不是原圖已標主鍵；本例的「只能選一門」也不能套用到所有一般大學選課系統。

<a id="db-p011"></a>

### DB-P011｜新增異常：尚無學員選修的 C004 無處可存

[原講義《資料庫正規化.pdf》第11頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=11)

**原稿說明**：學校要新增 C004 課程，但原表無法立即新增，除非至少有一位學員選修 C004。

**圖內完整資料與標記**：

|圖中記錄編號|學號|課號|學分費|
|---|---|---|---|
|#1|S0001|C001|3000|
|#2|S0002|C002|4000|
|#3|S0003|C001|3000|
|#4|S0004|C003|5000|
|#5|S0005|C002|4000|
|#6（另列於表外，無法新增）|Null|C004|3000|

- 表外第 #6 列是 `Null、C004、3000`，其中 3000 是圖片才有的新增課程費用，不可漏記。
- 左下折線箭頭旁標「無法新增」，朝上方現有表的底部指去；表示嘗試把 #6 插入，但缺少學號。
- **補充**：若學號被選為主鍵，NULL 違反主鍵不得為空的約束；根本問題是把課程存在／定價與學生選課混放，造成無選課者就不能獨立記錄課程。解法不應是虛構一位學員。

<a id="db-p012"></a>

### DB-P012｜修改異常：同課號的費用只改一部分

[原講義《資料庫正規化.pdf》第12頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=12)

**原稿情境**：C002 學分費由 4000 元調整為 4500 元；S0002 的資料改了，但漏改 S0005，造成不一致。

|圖中記錄編號|學號|課號|學分費／圖中註記|
|---|---|---|---|
|#1|S0001|C001|3000|
|#2|S0002|C002|4000 調整 ➜ 4500|
|#3|S0003|C001|3000|
|#4|S0004|C003|5000|
|#5|S0005|C002|4000 忘了調整|

**圖像閱讀**：正文將「4000 元調整為 4500 元」加底線；表內第 #2 列有向右調整箭頭，第 #5 列明寫「忘了調整」。圖下「造成 C002 課程的學分費不一致現象」配折線箭頭指向 #5。

**補充**：依「每門課均有同一收費標準」規則，C002 不應同時對應兩個不同標準費用。若是另行設計的個別折扣或歷史成交價，必須有不同的資料語意與欄位；原例並非這類情況。

<a id="db-p013"></a>

### DB-P013｜刪除異常：退選連帶失去 C003 及其學分費

[原講義《資料庫正規化.pdf》第13頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=13)

**原稿說明**：學員 S0004 退選，而 C003 只有 S0004 選修。若刪掉這一筆記錄，就失去 C003 課程及其學分費資訊。

|圖中記錄編號|學號|課號|學分費|原圖狀態|
|---|---|---|---|---|
|#1|S0001|C001|3000|保留|
|#2|S0002|C002|4000|保留|
|#3|S0003|C001|3000|保留|
|#4|S0004|C003|5000|記錄編號及該列各值均加刪除線|
|#5|S0005|C002|4000|保留|

**圖像閱讀**：下方文字「失去 C003 課程及其相關資訊」旁有向上箭頭，指到被劃掉的 C003 列。第 #4 列同時代表學生選課與課程定價，刪除一列即失去兩類事實。

**補充**：這不是說 S0004 退選後 C003 在真實世界必然取消，而是資料結構無法保留「無人選修但仍存在的課程」。這才是刪除異常。

<a id="db-p014"></a>

### DB-P014｜解決異常：分為選課表與課程收費對照表

[原講義《資料庫正規化.pdf》第14頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=14)

**原稿方法**：將不良的學員課程收費表，依 4-4 節的正規化方法分為「選課表」與「課程收費對照表」，避免前述異常。

**中央原始「課程收費表」**：

|學號|課號|學分費|
|---|---|---|
|S0001|C001|3000|
|S0002|C002|4000|
|S0003|C001|3000|
|S0004|C003|5000|
|S0005|C002|4000|

**左下「選課表」**：

|學號|課號|
|---|---|
|S0001|C001|
|S0002|C002|
|S0003|C001|
|S0004|C003|
|S0005|C002|

**右下「課程收費對照表」**：

|課號|學分費|
|---|---|
|C001|3000|
|C002|4000|
|C003|5000|

**圖像閱讀**：中央原表左右各有一個灰色彎曲向下箭頭，皆標「正規化」，分別指往左下選課表與右下收費對照表。本圖沒有明標 PK／FK，也沒有畫兩張新表之間的關聯線；原例數值恢復為初始狀態，C002 仍為 4000、S0004 仍存在，不是承接前兩頁實際執行修改／刪除後的結果。

**補充：拆表後的鍵與操作**：
- 依每位學員只能選一門課規則，可選 `選課表.學號` 為 PK；`課程收費對照表.課號` 為 PK；`選課表.課號` 為參照後者的 FK。
- 新增課程只在收費對照表新增，例如第 11 頁 `C004、3000`，不用捏造學號。
- 調整 C002 的標準費用只改收費對照表，不再逐一修改每位選課學員的費用副本。
- S0004 退選只刪選課資料，C003 與 5000 的資訊仍可保留。
- 以共同課號連接兩表，可重建原來每位學生及其課程費用。鍵與操作解說屬依原例推導，非圖中原有標記。

<a id="db-p015"></a>

### DB-P015｜4-3 功能相依：欄位之間的決定關係

[原講義《資料庫正規化.pdf》第15頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=15)

**原稿定義**：功能相依（Functional Dependence; FD）是資料表中各欄位間的相依性；原稿以「某欄位不能單獨存在，須與其他欄位一起存在才有意義」來說明。

**學生資料表欄位圖（依圖上從左到右順序）**：

|姓名|學號（底線）|性別|系所|電話|地址|
|---|---|---|---|---|---|

- 圖只有一排欄位，沒有任何學生資料列；學號帶底線，下一頁進一步說明其為主鍵。
- 原稿例解：「姓名」值搭配「學號」才有意義，因此稱「姓名欄位相依於學號欄位」。

**補充／正式定義釐清**：上述「有沒有意義」只是直覺說法，不能作嚴格判定。`X → Y` 是指任何符合業務限制的合法資料中，只要兩列 X 值相同，Y 值也必須相同。換言之，一個 X 值只能決定一個 Y 值；並不是 Y 必須沒有獨立語意，也不表示 Y 不能單獨儲存。「學號 → 姓名」不推出「姓名 → 學號」，因為可以有同名學生。

<a id="db-p016"></a>

### DB-P016｜學號決定學生的其他欄位：FD 圖的箭頭讀法

[原講義《資料庫正規化.pdf》第16頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=16)

**原稿欄位順序**：`姓名｜學號（底線）｜性別｜系所｜電話｜地址`。

**圖像結構**：學號下方接一段垂直線，連到橫向共用線；再分支成向上箭頭，分別指向姓名、性別、系所、電話、地址。箭頭表示這些欄位由學號決定，不是欄位的排列先後，也不是外鍵連線。

**原稿分析逐項整理**：
1. `學號 → 姓名`。
2. `學號 → {姓名，性別，系所，電話，地址}`。
3. 學號為**決定因素**，因為 `學號 → 姓名` 等功能相依成立。
4. 姓名、性別、系所、電話、地址為**相依因素**。
5. 原稿指定「學號」為主鍵，作為唯一辨識該筆記錄的欄位。姓名、地址等欄位均相依於學號。

**補充**：此處假定一個學號在本表中只有一組姓名、性別、系所、電話與地址值。如果需求容許多個電話、雙主修或歷史地址，須另訂結構與時間範圍，不能無條件套用本圖。能決定某欄位的因素不一定就是全表主鍵；本例學號能決定全部屬性且作唯一識別，才有主鍵角色。

<a id="db-p017"></a>

### DB-P017｜功能相依的符號、決定因素與相依因素

[原講義《資料庫正規化.pdf》第17頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=17)

**原稿表示法**：
- 假設資料表 R 含 X、Y、Z 三個欄位，寫成 `R={X,Y,Z}`。
- 若 Y 功能相依於 X，原頁列出兩種寫法：
  1. `Y ∝ X`，旁註「Y 功能相依於 X」。
  2. `X → Y`，旁註「X 決定 Y」。
- `X → Y` 左側 X 稱**決定因素（Determinant）**；右側 Y 稱**相依因素（Dependent）**。

**示意圖**：左邊橢圓為帶底線的「學號（X）」，右邊橢圓為「姓名（Y）」；一條上拱弧形箭頭由左指右，即 `學號（X）→ 姓名（Y）`。它畫的是 FD，而不是兩張表的 ER 關係。

**補充／符號勘誤**：原頁第一式確實使用外形為 `∝` 的符號，常規數學意義是「成正比」，不是資料庫 FD 的標準表示法。為避免與比例關係混淆，正式筆記／作答應使用 `X → Y`，或等價的 `Y ← X`，不要把 `Y ∝ X` 當標準記號。`R(X,Y,Z)` 可更清楚表示關聯綱要；`{X,Y,Z}` 是屬性集合，不是實際資料列集合。

<a id="db-p018"></a>

### DB-P018｜4-3.1 完全功能相依（Full Functional Dependency）

[原講義《資料庫正規化.pdf》第18頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=18)

**原稿核心定義**：在關聯表 `R(X,Y,Z)` 中，已有 `(X,Y) → Z`；若移去 X 或 Y 任一屬性，就無法維持對 Z 的決定關係，則 Z 完全功能相依於 `(X,Y)`。

**原稿例子**：
```text
{學號(X)，課號(Y)} → 成績(Z)
```
- 學號與課號必須共同決定成績，缺一不可。
- 原稿特別測試移除課號 Y：只剩 `學號(X) → 成績(Z)` 不成立。
- 若只知道學號對應的成績，就無法辨別是哪一門課的分數，因此成績完全相依於學號與課號的組合。
- **圖像閱讀**：本頁無資料表、數值或獨立關係圖；以文字、數學箭頭及「⇒這是完全功能相依」呈現。

**補充／精確判定**：完全相依是對左側屬性集合說的。若 `(X,Y) → Z` 成立，但 `X → Z` 與 `Y → Z` 均不成立，才能稱對這個雙屬性集合完全相依。一般形式：`A → B` 且沒有 A 的真子集能決定 B。

**原稿措辭問題**：
1. 原稿寫「從關聯表 R 中移除任一屬性」，容易誤會成真的刪掉欄位；判斷重點是從**決定因素集合**移去屬性後是否仍可決定 Z。
2. 原稿反面敘述「反之，若 `(X,Y) → Z` 存在，我們稱 Z 為部分功能相依」缺少關鍵條件。完全相依本來也有 `(X,Y) → Z`；正確應為移除某些左側屬性後，剩餘真子集仍能決定 Z，才是部分相依。
3. 本頁成績例假定學生可修多門課、同課有多名學生，且同一學號／課號配對只對應一筆成績；不是第 10 頁「每位只能選一門」情境的延伸。若容許重修，還需學期或開課識別等條件。

<a id="db-p019"></a>

### DB-P019｜4-3.2 部份功能相依（Partial Functional Dependency）

[原講義《資料庫正規化.pdf》第19頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=19)

**原稿定義與例子**：在 `R(X,Y,Z)` 中已有 `(X,Y) → Z`，若移去左側屬性後仍可決定 Z，則 Z 部分功能相依於 `(X,Y)`。本頁標題使用「部份」，內文也出現「部分」，兩者指同一概念。

```text
{學號(X)，身份證字號(Y)} → 姓名(Z)
移除身份證字號(Y)後：學號(X) → 姓名(Z) 仍成立
所以：姓名對 {學號，身份證字號} 是部分功能相依
```

**原稿理由**：學號本身已能決定姓名，兩者之間已具有功能相依，不必再把身份證字號一起放在決定因素中。

**圖像閱讀**：本頁為文字與公式，沒有資料列或獨立相依圖；「⇒這是部分功能相依」接在例式後。

**補充／定義釐清**：
- 部分相依只需存在某個真子集仍能決定右側屬性，不要求移去任何一個左側屬性都仍成立；原稿「任一」一詞易有歧義。
- 移去 Y 後應檢查 `X → Z`，不是仍原樣寫 `(X,Y) → Z`。原稿定義段未改變公式，是表達不精確；例子段已正確寫出 `(X) → Z`。
- 這個例子證明姓名對指定集合 `{學號，身份證字號}` 是部分相依，但這個集合未必是候選鍵。若學號本身已能唯一識別學生，這個雙屬性集合是冗餘的超鍵，而非最小候選鍵；不能據此例單獨判定某表違反 2NF。

<a id="db-p020"></a>

### DB-P020｜4-3.3 遞移相依（Transitive Dependency）

[原講義《資料庫正規化.pdf》第20頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=20)

**原稿定義**：兩個欄位間並非直接相依，而是借第三個欄位達成資料相依。

**公式與方向**：
```text
Y 相依於 X：X → Y
Z 相依於 Y：Y → Z
由此得到： X → Z
亦即 Z 遞移相依於 X
```

**圖像閱讀**：圖外左上標 R，裡面橫排三個灰色圓角框 `X、Y、Z`。下方兩條彎曲箭頭分別為 `X → Y` 與 `Y → Z`；上方跨過 Y 的大弧線從 X 指到 Z，表示經由中間 Y 推得 `X → Z`。圖中的灰影只是裝飾，不是第四個節點，也沒有反向箭頭。

**補充**：`X → Y` 與 `Y → Z` 推得 `X → Z` 是功能相依的遞移律。原稿的「不是直接相依」應理解為「可經中介欄位推得」，不代表 `X → Z` 不成立。進一步判定 3NF 違規時，還要考察決定因素是否超鍵、相依屬性是否為主屬性等條件，不是看到任何箭頭鏈就一定違反 3NF。

<a id="db-p021"></a>

### DB-P021｜遞移相依實例：課程代號、老師編號、老師姓名

[原講義《資料庫正規化.pdf》第21頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=21)

**原稿的兩個功能相依**：
1. `課程代號 → 老師編號`。
2. `老師編號 → 老師姓名`。
3. 因此 `課程代號 → 老師姓名` 是透過老師編號得到的遞移相依。

**完整圖像解讀**：下半部有三個灰色圓角框，左至右為「課程代號」「老師編號」「老師姓名」。下方兩條彎曲箭頭由課程代號指向老師編號，再由老師編號指向老師姓名；上方大弧線直接跨至老師姓名，上方標籤為「遞移相依性」。沒有表格資料列，沒有 PK／FK 或底線鍵標示。

**原稿文字理由**：課程代號可決定老師編號，而老師編號又可決定老師姓名，所以課程代號與老師姓名之間存在遞移相依性。

**補充與適用假設**：例子假定每個課程代號只對應一位授課老師，老師編號也唯一對應其姓名。若同一課程多人合授，或不同學期由不同老師授課，第一個 FD 可能不成立，應另有開課班別、學期或授課關聯表。此頁尚未拆表；可將「課程—老師編號」與「老師編號—姓名」分開理解，替後續正規化建立依據，但不要誤認原圖已畫出兩張新表。

<a id="db-p022"></a>

### DB-P022｜4-4 正規化與無損失分解（Lossless decomposition）

[原講義《資料庫正規化.pdf》第22頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=22)

**原稿定義**：原先關聯（表格）的所有資訊，經「分解」後，仍可由數個新關聯經「合併」得到相同資訊，稱為「無損失分解」的觀念。

**原稿公式**：將 R 分解成 `R1, R2, …, Rn` 後，能透過合併重建：
```text
R = R1 ⋈ R2 ⋈ … ⋈ Rn
```

**圖像逐項解讀**：
- 左邊單一 R 向右上 R1、正右 R2、右下 Rn 各畫一支箭頭，三支箭頭旁均標「分解」。R2 與 Rn 中間的垂直省略符號表示還可有其他新關聯。
- 中間空心粗箭頭向右，導向重建公式。
- 右邊公式 `R=R1⋈R2⋈…⋈Rn` 的連接符號上方標「合併」。圖不是 R 與各表的雙向外鍵連線。

**補充／概念精確化**：
- `⋈` 是關聯代數的 JOIN（此處可理解為以共同屬性做自然連接），不是把資料列上下接在一起的 UNION。
- 無損是重建後**恰好**等於原關聯：不遺失原資料，也不生出原本不存在的假配對資料列。
- 正規化是一系列依相依性與正規形式改善綱要的設計方法；無損分解是拆表的重要要求，但只滿足無損，不代表已達任一指定的高階正規形式。
- 若以二元分解 `R1、R2` 分析，在 FD 情境中常用判準是共同屬性能決定 R1 或 R2 的全部屬性；這是補充判準，原頁未列。

<a id="db-p023"></a>

### DB-P023｜無損分解實例：ABC → AB 與 BC → ABC

[原講義《資料庫正規化.pdf》第23頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=23)

**左側原關聯**：

|A|B|C|
|---|---|---|
|1|2|3|
|4|5|6|
|7|3|8|

**中上分解表 AB**：

|A|B|
|---|---|
|1|2|
|4|5|
|7|3|

**中下分解表 BC**：

|B|C|
|---|---|
|2|3|
|5|6|
|3|8|

**右側合併結果**：

|A|B|C|
|---|---|---|
|1|2|3|
|4|5|6|
|7|3|8|

**圖像／鍵標示忠實記錄**：
- 左 ABC 的 A、B 有實線底線；中上 AB 的 A 有實線底線、B 下方是斷續底線；中下 BC 的 B 有實線底線；右 ABC 的 A、B 有實線底線，C 均無底線。
- 左表有兩支向右斜箭頭，分別指向中上 AB 與中下 BC，旁標「分解」；兩張中間表再分別以箭頭指向右側 ABC，旁標「合併」。
- 本頁沒有鍵符號圖例或明寫 PK／FK，故底線形式照錄，不逕自斷言兩條獨立底線必定表示兩個候選鍵或一個複合主鍵；中上 B 的斷線可與外鍵概念對照，但原頁未明定。

**如何重建（補充解說）**：以共同欄位 B 做相等配對：AB 的 `(1,2)` 對到 BC 的 `(2,3)`，得到 `(1,2,3)`；同理 `(4,5)` 對 `(5,6)` 得 `(4,5,6)`；`(7,3)` 對 `(3,8)` 得 `(7,3,8)`。比的是兩表同名的 B 欄，不能因其他欄同樣出現 3 就錯配。

**Python 驗算**：已以原值執行投影與依 B 連接，得到 `[(1,2,3),(4,5,6),(7,3,8)]`，與原關聯比較為 `matches_original: true`。第 14 頁選課／收費兩表亦以課號連接驗算，得到原五列，`matches_original: true`。以上均為本機列表運算，沒有連線真實資料庫。

**原稿下方註解**：
- 「分解」：透過「正規化」技術，把一個大資料表分割成二個小資料表，本章介紹。
- 「合併」：透過「合併」理論，把數個小資料表整合成一個大資料表，第八章介紹。

**補充限制**：這個資料快照可以正確還原，不表示任意 ABC 資料都能無損分成 AB、BC；一般保證仍需相應 FD／鍵限制，避免同一 B 出現多個互不相屬的 A、C 而產生假配對。

<a id="db-p024"></a>

### DB-P024｜4-4.1 正規化示意圖：依規則逐步降低重複

[原講義《資料庫正規化.pdf》第24頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=24)

**原稿敘述**：對「非正規化」原始資料表，進行一連串「分割」，形成數個「不重複」儲存的資料表。利用「正規化的規則」循序漸進，將重複性高的資料表分成重複性低或沒有重複性的表。

**圖像完整結構**：
```text
未經過正規化的資料表
（重複儲存的資料表）
          │ 分割
          ├─ 資料表 1（不重複儲存）
          ├─ 資料表 2（不重複儲存）
          └─ ……資料表 N（不重複儲存）
```
上方是一個大型灰底框；下方實際畫出的框標「資料表 1」「資料表 2」「資料表 N」，2 與 N 之間有水平省略點，表示不限於畫出的表。連線為分支線，沒有逐階 1NF／2NF／3NF 標籤，也沒有資料欄位、資料列或 PK／FK。

**補充**：圖上的「不重複」應理解為減少重複維護同一事實，而不是禁止重複的外鍵值。正規化不是「表越多越好」，也不是每次分割就自動達到下一階；每一個結果表都須按相依性、鍵及該階規則檢查，並確認可無損重建。

<a id="db-p025"></a>

### DB-P025｜4-4.2 正規化規則與正規形式的包含關係

[原講義《資料庫正規化.pdf》第25頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=25)

**原稿引言**：
- 資料庫正規化有一些規則，每條規則稱為「正規形式」。
- 符合第一條規則，稱「第一正規化形式（1NF）」；符合前二條規則，視為「第二正規化形式（2NF）」。
- 原稿說正規化「最多可以進行到第五正規化形式」，且「在實務上，BCNF 被視為大部分應用程式所需的最高階正規形式」。

**圖像閱讀：下方灰底套疊矩形**：由外至內的標籤依序為：
```text
非正規化
  1NF
    2NF
      3NF
        BCNF
          4NF
            5NF
```
沒有轉換箭頭；框層層內縮表示條件逐漸嚴格，高階的資料表也須符合較低階條件。BCNF 在 3NF 內側、4NF 外側；5NF 位於最內層。矩形陰影是版面效果，並非額外階級。

**補充／原稿說法界線**：
- 正規形式不是單看「做了幾次拆表」，而是每一階的一組邏輯條件；通常是對關聯綱要／資料表判定，再討論整個資料庫。
- 「最多到 5NF」是本教材介紹範圍的簡化，不是資料庫理論的絕對上限，另有其他正規形式。
- BCNF 是重要設計目標，但不是所有應用的固定最高要求；有多值或連接相依的需求仍可能考慮更高階，且有時需權衡相依保留等設計性質。
- 外框若把「非正規化」嚴格解釋成「不符合 1NF 的關聯」，便不應包含 1NF；此圖宜讀作「原始資料與逐級正規化的示意範圍」，不要把最外框當成精確的集合定義。

<a id="db-p026"></a>

### DB-P026｜正規化循序漸進：高階必須滿足低階條件

[原講義《資料庫正規化.pdf》第26頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=26)

**原稿圖像**：上方再次放大展示第 25 頁的套疊圖；由外至內仍是「非正規化、1NF、2NF、3NF、BCNF、4NF、5NF」。圖中無英文全名、例題數值、鍵或箭頭，只有上述名稱／縮寫與矩形包含關係。

**原稿文字結論**：正規化是循序漸進的過程。資料表必須滿足第一正規化條件後，才能進行第二正規化；換句話說，第二正規化必須建立在符合第一正規化的資料表上，其後依此類推。

**補充：將包含關係寫成條件蘊含**：
```text
5NF ⇒ 4NF ⇒ BCNF ⇒ 3NF ⇒ 2NF ⇒ 1NF
```
這是「符合條件」的方向；學習或轉換流程則常從 1NF 往更高階走。符合 1NF 並不自動符合 2NF，符合 3NF 也不保證 BCNF。若一開始就設計出滿足更高階條件的表，並不一定要實際製造每一個中間版本；原稿強調的是條件累積與檢查次序。

**術語對照（補充，非本頁原有英文）**：NF 為 Normal Form；1NF／2NF／3NF／4NF／5NF 分別為 First／Second／Third／Fourth／Fifth Normal Form，BCNF 為 Boyce–Codd Normal Form。

<a id="db-p027"></a>

### DB-P027｜正規化步驟總圖：每一階轉換要處理什麼

[原講義《資料庫正規化.pdf》第27頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=27)

**原稿開場**：在 1NF 到 BCNF 的正規化過程中，每個階段都以欄位「相依性」作為分割資料表的依據之一；圖列出完整正規化步驟。

**流程圖逐項忠實轉錄**：

|左側起點|右側虛線連到的原稿處理條件|左側下一階|
|---|---|---|
|未經正規化的關聯表|除去重複群|第一正規化型式|
|第一正規化型式|除去部分相依|第二正規化型式|
|第二正規化型式|除去遞移相依|第三正規化型式|
|第三正規化型式|除去其他因功能相依所造成的異常|Boyce-Codd 正規化型式|
|Boyce-Codd 正規化型式|除去多值相依|第四正規化型式|
|第四正規化型式|除去剩下所有的異常|第五正規化型式|

**圖像結構與箭頭**：
- 左側為一串垂直排列、帶黑色陰影的圓角／切角框，由「未經正規化」依序往下走到「第五正規化型式」。原圖拼字為 `Boyce-Codd`。
- 相鄰左側框以向下實線箭頭串連，代表逐階轉換。
- 每個轉換箭頭中段都有一條水平虛線連到右側處理條件框；虛線是註解連線，不是外鍵，也不是另一條可以跳級走的流程。
- 本圖不含實體資料表、PK／FK、數值例題；「第一…第五正規化型式」的「型式」保留原稿用字。

**逐階理解（補充；避免把原圖口訣當完整定義）**：
1. **未正規化 → 1NF**：處理重複群，使每個欄位值符合所選資料域的原子性；不是把所有相同的值都刪掉。
2. **1NF → 2NF**：去除非主屬性對候選鍵真子集的部分功能相依；教材常以複合主鍵說明，正式判斷不能忽略其他候選鍵。
3. **2NF → 3NF**：教材用「去除遞移相依」概括。嚴格而言，對每個非平凡 FD `X → A`，X 為超鍵或 A 為主屬性即可符合 3NF；不是任何遞移律的使用都不允許。
4. **3NF → BCNF**：原圖寫去除其他 FD 異常；更精確的條件是每個非平凡 FD 的決定因素都必須是超鍵。不是所有決定因素都必須是最小候選鍵，超鍵也可以。
5. **BCNF → 4NF**：原圖口訣為「除去多值相依」。精確而言，是每個非平凡多值相依的決定因素須為超鍵，不是完全禁止任何多值相依。
6. **4NF → 5NF**：原圖寫「除去剩下所有的異常」，這過度概括。5NF 針對連接相依（join dependency），要求非平凡連接相依由候選鍵所蘊含；並不保證任何業務、交易、併發或程式問題都消失。

**範圍提醒**：本筆記至第 27 頁為止；本頁是流程總覽，沒有借用後續頁面的實例冒充本頁內容。判斷練習應回到三件事：業務規則是否成立、決定因素與候選鍵是什麼、拆分後能否無損重建。


## 資料庫正規化逐頁詳細筆記（第28–53頁）

來源：`資料庫正規化.pdf`。以下頁碼為 PDF 頁序。每頁均以頁圖核讀，文字層僅輔助；「原稿」忠實保留教材主張與數據，「補充／辨正」另行說明，避免把教材簡化說法當成完整形式定義。表格代碼及學號前導零均保留。PK＝主鍵；FK＝外鍵。

<a id="db-p028"></a>

### DB-P028｜正規化步驟：1NF、2NF、3NF

[原講義《資料庫正規化.pdf》第28頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=28)

本頁為「正規化步驟〈續〉」，純文字列出前三階，沒有資料表或關係圖。

1. **第一正規化（First Normal Form；1NF）**：原稿記載由 E.F.Codd 提出。所有記錄的屬性內含值都是**基元值（Atomic Value）**，亦即沒有重覆項目群。重點是每個儲存格放一個值，而不是在同一格放一組課程。
2. **第二正規化（Second Normal Form；2NF）**：原稿記載由 E.F.Codd 提出。先符合 1NF，且每一非鍵值欄位都「完全功能相依」於主鍵；不可只「部分功能相依」於主鍵。圖中文字特別把「主鍵」加底線。
3. **第三正規化（Third Normal Form；3NF）**：原稿記載由 E.F.Codd 提出。先符合 2NF，且每一非鍵值欄位不「遞移相依」於主鍵，也就是去除遞移相依問題。

**理解順序**：1NF 處理一格多值／重覆群；2NF 處理只依賴複合鍵一部分的欄位；3NF 處理透過其他非鍵屬性間接依賴鍵的欄位。

**補充／辨正**：本頁採「主鍵」的入門表述；完整判定須考慮所有候選鍵與非主屬性（不屬於任何候選鍵的屬性）。不能只換一個主鍵就認定部分相依消失。正式 3NF 條件為每個非平凡 FD `X → A`，至少滿足 `X` 是超鍵，或 `A` 是主屬性。

<a id="db-p029"></a>

### DB-P029｜正規化步驟：BCNF、4NF、5NF

[原講義《資料庫正規化.pdf》第29頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=29)

本頁續列後三階，沒有表格或相依箭頭圖。

| 型式 | 原稿提出者 | 原稿規則 |
|---|---|---|
| Boyce-Codd 正規化型式（Boyce-Codd Normal Form；BCNF） | R.F. Boyce 與 E.F.Codd 共同提出 | 符合 3NF，且每一決定因素（Determinant）皆是候選鍵 |
| 第四正規化（Fourth Normal Form；4NF） | R. Fagin | 符合 BCNF，再除去所有多值相依 |
| 第五正規化（Fifth Normal Form；5NF） | R. Fagin | 符合 4NF，且沒有合併相依 |

**補充／辨正（非原稿原文）**：
- BCNF 的精確說法是：每個**非平凡**功能相依 `X → Y` 的決定因素 `X` 都是**超鍵**；候選鍵是最小超鍵，因此「皆是候選鍵」並非最精確的普遍定義。
- 4NF 不是禁止所有多值相依，而是要求每個**非平凡**多值相依 `X ↠ Y` 的 `X` 都是超鍵。
- 原稿「合併相依」指 Join Dependency，亦常稱聯結相依。5NF 不是完全沒有聯結相依，而是其聯結相依均可由候選鍵所蘊涵。本頁僅總覽，尚無 4NF／5NF 的數據案例。

<a id="db-p030"></a>

### DB-P030｜第一正規化定義與學生選課原始報表

[原講義《資料庫正規化.pdf》第30頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=30)

章節：**4-4.3 第一正規化（1NF）**。定義為資料表所有記錄之屬性內含值都是基元值（Atomic Value），亦即無重覆項目群。

**表4-1(a)：某某科技大學「學生選課資料表」**。圖是分組報表，不是每列都重覆學生欄位的平面關聯表；每位學生上方先列學號、姓名、性別，下方列該生多門選課。完整內容如下。

學生：**學號 `001`；姓名「李碩安」；性別「男」**。

| 課程代碼 | 課程名稱 | 學分數 | 必選修 | 成績 | 老師編號 | 老師姓名 |
|---|---|---|---|---|---|---|
| C001 | 程式語言 | 4 | 必 | 74 | T001 | 李安 |
| C002 | 網頁設計 | 3 | 選 | 93 | T002 | 張三 |

學生：**學號 `002`；姓名「李碩崴」；性別「男」**。

| 課程代碼 | 課程名稱 | 學分數 | 必選修 | 成績 | 老師編號 | 老師姓名 |
|---|---|---|---|---|---|---|
| C002 | 網頁設計 | 3 | 選 | 63 | T002 | 張三 |
| C003 | 計概 | 2 | 必 | 82 | T003 | 李四 |
| C005 | 網路教學 | 4 | 選 | 94 | T005 | 王五 |

**讀圖重點**：學生表頭與課程明細是兩個不同層次；同一個學生擁有多筆課程明細。`C002` 出現在兩位學生名下，課程及教師資料相同，但成績為 `93` 與 `63`。因此成績不是單靠課程代碼就能決定。此報表尚未標示 PK／FK；後續頁才將它轉成未正規化二維表並展開。

<a id="db-p031"></a>

### DB-P031｜由分組報表轉為未正規化二維表

[原講義《資料庫正規化.pdf》第31頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=31)

上半頁重現表4-1(a)，數據逐筆與 P030 相同：`001／李碩安／男` 下列 `C001／程式語言／4／必／74／T001／李安`、`C002／網頁設計／3／選／93／T002／張三`；`002／李碩崴／男` 下列 `C002／網頁設計／3／選／63／T002／張三`、`C003／計概／2／必／82／T003／李四`、`C005／網路教學／4／選／94／T005／王五`。

右側粗灰色彎箭頭從上方報表指向下方的**表4-1(b)：未正規化的資料表／學生選課資料報表**，表示將原始報表改用二維表格儲存，**還不代表已完成 1NF**。下表用 `<br>` 保留原圖同一格內的上下排列；各多值欄位依同一順序配對。

| 學號 | 姓名 | 性別 | 課程代碼 | 課程名稱 | 學分數 | 必選修 | 成績 | 老師編號 | 老師姓名 |
|---|---|---|---|---|---|---|---|---|---|
| 001 | 李碩安 | 男 | C001<br>C002 | 程式語言<br>網頁設計 | 4<br>3 | 必<br>選 | 74<br>93 | T001<br>T002 | 李安<br>張三 |
| 002 | 李碩崴 | 男 | C002<br>C003<br>C005 | 網頁設計<br>計概<br>網路教學 | 3<br>2<br>4 | 選<br>必<br>選 | 63<br>82<br>94 | T002<br>T003<br>T005 | 張三<br>李四<br>王五 |

**結構問題**：一名學生一列，但課程代碼至老師姓名的七個欄位都容納整組明細，單一儲存格不再只有一個基元值。圖中未標 PK／FK。

<a id="db-p032"></a>

### DB-P032｜重複資料項目及未達1NF的缺點

[原講義《資料庫正規化.pdf》第32頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=32)

本頁再列 P031 的表4-1(b)，所有欄位與值均相同。兩個粗黑圓角框分別框住 `001` 的兩門課、`002` 的三門課，範圍均從「課程代碼」到「老師姓名」，框下註記**重複資料項目**。學生欄位（學號、姓名、性別）不在框內。

- `001／李碩安／男`：`(C001, 程式語言, 4, 必, 74, T001, 李安)`、`(C002, 網頁設計, 3, 選, 93, T002, 張三)`。
- `002／李碩崴／男`：`(C002, 網頁設計, 3, 選, 63, T002, 張三)`、`(C003, 計概, 2, 必, 82, T003, 李四)`、`(C005, 網路教學, 4, 選, 94, T005, 王五)`。

**原稿說明**：許多屬性的內含值有兩個或以上的值，是尚未進行第一正規化。課程代碼、課程名稱、學分數、必選修、成績、老師編號、老師姓名這七個欄位的長度無法確定，因為無法預先知道每名學生選修多少門課（本例李碩安選兩門、李碩崴選三門）；若為七欄預留很大的空間，就會浪費儲存空間。

**補充**：這裡的「重複資料項目」是**同一列中的重覆群／多值結構**，不是說相同文字不能出現在不同列。儲存空間是否真的預留取決於實作；1NF 的核心是資料結構與基元值，不是要求 SQL 欄位都使用固定長度型別。

<a id="db-p033"></a>

### DB-P033｜第一正規化的三項規則與相依性

[原講義《資料庫正規化.pdf》第33頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=33)

本頁純文字列出規則，並用底線強調基元值、無完全重覆記錄及成績的複合相依。

1. 每個欄位只能有一個基元值（Atomic），即單一值；例如「課程名稱」欄位不能存放兩科或更多科的名稱。
2. 不存在兩筆或以上完全重覆的資料。這是**整列不得完全相同**，不是任何欄位都不得重覆。
3. 資料表中有主鍵，其他所有欄位都相依於主鍵。

原稿列出三組關係，可寫為：

```text
學號 → 姓名、性別
課程代碼 → 課程名稱、學分數、必選修、老師編號、老師姓名
(學號, 課程代碼) → 成績
```

**解釋**：姓名、性別可由學號決定；課程資訊可由課程代碼決定；成績要同時知道學生及課程。全表用 `(學號, 課程代碼)` 作複合主鍵時能決定所有欄位，但仍存在只相依於主鍵一部分的欄位，故符合 1NF 不等於符合 2NF。本頁最後提示下一頁深入探討成績相依。

**補充**：此處規則採關聯模型教學說法；不要誤以為只要宣告 SQL `PRIMARY KEY` 就已證明所有欄位都是基元值。

<a id="db-p034"></a>

### DB-P034｜成績為何不能單獨存在或只搭配課程

[原講義《資料庫正規化.pdf》第34頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=34)

頁首提問：「為什麼『成績』欄位一定要相依於『學號』與『課程代碼』欄位？」本頁前兩種分析如下。

**分析一：只有成績。**

| 成績 |
|---|
| 74 |
| 93 |

圖以左右大括號包住兩個分數，灰色對話框箭頭指向分數並寫「沒有意義」。原稿意思是缺少學生及課程識別，無法知道是哪一位學生的哪一門課。

**分析二：只有課程代碼與成績。**

| 課程代碼 | 成績 |
|---|---|
| C001 | 74 |
| C002 | 93 |

下方圖同樣用大括號框成績欄、灰色箭頭註記「沒有意義」。知道課程，仍不知道分數屬於哪位學生。內文稱「課程編號」，表頭用「課程代碼」，本例指同一識別欄位。

**補充／辨正**：「沒有意義」是指不足以表示本案例的一筆**學生個別修課成績**，不是說數字或課程統計在所有情境都沒有意義。FD 應由業務規則決定，不能因這兩列課程代碼剛好不同，就宣稱一般情況有 `課程代碼 → 成績`。

<a id="db-p035"></a>

### DB-P035｜成績必須由學號與課程共同決定

[原講義《資料庫正規化.pdf》第35頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=35)

**分析三：只有學號及成績。**

| 學號 | 成績 |
|---|---|
| 001 | 74 |
| 001 | 93 |

成績欄旁的大括號及灰色對話框寫「沒有意義」，表示雖然知道學生，卻不知道是哪門課的成績。同一學號對應不同成績，也直接顯示本例不能使用 `學號 → 成績`。

**分析四：學號、課程代碼及成績一起儲存。**

| 學號 | 課程代碼 | 成績 |
|---|---|---|
| 001 | C001 | 74 |
| 001 | C002 | 93 |

下圖成績欄仍有大括號，但較大的灰色對話框改標「有意義」。此時能明確讀出 `001` 修 `C001` 得 `74`、修 `C002` 得 `93`。原稿內文稱「課程編號」，表頭仍用「課程代碼」。

**結論**：`(學號, 課程代碼) → 成績`；在教材業務假設下，成績完全功能相依於兩欄組合。**補充**：若實務允許跨學期重修、同課多班或多次成績，必須再加入學期、開課班別等識別，不能直接沿用本例兩欄鍵。

<a id="db-p036"></a>

### DB-P036｜1NF作法第一步：找出重覆群

[原講義《資料庫正規化.pdf》第36頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=36)

原稿總作法：「將重複的資料項分別儲存到不同的記錄中，並加上適當的主鍵。」本頁執行**步驟一：檢查是否存在『重複資料項』**。

圖名「未經正規化前的學生選課表」。欄位為學號、姓名、性別、課程代碼、課程名稱、學分數、必選修、成績、老師編號、老師姓名。圖中以課程名稱旁的大括號包住每位學生的多門課，再以氣泡連到上方雲狀註記「重複資料項目」。

| 學生（學號／姓名／性別） | 同一列中重覆的課程群（課程代碼／課程名稱／學分數／必選修／成績／老師編號／老師姓名） |
|---|---|
| 001／李碩安／男 | C001／程式語言／4／必／74／T001／李安<br>C002／網頁設計／3／選／93／T002／張三 |
| 002／李碩崴／男 | C002／網頁設計／3／選／63／T002／張三<br>C003／計概／2／必／82／T003／李四<br>C005／網路教學／4／選／94／T005／王五 |

**操作要點**：不只分開課程名稱；課程代碼、學分、必選修、分數及老師資訊也要跟同一門課一起展開，否則會破壞各欄原有對應關係。

<a id="db-p037"></a>

### DB-P037｜1NF作法第二步：展開成不同記錄並選複合主鍵

[原講義《資料庫正規化.pdf》第37頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=37)

上圖仍是 P036 的未正規化資料，`001` 的「程式語言／網頁設計」被粗框圈起，標「重複資料項」。右側粗彎箭頭往下，標「儲存到不同的記錄」，指向下圖中分成兩列的這兩門課。上圖 `002` 的三門課也依同樣方式展開。

**下圖：經過正規化後的學生選課表（1NF）**。

| 學號（PK之一） | 姓名 | 性別 | 課程代碼（PK之一） | 課程名稱 | 學分數 | 必選修 | 成績 | 老師編號 | 老師姓名 |
|---|---|---|---|---|---|---|---|---|---|
| 001 | 李碩安 | 男 | C001 | 程式語言 | 4 | 必 | 74 | T001 | 李安 |
| 001 | 李碩安 | 男 | C002 | 網頁設計 | 3 | 選 | 93 | T002 | 張三 |
| 002 | 李碩崴 | 男 | C002 | 網頁設計 | 3 | 選 | 63 | T002 | 張三 |
| 002 | 李碩崴 | 男 | C003 | 計概 | 2 | 必 | 82 | T003 | 李四 |
| 002 | 李碩崴 | 男 | C005 | 網路教學 | 4 | 選 | 94 | T005 | 王五 |

圖中「學號」「課程代碼」以粗體底線標成主鍵欄位；兩者是**同一個複合主鍵**，不是各自唯一。第一、第二列從學號至課程名稱以粗框強調，對應上方的一組多值資料。此步新增記錄、重覆填入相應學生基本資料，但沒有憑空新增課程或改分數。

<a id="db-p038"></a>

### DB-P038｜1NF結果與複合鍵到成績的箭頭

[原講義《資料庫正規化.pdf》第38頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=38)

本頁再次列出 P037 完整五列十欄資料，數據未變；依列為：

```text
001, 李碩安, 男, C001, 程式語言, 4, 必, 74, T001, 李安
001, 李碩安, 男, C002, 網頁設計, 3, 選, 93, T002, 張三
002, 李碩崴, 男, C002, 網頁設計, 3, 選, 63, T002, 張三
002, 李碩崴, 男, C003, 計概,     2, 必, 82, T003, 李四
002, 李碩崴, 男, C005, 網路教學, 4, 選, 94, T005, 王五
```

**箭頭及框線**：學號與課程代碼的表頭各被粗黑框圈起，上方括接線把兩欄合成一組，再延伸向右，以向下箭頭指向也被粗框圈住的「成績」，即 `(學號, 課程代碼) → 成績`。不是兩個欄位各自都能決定成績。

**原稿結論**：第一正規化後每欄只能有一個資料（基元值）；雖然記錄數增加，但每個欄位的「長度」及「數目」都可以固定。以課程代碼加學號當主鍵，便於查詢某生某課的成績。

**補充**：固定的是綱要及每欄的資料意義，不必一律使用固定長度字串；查詢效能仍受索引及資料量影響。1NF 尚未消除跨列冗餘：例如兩列 `C002` 重覆課名、學分與老師，正是下一節 2NF 要處理的結構問題。

<a id="db-p039"></a>

### DB-P039｜1NF後的新增異常與實體完整性

[原講義《資料庫正規化.pdf》第39頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=39)

章節：**4-4.4 第二正規化（2NF）**。原稿先指出 1NF 後仍有大量重覆資料，浪費空間且易有新增、刪除、更新異常。本頁示範 **Insert Anomaly（新增異常）**。

圖中在原五列左側加「記錄」編號；編號是說明用行號，不是本例另設的主鍵。

| 記錄 | 學號 | 姓名 | 性別 | 課程代碼 | 課程名稱 | 學分數 | 必選修 | 成績 | 老師編號 | 老師姓名 |
|---|---|---|---|---|---|---|---|---|---|---|
| #1 | 001 | 李碩安 | 男 | C001 | 程式語言 | 4 | 必 | 74 | T001 | 李安 |
| #2 | 001 | 李碩安 | 男 | C002 | 網頁設計 | 3 | 選 | 93 | T002 | 張三 |
| #3 | 002 | 李碩崴 | 男 | C002 | 網頁設計 | 3 | 選 | 63 | T002 | 張三 |
| #4 | 002 | 李碩崴 | 男 | C003 | 計概 | 2 | 必 | 82 | T003 | 李四 |
| #5 | 002 | 李碩崴 | 男 | C005 | 網路教學 | 4 | 選 | 94 | T005 | 王五 |

下方嘗試鍵入第 `#6` 筆：

| 記錄 | 學號 | 姓名 | 性別 | 課程代碼 | 課程名稱 | 學分數 | 必選修 | 成績 | 老師編號 | 老師姓名 |
|---|---|---|---|---|---|---|---|---|---|---|
| #6 | NULL | （空白） | （空白） | C004 | 系統分析 | （空白） | （空白） | （空白） | NULL | （空白） |

**圖示**：左側從 `#6` 彎向上方表格的線箭頭被叉號擋住，直排文字「無法新增」。原圖只在學號及老師編號明寫 `NULL`；其餘未填格在筆記標「空白」，不擅自把所有空白改寫成 `NULL`。

**原因**：還沒有人選修 `C004／系統分析`，無法提供學號；但主鍵是 `(學號, 課程代碼)`，任何主鍵組成欄位都不能為 `NULL`，違反**實體完整性規則**。因此無法先新增獨立的課程資訊，必須等有人選課。老師編號非本表主鍵，其 `NULL` 並不是本頁所述主鍵違規的直接原因。

<a id="db-p040"></a>

### DB-P040｜修改異常示例及教材例子的限制

[原講義《資料庫正規化.pdf》第40頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=40)

標題：**修改異常檢查（Update Anomaly）**。表格與 P039 的 `#1–#5` 完全相同；粗黑框橫跨整個 `#2`、`#3`，凸顯兩筆「網頁設計」選課：

| 記錄 | 學號 | 姓名 | 性別 | 課程代碼 | 課程名稱 | 學分數 | 必選修 | 成績 | 老師編號 | 老師姓名 |
|---|---|---|---|---|---|---|---|---|---|---|
| #1 | 001 | 李碩安 | 男 | C001 | 程式語言 | 4 | 必 | 74 | T001 | 李安 |
| #2 | 001 | 李碩安 | 男 | C002 | 網頁設計 | 3 | 選 | 93 | T002 | 張三 |
| #3 | 002 | 李碩崴 | 男 | C002 | 網頁設計 | 3 | 選 | 63 | T002 | 張三 |
| #4 | 002 | 李碩崴 | 男 | C003 | 計概 | 2 | 必 | 82 | T003 | 李四 |
| #5 | 002 | 李碩崴 | 男 | C005 | 網路教學 | 4 | 選 | 94 | T005 | 王五 |

**原稿主張**：「網頁設計」重覆多次，修改此課程成績時可能漏改；例如修這門課的同學各加 `5` 分，有些有加、有些沒有加，造成不一致。原圖尚未顯示加分後的數值。

**計算補充（已用 Python 驗算，非圖中原值）**：完整執行加分應為 `93 + 5 = 98`、`63 + 5 = 68`。

**重要辨正**：兩位學生的 `93` 與 `63` 是不同的個別成績，不是同一事實的重覆副本。全班加分漏掉某人是批次更新／交易執行問題，即使已拆到 2NF／3NF 的成績表仍可能發生，不能宣稱 2NF 自動消除此問題。更準確的正規化修改異常例子是：`C002` 的課程名稱或學分數變更，卻只改 `#2`、未改 `#3`，造成同一課程的固定資訊矛盾。此例是補充說明，並非替換原稿數據。

<a id="db-p041"></a>

### DB-P041｜刪除一筆選課造成課程資訊遺失

[原講義《資料庫正規化.pdf》第41頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=41)

標題：**刪除異常檢查（Delete Anomaly）**。上表仍為 P039 的五筆：`#1=(001,C001,74)`、`#2=(001,C002,93)`、`#3=(002,C002,63)`、`#4=(002,C003,82)`、`#5=(002,C005,94)`；其姓名、性別、課名、學分、必選修、老師資料逐欄均與 P040 表相同。

粗黑圓角框圈住整個 `#4`：

| 記錄 | 學號 | 姓名 | 性別 | 課程代碼 | 課程名稱 | 學分數 | 必選修 | 成績 | 老師編號 | 老師姓名 |
|---|---|---|---|---|---|---|---|---|---|---|
| #4 | 002 | 李碩崴 | 男 | C003 | 計概 | 2 | 必 | 82 | T003 | 李四 |

**原稿說明**：刪除 `#4` 學生的記錄，也會刪除課程名稱、學分數及相關資訊；「計概」的 `2` 學分資料也同時消失。頁底大字結論：需進行「第二階正規化」消除上述三種異常。

**精確解讀**：`#4` 是記錄編號，不是第四位學生。這裡刪的是學號 `002` 的一筆修課記錄；`002` 尚有 `#3`、`#5`，學生資訊不會全失，但 `C003` 只出現這一列，刪後就無從查知該課程及其教師資訊。將課程主檔與選課記錄分離，才能退選而不抹除課程。

<a id="db-p042"></a>

### DB-P042｜第二正規化規則：消除部分功能相依

[原講義《資料庫正規化.pdf》第42頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=42)

本頁純文字，標題「第二正規化的規則」。**Second Normal Form，簡稱 2NF**，條件：

1. 已符合 1NF。
2. 每一非鍵屬性（原稿舉姓名、性別）必須「完全相依」於主鍵，不能「部分功能相依」於主鍵。

**原稿解釋**：部分功能相依出現在主鍵由多個欄位組成時（複合主鍵）；某些非鍵欄位只依賴主鍵中的部分欄位，不需要另一部分。

**連回本例**：
- 原選課表鍵為 `(學號, 課程代碼)`，不是單獨學號。
- `學號 → 姓名、性別`：不需要課程代碼，是部分相依。
- `課程代碼 → 課程名稱、學分數、必選修、老師編號、老師姓名`：不需要學號，也是部分相依。
- `(學號, 課程代碼) → 成績`：在本例需整組，屬完全相依。

**補充／辨正**：本頁「主鍵（學號）」是一般學生資料表的簡化舉例，不能套成先前未分割選課表的主鍵。正式 2NF 需檢查非主屬性對**每一候選鍵**的完全相依；不能只因另外新增單欄流水號主鍵，就斷言原本複合候選鍵的部分相依被消除。

<a id="db-p043"></a>

### DB-P043｜2NF作法第一步：辨認兩組部分相依

[原講義《資料庫正規化.pdf》第43頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=43)

原稿作法：分割資料表，把「部分功能相依」欄位分割出去，另組新表。**步驟一：檢查是否存在部分功能相依**。

圖上兩句提示：「姓名」只相依於「學號」；「課程名稱」只相依於「課程代碼」。表格仍為五列原選課資料：

| 記錄 | 學號 | 姓名 | 性別 | 課程代碼 | 課程名稱 | 學分數 | 必選修 | 成績 | 老師編號 | 老師姓名 |
|---|---|---|---|---|---|---|---|---|---|---|
| #1 | 001 | 李碩安 | 男 | C001 | 程式語言 | 4 | 必 | 74 | T001 | 李安 |
| #2 | 001 | 李碩安 | 男 | C002 | 網頁設計 | 3 | 選 | 93 | T002 | 張三 |
| #3 | 002 | 李碩崴 | 男 | C002 | 網頁設計 | 3 | 選 | 63 | T002 | 張三 |
| #4 | 002 | 李碩崴 | 男 | C003 | 計概 | 2 | 必 | 82 | T003 | 李四 |
| #5 | 002 | 李碩崴 | 男 | C005 | 網路教學 | 4 | 選 | 94 | T005 | 王五 |

**重要：圖的箭頭方向**：姓名表頭被粗框圈住，粗線由姓名往左上折，再以箭頭向下指「學號」；性別也用細線接到該依附端。課程名稱同樣被粗框圈住，粗線往左折後指「課程代碼」；學分數、必選修、老師編號、老師姓名由細線接入這組。這是**由相依者指回所依賴欄位**的視覺畫法，與標準 FD「決定者 → 被決定者」的方向相反，切勿照圖寫成 `姓名 → 學號`。

標準 FD 改寫為：

```text
學號 → 姓名、性別
課程代碼 → 課程名稱、學分數、必選修、老師編號、老師姓名
```

學號、課程代碼均以粗體底線表示同一複合主鍵的組成部分；兩組非鍵欄位各只需鍵的一部分。成績未接在上述部分相依群，因其需整個複合鍵。頁底結論：存在部分功能相依。

<a id="db-p044"></a>

### DB-P044｜2NF作法第二步：學生表與成績表

[原講義《資料庫正規化.pdf》第44頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=44)

**步驟二**：將部分功能相依欄位分割，另組新資料表。原稿把選課表分成三個較小表格，並說明「加底線」的欄位為主鍵；本頁列前兩張，第三張在 P045。

**一、學生資料表（學號，姓名，性別）**；綱要中只有學號有底線，PK＝`學號`。

| 學號（PK） | 姓名 | 性別 |
|---|---|---|
| 001 | 李碩安 | 男 |
| 002 | 李碩崴 | 男 |

`學號 → 姓名、性別`。學生姓名及性別各存一次，不再跟著每門選課重覆。

**二、成績資料表（學號，課程代碼，成績）**；綱要中「學號，課程代碼」均有底線，PK＝`(學號, 課程代碼)`。

| 學號（PK之一） | 課程代碼（PK之一） | 成績 |
|---|---|---|
| 001 | C001 | 74 |
| 001 | C002 | 93 |
| 002 | C002 | 63 |
| 002 | C003 | 82 |
| 002 | C005 | 94 |

`(學號, 課程代碼) → 成績`。成績表保留哪個學生選哪一課及其分數，不攜帶姓名、性別等部分相依欄位。

**補充（本頁未畫 FK 箭頭）**：成績表的學號宜設為參照學生表學號的 FK；課程代碼宜參照 P045 課程表。它們可同時是複合 PK 的成員與各自 FK，不衝突。教材的粗底線只是在標 PK，不應誤讀成所有底線都代表 FK。

<a id="db-p045"></a>

### DB-P045｜2NF的第三張表：課程資料表與剩餘問題

[原講義《資料庫正規化.pdf》第45頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=45)

**三、課程資料表（課程代碼，課程名稱，學分數，必選修，老師編號，老師姓名）**。綱要中「課程代碼」加底線，為 PK。

| 課程代碼（PK） | 課程名稱 | 學分數 | 必選修 | 老師編號 | 老師姓名 |
|---|---|---|---|---|---|
| C001 | 程式語言 | 4 | 必 | T001 | 李安 |
| C002 | 網頁設計 | 3 | 選 | T002 | 張三 |
| C003 | 計概 | 2 | 必 | T003 | 李四 |
| C005 | 網路教學 | 4 | 選 | T005 | 王五 |

原來兩列的 `C002` 課程固定資訊，現在課程表只保留一次；兩位學生的不同成績仍在成績表，不會被合併掉。

**原稿結論**：第二正規化產生學生、成績、課程三表；除了課程表，其餘兩表都已符合 2NF、3NF 及 BCNF。

**釐清**：這不是說課程表連 2NF 都不符合。課程表已排除原複合鍵的部分相依，但仍有 `課程代碼 → 老師編號 → 老師姓名` 的遞移相依，故在教材業務規則下尚未達 3NF／BCNF。學生與成績表達 BCNF 的結論也以教材給定 FD 為前提，不能只由目前幾列值的偶然唯一性判斷。

<a id="db-p046"></a>

### DB-P046｜2NF後的新增異常：不能先建立老師

[原講義《資料庫正規化.pdf》第46頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=46)

章節：**4-4.5 第三正規化（3NF）**。原稿說完成 2NF 後仍可能有新增、刪除、更新異常。本頁為 **Insert Anomaly**。

上方課程表四筆，資料同 P045，新增了展示用行號：

| 記錄 | 課程代碼 | 課程名稱 | 學分數 | 必選修 | 老師編號 | 老師姓名 |
|---|---|---|---|---|---|---|
| #1 | C001 | 程式語言 | 4 | 必 | T001 | 李安 |
| #2 | C002 | 網頁設計 | 3 | 選 | T002 | 張三 |
| #3 | C003 | 計概 | 2 | 必 | T003 | 李四 |
| #4 | C005 | 網路教學 | 4 | 選 | T005 | 王五 |

下方嘗試鍵入：

| 記錄 | 課程代碼 | 課程名稱 | 學分數 | 必選修 | 老師編號 | 老師姓名 |
|---|---|---|---|---|---|---|
| #5 | NULL | （空白） | （空白） | （空白） | T004 | 李白 |

左側由 `#5` 往上方課程表的折線箭頭遭叉號擋住，標「無法新增」。尚未決定 `T004／李白` 的課程代碼時不能存老師資料，因為本表 PK＝課程代碼，不得 `NULL`；這違反實體完整性規則。空白欄維持空白，不虛構課名、學分或必選修。

**設計問題**：老師是可獨立存在的實體，卻被迫附著於課程列；後續應把老師編號和姓名放入獨立老師表，使尚未授課的老師也能登錄。

<a id="db-p047"></a>

### DB-P047｜老師姓名重覆儲存造成修改異常

[原講義《資料庫正規化.pdf》第47頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=47)

標題：**修改異常（Update Anomaly）**。假設「李安」老師開多門課，欲把姓名改為「李碩安」，可能只修改部分記錄，造成同一老師姓名不一致。

本頁擴充課程表，所有實際顯示的列如下；省略號是原圖的一部分，不代表筆記漏讀，也不能自行補出中間課程。

| 記錄 | 課程代碼 | 課程名稱 | 學分數 | 必選修 | 老師編號 | 老師姓名（圖中狀態） |
|---|---|---|---|---|---|---|
| #1 | C001 | 程式語言 | 4 | 必 | T001 | 李安 → 李碩安 |
| #2 | C002 | 網頁設計 | 3 | 選 | T002 | 張三 |
| #3 | C003 | 計概 | 2 | 必 | T003 | 李四 |
| #4 | C005 | 網路教學 | 4 | 選 | T005 | 王五 |
| … |  |  |  |  |  |  |
| #10 | C010 | 資料結構 | 4 | 必 | T001 | 李安 → 李碩安 |
| … |  |  |  |  |  |  |
| #100 | C100 | 資料庫系統 | 4 | 必 | T001 | 李安（未修改） |

**圖示細節**：`#1`、`#10`、`#100` 各被粗黑橫框圈住；前兩列的「李安」有刪除線並以向右箭頭改成「李碩安」。`#100` 仍寫「李安（未修改）」，頁底「未修改到」註記用向上箭頭指向此格。

**相依性解釋**：`T001` 代表同一老師，理應由 `老師編號 → 老師姓名` 保證一致；把姓名重覆放進多個課程列，會形成同一事實的多份副本。這是正規化可處理的典型修改異常，與 P040 不同學生的不同成績不同。P047 的擴充課程及改名是獨立假設例，不應擅自帶入後續回到原始四課的表格。

<a id="db-p048"></a>

### DB-P048｜刪除最後一門課連帶遺失老師

[原講義《資料庫正規化.pdf》第48頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=48)

標題：**刪除異常（Delete Anomaly）**。本頁回到四筆原始課程，不使用 P047 擴充的 `C010`、`C100`。

| 記錄 | 課程代碼 | 課程名稱 | 學分數 | 必選修 | 老師編號 | 老師姓名 |
|---|---|---|---|---|---|---|
| #1 | C001 | 程式語言 | 4 | 必 | T001 | 李安 |
| #2 | C002 | 網頁設計 | 3 | 選 | T002 | 張三 |
| #3 | C003 | 計概 | 2 | 必 | T003 | 李四 |
| #4 | C005 | 網路教學 | 4 | 選 | T005 | 王五 |

粗黑框圈住整列 `#1`。原稿說刪除該課程時，也刪掉老師編號 `T001` 及老師姓名，因此丟失老師資訊。頁底結論：綜合新增、修改、刪除三種異常，需要「第三階正規化」。

**條件釐清**：刪除課程會讓該老師的資訊完全消失，前提是這是資料表中該老師的**最後一筆／唯一一筆課程**。本頁四列的確只有 `C001` 使用 `T001`；若仍採 P047 的擴充資料，刪 `C001` 不會讓 `T001` 完全消失。不能把兩頁的不同假設混成同一次資料狀態。

<a id="db-p049"></a>

### DB-P049｜第三正規化規則與遞移相依的檢查

[原講義《資料庫正規化.pdf》第49頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=49)

本頁純文字：「第三正規化的規則」，**Third Normal Form，簡稱 3NF**。

原稿兩項條件：
1. 符合 2NF。
2. 各欄位與「主鍵」之間沒有「遞移相依」關係。

原稿提出檢查法：由左至右掃描資料表各欄，看是否存在「與主鍵無關的相依性」。有則代表有遞移相依；沒有則代表沒有。第二點原句為「如果有不存在時」，是語句不順，應按上下文理解為「如果不存在時」。

**本例實際檢查**：課程代碼是 PK；在非鍵欄位間發現 `老師編號 → 老師姓名`，再配合 `課程代碼 → 老師編號`，便得到 `課程代碼 → 老師姓名` 的遞移路徑。

**補充／辨正**：
- 「由左至右」只是閱讀習慣，欄位換序不會改變 FD 或正規化程度。
- 「與主鍵無關」不是說老師姓名完全不相依於課程代碼，而是其**直接決定因素是另一個非鍵欄位**；透過該欄仍可由主鍵決定。
- 完整 3NF 定義不是禁止任何可經遞移律推出的 FD，而是每個非平凡 FD `X → A` 中，`X` 為超鍵或 `A` 為主屬性。本例老師編號不是課程表超鍵、老師姓名不是主屬性，故違反 3NF。

<a id="db-p050"></a>

### DB-P050｜3NF作法第一步：找出老師姓名的遞移相依

[原講義《資料庫正規化.pdf》第50頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=50)

原稿作法：把具有「遞移相依」或「間接相依」的欄位分割出去，另組新表。**步驟一：檢查是否存在遞移相依**。

內文解釋每門課有授課老師，故老師編號相依於課程代碼；老師姓名又相依於老師編號（內文也稱「教師編號」），因此存在教材所稱「與主鍵無關的相依性」。

右下圖課程表完整數據：

| 記錄 | 課程代碼 | 課程名稱 | 學分數 | 必選修 | 老師編號 | 老師姓名 |
|---|---|---|---|---|---|---|
| #1 | C001 | 程式語言 | 4 | 必 | T001 | 李安 |
| #2 | C002 | 網頁設計 | 3 | 選 | T002 | 張三 |
| #3 | C003 | 計概 | 2 | 必 | T003 | 李四 |
| #4 | C005 | 網路教學 | 4 | 選 | T005 | 王五 |

**三條關係線逐一解讀**：
1. 表上方由老師編號向左折回、箭頭指課程代碼，標「『老師編號』相依於『課程代碼』」。
2. 表下方短折線由老師姓名向左，箭頭指老師編號，標「老師姓名相依於老師編號（與主鍵無關的相依性）」。
3. 表下方長折線由老師姓名下繞至左端、箭頭指課程代碼，標「『老師姓名』遞移相依於『課程代碼』」。

與 P043 一樣，原圖是**相依者指向被依賴者**。用標準 FD 箭頭重寫為：

```text
課程代碼 → 老師編號
老師編號 → 老師姓名
∴ 課程代碼 → 老師姓名（經老師編號遞移）
```

**補充條件**：由「每門課有老師」推成 FD，還須採用本教材的「一個課程代碼對應一位老師」假設；若共同授課或跨學期換老師，就要用課程班別／授課關聯等更完整模型。

<a id="db-p051"></a>

### DB-P051｜遞移相依的完整圖解與符號式

[原講義《資料庫正規化.pdf》第51頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=51)

本頁上方放大 P050 的同一張相依圖，並在下方文字解釋直接、間接相依。表格仍有六個資料欄及記錄編號：

| 記錄 | 課程代碼（底線為PK） | 課程名稱 | 學分數 | 必選修 | 老師編號 | 老師姓名 |
|---|---|---|---|---|---|---|
| #1 | C001 | 程式語言 | 4 | 必 | T001 | 李安 |
| #2 | C002 | 網頁設計 | 3 | 選 | T002 | 張三 |
| #3 | C003 | 計概 | 2 | 必 | T003 | 李四 |
| #4 | C005 | 網路教學 | 4 | 選 | T005 | 王五 |

**圖中三個註記與箭頭**：
- 表頂「老師編號」相依於「課程代碼」：線從老師編號繞到左邊、箭頭指課程代碼。
- 右下「老師姓名相依於老師編號（與主鍵無關的相依性）」：短線從姓名回指編號。
- 底部「老師姓名」遞移相依於「課程代碼」：長線從姓名繞過表底回指課程代碼。

**原稿解釋**：課程名稱、學分數、必選修、老師編號都直接相依於主鍵課程代碼，原稿稱它們是課程資料的必需欄位；「老師名稱」（表頭實際為「老師姓名」）則直接相依於老師編號，再間接相依於課程代碼，稱**遞移相依（Transitive Dependency）**或**間接相依**。

原稿公式：`A → B`、`B → C`，則 `A → C`。代入本例：

```text
A = 課程代碼
B = 老師編號
C = 老師姓名
課程代碼 → 老師編號 → 老師姓名
```

**補充**：`A → C` 仍然是成立的功能相依；「不是直接相依」是解釋來源，不是說該 FD 不成立。單有遞移律並不足以證明違反 3NF；此例問題在於中間決定因素老師編號不是課程表的超鍵，而姓名是非主屬性。教材「必需欄位」也不是 SQL `NOT NULL` 的正式宣告。

<a id="db-p052"></a>

### DB-P052｜3NF作法第二步：課程、老師分表並以FK相連

[原講義《資料庫正規化.pdf》第52頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=52)

原稿步驟二：將「遞移相依」欄位分割出去，另組新表；將課程表分成兩表，利用外鍵（F.K.）連接。

**原稿數據差異，必須保留**：本頁課程代碼由前頁的 `C001/C002/C003/C005` 改為 **`A001/A002/A003/A005`**，上方分割前表與下方分割後表都是 A 開頭。原稿沒有解釋改碼原因；可能是教材版本不一致，但不能自行改回 C，也不能把改碼說成正規化步驟。

**分割前表**：左側列號 `#1–#4`，該列表頭空白。

| 原圖列號 | 課程代碼 | 課程名稱 | 學分數 | 必選修 | 老師編號 | 老師姓名 |
|---|---|---|---|---|---|---|
| #1 | A001 | 程式語言 | 4 | 必 | T001 | 李安 |
| #2 | A002 | 網頁設計 | 3 | 選 | T002 | 張三 |
| #3 | A003 | 計概 | 2 | 必 | T003 | 李四 |
| #4 | A005 | 網路教學 | 4 | 選 | T005 | 王五 |

中央空心粗向下箭頭旁寫「第三正規化，去除遞移相依」，指向下方兩張表。

**分割後：課程資料表**。原表頭實際標 `課程代碼*`、`老師編號#`；依內文及前後頁，`*` 表示課程主鍵、`#` 表示老師編號為外鍵。

| 課程代碼*（PK） | 課程名稱 | 學分數 | 必選修 | 老師編號#（FK） |
|---|---|---|---|---|
| A001 | 程式語言 | 4 | 必 | T001 |
| A002 | 網頁設計 | 3 | 選 | T002 |
| A003 | 計概 | 2 | 必 | T003 |
| A005 | 網路教學 | 4 | 選 | T005 |

**分割後：老師資料表**。本頁老師編號表頭未加星號，依其決定姓名的角色識別為該表 PK（P053 以底線明示）。

| 老師編號（PK） | 老師姓名 |
|---|---|
| T001 | 李安 |
| T002 | 張三 |
| T003 | 李四 |
| T005 | 王五 |

兩表下方都標「符合 3NF，BCNF」。本圖沒有畫實際橫跨兩表的 FK 線，但內文明確說明用 FK 相連；其關係為 `課程.老師編號（FK） → 老師.老師編號（PK）`（這是參照方向）。

**分割要點**：老師姓名移到老師表；課程表保留老師編號，不能連它一起刪去，否則無法知道每門課由誰教。老師表中的 FD 是 `老師編號 → 老師姓名`，課程表中的 FD 是 `課程代碼 → 課程名稱、學分數、必選修、老師編號`。本例可讓一位老師對應多門課；分割不是一門課建立一份老師副本。

<a id="db-p053"></a>

### DB-P053｜第三正規化完成後的四個表格

[原講義《資料庫正規化.pdf》第53頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/%E8%B3%87%E6%96%99%E5%BA%AB%E6%AD%A3%E8%A6%8F%E5%8C%96.pdf#page=53)

本頁總結：「完成第三正規化後，共產生四個表格」。圖用上下兩個大型粗黑圓角框分群：上框為**第二正規化產生的表格**（學生、成績），下框為**第三正規化產生的表格**（課程、老師）。本頁沿用 P052 的 **A 開頭課程代碼**，包括成績表；與 P044 的 C 開頭不同，忠實保留不改碼。

**一、學生資料表（左上）**。

| 學號（PK，原圖底線） | 姓名 | 性別 |
|---|---|---|
| 001 | 李碩安 | 男 |
| 002 | 李碩崴 | 男 |

下方註記「符合 2NF，3NF」。`學號 → 姓名、性別`。

**二、成績資料表（右上）**。

| 學號（複合PK之一，原圖底線） | 課程代碼（複合PK之一，原圖底線） | 成績 |
|---|---|---|
| 001 | A001 | 74 |
| 001 | A002 | 93 |
| 002 | A002 | 63 |
| 002 | A003 | 82 |
| 002 | A005 | 94 |

下方註記「符合 2NF，3NF」。`(學號, 課程代碼) → 成績`。

**三、課程資料表（左下）**。

| 課程代碼（PK，原圖底線） | 課程名稱 | 學分數 | 必選修 | 老師編號#（FK） |
|---|---|---|---|---|
| A001 | 程式語言 | 4 | 必 | T001 |
| A002 | 網頁設計 | 3 | 選 | T002 |
| A003 | 計概 | 2 | 必 | T003 |
| A005 | 網路教學 | 4 | 選 | T005 |

下方註記「符合 3NF」。與 P052 相比，本頁課程代碼用底線、不加 `*`；老師編號仍附 `#`。

**四、老師資料表（右下）**。

| 老師編號（PK，原圖底線） | 老師姓名 |
|---|---|
| T001 | 李安 |
| T002 | 張三 |
| T003 | 李四 |
| T005 | 王五 |

下方註記「符合 3NF」。本頁沒有畫跨表箭頭；標示並非宣稱這些表不符合 BCNF，P045／P052 已分別說明更高程度。

**依表結構整理的關係（補充，非原圖另有箭頭）**：

```text
學生.學號 (PK) ← 成績.學號 (FK，亦為複合PK之一)
課程.課程代碼 (PK) ← 成績.課程代碼 (FK，亦為複合PK之一)
老師.老師編號 (PK) ← 課程.老師編號# (FK)
```

- 學生到成績、課程到成績、老師到課程均可是一對多。
- 學生與課程透過成績表形成多對多關係，分數屬於此關聯，不屬於單獨學生或課程。
- 新增老師不需先新增課程；修改老師姓名只需改老師表的一列；刪掉一門課不必刪掉老師主檔。實際刪除規則仍需設定參照完整性，不應把正規化等同於自動選定 `CASCADE` 等政策。
- `C004／系統分析`、`T004／李白` 是前頁嘗試新增而失敗的示例；`C010`、`C100` 是修改異常的假設擴充，均未出現在本頁，不得自行加入最終四表。

**全段脈絡**：原始一生多課重覆群 → 1NF 展成逐筆選課 → 2NF 將學生、成績、課程分開 → 3NF 再把老師從課程分出。正規化處理的是資料依賴與重覆事實，不是改學號、改課碼或改成績。











---

## 補充講義：20260907AI應用(20260915).pdf（76頁）

## AI應用講義第1–26頁｜逐頁詳細知識筆記

來源：`20260907AI應用(20260915).pdf`。本段依 PDF 實際頁序；每頁已對照頁圖，文字層僅作輔助。授課教師：葉呈祥。以下「講義內容」為原文、圖表與操作的整理；「補充／勘誤」是另行說明，不混作原文。範例房價、模型輸出與介面均屬講義案例，非即時行情或重新執行結果。未執行圖片中的程式、外部指令、登入或購買。

<a id="ai-p001"></a>

### AI-P001｜第四章目錄與學習路線

[原講義《20260907AI應用(20260915).pdf》第1頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=1)

**講義內容／目錄逐項對應**

|章節／主題|講義頁碼|
|---|---:|
|第四章 機器學習分類器|2|
|4.1 機器學習演算法分類|2|
|監督式學習（Supervised Learning）|2|
|非監督式學習（Unsupervised Learning）|3|
|線性預測（Linear Prediction）|4|
|線性模型特色|5|
|建議的教學順序（適合初學者）|6|
|4.2 Linear Regression／說明|7|
|房價預測1（California Housing）|12|
|房價預測2（California Housing）|15|
|房價預測（已訓練好模型＋Django Web）|27|
|4.2 KNN（K-Nearest Neighbors，K最近鄰演算）／說明|31|
|利用身高來判斷男生或女生，使用knn演算法|32|
|利用knn的手寫數字辨識系統（使用學者的資料庫與方法）|36|
|利用knn的手寫數字辨識系統（匯出資料庫成圖片、匯出模型、測試圖片）|37|
|利用knn的手寫數字辨識系統修改1（重新產生與訓練資料庫）|47|
|利用knn的手寫數字辨識系統修改2|55|
|利用knn的手寫數字辨識系統 by Django Web|66|

**圖文閱讀註記**：此頁是完整目錄，沒有額外操作圖。原目錄將 Linear Regression 與 KNN 都編為「4.2」，本筆記保留，不擅自更改章號。第27頁以後只在此記錄目錄，不納入本段正文。

<a id="ai-p002"></a>

### AI-P002｜機器學習類型、監督式學習與分類

[原講義《20260907AI應用(20260915).pdf》第2頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=2)

**講義內容**

- 機器學習演算法大致列為三類：監督式學習（Supervised Learning）、非監督式學習（Unsupervised Learning）、強化式學習（Reinforcement Learning）。本頁開始解釋監督式；強化式在此僅列名。
- 監督式學習：資料已具有正確答案（Label），以大量已知答案的資料訓練模型，再預測新資料。原文「模型知道答案，因此稱為監督式」，指訓練階段提供標籤。
- 圖中「圖片／答案（Label）」表格實際包含四組資料：貓圖片→貓、狗圖片→狗、手寫數字→5、房屋資料→800萬元。因此 Label 可以是類別，也可以是數值。
- 流程：**資料 → 特徵（X） → 模型訓練 → 建立模型 → 新資料預測**。
- 監督式的第一種主要工作是**分類（Classification）**，回答「是哪一類」。例：垃圾郵件／正常郵件、貓／狗、數字0–9、好瓜／壞瓜。
- 本頁列出的分類演算法：KNN、Decision Tree、Random Forest、Logistic Regression、SVM、Naive Bayes；清單續下頁。

**補充**：流程圖簡寫成只列 X，但監督式訓練實際也要使用標籤 y；新資料預測才是不提供答案給模型。

<a id="ai-p003"></a>

### AI-P003｜回歸任務與非監督式分群

[原講義《20260907AI應用(20260915).pdf》第3頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=3)

**講義內容**

- 承接分類演算法：XGBoost、LightGBM、CNN（影像）、RNN/LSTM（時間序列）、Transformer（文字）。括號是講義列出的常見應用，並非限制只能處理該類資料。
- 監督式的第二種工作是**回歸（Regression）**，用於預測數值；例子為房價、股票價格、溫度、銷售額。
- 回歸演算法清單：Linear Regression、Polynomial Regression、Ridge、Lasso、Elastic Net、SVR、Random Forest Regression、XGBoost Regression。
- **非監督式學習（Unsupervised Learning）**：沒有 Label，只有大量資料，希望由電腦找出規律。例：10,000位客戶資料，未標記VIP或一般客戶，由模型自行分群。
- 流程：**資料（X） → 沒有答案（Label） → 找規律 → 得到群組**。
- 第一種常見工作為**分群（Clustering）**。本頁舉「電商，學生A、學生B、學生C…」資料，自動分為第一群、第二群、第三群；原文把電商與學生例子並列，沒有提供更詳細欄位。

**圖文閱讀註記**：本頁全為文字，沒有獨立圖像或程式碼。分類與回歸的判斷關鍵是欲預測的答案類型，而非輸入資料是否含數字。

<a id="ai-p004"></a>

### AI-P004｜分群、降維、異常偵測與線性模型公式

[原講義《20260907AI應用(20260915).pdf》第4頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=4)

**講義內容**

1. **分群演算法**：K-Means、GMM、DBSCAN、Hierarchical Clustering、Mean Shift。
2. **降維**：將很多特徵轉為較少特徵，例如1,000個特徵變成20個；目的為方便視覺化、降低運算量、去除雜訊。演算法：PCA、t-SNE、UMAP。
3. **異常偵測**：信用卡盜刷、設備故障、網路攻擊；演算法為 Isolation Forest、One-Class SVM、LOF。
4. **線性預測（Linear Prediction）**通常指線性模型（Linear Models），屬監督式學習，以輸入與輸出間的線性關係建立預測。

圖片公式完整轉寫：

\[
y=w_1x_1+w_2x_2+\cdots+w_nx_n+b
\]

- x：特徵（Feature）；w：權重（Weight）；b：偏差（Bias）；y：預測值。
- 單一輸入可視為直線，多個輸入則以超平面表示。
- 訓練目標：找出合適的權重與偏差，使預測結果最接近真實值。

**補充**：以上公式中的 n 是特徵數；後續誤差公式中的 n 通常是樣本數，閱讀時要依上下文區分。原圖使用 y 表示預測，本筆記討論真值與預測差異時會以 ŷ 區別預測值。

<a id="ai-p005"></a>

### AI-P005｜線性迴歸、邏輯斯迴歸與三大類型比較

[原講義《20260907AI應用(20260915).pdf》第5頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=5)

**講義內容**

- **Linear Regression（線性迴歸）**預測連續數值，例：房價、氣溫、銷售量。
- **Logistic Regression（邏輯斯迴歸）**名稱雖有 Regression，實際用於分類。例：是否違約、是否生病、是否為垃圾郵件。通常先得到0–1的機率，再依門檻分類。
- 線性模型優點：容易理解與解釋、訓練快、適合入門、可分析各特徵的影響方向。
- 限制：假設線性關係；面對複雜非線性問題能力有限；需要適當的特徵工程。

**頁底圖片「各類型比較」完整整理**

|類型|是否有Label／回饋|主要目的|常見演算法|應用範例|
|---|---|---|---|---|
|監督式學習|有|分類、回歸|Linear Regression、Logistic Regression、KNN、Decision Tree、Random Forest、SVM、CNN、XGBoost|手寫數字辨識、垃圾郵件分類、房價預測|
|非監督式學習|無|分群、降維、異常偵測|K-Means、GMM、DBSCAN、PCA、t-SNE、UMAP|客戶分群、資料探索、異常交易偵測|
|強化式學習|回饋獎勵|學習最佳策略|Q-Learning、Deep Q Network（DQN）、Policy Gradient|遊戲AI、機器人控制、自動駕駛|

**補充**：係數的正負可用於解釋影響方向，但不等於已證明因果；不同單位的係數大小不能直接當成可比較的重要性排名。

<a id="ai-p006"></a>

### AI-P006｜初學者教學順序與對應實作

[原講義《20260907AI應用(20260915).pdf》第6頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=6)

**講義內容**

1. 先學概觀：監督式、非監督式、強化式學習的差異。
2. 學監督式：線性迴歸先行，再到分類：Logistic Regression、KNN、Decision Tree、Random Forest、CNN。
3. 學非監督式：K-Means、GMM、PCA，理解資料探索與分群。
4. 配合代表案例：
   - Linear Regression：房價預測（Boston Housing 或 California Housing）。
   - KNN：MNIST手寫數字辨識。
   - Random Forest：Iris鳶尾花分類。
   - CNN：MNIST手寫數字辨識。
   - K-Means：客戶分群。
   - PCA：資料降維與視覺化。

本頁以紅字突出 Linear Regression 房價預測與 KNN 手寫辨識。目的是先理解基本概念，再用代表演算法建立知識架構，銜接深度學習（如CNN）及實務。資料集名稱依講義原文保存，不代表已確認套件現行供應狀態。

<a id="ai-p007"></a>

### AI-P007｜單變量線性迴歸：截距與斜率

[原講義《20260907AI應用(20260915).pdf》第7頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=7)

**講義內容及圖片公式**

Linear Regression 是監督式演算法，尋找 X 與 Y 的線性關係，建立最佳直線預測未知資料。

\[
\hat y=b_0+b_1x
\]

|符號|圖中意義|
|---|---|
|x|輸入（特徵）|
|ŷ|預測值|
|b₀|截距（Intercept）|
|b₁|斜率（Coefficient）|

- 圖中範例：`ŷ = 100 + 20x`。
- 下方「圖形說明」再次列相同公式，繪圖介面左側寫 `y = 20x + 100`，右側是往右上方延伸的藍色直線，並標記與座標軸相交位置。它呈現正斜率及非零截距。
- 截圖本身小節標為「二、數學公式」與「三、圖形說明」；這是貼入圖片的編號，不是新增主章節。

**補充**：b₀是x為0時的模型預測；b₁是x每增加1單位，模型預測增加的量。案例係數是示範，不代表真實房市的固定關係。

<a id="ai-p008"></a>

### AI-P008｜資料不完全共線時：尋找最接近的直線

[原講義《20260907AI應用(20260915).pdf》第8頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=8)

**圖片內容**：小節「六、如果資料不是一直線？」提供五筆資料：

|X|Y|
|---:|---:|
|1|118|
|2|141|
|3|159|
|4|182|
|5|198|

- 下方以文字式散點圖呈現五點向右上方排列；縱軸標示約120至200，橫軸標示1至5。
- 說明強調：這些點沒有完全落在同一直線上；Linear Regression 要找的是「最接近所有點的那條直線」。
- 本頁沒有給出訓練後精確係數，也沒有程式，不能把散點草圖當作精密座標圖。

**補充**：如何定義「最接近」由下一頁平方誤差／最小平方法說明；不是把每個點逐點串接成折線。

<a id="ai-p009"></a>

### AI-P009｜最小平方法：為何不能直接加總誤差

[原講義《20260907AI應用(20260915).pdf》第9頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=9)

**圖片「七、什麼叫 Least Squares（最小平方法）？」完整內容**

- 每一資料點都有誤差。示意圖上方是實際值點，下方是預測直線，中間以垂直距離標示「誤差（Error）」。
- 範例：預測=160、實際=170，圖中算式為 `170−160=10`。
- 若多筆誤差為 `5, −3, 8, −10, …`，直接相加，圖中得到 `5−3+8−10=0`。
- 問題：正負會互相抵消，總和為0不代表每筆預測都正確。

**補充**：圖中使用「實際－預測」作為殘差方向；改採相反方向時，平方誤差不受符號影響。本頁只是教學示例，不是實際模型測試輸出。

<a id="ai-p010"></a>

### AI-P010｜平方誤差和 SSE 與訓練目標

[原講義《20260907AI應用(20260915).pdf》第10頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=10)

**圖片內容**

- 為避免正負抵消，將前頁誤差平方：`5²=25`、`(−3)²=9`、`8²=64`、`(−10)²=100`。
- 全部加總，圖中寫為 `25+9+64+100`，未另印總值。
- 名稱為 **SSE（Sum of Squared Errors，平方誤差和）**：

\[
SSE=\sum_{i=1}^{n}(y_i-\hat y_i)^2
\]

- Linear Regression 的目的：找到一條直線，使 SSE 最小。
- 頁底「公式如下」銜接下一頁，沒有額外隱藏的數值表格。

**補充**：平方後大誤差受到更大的懲罰；SSE是加總，不是平均，也不是開根號後的RMSE。n為樣本數，yᵢ為第i筆實際值，ŷᵢ為第i筆預測值。

<a id="ai-p011"></a>

### AI-P011｜最小平方目標函數與擬合圖操作元素

[原講義《20260907AI應用(20260915).pdf》第11頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=11)

**講義圖片：單一變數線性迴歸**

\[
\hat y_i=b_0+b_1x_i
\]

符號：b₀為截距、b₁為斜率、yᵢ為第i筆實際值、ŷᵢ為第i筆預測值。

**互動圖截圖**

- 左側顯示模型 `ŷ=b₀+b₁x`，並顯示一次擬合的結果：`ŷ = 8.49 − 0.54x；R² = 0.72`。
- 右側藍圈為觀測資料，淺綠色直線向右下方延伸，另有直線上的預測點與連接觀測點、直線的細線，呈現預測差異。
- 左下「焦點」選項依序為「資料」「最佳擬合線」「預測值」「殘差」；下方按鈕為「產生新資料」。這些是截图中的介面，不是本次實際點擊的操作。

**圖片：最小平方誤差**

最佳 b₀、b₁ 需使下列函數最小：

\[
SSE(b_0,b_1)=\sum_{i=1}^{n}[y_i-(b_0+b_1x_i)]^2
\]

最佳解記法：

\[
(\hat b_0,\hat b_1)=\arg\min_{b_0,b_1}\sum_{i=1}^{n}[y_i-(b_0+b_1x_i)]^2
\]

**補充**：arg min 是「讓目標函數最小的參數」，不是最小誤差的數值本身。本頁的負斜率資料與前面的正斜率房價示例不同，不宜混成同一組資料。

<a id="ai-p012"></a>

### AI-P012｜以偏微分推導線性迴歸係數

[原講義《20260907AI應用(20260915).pdf》第12頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=12)

**圖片「4.公式推導概念」逐步內容**

1. 平方誤差函數：
   \[
   SSE=\sum_{i=1}^{n}(y_i-b_0-b_1x_i)^2
   \]
2. 分別對 b₀、b₁ 偏微分，令其等於0：
   \[
   \frac{\partial SSE}{\partial b_0}=0,\qquad\frac{\partial SSE}{\partial b_1}=0
   \]
3. 得到常態方程式（Normal Equations）：
   \[
   \sum_{i=1}^{n}(y_i-b_0-b_1x_i)=0
   \]
   \[
   \sum_{i=1}^{n}x_i(y_i-b_0-b_1x_i)=0
   \]
4. 整理為係數解析解：
   \[
   \hat b_1=\frac{\sum(x_i-\bar x)(y_i-\bar y)}{\sum(x_i-\bar x)^2},\qquad
   \hat b_0=\bar y-\hat b_1\bar x
   \]

**補充**：x̄、ȳ分別是X與Y的樣本平均；上述斜率公式需要X不是全部相同，否則分母為0，無法用此式求出唯一斜率。

頁面下方開始下一節 **「房價預測1（California Housing）」**，本頁尚未提供程式或房屋資料；實例在後頁展開。

<a id="ai-p013"></a>

### AI-P013｜用坪數預測房價：五筆示範資料與迴歸線

[原講義《20260907AI應用(20260915).pdf》第13頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=13)

**講義圖片表格**

|房屋坪數X|房價Y（萬元）|
|---:|---:|
|10|300|
|20|500|
|30|700|
|40|900|
|50|1100|

- 上方以文字式散點圖呈現坪數越大、房價越高，X軸為坪數、Y軸為房價（萬元）。
- 文字解釋：Linear Regression 要找最符合所有資料的直線。
- 下方實際繪圖視窗標題為「線性回歸」，X軸「坪數」、Y軸「房價」；五個藍點恰落在紅色上升直線上。視窗工具列可見首頁、前後導覽、平移、縮放、設定與儲存圖示，未顯示操作過程。

**補充／資料來源界線**：雖然節名沿用 California Housing，本頁明確寫「假設有以下資料」，展示的是五筆坪數與萬元的教學數據，不是已證明載入 California Housing 原始資料集的結果。

<a id="ai-p014"></a>

### AI-P014｜fit訓練、predict預測與輸出

[原講義《20260907AI應用(20260915).pdf》第14頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=14)

**圖片與流程**

- 上方直線互動圖寫 `y=mx+b`，滑桿顯示 `m=1.0`、`b=5.0`，藍線對應此示意設定。
- 圖下符號表使用另一組記號：Y是預測值（例如房價）、X是輸入值（例如坪數）、b₀是截距（Intercept）、b₁是斜率（Slope）。對照關係是 m=b₁、b=b₀。
- 講義完整流程：**房屋資料（坪數、房價） → 建立X、y → Linear Regression → 模型訓練fit() → 得到方程式Y=100+20X → predict() → 預測新房價**。

**黑底輸出截圖逐字數值**

```text
截距: 100.00000000000011
斜率: 19.999999999999996
35坪預測房價: 800.0
```

**補充／圖文不一致提醒**：互動圖的m=1、b=5是一般直線示意，並非此房價模型的20與100；不能把上圖斜率當成訓練結果。上列是講義畫面，不是本次重跑程式的輸出。

<a id="ai-p015"></a>

### AI-P015｜浮點誤差、LE01.py與第二個房價案例

[原講義《20260907AI應用(20260915).pdf》第15頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=15)

**講義圖片內容**

- 說明前頁截距與斜率尾數是浮點數（Floating Point）的精度誤差，可以視為截距100、斜率20。
- 模型公式框：`y=20x+100`。
- x代表房屋坪數，y代表預測房價（萬元）。
- 本頁再貼一次 `y=mx+b` 互動圖，滑桿仍顯示m=1.0、b=5.0，並不是房價係數已更新的圖。
- 黃底紅字指出範例檔 **`LE01.py`**。本頁沒有展示該檔完整原始碼，故不可憑頁面捏造程式。
- 頁底開始 **「房價預測2（California Housing）」**，並寫「原始資料」，資料表續下一頁。

**補充**：浮點表示造成極小尾差，與房價預測的統計誤差是兩件不同的事；不能因為係數接近整數就推論真實房價毫無不確定性。

<a id="ai-p016"></a>

### AI-P016｜多特徵房價CSV、資料列與預測目標

[原講義《20260907AI應用(20260915).pdf》第16頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=16)

**講義內容**：共有120筆，80%訓練、20%測試；模型為 Linear Regression。Excel截圖顯示前19筆資料，以下完整轉錄可見欄位及數字（原欄名為「房價萬元」）。

|編號|行政區|坪數|屋齡|房間數|樓層|捷運距離|學校距離|有車位|房價萬元|
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
|1|台北市信義區|19.2|17|2|5|1103|1485|0|1534|
|2|台南市東區|19.5|5|2|17|995|154|1|580|
|3|新北市新店區|51.7|34|4|15|1818|669|1|2500|
|4|新北市板橋區|50.8|21|4|7|1238|309|1|2776|
|5|台北市信義區|35.9|22|3|2|1508|1198|1|3347|
|6|台北市信義區|43.9|40|4|23|1581|193|0|3902|
|7|新北市新店區|54.3|5|4|13|1053|1028|1|2779|
|8|台中市西屯區|34.7|17|3|18|392|434|0|1328|
|9|高雄市左營區|35.8|40|3|22|2381|1673|1|1087|
|10|台北市大安區|55.8|25|4|7|1196|1570|1|5159|
|11|台中市西屯區|28|31|3|5|1720|385|1|1061|
|12|桃園市中壢區|53.1|27|5|12|2490|383|0|1473|
|13|高雄市左營區|22.3|3|2|21|549|1722|0|727|
|14|台南市東區|35.9|29|3|18|2267|1493|0|598|
|15|台北市信義區|50|34|4|4|1192|990|1|4380|
|16|桃園市中壢區|63.7|11|4|21|2179|1408|1|1989|
|17|新北市新店區|25.2|10|1|20|2309|1100|1|1603|
|18|桃園市中壢區|29.3|15|1|3|2423|1771|1|825|
|19|台北市信義區|64|34|5|22|615|1225|1|5847|

**要預測的新房子**

- 中壢區、35坪、屋齡8年、3房、12樓。
- 距捷運400公尺、距學校600公尺、有車位。
- 講義所列預測：**1022.9萬元**。
- 本頁只在底部寫「流程如下」，完整流程位於下一頁。

**補充／資料來源疑點**：本例表格明確列台灣行政區，與節名 California Housing 不相符，故以「講義的台灣行政區房價CSV案例」理解，不冒稱其為加州資料集。截圖只顯示19筆，不能推造其餘101筆，120筆總數依正文記錄。價格是教材資料，非目前行情。

<a id="ai-p017"></a>

### AI-P017｜房價預測完整流程與行政區虛擬變數

[原講義《20260907AI應用(20260915).pdf》第17頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=17)

**正文流程**

CSV房價資料 → 讀取資料（pandas） → 資料前處理（文字轉數字） → 建立X/y → 切分Train/Test → 建立Linear Regression → 模型訓練fit() → 模型預測predict() → 模型評估（MAE、RMSE、R²） → 預測新房價。

**步驟1：讀取CSV資料**。本頁只列步驟名稱，未印出讀取檔名或 `read_csv` 呼叫。

**步驟2：文字轉數字**。原文程式：

```python
df = pd.get_dummies(df, columns=["行政區"], drop_first=True)
```

- 註解：行政區欄位轉為虛擬變數，並刪除第一個欄位以避免多重共線性。
- 原文舉例：行政區_中壢區、行政區_桃園區、行政區_平鎮區、行政區_八德區，變成0、1方便模型學習。
- 「轉換前」截圖是前頁相同房價表的前14筆，欄位與數值同AI-P016。
- 「轉換後」圖實際顯示的七個行政區欄，依序是：
  1. `行政區_台北市信義區`
  2. `行政區_台北市大安區`
  3. `行政區_台南市東區`
  4. `行政區_新北市新店區`
  5. `行政區_新北市板橋區`
  6. `行政區_桃園市中壢區`
  7. `行政區_高雄市左營區`
- 圖中其他欄為坪數、屋齡、房間數、樓層、捷運距離公尺、學校距離公尺、有車位、房價萬元；注意與先前Excel畫面相比，距離欄名多了「公尺」。
- 前五筆數值仍是原資料1–5；行政區布林向量按上列順序為：

|原編號|七個行政區欄位的TRUE/FALSE（T/F簡記）|
|---:|---|
|1|T,F,F,F,F,F,F|
|2|F,F,T,F,F,F,F|
|3|F,F,F,T,F,F,F|
|4|F,F,F,F,T,F,F|
|5|T,F,F,F,F,F,F|

**補充／圖文差異**

- 正文示例行政區是簡化示例，與實際截圖的行政區名稱不同，不可直接照正文四個名字建立此模型輸入。
- 圖片實際輸出的是TRUE/FALSE，而非字面上的0/1；兩者表達相同的二元指示概念，但資料型別及匯出形式仍須分清。
- `drop_first=True` 留一類為基準，不是任意刪掉原資料第一欄。依前後圖推斷，此例省略的基準類別為台中市西屯區；這是圖表對照推論，不是本頁正文直接宣布。
- 這樣可避免「截距＋所有類別指示欄」必然線性相依，但不保證消除其他特徵間的所有共線性。

<a id="ai-p018"></a>

### AI-P018｜建立X/y、分割資料與多維迴歸

[原講義《20260907AI應用(20260915).pdf》第18頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=18)

**上方公式圖**：重用 `ŷ=b₀+b₁x` 的互動圖，示例擬合 `ŷ=8.49−0.54x；R²=0.72`，含「資料／最佳擬合線／預測值／殘差」焦點切換和「產生新資料」按鈕。這是單特徵說明圖，不是下方房價CSV的訓練成績。

**步驟3：建立X、y**

- X（Features，特徵、輸入資料）：模型拿來學習的資料。黑底截圖含7個數值／二元欄，以及AI-P017列出的7個行政區指示欄；不含房價及編號。
- X前五筆數值欄完整內容：

|索引|坪數|屋齡|房間數|樓層|捷運距離公尺|學校距離公尺|有車位|
|---:|---:|---:|---:|---:|---:|---:|---:|
|0|19.2|17|2|5|1103|1485|0|
|1|19.5|5|2|17|995|154|1|
|2|51.7|34|4|15|1818|669|1|
|3|50.8|21|4|7|1238|309|1|
|4|35.9|22|3|2|1508|1198|1|

- 各列行政區布林值與前頁五筆轉換結果相同。
- y（Target、Label、目標值）：模型要預測的答案。圖中索引0–4依序是 `1534, 580, 2500, 2776, 3347`，即這五筆房價萬元。

**步驟4：切分Train/Test**：20%測試、80%訓練。本頁沒有提供 `random_state` 或分割程式，不能推斷測試資料的抽樣設定。

**步驟5：建立Linear Regression並fit()**：一個特徵（如坪數）時可畫成直線；若多於兩個特徵（文中以10個特徵為例），模型是高維超平面，無法直接完整畫在三維空間。

**補充**：圖中可見實際X共有14個欄位；「10個特徵」只是正文舉例。兩個特徵加一個輸出可畫成三維中的平面，下一頁以圖說明。

<a id="ai-p019"></a>

### AI-P019｜直線／平面示意、測試輸入與預測結果

[原講義《20260907AI應用(20260915).pdf》第19頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=19)

**上方圖解**

- 左圖：房價對坪數的上升散點，說明單特徵線性關係。
- 右上圖：三個方向分別標房價、坪數、屋齡；右下圖寫「這是一個平面（如果只有兩個特徵）」，以虛線三角形狀示意坪數與屋齡共同影響房價y。
- 圖是概念草圖，未提供平面係數、刻度或實際二特徵訓練結果。

**步驟6：predict()**。正文標題「模型預測與模型預測predict()」有重複用字，依原意是使用模型預測。

**測試輸入圖：全部10筆可見資料**。以下將七個行政區指示欄還原為唯一TRUE的欄名，其他六欄均FALSE；這是無損文字呈現，不是另造行政區。

|畫面順序|坪數|屋齡|房間數|樓層|捷運距離公尺|學校距離公尺|有車位|TRUE的行政區|
|---:|---:|---:|---:|---:|---:|---:|---:|---|
|1|62.6|12|5|8|183|1069|0|台北市大安區|
|2|28.6|12|1|2|703|1073|0|桃園市中壢區|
|3|30.8|38|3|7|962|1135|1|新北市板橋區|
|4|34.5|32|3|1|1737|634|0|桃園市中壢區|
|5|34.2|35|4|15|2325|486|1|高雄市左營區|
|6|38.8|35|2|21|501|130|1|台北市信義區|
|7|49.3|29|4|3|1278|807|1|桃園市中壢區|
|8|44.2|7|4|15|1969|1244|1|台北市大安區|
|9|51.3|3|3|2|1037|245|1|台北市信義區|
|10|24.2|19|2|25|1972|119|0|台南市東區|

**黑底結果截圖（房價單位沿用萬元）**

|索引|實際房價|預測房價|
|---:|---:|---:|
|0|5870|4651.396271|
|1|565|411.858522|
|2|1821|1640.955176|
|3|834|279.166959|
|4|1127|890.420510|
|5|3789|3926.570905|
|6|1482|1353.482006|
|7|4239|4139.871969|
|8|4805|4370.453261|
|9|487|222.584098|

本頁開始步驟7「模型評估」，列出 **MAE：mean absolute error（平均絕對誤差）**，公式續下頁。以上數值逐字抄錄自教材截圖，非執行所得，也不表示完整測試集只有這10筆。

<a id="ai-p020"></a>

### AI-P020｜MAE公式、手算範例與RMSE名稱勘誤

[原講義《20260907AI應用(20260915).pdf》第20頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=20)

**講義圖片：MAE（Mean Absolute Error，平均絕對誤差）**

MAE是預測值與真實值誤差的平均，不考慮誤差方向，全部取絕對值。

\[
MAE=\frac1n\sum_{i=1}^{n}|y_i-\hat y_i|
\]

n是資料筆數；yᵢ是第i筆真實值（Actual）；ŷᵢ是第i筆預測值（Predicted）；絕對值符號表示取非負的誤差大小。

|真實值|預測值|誤差|絕對誤差|
|---:|---:|---:|---:|
|100|95|5|5|
|120|125|−5|5|
|90|85|5|5|

圖中計算 `MAE=(5+5+5)/3=5`，代表平均每筆資料預測誤差約5單位。

**原文與勘誤分開**

- 頁底原文是：`RMSE: mean squared error（中文：均方誤差）`。
- **勘誤**：Mean Squared Error／均方誤差的縮寫是 **MSE**；**RMSE**應為 **Root Mean Squared Error／均方根誤差**。下頁圖片有平方根，實際教的是RMSE，不應沿用此處錯置英文。

<a id="ai-p021"></a>

### AI-P021｜RMSE與MSE的區別及MAE比較

[原講義《20260907AI應用(20260915).pdf》第21頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=21)

**講義圖片：RMSE（Root Mean Squared Error，均方根誤差）**

RMSE先把誤差平方、求平均，再開根號，因此對較大的誤差給予較大懲罰。

\[
RMSE=\sqrt{\frac1n\sum_{i=1}^{n}(y_i-\hat y_i)^2}
\]

n為資料筆數、yᵢ為真實值、ŷᵢ為預測值。

本頁圖片明確提醒：RMSE不是MSE；均方誤差的公式是

\[
MSE=\frac1n\sum_{i=1}^{n}(y_i-\hat y_i)^2,\qquad RMSE=\sqrt{MSE}
\]

**範例表格**

|真實值|預測值|誤差|誤差平方|
|---:|---:|---:|---:|
|100|95|5|25|
|120|125|−5|25|
|90|85|5|25|

圖中算式：`RMSE=√((25+25+25)/3)=√25=5`。

**下方比較三點**

- MAE：每個誤差權重相同，容易理解，代表平均誤差。
- RMSE：大誤差會被放大，較能反映嚴重預測錯誤。
- 兩者越小越好，表示預測越準。

頁底開始「8、模型評估（MAE、RMSE、R²）」。

**補充**：MAE與RMSE有原目標值的單位，MSE為平方單位；跨資料集比較時也要看房價尺度，不能只比未正規化誤差數值。本頁剛好每筆絕對誤差都相同，因此兩種指標得到同一結果，不代表它們普遍相等。

<a id="ai-p022"></a>

### AI-P022｜R²公式、RSS與TSS的意義

[原講義《20260907AI應用(20260915).pdf》第22頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=22)

**講義圖片公式**

\[
R^2=1-\frac{\sum(y_i-\hat y_i)^2}{\sum(y_i-\bar y)^2}
\]

- yᵢ：真實值。
- ŷᵢ：模型預測值。
- ȳ：所有真實值的平均。

**拆開理解**

1. 分子 **RSS（Residual Sum of Squares）**：`Σ(yᵢ−ŷᵢ)²`。講義稱模型預測的誤差總和，越小越好；精確而言是「誤差平方和」，不是帶符號誤差直接相加。
2. 分母 **TSS（Total Sum of Squares）**：`Σ(yᵢ−ȳ)²`。代表資料本身的總變異，即原資料有多少變化。
3. 因此 `R²=1−模型誤差／資料總變異`，表示模型解釋了多少比例的資料變異。

**補充**：此處RSS與前文SSE採同一個殘差平方和公式；不同教材符號可能有差異，應看公式而非只看縮寫。R²不是分類正確率，也不是每一筆房價的相對誤差。若真實值全相同，TSS為0，此比例式不能直接使用。

<a id="ai-p023"></a>

### AI-P023｜R²範圍、平均值基準與五筆示範資料

[原講義《20260907AI應用(20260915).pdf》第23頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=23)

**講義圖片**：通常 `−∞ < R² ≤ 1`。

|R²|講義解讀|
|---:|---|
|1.0|完全預測正確|
|0.9|非常好|
|0.8|良好|
|0.6|尚可|
|0|與直接用平均值預測一樣|
|<0|比直接預測平均值還差|

**下方例子**：假設5筆房價資料：

|房屋|真實值y|預測值ŷ|
|---|---:|---:|
|A|500|490|
|B|600|610|
|C|700|690|
|D|800|790|
|E|900|910|

這組資料用於後續分步計算R²，與前面120筆CSV測試輸出不同。

**補充／適用界線**：0.9、0.8、0.6的「非常好／良好／尚可」是講義教學標籤，不是各領域通用驗收門檻；實務還要看資料噪音、基準模型、留出測試資料表現及誤差是否可接受。R²負值並非公式錯誤，代表相對該評估集平均值基準更差。

<a id="ai-p024"></a>

### AI-P024｜R²手算第一、二步：真值平均與RSS

[原講義《20260907AI應用(20260915).pdf》第24頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=24)

**第一步：求平均值**

圖中真實房價平均：

\[
\bar y=\frac{500+600+700+800+900}{5}=700
\]

**第二步：計算RSS（Residual Sum of Squares，殘差平方和）**

\[
RSS=\sum(y_i-\hat y_i)^2
\]

逐筆計算表：

|真實值|預測值|誤差|誤差平方|
|---:|---:|---:|---:|
|500|490|10|100|
|600|610|−10|100|
|700|690|10|100|
|800|790|10|100|
|900|910|−10|100|

圖中加總：`RSS=100+100+100+100+100=500`。

**觀念補充**：這一步以模型預測ŷ為比較基準；下一頁TSS則使用整組真實值的平均ȳ，兩者比較的對象不同，不可混用。

<a id="ai-p025"></a>

### AI-P025｜R²手算第三、四步與實際／預測散點圖

[原講義《20260907AI應用(20260915).pdf》第25頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=25)

**第三步：計算TSS（Total Sum of Squares，總平方和）**

\[
TSS=\sum(y_i-\bar y)^2
\]

因平均值為700，表格如下：

|真實值|平均值|差值|差值平方|
|---:|---:|---:|---:|
|500|700|−200|40000|
|600|700|−100|10000|
|700|700|0|0|
|800|700|100|10000|
|900|700|200|40000|

圖中加總：`TSS=40000+10000+0+10000+40000=100000`。

**第四步：代入R²公式**

\[
R^2=1-\frac{RSS}{TSS}=1-\frac{500}{100000}=1-0.005=0.995
\]

圖中結果框為 `R²=0.995`，解釋為模型可以解釋99.5%的房價變異。這是前述A–E五筆教學數據的手算結果。

**下方「實際房價與預測房價」圖表**

- 視窗為 Figure 1，圖名 `Linear Regression`。
- X軸 `Actual Price`（實際房價），Y軸 `Predict Price`（預測房價）。
- 藍點表示每筆實際／預測配對，紅色對角線代表理想的預測=實際；後頁正文說明點越接近此線越好。
- 圖上可見：較高實際房價的數個點在紅線下方，部分中價點在紅線上方；左下方另有預測落在0以下的點。圖形只支持這些定性觀察，不提供每一點可精確回讀的原始數值。
- 工具列含首頁、前後導覽、平移、縮放、子圖配置、儲存按鈕；本次未操作。

**補充／避免誤讀**

- 下方散點圖不是A–E五筆手算資料的圖，點數與房價範圍明顯不同，不能把 `R²=0.995` 當成此CSV模型的測試成績。
- 無約束線性迴歸可產生負預測；對房價而言不具實際意義，是應檢查模型、資料與業務限制的訊號，不應將負值直接視為合理成交價。
- 本段頁面未列這個房價CSV模型完整的MAE、RMSE與R²數值輸出，不能用前面手算範例替代。

<a id="ai-p026"></a>

### AI-P026｜新房價輸入向量、最終示範輸出與LE02.py

[原講義《20260907AI應用(20260915).pdf》第26頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=26)

**承接圖表說明**：原文註解為「如果預測效果好，大部分點會靠近紅色對角線。」這是實際值／預測值一致性的視覺檢查。

**步驟9：預測新房價**

黑底單列DataFrame截圖之欄名沿用訓練X；因中文表頭與資料字元顯示寬度造成視覺錯位，以下依欄位順序並與AI-P016條件對照整理：

|特徵|新資料值|
|---|---:|
|坪數|35|
|屋齡|8|
|房間數|3|
|樓層|12|
|捷運距離公尺|400|
|學校距離公尺|600|
|有車位|1|
|行政區_台北市信義區|0|
|行政區_台北市大安區|0|
|行政區_台南市東區|0|
|行政區_新北市新店區|0|
|行政區_新北市板橋區|0|
|行政區_桃園市中壢區|1|
|行政區_高雄市左營區|0|

圖中索引為0。紅框標示最終輸出：

```text
預測房價：1022.9 萬元
```

黃底紅字標註範例檔 **`LE02.py`**，本頁未提供完整程式內容。本段只轉錄教材畫面，沒有執行此檔，也沒有驗證教材外部CSV及模型檔是否可重現這個數字。

**補充／實作時要注意**

- 新資料必須使用與訓練相同的欄名、順序、編碼規則及單位；不能只丟入「中壢區」文字就視為已完成前處理。
- `fit()`是從訓練資料估計係數，`predict()`是以已建立的係數計算新資料輸出；新資料預測不應重新fit單筆房子。
- 行政區指示欄須依模型的類別集合對齊；七欄全0通常代表本例省略的基準類別，不自動代表「任何未知行政區」。
- 1022.9萬元是此教材示範值，不能視為目前中壢房價或個案估價保證。



## AI 應用講義逐頁知識筆記（第27–51頁）

來源：`20260907AI應用(20260915).pdf`。以下依 PDF 實際頁次記錄，已逐頁觀看頁圖，並與文字層交叉核對。**「講義內容」保留原有名稱、步驟與畫面；「補充／辨誤」為整理者說明，不冒充講義原文。** 截圖的執行結果只代表該次示範，未在本次閱讀工作執行其中程式；價格、功能與介面（若有）不視為今日狀態。

<a id="ai-p027"></a>

### AI-P027｜把已訓練房價模型接到 Django：建立專案與樣板設定

[原講義《20260907AI應用(20260915).pdf》第27頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=27)

**講義內容與操作順序**

本節是「房價預測（已訓練好模型＋Django Web）」，重點是將既有模型接上網頁，而不是在每次網頁請求重新訓練。

講義依序列出的命令（原文行首皆有 `#`）：
```text
# pip install Django
# Django-admin startproject Leweb
# cd Leweb
# python manage.py startapp myapp
# mkdir templates
# mkdir static
```

接著修改 `settings.py`：
```python
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

**各設定的意義（補充）**
- `myapp` 加入應用程式清單；原有 admin、auth、contenttypes、sessions、messages、staticfiles 保留。
- `DIRS` 紅字表示要加入專案根目錄下的 `templates`；`APP_DIRS=True` 另允許搜尋 app 內的樣板。
- context processors 提供除錯、request、登入驗證、訊息等樣板環境資料。
- `ALLOWED_HOSTS=['*']` 是講義示範值；正式服務應限制合法網域，不能把萬用字元當作部署安全預設。
- 原文 `Django-admin` 大小寫與一般使用的 `django-admin` 不同；此處保留原文。命令行首 `#` 是教材列示方式，在 shell 直接照貼會成為註解。
- 本頁只提供專案／設定步驟，沒有展示載入 `.pkl`、view、URL 或 HTML 完整實作，不補造缺失程式。

<a id="ai-p028"></a>

### AI-P028｜繁中／時區／靜態檔設定與房價網站生成提示詞

[原講義《20260907AI應用(20260915).pdf》第28頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=28)

**講義設定續接**
```python
LANGUAGE_CODE = 'zh-Hant'
TIME_ZONE = 'Asia/Taipei'
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```
- 語系設為繁體中文、時區設為臺北；靜態檔目錄為專案下 `static`。
- 接續操作：`python manage.py makemigrations`（建立 migration 資料檔）、`python manage.py migrate`（模型與資料庫同步）、`python manage.py runserver 0.0.0.0:8080`。
- **補充**：此處「模型與資料庫同步」指 Django 資料模型，不是機器學習模型。`0.0.0.0` 是服務綁定所有網路介面，開發伺服器不應直接當正式部署。

**講義給 ChatGPT 的需求內容**（原文標作「尋問 ChaptGPT」）
1. 提供完整特徵欄位，順序為：`坪數,屋齡,房間數,樓層,捷運距離公尺,學校距離公尺,有車位,行政區_台北市信義區,行政區_台北市大安區,行政區_台南市東區,行政區_新北市新店區,行政區_新北市板橋區,行政區_桃園市中壢區,行政區_高雄市左營區`。
2. 提供範例資料：`59.3,23,5,15,1267,1540,1,True,False,False,False,False,False,False`。
3. 說明利用 Linear Regression 建立模型，檔名 `LinearRegressionModel.pkl`。
4. 要求「建立一個 django 網站使用初學者的程式寫法」，專案名為 **`Lewweb`**，app 名為 `myapp`，讓使用者輸入資料。

本頁的 `new_house` 前半段：
```python
new_house = pd.DataFrame({
    "坪數": [35],
    "屋齡": [8],
    "房間數": [3],
    "樓層": [12],
    "捷運距離公尺": [400],
    "學校距離公尺": [600],
    "有車位": [1],
    # 行政區欄位接下一頁
```
**補充／辨誤**：第27頁命令用 `Leweb`，本頁提示詞用 `Lewweb`，兩者拼字不一致，不能默認相同路徑。提示詞給的是既有特徵與模型名稱；本頁沒有給目標價格欄，因此不能僅憑這一列自行重建其訓練模型。

<a id="ai-p029"></a>

### AI-P029｜行政區 one-hot 選擇與房價預測網站需求完成

[原講義《20260907AI應用(20260915).pdf》第29頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=29)

**講義內容**
承接前頁的 `pd.DataFrame`，最後七欄如下：
```python
    "行政區_台北市信義區": [0],
    "行政區_台北市大安區": [0],
    "行政區_台南市東區": [0],
    "行政區_新北市新店區": [0],
    "行政區_新北市板橋區": [0],
    "行政區_桃園市中壢區": [1],
    "行政區_高雄市左營區": [0]
})
```
- 原文再次逐行列出這七個行政區欄位，要求「讓使用者選擇」，「最後產生預測房價結果」。本例選的是桃園市中壢區。
- 黃底標示生成式 AI 範例檔：`範例:Django 房價預測網站(LE).mhtml`（前有「生成式 AI 範例」字樣）。這是講義指向的本地範例檔名，並未提供網路網址或檔案內容。
- 頁尾「結果：」的截圖接在第30頁，本頁沒有預測數值。

**知識說明（補充）**
- 七個 0/1 欄位是行政區的 one-hot 表示；網頁可用單一行政區選單，再轉成模型所需的完整欄位，不能直接把行政區字串當數值特徵。
- 資料框每個值使用單元素串列，形成一筆資料。實際送入模型時，欄位名稱、順序、型別與訓練期必須一致；不同頁面出現的 `True/False` 與 `1/0` 也應以既有模型輸入規格為準。

<a id="ai-p030"></a>

### AI-P030｜房價預測網站實際畫面

[原講義《20260907AI應用(20260915).pdf》第30頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=30)

**圖中操作與結果**
- 瀏覽器頁籤為「房價預測系統」，網址顯示 `192.168.57.246:8080`，HTTP 畫面旁標示「不安全」。這是課堂區域網路位址，非公開服務連結。
- 表單標題：`Linear Regression 房價預測系統`；上方藍色標題、白色卡片，底部綠色結果區。
- 依序輸入：坪數 `35`、屋齡 `8`、房間數 `3`、樓層 `12`、捷運距離（公尺）`400`、學校距離（公尺）`600`。
- 「是否有車位」下拉選單選「有車位」；「行政區」選「桃園市中壢區」。
- 按鈕：「預測房價」。結果區顯示「預測結果」「預測房價：1049.51 萬元」。
- **補充**：這是講義模型對示範輸入的輸出，不是真實成交價，也不是現行房價估值保證；本頁未展示誤差範圍或外部驗證。

<a id="ai-p031"></a>

### AI-P031｜KNN 定義、歐氏距離與優缺點

[原講義《20260907AI應用(20260915).pdf》第31頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=31)

**講義內容**
- 節名為 `4.2 KNN（K-Nearest Neighbors，K 最近鄰演算）`。
- KNN 是監督式學習。以「物以類聚，人以群分」說明：新資料進來時，找距離最近的 K 個已知資料，再依鄰居結果預測。
- 講義說「不會先建立數學公式」，意指先保留已知資料，預測時找鄰居投票；重點在於距離計算。
- 最常見距離是歐氏距離。圖中二維公式：
  \(d=\sqrt{(x_1-x_2)^2+(y_1-y_2)^2}\)。
- 圖例 A=`(150,45)`、B=`(160,50)`，圖中推導：
  \(d=\sqrt{(160-150)^2+(50-45)^2}=\sqrt{100+25}=\sqrt{125}=11.18\)。此處 `11.18` 是講義顯示的近似值。
- 圖中文字：「距離越小，代表兩筆資料越相似」。

| 優點 | 限制 |
|---|---|
| 演算法簡單、容易理解 | 資料量大時預測較慢，講義以與所有資料比較距離說明 |
| 不需要建立複雜模型 | 對雜訊較敏感 |
| 適合小型資料集 | K 值的選擇會影響結果 |
| 可用於分類與迴歸 | 特徵尺度差異大時須標準化或正規化 |

**補充**：分類常用多數決，迴歸則聚合鄰居的數值（如平均），不能將「投票」視為所有 KNN 任務唯一規則。所謂不建公式不代表沒有 `fit` 或可忽略訓練資料；距離仍有數學定義。圖中距離例子只是座標計算，未明示兩軸單位。

<a id="ai-p032"></a>

### AI-P032｜身高分類教學：資料、距離與選取最近 K 位

[原講義《20260907AI應用(20260915).pdf》第32頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=32)

**講義資料與假設**
以身高判斷範例資料的「男／女」標籤，待預測輸入是 `165 cm`。

| 編號 | 身高（cm） | 講義標籤 | 與165的距離（照圖） |
|---|---:|---|---:|
| 1 | 150 | 女 | 15 |
| 2 | 155 | 女 | 10 |
| 3 | 160 | 女 | 5 |
| 4 | 170 | 男 | 5 |
| 5 | 175 | 男 | 10 |
| 6 | 180 | 男 | 15 |

1. **第一步：計算距離**。本例只有一個特徵，圖中公式「距離＝\(|A-B|\)」，例子 \(|165-150|=15\)。對所有已知身高重複計算。
2. **第二步：選 K 個最近**。假設 `K=3`，圖中選出：160／女／5，170／男／5，155／女／10。
3. 投票在下一頁。

**補充／辨誤**
- 155 與175距離同為10，第三個鄰居的選擇存在距離平手；講義選155但本頁未說明排序或 tie-breaking 規則。因此這組結果依賴鄰居挑選方式，不能宣稱是唯一可能結果。
- 此為極小的分類演算法教學資料；身高不足以可靠判定真實人物的性別，更不應把教材的二元標籤當作對所有人的完整描述。

<a id="ai-p033"></a>

### AI-P033｜KNN 身高圖解：距離排序與多數決

[原講義《20260907AI應用(20260915).pdf》第33頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=33)

**四張圖的內容**
1. 數線將150、155、160置於「女」側，170、175、180置於「男」側；箭頭標示新資料「身高165cm」，位置介於160與170。
2. 依距離列出：`160 女 ↔5`、`170 男 ↔5`、`155 女 ↔10`、`175 男 ↔10`、`150 女 ↔15`、`180 男 ↔15`。
3. 「第三步：投票」：女生2票、男生1票，因此「預測結果：女生」。
4. 再以核取標記強調只取最近三位：160女、170男、155女；不是把六筆資料全部拿來投票。下方重列女生2票、男生1票。

**補充**：這一頁延續上一頁選155為第三位的前提。數線展示的是一維距離概念，不是統計上證明身高與性別的固定界線。

<a id="ai-p034"></a>

### AI-P034｜改變 K 值、完整預測流程與平手處理

[原講義《20260907AI應用(20260915).pdf》第34頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=34)

**講義圖文**
- 若 `K=5`，圖列最近五位：160女、170男、155女、175男、150女。女生3票、男生2票，結果仍是女生。
- 完整流程：`訓練資料 → 不建立公式 → 輸入新資料 → 計算與所有資料的距離 → 找最近 K 個鄰居 → 投票 → 輸出分類結果`。
- 平手問題的三種方法：
  1. 「K 選奇數（就沒有平手問題）」——原文如此。
  2. 看誰距離最近。圖中待預測值沿用165：166男距離1、164女距離1，仍然平手；改成166男距離1、160女距離5，就可選距離最近的男生。
  3. 距離加權投票（Weighted KNN），示例續第35頁。

**補充／辨誤**
- 奇數 K 只是在二元、每鄰居同權投票且鄰居集合已固定時避免票數平手；多類別、距離加權、鄰居邊界同距離仍可能平手。
- `K=5` 的150與180同距離；本圖選150，仍有選取規則未說明的問題。
- 選最近者與距離加權並非任何情況都能消除平手，仍需明確而可重現的處理規則。

<a id="ai-p035"></a>

### AI-P035｜Weighted KNN 權重範例與身高散點輸出

[原講義《20260907AI應用(20260915).pdf》第35頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=35)

**上方加權例子**
圖中權重採 `1/d`：

| 身高 | 性別標籤 | 距離 | 權重1/d |
|---:|---|---:|---:|
| 164 | 女 | 1 | 1.00 |
| 170 | 男 | 5 | 0.20 |

雖然各一票，女生總權重1.00、男生0.20，因此預測女生。距離小者的影響較大。

**下方程式結果**
- Matplotlib `Figure 1`：藍點圖例「訓練資料」、紅點圖例「預測資料」。
- 六個藍點位在身高150、155、160、170、175、180；紅點位在165。各點皆排在 `y=0` 水平線，縱軸只是繪圖配置，不是第二個訓練特徵。
- 黃底標示範例：`knn01.py`。本頁沒有展示該程式的原始碼或文字分類輸出，不能從圖例顏色推定藍色就是某個性別。

**補充**：`1/d` 在距離為0時需特殊處理，不能直接除以0；圖例未討論此情況。

<a id="ai-p036"></a>

### AI-P036｜KNN 與線性迴歸比較；手寫數字資料來源

[原講義《20260907AI應用(20260915).pdf》第36頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=36)

**圖中比較表**
| 比較項目 | Linear Regression | KNN |
|---|---|---|
| 模型類型 | 建立一條最佳迴歸線 | 不建立公式，直接比鄰居 |
| 學習方式 | 訓練時求係數 | 只記住所有訓練資料 |
| 預測方式 | 代入公式計算 | 找最近的 K 個資料投票 |
| 適合用途 | 連續數值預測，如房價、溫度 | 分類，如是否為垃圾郵件、手寫數字、是否生病 |
| 是否需要距離 | 否 | 是，通常使用歐氏距離 |

**補充**：這是教材用來比較線性迴歸與 KNN 分類的簡表；KNN 也可做迴歸（第31頁已提及），不可把表格當作排除 KNN 迴歸的定義。

**新案例：利用 KNN 的手寫數字辨識系統（使用學者的資料庫與方法）**
- 講義原始參考連結：<https://archive.ics.uci.edu/ml/datasets/Optical+Recognition+of+Handwritten+Digits>。
- 參考論文：*Methods of Combining Multiple Classifiers and Their Applications to Handwritten Digit Recognition*。
- 下方資料來源截圖題為 `Class Labels`，分別列出原資料的 training set 與 testing set 各類樣本數：

| 類別 | 原來源 training set | 原來源 testing set |
|---:|---:|---:|
| 0 | 376 | 178 |
| 1 | 389 | 182 |
| 2 | 380 | 177 |
| 3 | 389 | 183 |
| 4 | 387 | 181 |
| 5 | 376 | 182 |
| 6 | 377 | 181 |
| 7 | 387 | 179 |
| 8 | 380 | 174 |
| 9 | 382 | 180 |

**補充**：這是來源頁的分配表，不是第37頁之後自行對 `load_digits()` 做80/20切分後的樣本數。閱讀後續結果時，應區分資料來源的既有分割與教學程式重新分割。

<a id="ai-p037"></a>

### AI-P037｜內建 digits 辨識結果與匯出 BMP 的完整需求

[原講義《20260907AI應用(20260915).pdf》第37頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=37)

**上半頁圖中結果**
- Matplotlib 視窗以兩排五欄展示標籤0至9的灰階手寫數字；黑底、白／灰筆畫，明顯看得出8×8的像素格。
- 終端執行 `knn02.py`，畫面顯示 `Accuracy: 0.9833333333333333`。這是該範例執行結果，不代表下一個匯出後重訓實驗必有相同準確率。
- 黃底範例檔名：`knn02.py`；本頁未提供其完整程式。

**新流程名稱**：「利用 KNN 的手寫數字辨識系統（匯出資料庫成圖片、匯出模型、測試圖片）」。第1步為「將現有資料庫匯出成圖片」。

**給 ChatGPT 的提示詞逐項保留**
- 角色／程度：「我是一位初階 python 程師」。
- 訓練來源：`digits = load_digits()`；共有1797筆資料，每筆為8×8灰階圖片，標籤是0～9。
- 希望將資料匯出成圖片檔，依標籤分類存放。
- 所有資料存成 `.bmp` 圖片，放在 `output` 下的 `handwritten` 資料夾。
- 分成 `train`、`test`，數量為80%與20%；各自依類別存放。
- 要顯示執行完成度，程式在 Mac 也能使用，請提供 Python 程式碼。
- 生成式 AI 範例：`Python 圖片匯出分類.mhtml`；「結果如下」延續到第38頁。

**補充**：`load_digits()` 是此例的8×8資料；不要與28×28的 MNIST 混為一談。提示詞要求跨平台，但單憑需求文字與 Windows 截圖不能證明 Mac 已測試通過。

<a id="ai-p038"></a>

### AI-P038｜BMP 匯出資料夾結構與重新訓練任務

[原講義《20260907AI應用(20260915).pdf》第38頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=38)

**兩張檔案總管畫面**
1. 路徑為 `D:\backup\myExam\machineLearning\output\handwritten`，紅框圈出 `test` 與 `train` 兩個資料夾。
2. 開啟 `output\handwritten\test\2`，紅框強調「分割／類別」路徑；內含數字2的 BMP 檔。可見命名從 `test_2_0000.bmp` 到 `test_2_0034.bmp`，檔名在小圖示下分行顯示。這是輸出程式的命名示例，不是後續讀檔的必要格式。
- 黃底範例檔：`knn03.py`。

**第2步的講義需求**
讀取現有資料庫，利用 KNN 訓練與測試，最後匯出模型 `knn_model.pkl`。給 ChatGPT 的資料夾描述從本頁開始、下頁續接，完整形狀為：
```text
data/
└── handwritten/
    ├── train/          # 訓練資料
    │   ├── 0/          # 數字0
    │   ├── 1/          # 數字1
    │   ├── 2/
    │   ├── ...
    │   └── 9/
    └── test/           # 測試資料
        ├── 0/
        ├── 1/
        ├── 2/
        ├── ...
        └── 9/
```
**補充／路徑注意**：匯出畫面在 `output/handwritten`，新訓練提示詞卻指定 `data/handwritten`；因此使用時需確認是否已搬移或改設定，本頁未展示搬移動作。此處只記錄講義差異，不假定兩處自動同步。

<a id="ai-p039"></a>

### AI-P039｜讀取任意 BMP 檔名、依資料夾標籤訓練測試

[原講義《20260907AI應用(20260915).pdf》第39頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=39)

**提示詞完成**
- `train`、`test` 各有0～9子資料夾（本頁接續前頁樹狀圖）。
- 內部圖片為 `.bmp`，名稱無固定。
- 「請給我簡單好理解的 python 程式，將這些資料讀取。利用 knn 訓練，再進行測式。」（原文「測式」指測試。）
- 生成式 AI 範例：`KNN 訓練與測試.mhtml`。

**終端畫面：knn04.py 的讀取結果**
| 數字標籤 | 成功讀取訓練圖片 | 成功讀取測試圖片 |
|---:|---:|---:|
| 0 | 142 | 36 |
| 1 | 146 | 36 |
| 2 | 142 | 35 |
| 3 | 146 | 37 |
| 4 | 145 | 36 |
| 5 | 145 | 37 |
| 6 | 145 | 36 |
| 7 | 143 | 36 |
| 8 | 139 | 35 |
| 9 | 144 | 36 |

**補充**：標籤應取自0～9資料夾，不可依賴固定檔名；這正是提示詞特別指出「名稱無固定」的原因。上方可見 PowerShell／VS Code Python 除錯啟動字串，部分超出截圖右側，這不是辨識演算法的必要操作指令，本次也沒有執行它。

<a id="ai-p040"></a>

### AI-P040｜8×8 KNN 訓練資料形狀、測試準確率與分類報告

[原講義《20260907AI應用(20260915).pdf》第40頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=40)

**第一張終端輸出**
```text
訓練圖片數量：1437
測試圖片數量：360
每張圖片的特徵數量：64
訓練資料形狀：(1437, 64)
訓練標籤形狀：(1437,)
測試資料形狀：(360, 64)
測試標籤形狀：(360,)
開始訓練 KNN 模型
KNN 模型訓練完成
開始測試
測試正確率：93.89%
```

**第二張圖的分類報告（逐列抄錄）**
| 類別 | precision | recall | f1-score | support |
|---|---:|---:|---:|---:|
| 0 | 0.95 | 0.97 | 0.96 | 36 |
| 1 | 0.77 | 1.00 | 0.87 | 36 |
| 2 | 0.95 | 1.00 | 0.97 | 35 |
| 3 | 0.93 | 1.00 | 0.96 | 37 |
| 4 | 1.00 | 0.97 | 0.99 | 36 |
| 5 | 0.97 | 1.00 | 0.99 | 37 |
| 6 | 0.97 | 0.94 | 0.96 | 36 |
| 7 | 0.97 | 0.97 | 0.97 | 36 |
| 8 | 0.96 | 0.66 | 0.78 | 35 |
| 9 | 1.00 | 0.86 | 0.93 | 36 |
| accuracy | — | — | 0.94 | 360 |
| macro avg | 0.95 | 0.94 | 0.94 | 360 |
| weighted avg | 0.95 | 0.94 | 0.94 | 360 |

範例檔名：`knn04.py`。本頁為資料資訊與分類報告，並沒有混淆矩陣。

**解讀（補充）**
- 一張圖轉成64維向量；資料陣列第一軸是圖片數，第二軸是特徵數；標籤是一維陣列。
- precision：預測成某類者之中，有多少是真的；recall：真實某類者之中，有多少被找回；F1 是兩者的調和平均；support 是該類真實測試樣本數。
- macro avg 是各類別等權平均；weighted avg 依 support 加權；accuracy 是整體分類正確比例。表格0.94是報告四捨五入顯示，不與上方93.89%衝突。
- 本例數字8的 recall 只有0.66，不能只看整體準確率而忽略類別落差；數字1的 recall 雖1.00，precision卻0.77。
- 與第37頁直接使用原始資料的 `knn02.py` 結果不同，不能在未控制分割與前處理條件下推斷單一原因。

<a id="ai-p041"></a>

### AI-P041｜訓練圖片前處理流程與自行手寫測試圖

[原講義《20260907AI應用(20260915).pdf》第41頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=41)

**講義完整流程**
```text
開始
→ 讀取0～9資料夾
→ 讀取BMP圖片
→ 灰階化
→ 縮放成8×8
→ 二值化
→ 正規化（0～1）
→ 攤平成64維特徵
→ 加入訓練資料X
→ 加入標籤y
→ 全部圖片完成
→ 回傳X、y、file_paths
→ 結束
```

**第3步：用同樣前處理預測新圖**
- 讀取 `knn_model.pkl`，前處理須與訓練時一致。
- 把 `knn04.py` 產生、位於 `output` 的 `knn_model.pkl` 放到 `data` 下，名稱仍為 `knn_model.pkl`。
- 講義要求使用小畫家寫出圖片「64x64」，存成 `hand_sample01.png`；下一行又寫「一定要用圖形大約：8x8（不然縮小後會變形）、背景為黑色、前景白色」。兩種尺寸說法保留，不自行統一。
- 小畫家「調整大小及扭曲」視窗：依據選「像素」，水平8、垂直8，勾選維持外觀比例；扭曲水平0、垂直0，下方有確定與取消。

**補充／辨誤**
- 訓練特徵是8×8、64維；64×64可作繪製或展示尺寸，但模型實際輸入仍需符合訓練特徵。講義文字與對話框未交代各尺寸的完整操作先後，不能把8與64當同一值。
- 黑底白字的極性、縮放方法、二值化閾值、正規化尺度、攤平順序都影響距離；只確保檔案副檔名一致並不足夠。
- `.pkl` 只應載入可信來源；此處是課堂自己訓練模型的流程，不是建議執行不明來源 pickle。

<a id="ai-p042"></a>

### AI-P042｜傳給 ChatGPT 的 load_images 函式：介面與資料夾迴圈

[原講義《20260907AI應用(20260915).pdf》第42頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=42)

**頁首圖片**
- 小畫家視窗標題為 **`hand_sample01.bmp`**，畫面是黑底白色直線，外觀像數字1。
- 前頁與後面的提示詞用 `hand_sample01.png`，但此截圖是 `.bmp`，副檔名差異需自行核對；不將圖片標題改成PNG。

**講義程式片段（續至44頁）**
```python
def load_images(folder_path):
    """
    讀取資料夾中的 BMP 圖片。

    資料夾格式：
    folder_path/
    ├── 0/
    ├── 1/
    ├── ...
    └── 9/

    回傳：
    X：圖片資料
    y：圖片標籤
    file_paths：圖片路徑
    """
    images = []
    labels = []
    file_paths = []

    # 依序讀取數字 0 到 9
    for label in range(10):
        # 例如：data/handwritten/train/0
        number_folder = os.path.join(folder_path, str(label))
        # 檢查資料夾是否存在
```

**逐段理解（補充）**
- 傳入 `train` 或 `test` 的根資料夾即可共用讀取函式。
- 三個串列必須保持對齊：同一位置分別是特徵、正確標籤、原檔路徑。
- `range(10)` 依數字標籤建立子資料夾；`str(label)` 把整數轉成路徑部分；`os.path.join` 組合平台對應的路徑。
- 本頁函式尚未結束，單獨此段不可視為完整可執行程式。

<a id="ai-p043"></a>

### AI-P043｜讀檔防呆、灰階化、尺寸統一與二值化

[原講義《20260907AI應用(20260915).pdf》第43頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=43)

**講義函式續段**
```python
        if not os.path.exists(number_folder):
            print(f"找不到資料夾：{number_folder}")
            continue

        # 取得資料夾內所有檔案
        filenames = os.listdir(number_folder)
        # 計算成功讀取的圖片數量
        image_count = 0
        for filename in filenames:
            # 只處理 BMP 圖片
            if not filename.lower().endswith(".bmp"):
                continue
            image_path = os.path.join(number_folder, filename)
            # 以灰階方式讀取圖片
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            # 如果讀取失敗
            if image is None:
                print(f"圖片讀取失敗：{image_path}")
                continue
            # 將圖片統一成 28 x 28
            image = cv2.resize(
                image,
                (IMAGE_WIDTH, IMAGE_HEIGHT)
            )
            # 二值化
            # 大於 127 的像素變成 255
            # 小於或等於 127 的像素變成 0
            _, image = cv2.threshold(
                image,
```
本頁在 `threshold` 引數中間換頁，剩下引數在44頁。

**理解與辨誤（補充）**
- 不存在資料夾、非BMP檔、讀圖失敗均使用 `continue` 跳過，避免後續處理空影像。
- `filename.lower()` 使 `.BMP` 等大小寫變體也能通過副檔名篩選；此段仍不會讀取PNG。
- `cv2.IMREAD_GRAYSCALE` 將讀入影像設為單通道；`cv2.resize` 的尺寸順序是寬、高，真正尺寸由 `IMAGE_WIDTH`、`IMAGE_HEIGHT` 決定。
- **原註解寫28×28，但第41頁流程和第40頁輸出是8×8／64維。** 此頁未展示常數定義，不能僅憑註解斷言此版程式實際採28×28。這是教材內部不一致，需檢查真正程式與模型特徵數。
- `_, image` 丟棄 threshold 的第一個回傳值，保留二值圖。

<a id="ai-p044"></a>

### AI-P044｜正規化、攤平特徵、回傳資料與單張圖推論提示詞

[原講義《20260907AI應用(20260915).pdf》第44頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=44)

**講義函式結尾**
```python
                127,
                255,
                cv2.THRESH_BINARY
            )
            # 將像素由 0～255 轉成 0～1
            image = image.astype("float32") / 255.0
            # 將 28 x 28 圖片攤平成 784 個數字
            image_data = image.flatten()
            # 儲存圖片資料
            images.append(image_data)
            # 儲存正確答案
            labels.append(label)
            # 儲存檔案路徑
            file_paths.append(image_path)
            image_count += 1

        print(f"數字 {label}：讀取 {image_count} 張圖片")

    # 轉成 NumPy 陣列
    X = np.array(images)
    y = np.array(labels)
    return X, y, file_paths
```

**每個動作的用途（補充）**
- `THRESH_BINARY` 以127為閾值，超過者255，其餘0；接著轉成 `float32` 並除以255.0，此流程二值化後的特徵值是0或1。
- `flatten()` 把二維像素依固定順序攤平；特徵長度由實際輸入尺寸決定，函式本身不固定為784。
- 只在成功處理後 append 三種資訊並增加數量；每完成一類就列印其成功讀圖數。
- `X`、`y` 轉為 NumPy 陣列，`file_paths` 保留路徑串列，方便追蹤錯誤圖片。
- **註解「28×28、784」與前頁8×8流程矛盾，照原文保留。** 模型的訓練與預測維度必須相同，不能把64與784維混用。

**講義給 ChatGPT 的單張圖任務**
把上述讀取與前處理程式提供給AI，請產生新程式；假設已建立好的 KNN 模型為 `./data/knn_model.pkl`，新手寫圖片檔是 `hand_sample01.png`，要求讀取此檔、做前處理、再預測。
- 黃底生成式 AI 範例檔：`手寫數字預測程式.mhtml`。
- 此提示詞要求的是新推論程式，而上面 `load_images()` 是按資料夾讀BMP的既有函式；不能直接以原函式去讀單一PNG檔。本頁未刊出AI生成的新程式全文。

<a id="ai-p045"></a>

### AI-P045｜手寫3的四階段可視化與推論結果

[原講義《20260907AI應用(20260915).pdf》第45頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=45)

**本頁四列操作／圖像，已逐圖觀看**
1. 「顯示原圖，並放大成64×64，方便觀看，並顯示視窗1」：黑底白色手寫3，筆畫平滑連續，背後編輯器檔案為 `knn05.py`。
2. 「將圖片調整成8×8，並顯示視窗2」：縮小後以大像素方塊展示，筆畫包含灰階邊緣，字形明顯粗化。
3. 「二值化，並顯示視窗3」：灰色變為純黑／純白，部分筆畫連接形狀已與原圖差異很大。
4. 「預測結果，並顯示視窗4」：疊字 **`Prediction: 3`**。不能根據二值化外觀像其他數字就改寫模型輸出；講義顯示的分類確實是3。

**第4圖局部放大後可讀內容**
- 終端：「圖片前處理完成」「輸入資料形狀：(1, 64)」。
- 圖片檔案：`./data/hand_sample01.bmp`；「預測結果：數字3」；「按任意鍵關閉圖片視窗」。
- 背後可見函式 `preprocess_image(image_path)`，局部程式如下（不是完整函式）：
```python
# 顯示並放大成 64 x 64，方便觀看
# 原圖程式實際傳入 (128, 128)，與註解不同
display_image = cv2.resize(
    image,
    (128, 128),
    interpolation=cv2.INTER_NEAREST
)
cv2.imshow("Processed Image", display_image)
cv2.waitKey(0)
# 檢查圖片是否讀取成功
if image is None:
    raise ValueError(f"圖片讀取失敗：{image_path}")
```
上面第二行指出128的註解是**整理者加註**，其餘為圖中可見程式整理。部分先前程式被視窗遮住，不補造。

**補充／辨誤**
- 顯示放大與模型特徵大小不同；畫面可以放大，但 `(1,64)` 表示模型使用一張64維資料。
- 截圖顯示尺寸為128×128，註解／左欄則寫64×64；應依實際程式為準，不把註解當執行證據。
- 此截圖局部把 `image is None` 判斷放在已呼叫 `resize` 之後；若之前沒有其他檢查，讀圖失敗可能先在resize報錯。完整函式未展示，僅指出所見順序的風險。
- 路徑使用BMP，與第44頁提示詞PNG不同。

<a id="ai-p046"></a>

### AI-P046｜手寫2縮小失真後被判為0的失敗案例

[原講義《20260907AI應用(20260915).pdf》第46頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=46)

**四個視窗依序觀察**
1. 原始黑底白字清楚是手寫2；左欄同樣說放大成64×64供觀看，顯示視窗1。
2. 縮放成8×8並顯示視窗2：字形只剩少數灰白像素方塊，上弧、斜線、底橫之間出現間斷。
3. 二值化並顯示視窗3：灰階像素被截斷，剩下黑白方塊，筆畫斷裂更加明顯。
4. 預測視窗4清楚寫 **`Prediction: 0`**，與原始手寫2不符。

**本頁要學的事（補充）**
- 前頁3預測成功不代表所有手寫字都成功；本頁特別保留錯誤輸出0，不以「應該是2」取代結果。
- 看原圖、縮放圖、二值圖、最後標籤四個階段，有助定位錯誤是否已發生在前處理。
- 本頁背後只是部分編輯器與檔案總管，未完整展示函式；可見 `hand_sample01.bmp`、`hand_sample02.bmp` 等檔案名稱，但不能據此確定當次待測2所用完整路徑。

<a id="ai-p047"></a>

### AI-P047｜8×8失真的問題與64×64新資料集生成需求

[原講義《20260907AI應用(20260915).pdf》第47頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=47)

**講義問題診斷**
「讀取訓練資料庫圖片太小8x8，容易失真」。上一個單張圖預測範例檔為 `knn05.py`。

**修改1：重新產生與訓練資料庫**
給 ChatGPT 的需求：「請幫我產生64x64的手寫資料庫，train1000張」。要求如下目錄結構：
```text
data/
└── handwritten/
    ├── train/       # 訓練資料
    │   ├── 0/      # 數字0
    │   ├── 1/      # 數字1
    │   ├── 2/
    │   ├── ...
    │   └── 9/
    └── test/        # 測試資料
        ├── 0/
        ├── 1/
        ├── 2/
        ├── ...
        └── 9/
```
- 生成式 AI 範例檔：`手寫資料庫生成.mhtml`。
- 資料集壓縮檔：`handwritten_64x64_dataset.zip`。
- 講義指示將產生的資料庫複製並重新命名為 **`handwritten_new`**。

**補充／保留未決事項**
- 提示詞只明確指定train1000張，沒有說每類1000或總數1000，也沒有指定test張數；後續截圖才呈現實際訓練／測試規模。
- 此頁未提供資料生成方法、字體／手寫來源、隨機變換或去重方法，因此不能宣稱是真人手寫資料、MNIST放大版或某種特定合成算法。
- 提高尺寸與換資料庫是新的實驗，需重新訓練並匹配新模型，不能只把8×8模型拿去接更長向量。

<a id="ai-p048"></a>

### AI-P048｜新資料集實際目錄與數字2測試圖片

[原講義《20260907AI應用(20260915).pdf》第48頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=48)

**第一張檔案總管**
- 路徑：`D:\backup\myExam\machineLearning\data\handwritten_new`。
- 紅框標出 `data > handwritten_new`；裡面確有 `test` 與 `train` 資料夾。這是第47頁改名後的實際存放位置。

**第二張檔案總管**
- 進入 `data\handwritten_new\test\2`，底部狀態列顯示「20個項目」。
- 20張黑底白字的數字2，檔名依序為 `2_0001.bmp`、`2_0002.bmp`、`2_0003.bmp`、`2_0004.bmp`、`2_0005.bmp`、`2_0006.bmp`、`2_0007.bmp`、`2_0008.bmp`、`2_0009.bmp`、`2_0010.bmp`、`2_0011.bmp`、`2_0012.bmp`、`2_0013.bmp`、`2_0014.bmp`、`2_0015.bmp`、`2_0016.bmp`、`2_0017.bmp`、`2_0018.bmp`、`2_0019.bmp`、`2_0020.bmp`。
- 縮圖可見大小、粗細、傾斜和字形不完全相同；例如第9張明顯比許多其他樣本細。這是圖面可觀察到的多樣性，不等於已知具體生成演算法。
- **補充**：此頁只直接證明數字2測試夾有20張，不單憑這張圖推定所有類別都同數量；第50頁報告才列出每類support皆20。

<a id="ai-p049"></a>

### AI-P049｜建立 knn06／knn07，修改訓練來源與64×64尺寸

[原講義《20260907AI應用(20260915).pdf》第49頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=49)

**上方資料夾圖**
- 路徑為 `data\handwritten_new\train\3`，底部顯示「100個項目」。
- 所見是黑底白色數字3，多種粗細、大小及傾斜；完整可讀的前段檔名由 `3_0001.bmp` 連續到 `3_0048.bmp`，下方下一排只有部分縮圖，不臆造被截斷檔名。
- 因此本頁可確認數字3的訓練夾有100項，不能把47頁「train1000張」理解成已證實每一類都有1000張。

**講義操作**
1. 將 `knn04.py` 複製並更名為 `knn06.py`：新資料集的訓練／測試程式。
2. 將 `knn05.py` 複製並更名為 `knn07.py`：新模型的單張圖預測程式。
3. 更改訓練資料與圖片大小。下圖紅框：
```python
TRAIN_FOLDER = "./data/handwritten_new/train"
TEST_FOLDER = "./data/handwritten_new/test"
# 所有圖片都統一成 8 x 8
IMAGE_WIDTH = 64
IMAGE_HEIGHT = 64
```
上述註解「8×8」是圖中原文，實際常數已改64，註解未同步更新。

**下圖其餘完整可見匯入與結構**
```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
```
程式下方接「讀取圖片資料」及 `def load_images(folder_path):`；上方更早的匯入被頁面捲動遮去，不能把此段當成完整匯入清單。

**補充**：匯入混淆矩陣工具不代表本頁已顯示混淆矩陣結果。修改實際常數後要用新資料重新 `fit`，並讓推論端採同樣尺寸；檔案複製有助保留舊實驗以比較，而非直接覆蓋。

<a id="ai-p050"></a>

### AI-P050｜匯出新模型與64×64新資料集分類報告

[原講義《20260907AI應用(20260915).pdf》第50頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=50)

**模型保存截圖**
`knn06.py` 在 `main()` 訓練完成後列印「KNN 模型訓練完成」，接著：
```python
# 將模型儲存成檔案
import joblib
model_filename = "./data/knn_model_new1.pkl"
joblib.dump(model, model_filename)
```
後續進行測試，畫面可見：
```python
print()
print("=" * 50)
print("開始測試")
print("=" * 50)
```
- 新檔名是 **`knn_model_new1.pkl`**，有數字1；不要誤寫成 `knn_model_new.pkl`。
- 本版直接寫入 `data`，與舊版先在 `output` 再搬去 `data` 的流程不同。

**第二張圖的逐檔錯誤範例**
`檔案：9_0020.bmp　實際：9　預測：0　結果：錯誤`。

**分類報告（局部放大逐列確認）**
| 類別 | precision | recall | f1-score | support |
|---|---:|---:|---:|---:|
| 0 | 0.49 | 0.85 | 0.62 | 20 |
| 1 | 0.55 | 0.90 | 0.68 | 20 |
| 2 | 0.82 | 0.70 | 0.76 | 20 |
| 3 | 0.53 | 0.50 | 0.51 | 20 |
| 4 | 0.82 | 0.90 | 0.86 | 20 |
| 5 | 0.60 | 0.60 | 0.60 | 20 |
| 6 | 0.44 | 0.35 | 0.39 | 20 |
| 7 | 0.82 | 0.70 | 0.76 | 20 |
| 8 | 0.60 | 0.30 | 0.40 | 20 |
| 9 | 0.91 | 0.50 | 0.65 | 20 |
| accuracy | — | — | 0.63 | 200 |
| macro avg | 0.66 | 0.63 | 0.62 | 200 |
| weighted avg | 0.66 | 0.63 | 0.62 | 200 |

黃底範例：`knn06.py`。

**結果解讀（補充）**
- 本次報告accuracy是0.63，並非改善到接近全對；更高影像尺寸不保證更好準確率。
- 數字8 recall=0.30、6 recall=0.35，顯示弱勢類別；數字9 precision高0.91，但recall僅0.50，不能只看單一指標。
- 十類support都20，所以這份報告的macro與weighted顯示值一致。資料集與前處理條件已變，不可將新舊準確率差全歸因於尺寸。
- 沒有訓練集全部讀取數、資料來源細節或完整模型超參數，不能把此結果冒稱為所有64×64 KNN的固定表現。

<a id="ai-p051"></a>

### AI-P051｜knn07 載入新模型：路徑設定與64×64手寫圖前兩階段

[原講義《20260907AI應用(20260915).pdf》第51頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=51)

**講義操作與資料夾圖**
- 文字：「開啟knn07.py，修改模組來源、測試檔與大小參數」。此處「模組來源」在圖中實際是模型檔案路徑。
- 檔案總管開在 `D:\backup\myExam\machineLearning\data`。紅框圈出 `hand_sample01.bmp`、`hand_sample02.bmp`，縮圖分別是3與2；另圈出 `knn_model_new1.pkl`。
- 同一資料夾還可見舊 `handwritten`、解壓資料夾 `handwritten_64x64_dataset`、`handwritten_new`、壓縮檔 `handwritten_64x64_dataset.zip`、舊 `knn_model.pkl`、`knn_model2.pkl`，以及房價範例的CSV／模型檔。要選對本次新模型，不是任取一個 `.pkl`。

**下方第一張編輯器截圖的可見程式（局部放大核對）**
```python
import os
import cv2
import joblib
import numpy as np

# 基本設定
IMAGE_WIDTH = 64
IMAGE_HEIGHT = 64
MODEL_PATH = "./data/knn_model_new1.pkl"
IMAGE_PATH = "./data/hand_sample01.bmp"

# 圖片前處理函式
# 下方接 def preprocess_image(image_path):
# docstring：讀取單張手寫數字圖片並進行前處理。
```
最後兩行是為避免把未刊完整函式當成完整程式而加的說明式註解；圖中實際可見函式名稱和該docstring。

**本頁顯示的手寫測試只有前兩階段**
1. 左欄：「顯示原圖並放大成64×64，方便觀看，並顯示視窗1」。右圖顯示黑底白色數字 **6**。
2. 左欄：「將圖片調整成64x64，並顯示視窗2」。右圖仍是黑底白色6，保留連續曲線與內部黑色孔洞，不像8×8示例變成稀少的大方塊。

**補充／來源差異**
- 頁首檔案總管 `hand_sample01.bmp` 縮圖是3，但下面相同路徑的執行視窗顯示6；可能拍攝於不同操作時點，講義未交代，不擅自改寫成一致。
- 本頁沒有二值化視窗3或預測視窗4，**未展示6的最終預測標籤**；不得將看見6解讀成模型已判對6。此段筆記範圍到第51頁為止，不引用下一頁來補結果。

<!-- END_AI_P027_P051 -->


## AI 應用講義逐頁知識筆記（第 52–76 頁）

> 來源：`20260907AI應用(20260915).pdf`。以下以講義頁碼定位，逐頁核對文字層及頁面圖片。程式／操作是講義記錄，未代為執行圖片中的指令、登入或對外操作；「補充辨析」與講義原文分開。截圖中未完整呈現的程式不冒充完整原始碼，無法辨識的小字明示保留。

<a id="ai-p052"></a>

### AI-P052｜未裁切前景的手寫數字辨識：6 的誤判與 2 的前處理

[原講義《20260907AI應用(20260915).pdf》第52頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=52)

**講義與圖中操作**

本頁接續 `knn07.py` 的單張圖片辨識示範，上半部是數字 6 的後續處理，下半部改測數字 2。VS Code 程式可見匯入 `os`、`cv2`、`joblib`、`numpy as np`，設定 `IMAGE_WIDTH = 64`、`IMAGE_HEIGHT = 64`；載入模型路徑 `./data/knn_model_new1.pkl`。

1. **6：二值化，顯示視窗 3。** 圖片為黑色背景、白色手寫 6；上方斜筆與下方封閉圈皆保留。
2. **6：預測，顯示視窗 4。** 視窗放大呈現同一個 6，但左上角標示 `Prediction: 4`，是實際誤判示例，不能把圖中的人工可辨數字 6 說成模型預測 6。此例使用 `IMAGE_PATH = "./data/hand_sample01.bmp"`。
3. **改成測試數字 2。** 程式中紅框標出 `IMAGE_PATH = "./data/hand_sample02.bmp"`，說明透過換測試檔重跑辨識。第一個視窗先呈現黑底白字的原圖；左側講義稱「顯示原圖，並放大成 64 x 64，方便觀看，並顯示視窗 1」。
4. **2：調整大小。** 左側註解是「將圖片調整成 64x64，並顯示視窗 2」；第二張 2 的視窗用來觀察縮放後字形。本頁尚未顯示 2 的最終預測，要接下一頁。

**學習重點／補充辨析**

- 視窗編號是除錯階段，不是數字的分類標籤。應依原圖、縮放圖、二值圖、預測圖逐一比較。
- 單純把整張圖縮放到固定尺寸，仍保留字周圍背景及位置差異；本例 6 被判為 4，為後文改成前景裁切提供問題背景。
- 講義顯示用尺寸的文字與後續程式中實際放大的 `128 × 128` 不完全一致；本頁按原圖說明記錄，不將顯示尺寸混同為模型輸入尺寸。

<a id="ai-p053"></a>

### AI-P053｜2、4 的辨識結果與階段性影像檢查

[原講義《20260907AI應用(20260915).pdf》第53頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=53)

**講義與圖中操作**

- 上方：承接前頁 `hand_sample02.bmp`，二值化後顯示視窗 3。白色筆畫／黑色背景清楚，數字 2 的上方弧線、斜向筆畫及底部橫線保留。
- 中段：預測後顯示視窗 4，左上角 `Prediction: 2`。這次人工可辨字形與模型輸出一致。VS Code 終端機以紅框標出辨識結果「數字 2」，截圖中也有先前測試的輸出紀錄，不能把所有歷史輸出當成本次輸出。
- 下方：另一個手寫 4 的預測視窗標示 `Prediction: 4`，字形較窄、直筆較長。這張截圖只展示結果，未在左欄提供完整的前處理步驟標籤。
- 程式背景可見 `preprocess_image(image_path)`、圖片存在檢查 `if not os.path.exists(image_path)`、`FileNotFoundError`，以及 `cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)`：前處理從讀取單張灰階圖開始。

**補充辨析與可讀限制**

- 此頁結果為 2→2、4→4，僅是個別測試成功，不代表所有數字都已達相同辨識率。
- 背景函式說明還出現「784 個數字／28 × 28」等舊文字，與這一版設定的 64×64 並不一致；尺寸及特徵數要以實際程式設定為準，後面第 66–68 頁可直接核對這個註解殘留問題。
- 終端機裡其他執行器路徑、歷史命令與細小訊息未逐字抄錄；本頁能明確核對的是兩個預測視窗標籤及紅框中的數字 2。

<a id="ai-p054"></a>

### AI-P054｜5 被判為 3：背景與位置特徵造成的限制

[原講義《20260907AI應用(20260915).pdf》第54頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=54)

**講義原文與截圖**

- 範例檔名：`knn07.py`。
- 截圖紅框標出測試圖片 `./data/hand_sample04.bmp`。前景清楚是手寫 5，但結果視窗左上角顯示 `Prediction: 3`；終端機下方紅框也指向預測「數字 3」。
- 講義列出的問題原文：「使用的特徵為相對位置，因此背景的資訊容易讓訓練產生錯誤資訊。」

**知識拆解／補充辨析**

此版直接以固定影像格點中的像素值當特徵。雖然同樣是數字，若文字在畫布上的位置、大小或留白不同，對應格點的值也會不同。KNN 比較特徵距離時，這些差異會影響最近鄰關係；講義以 5→3 的誤判指出只做整圖縮放並不夠。

下一步改良的方向不是直接更換分類器，而是先改善特徵輸入：找出白色前景的邊界，裁掉外圍背景，再調整成一致大小。這可減少留白與平移造成的差異，但不代表可以完全消除筆畫形狀、傾斜及噪聲影響。

---

<a id="ai-p055"></a>

### AI-P055｜修改 2：先裁切前景，再統一成 64×64

[原講義《20260907AI應用(20260915).pdf》第55頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=55)

**講義問題與解法**

講義再次指出背景資訊會干擾位置相關的像素特徵，解決方式是「將前景字找到邊界並截取出來，再放大成 64×64」。本次分別改寫訓練端與預測端，而不是只改預測圖片。

**檔案與設定**

1. 複製 `knn04.py`，更名為 `knn08.py`（重新載入訓練／測試資料、訓練與保存模型）。
2. 複製 `knn05.py`，更名為 `knn09.py`（單張測試圖辨識）。
3. `knn08.py` 截圖紅框設定：

```python
TRAIN_FOLDER = "./data/handwritten_new/train"
TEST_FOLDER = "./data/handwritten_new/test"
IMAGE_WIDTH = 64
IMAGE_HEIGHT = 64
```

畫面亦可見 `from sklearn.metrics import ConfusionMatrixDisplay`，後面將以混淆矩陣檢視分類表現。

**利用 GitHub Copilot 修改程式的原始提示**

講義要求先寫註解，讓 Copilot 產生相應程式：

```python
#將前景切割出來，自動產生程式
#再將大小調整回 IMAGE_WIDTH、IMAGE_HEIGHT
#show image
```

提示由三個具體子工作組成：定位並裁切前景、恢復模型要求的尺寸、顯示處理後圖像。下一頁展示生成後的實際程式。

**補充辨析**

- 圖中「所有圖片都統一成 28 x 28」是未同步修改的舊註解；緊接的變數值確實都是 64，筆記不把舊註解當作本版輸入尺寸。
- 訓練及推論必須使用一致前處理，否則即使輸入維度相同，特徵分布仍會不一致。

<a id="ai-p056"></a>

### AI-P056｜前景框裁切程式、KNN 訓練與模型另存

[原講義《20260907AI應用(20260915).pdf》第56頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=56)

**圖 1：在 `load_images(folder_path)` 補上前處理**

截圖位於二值化之後，紅框中的有效操作如下（省略不影響操作的裝飾性註解）：

```python
x, y, w, h = cv2.boundingRect(image)
image = image[y:y+h, x:x+w]
image = cv2.resize(image, (IMAGE_WIDTH, IMAGE_HEIGHT))
cv2.imshow("image", image)
cv2.waitKey(0)
```

- `boundingRect` 對這種黑底白字的單通道影像找非零前景外接矩形；`x, y` 是左上角，`w, h` 是寬高。
- NumPy 切片先列（y）、後欄（x）；只留下矩形中的內容。
- 裁切後重新縮放到 64×64，使每張圖最後都有相同特徵數。
- `imshow` 用來實際看到裁切結果，`waitKey(0)` 暫停直到按鍵，方便逐張檢查。

**圖 2：訓練與輸出模型**

```python
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
import joblib
model_filename = "./data/knn_model_new2.pkl"
joblib.dump(model, model_filename)
```

截圖註解說 `n_neighbors=3` 表示找距離最近的 3 張圖片進行投票；訓練前後印出「開始訓練 KNN 模型」「KNN 模型訓練完成」。模型輸出名稱改為 `knn_model_new2.pkl`，以區分前一版。

**圖 3：先少量測試，再全量訓練**

講義寫「測試時先跑幾張圖，比較切割前與切割後差異」。截圖在裁切前額外插入 `cv2.imshow("image", image)`、`cv2.waitKey(0)`，並保留裁切後同樣的顯示段；因此每張圖有前後兩次停頓。本頁看到的是畫布中較小的白色 0，下一頁展示裁切後放大的 0。

**補充辨析**

此作法直接將外接框拉伸成正方形，沒有展示等比例補邊；字的寬高比例可能改變。若畫布全黑沒有前景，外接框可能為空，應另外檢查再縮放；講義此片段未展示該防護。

<a id="ai-p057"></a>

### AI-P057｜目視驗證：0 的裁切前後對照

[原講義《20260907AI應用(20260915).pdf》第57頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=57)

**本頁三張圖的閱讀順序**

1. 上圖承接上一頁的小型 0：黑色周邊留白被移除，白色 0 放大到接近整個顯示區；其孔洞仍維持黑色。程式紅框上段是「切割前的圖片顯示」加 `waitKey(0)`，下段是裁切、縮放後的「show image」。
2. 中圖是另一張 0 的裁切前影像。數字相對畫布較小，位於黑底中的局部範圍，周圍還有大量留白。
3. 下圖是同類流程裁切後的 0。外接框填滿目標區，傾斜方向與筆畫差異仍可觀察，但外圍留白明顯減少。

**圖中可核對的處理順序**

`cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)` → 顯示裁切前 → `cv2.boundingRect(image)` → `image[y:y+h, x:x+w]` → `cv2.resize(..., (IMAGE_WIDTH, IMAGE_HEIGHT))` → 顯示裁切後。

這一頁展示的是前處理檢驗，並非分類結果頁；圖中沒有足以支持某一辨識率的新數據。白色字放大不等於筆畫變得更正確，只說明外接框與尺寸正規化有執行。

**補充辨析**

裁切會保留字內部的背景（例如 0 的孔洞），不會把整個黑色區域通通刪除。它只移除前景外接框之外的留白，因此內部孔洞仍是可用的辨識特徵。

---

<a id="ai-p058"></a>

### AI-P058｜關閉逐張顯示、完整執行訓練與測試

[原講義《20260907AI應用(20260915).pdf》第58頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=58)

**講義步驟**

「再註解顯示程式，並更改模型輸出名稱，並執行」。兩張截圖分別示範取消互動式影像暫停，以及保存新模型後進行測試。

1. `load_images` 仍保留二值化、前景框裁切與 `cv2.resize`；只把裁切前及裁切後的兩組顯示程式註解掉：

   ```python
   # cv2.imshow("image", image)
   # cv2.waitKey(0)
   ```

   這樣批次載入資料不再逐張等待按鍵。移除的是除錯顯示，不是裁切功能。
2. 訓練完成後以 `model_filename = "./data/knn_model_new2.pkl"` 指定輸出，使用 `joblib.dump(model, model_filename)` 保存。
3. 顯示「開始測試」，呼叫 `y_pred = model.predict(X_test)` 對測試集產生預測。
4. 頁末「訓練與測試結果：」是下一頁結果的引導；本頁本身沒有分類報告的數值。

**補充辨析**

新模型檔應與新前處理版本配對保存。只換檔名不會自動改模型內容，必須確實重新執行資料處理及 `fit`；本講義流程是在前景裁切改完後重新訓練，再保存 `new2`。

<a id="ai-p059"></a>

### AI-P059｜裁切後模型的分類報告與輸出檔確認

[原講義《20260907AI應用(20260915).pdf》第59頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=59)

**圖 1：`knn08.py` 分類報告（已局部放大核對）**

| 數字類別 | precision | recall | f1-score | support |
|---|---:|---:|---:|---:|
| 0 | 1.00 | 1.00 | 1.00 | 20 |
| 1 | 0.95 | 1.00 | 0.98 | 20 |
| 2 | 1.00 | 1.00 | 1.00 | 20 |
| 3 | 1.00 | 1.00 | 1.00 | 20 |
| 4 | 1.00 | 1.00 | 1.00 | 20 |
| 5 | 1.00 | 0.95 | 0.97 | 20 |
| 6 | 0.95 | 0.95 | 0.95 | 20 |
| 7 | 1.00 | 0.95 | 0.97 | 20 |
| 8 | 0.95 | 1.00 | 0.98 | 20 |
| 9 | 1.00 | 1.00 | 1.00 | 20 |
| macro avg | 0.99 | 0.98 | 0.98 | 200 |
| weighted avg | 0.99 | 0.98 | 0.98 | 200 |

`accuracy` 一列顯示 **0.98，support 200**。以上完全保留截圖四捨五入後的顯示值，不自行提高小數精度。

**圖 2：模型檔產生的確認**

檔案總管位於 `data` 資料夾，紅框圈選 `knn_model_new2.pkl`。畫面也可見 `knn_model.pkl`、`knn_model_new1.pkl`、手寫圖資料夾 `handwritten`、`handwritten_64x64_dataset`、`handwritten_new`、測試 BMP 縮圖及其他線性迴歸 CSV／模型檔；核心操作是確認新模型另存，不是刪掉其他版本。本頁講義結論為「結果：明顯提高辨識率」，範例標示 `knn08.py`。

**指標解讀（補充）**

- precision：被預測為某數字的樣本中，有多少真的屬於它。
- recall：實際屬於某數字的樣本中，有多少被找回。
- f1-score：precision 與 recall 的綜合指標。
- support：該類在測試集中的真實樣本數；本例各類皆 20，總數 200。
- macro avg 對各類平均；weighted avg 依各類 support 加權。本例 support 相同，兩種平均顯示相同。
- 報告仍有 5、6、7 的 recall 低於 1.00，所以改善不等於完全不會誤判。僅憑此報告不能重建每筆誤判究竟流向哪一類；本頁沒有混淆矩陣圖，不應補造。
- 「明顯提高」是講義對該次實驗的評語，並非對任何新使用者字跡、其他資料集或今日版本的保證。

<a id="ai-p060"></a>

### AI-P060｜推論端 `knn09.py`：同步新模型、測試圖與尺寸

[原講義《20260907AI應用(20260915).pdf》第60頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=60)

**講義操作**

開啟 `knn09.py`，修改「模組來源、測試檔、大小參數、取出前景」，方法與 `knn08` 相同。這裡截圖實際指定的是模型檔路徑。

圖 1 在檔案總管中用紅框分別標出 `knn_model_new2.pkl` 和手寫測試圖 `hand_sample01.bmp`（6）、`hand_sample02.bmp`（2），強調推論要使用剛訓練好的模型，並有實際圖片可測。

圖 2 的程式設定為：

```python
import os
import cv2
import joblib
import numpy as np

IMAGE_WIDTH = 64
IMAGE_HEIGHT = 64
MODEL_PATH = "./data/knn_model_new2.pkl"
IMAGE_PATH = "./data/hand_sample01.bmp"
```

下面接著定義 `preprocess_image(image_path)`；前景裁切的具體修改在下一頁展示。

**補充辨析**

四個項目要一起核對：輸入檔存在、模型版本正確、影像大小符合訓練、裁切及二值化方法一致。只改 `MODEL_PATH` 而仍沿用未裁切的特徵，就未完成講義要求的修改。

---

<a id="ai-p061"></a>

### AI-P061｜單張圖片的裁切、像素正規化與二維特徵輸出

[原講義《20260907AI應用(20260915).pdf》第61頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=61)

**圖 1：在 `preprocess_image` 加入與訓練端相同的裁切**

二值化後加入：

```python
x, y, w, h = cv2.boundingRect(image)
image = image[y:y+h, x:x+w]
image = cv2.resize(image, (IMAGE_WIDTH, IMAGE_HEIGHT))
cv2.imshow("image", image)
cv2.waitKey(0)
processed_image = image.copy()
```

`processed_image` 保留處理後影像，用於最後顯示；下面仍會繼續變更 `image` 的資料型態與形狀，因此先複製。

**圖 2：正規化及模型輸入整理**

```python
image = image.astype("float32") / 255.0

display_image = cv2.resize(
    image,
    (128, 128),
    interpolation=cv2.INTER_NEAREST
)
cv2.imshow("Processed Image", display_image)
cv2.waitKey(0)

image_data = image.flatten()
image_data = image_data.reshape(1, -1)
return image_data, processed_image
```

- `astype("float32") / 255.0` 把像素範圍由 0～255 轉為 0～1。
- `display_image` 是額外放大成 128×128 的觀察圖，不取代原本 64×64 的模型影像；最近鄰插值方便觀察像素階梯。
- `flatten()` 把二維影像轉成一維特徵，`reshape(1, -1)` 加上樣本軸，成為模型要求的「一筆樣本、多個特徵」。
- 圖中舊註解仍寫「28×28 攤平成 784」「(784,) → (1,784)」，但這版真正使用 64×64，應是 4096 個特徵；後面第 68 頁文字程式已改為 4096。本頁紅框上方的「顯示並放大成64×64」也與下方實際 `(128,128)` 不一致。

**圖 3：開始手寫圖測試**

講義標題「手寫文字測試結果如下」，先測 `./data/hand_sample01.bmp`。紅框標示圖片路徑；視窗 1 是原圖黑底白字 6 的放大觀察，模型則是 `knn_model_new2.pkl`。接著會逐步觀察縮放、二值化及裁切後結果。

<a id="ai-p062"></a>

### AI-P062｜數字 6 的三個中間處理階段

[原講義《20260907AI應用(20260915).pdf》第62頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=62)

**按講義左欄逐步核對**

1. **視窗 2：將圖片調整成 64×64。** 畫面仍呈現相同手寫 6，處理的是整張原圖；文字位置及留白還未用前景框統一。
2. **視窗 3：二值化。** 白色筆畫與黑色背景分離，移除中間灰階。本張截圖顯示視窗較小，不應以螢幕上視窗大小判定模型輸入解析度改變。
3. **視窗 4：切割並大小正規化到 64×64。** 字周圍多餘黑底被裁去，6 的筆畫擴張到接近影像邊界，字形比前兩階段更充滿框。

各張背景程式都顯示 `IMAGE_WIDTH = 64`、`IMAGE_HEIGHT = 64`、`MODEL_PATH = "./data/knn_model_new2.pkl"` 及 `IMAGE_PATH = "./data/hand_sample01.bmp"`，表示是同一測試樣本在不同階段，而不是不同模型的三張結果。

**補充辨析**

本頁「大小正規化」是空間尺寸的處理；第 61 頁除以 255 的「像素正規化」是數值尺度的處理。兩者用途不同，不能只做其中一項就宣稱已完成所有前處理。

<a id="ai-p063"></a>

### AI-P063｜新模型正確判出 6，接續測試 2

[原講義《20260907AI應用(20260915).pdf》第63頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=63)

**上圖：6 的預測結果（視窗 5）**

- 結果視窗顯示已裁切放大的 6，左上角 `Prediction: 6`。
- 終端機紅框顯示預測「數字 6」，並可見模型輸入形狀 `(1, 4096)`。
- 這與第 52 頁同名測試圖在舊流程下出現 `Prediction: 4` 形成具體對照：新流程加入前景裁切並用配對模型後，此例可正確判為 6。這是單例比較，不等於已控制所有實驗變因的普遍保證。

**中圖：改測 2，視窗 1**

將 `IMAGE_PATH` 改為 `"./data/hand_sample02.bmp"`（紅框）。第一個觀察視窗顯示原始黑底白字 2；模型維持 `knn_model_new2.pkl`，寬高維持 64。

**下圖：2 的視窗 2**

將圖片調整成 64×64，保留上弧、斜向主筆及底橫。此頁只展示 2 的原圖及整圖縮放，二值化、裁切與最終預測在下一頁。

**流程記憶**

這個修改版教學的五階段圖示為：原圖觀察 → 統一尺寸 → 二值化 → 裁切前景後再統一尺寸 → 顯示預測。其目的不只是「有答案」，而是能追查模型在各階段究竟收到什麼圖。

---

<a id="ai-p064"></a>

### AI-P064｜數字 2：二值化、前景裁切及正確分類

[原講義《20260907AI應用(20260915).pdf》第64頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=64)

**本頁三張流程圖**

1. **視窗 3／二值化：** 2 已轉為黑底白字二值圖。背景程式仍是 `knn09.py`，使用 `hand_sample02.bmp` 與 `knn_model_new2.pkl`。
2. **視窗 4／切割並大小正規化到 64×64：** 擷取前景外接框後，再縮放成固定大小，白色 2 擴展到影像邊緣；其上方弧形與底部橫畫完整保留。
3. **視窗 5／預測：** 左上角清楚顯示 `Prediction: 2`。終端機底部紅框標示本次預測「數字 2」，並保留前幾次執行的紀錄。

**學習連結**

第 53 頁未裁切版本也能正確辨識此張 2；本次結果說明在改善其他錯例時，這個樣本仍維持正確，不是所有樣本都必須從錯誤變正確才能證明流程有用。至此，第 63–64 頁構成 2 的完整五階段觀察。

<a id="ai-p065"></a>

### AI-P065｜追加 4、5 測試，完成 `knn09.py` 示範

[原講義《20260907AI應用(20260915).pdf》第65頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=65)

**上圖：手寫 4**

- 紅框為 `IMAGE_PATH = "./data/hand_sample03.bmp"`。
- 模型維持 `./data/knn_model_new2.pkl`，寬高皆 64。
- 視窗顯示經裁切放大的 4，左上角 `Prediction: 4`；字形內部三角狀空隙、橫畫與長直畫皆可見。

**下圖：手寫 5**

- 紅框為 `IMAGE_PATH = "./data/hand_sample04.bmp"`。
- 視窗顯示 `Prediction: 5`；這個黑底白字 5 經裁切後佔滿畫面。
- 第 54 頁同名檔在 `knn07.py` 示範中被判為 3，現在新模型及新前處理配合後顯示 5，呈現改良的另一個具體例子。

頁末黃色標記為「範例：knn09.py」，標示單張測試程式段落告一段落。這兩張只呈現最終結果，不應另編未展示的每一步畫面。

**截至本頁的角色分工（補充整理）**

- `knn08.py`：讀入分類資料夾、二值化及前景裁切、統一尺寸、訓練 KNN、測試、保存 `knn_model_new2.pkl`。
- `knn09.py`：載入保存好的模型，對單張 `hand_sample*.bmp` 做相同前處理、預測、顯示。
- 這種「離線訓練 → 保存模型 → 獨立推論」的切分，正是下一段 Django 網頁整合的基礎。

<a id="ai-p066"></a>

### AI-P066｜把已訓練 KNN 模型接到 Django：提供生成式 AI 的需求

[原講義《20260907AI應用(20260915).pdf》第66頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=66)

**本頁主題**：「利用 knn 的手寫數字辨識系統 by Django Web」。

**講義提供給 ChatGPT 的提示詞（保留需求及名稱）**

> 我利用knn演算法，產生出辨識手寫數字的模型，模型名稱為「knn_model_new2.pkl」，其中前景為白色、背景為黑色。
> 輸入圖片前的前處理程式如下，我想建立一個django網站使用初學者的程式寫法，專案名為knnweb，app名為myapp，讓使用者可以用滑鼠寫數字，利用模型預測0-9的數字。

接著要求把既有 `preprocess_image` 程式一起貼給 AI。提示的重要限制有：沿用既有模型、不改黑底白字的輸入慣例、Django 專案／app 名稱固定、程式寫法適合初學者、輸入改由網頁滑鼠書寫、輸出是 0–9 分類。

**本頁貼入程式的前半段**

```python
def preprocess_image(image_path):
    """
    讀取單張手寫數字圖片並進行前處理。

    處理流程：
    1. 灰階讀取
    2. 調整成 28 x 28
    3. 二值化
    4. 像素轉成 0～1
    5. 攤平成 784 個數字

    回傳：
    image_data：提供模型預測的資料
    processed_image：處理完成的 28 x 28 圖片
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"找不到圖片：{image_path}")

    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
```

頁尾開始 `display_image = cv2.resize(`，參數接到下一頁，不是語法完整的獨立頁面程式。

**補充辨析：提示詞也必須做一致性檢查**

- docstring 原文仍寫 28×28、784，與這版 64×64、4096 的實際流程不符；此處為忠實記錄原文，不能拿錯誤註解覆蓋模型規格。
- 原函式接受磁碟圖片路徑；網頁版將接收 Canvas 的 Base64 圖片，後端需要另做解碼與影像轉換。這正是把現有前處理一併提供給 AI 的理由：讓輸入方式改變時仍保留同一特徵定義。
- 桌面程式的 OpenCV 視窗與等待按鍵只是除錯用途，不適合原封不動放到伺服器處理每個網路請求。後文網頁版應改用 HTTP 回應呈現結果。

---

<a id="ai-p067"></a>

### AI-P067｜提供給 AI 的前處理原碼：顯示、讀取檢查、縮放與二值化

[原講義《20260907AI應用(20260915).pdf》第67頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=67)

**承接第 66 頁的函式內容（程式續段）**

```python
    display_image = cv2.resize(
        image,
        (128, 128),
        interpolation=cv2.INTER_NEAREST
    )
    cv2.imshow("Processed Image1", display_image)
    cv2.waitKey(0)

    # 檢查圖片是否讀取成功
    if image is None:
        raise ValueError(f"圖片讀取失敗：{image_path}")

    # 將圖片調整成 64 x 64
    image = cv2.resize(image, (IMAGE_WIDTH, IMAGE_HEIGHT))

    # 講義註解寫放大成64x64；實際顯示參數為128x128
    display_image = cv2.resize(
        image,
        (128, 128),
        interpolation=cv2.INTER_NEAREST
    )
    cv2.imshow("Processed Image2", display_image)
    cv2.waitKey(0)

    _, image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
```

頁末註解「將前景切割出來」，實作接續第 68 頁。

**逐段知識**

- 第一個 `display_image` 觀察剛讀入的圖片；第二個則觀察已用 `IMAGE_WIDTH`、`IMAGE_HEIGHT` 統一大小的圖片。兩者都用 128×128 顯示。
- `cv2.imread` 可能讀取失敗並得到 `None`；講義以 `ValueError` 提供帶有圖片路徑的錯誤訊息。
- 二值化門檻 127：大於 127 的像素變成 255，小於或等於 127 的變成 0，使用 `cv2.THRESH_BINARY`，不是反相二值化。
- `_` 接收但不使用 threshold 回傳的門檻值，`image` 接收二值影像。

**補充辨析：本頁可直接發現的錯誤順序**

原文把 `if image is None` 放在第一次 `cv2.resize(image, ...)` 之後。如果讀檔失敗，可能先在 resize 發生 OpenCV 錯誤，尚未走到自訂的 `ValueError`。實作時應先確認讀取成功，再做縮放與顯示；這是筆記的修正建議，不是講義已經採用的順序。

<a id="ai-p068"></a>

### AI-P068｜提供給 AI 的前處理原碼：裁切、0～1 正規化與 4096 維

[原講義《20260907AI應用(20260915).pdf》第68頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=68)

**函式後半段（依講義有效程式完整記錄）**

```python
    x, y, w, h = cv2.boundingRect(image)
    image = image[y:y+h, x:x+w]
    image = cv2.resize(image, (IMAGE_WIDTH, IMAGE_HEIGHT))

    cv2.imshow("Processed Image3", image)
    cv2.waitKey(0)

    processed_image = image.copy()
    image = image.astype("float32") / 255.0

    display_image = cv2.resize(
        image,
        (128, 128),
        interpolation=cv2.INTER_NEAREST
    )
    cv2.imshow("Processed Image4", display_image)
    cv2.waitKey(0)

    image_data = image.flatten()
    image_data = image_data.reshape(1, -1)
    return image_data, processed_image
```

**資料流與回傳值**

1. 對二值圖取得前景框，切下白色筆畫的範圍，再還原為 `IMAGE_WIDTH × IMAGE_HEIGHT`。
2. 顯示 `Processed Image3`，供人工檢查裁切後圖片。
3. `processed_image = image.copy()` 留下顯示用影像。
4. 像素轉成 `float32` 並除以 255.0，轉成 0～1 尺度。
5. 放大顯示 `Processed Image4`，確認正規化後內容仍正確。
6. 此頁註解明確寫 **64×64 攤平成 4096 個數字**，以及 `(4096,) → (1, 4096)`；與第 66 頁仍寫 784 的 docstring 相比，此處已反映目前模型輸入。
7. 回傳兩個值：`image_data` 是模型可接受的二維樣本矩陣；`processed_image` 是最後呈現用的二維圖。

**補充辨析**

- 64×64 是特徵影像，128×128 是顯示影像；`flatten` 操作的是 `image`，不是 `display_image`。
- 先二值化、後 `cv2.resize` 時，縮放插值可能再產生中間灰階。因此「二值化過」不保證最後每個值只剩 0 或 1；講義實際做的是把最終像素縮放到 0～1。
- 全黑空白圖應在裁切後 resize 之前防呆；此段沒有檢查 `w == 0` 或 `h == 0`。
- `Processed Image1`～`4` 是這段貼給 AI 的實際視窗名稱，不必硬套前面圖表所稱五個教學階段的編號。

<a id="ai-p069"></a>

### AI-P069｜網頁化第一次修改：依賴套件、保存對話與模型位置

[原講義《20260907AI應用(20260915).pdf》第69頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=69)

**上方截圖：把現有程式提供給 AI**

VS Code 選中 `knn09.py`，紅框圈住 `def preprocess_image(image_path):`，明確指出要複製的既有函式來源。畫面中 `IMAGE_PATH` 為 `./data/hand_sample04.bmp`，並可見灰階讀取、檔案存在檢查及 `Processed Image1` 顯示片段。

**講義附帶參考名稱（按原文保存）**

- `生成式ai 範例：Django 手寫數字辨識網站設置／Django 手寫數字辨識網站設置.mhtml`
- `生成式ai 範例：第一次修改程式`

這些是講義標示的範例／對話保存檔名稱；本頁未呈現可逐字抄錄的外部網址，不補造下載 URL，也未聲稱已開啟該 mhtml。

**操作步驟**

講義列出安裝指令（僅記錄，未執行）：

```bash
pip install django opencv-python numpy scikit-learn joblib pillow
```

第一步：將模型檔 `knn_model_new2.pkl` 放在與 `manage.py` 同一層。

**套件用途（補充解釋）**

- `django`：網站、URL 路由、模板與 HTTP／JSON 回應。
- `opencv-python`：灰階、二值化、前景框及尺寸處理。
- `numpy`：影像陣列、像素型態與特徵形狀。
- `scikit-learn`：既有 KNN 模型所使用的分類器實作；載入序列化模型也需相容環境。
- `joblib`：讀寫已訓練模型。
- `pillow`：將收到的圖片資料開啟並轉為灰階影像。

講義這一頁沒有展示套件安裝成功輸出，也沒有提供版本鎖定檔，不能據此宣稱任意今日版本組合必定相容。使用模型檔時亦應只載入可信來源的 pickle/joblib 檔。

---

<a id="ai-p070"></a>

### AI-P070｜Django 專案層與 app 層路由

[原講義《20260907AI應用(20260915).pdf》第70頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=70)

**圖 1：目錄及模型位置**

VS Code 檔案樹確認 `knn_model_new2.pkl` 與 `manage.py` 同層；此外可見 `knnweb` 專案套件、`myapp` 應用、`templates/myapp`、`index.html`、備份 `index_old.html` 及 `db.sqlite3`。上方編輯區已顯示 app 的兩條 URL，後面依步驟再特別圈出。

**步驟 2：修改 `knnweb/urls.py`**

```python
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
```

空字串路徑把網站根目錄交給 `myapp.urls`；`admin/` 保留 Django 管理站台。圖中的紅框標記要新增／檢查的路由區。

**步驟 3：建立 `myapp/urls.py`**

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('predict/', views.predict_digit, name='predict_digit'),
]
```

- 根路徑呼叫 `views.index`：呈現書寫頁面。
- `predict/` 呼叫 `views.predict_digit`：處理辨識請求。
- `name` 是 URL 名稱，與 Python 函式及網址字串用途不同；此頁保留尾端斜線 `predict/`。

**步驟 4：撰寫 `myapp/views.py`**，實際截圖在下一頁。

**補充辨析**

本頁展示的是目錄與路由，不包括 Django 專案建立、app 註冊或模板設定的全部指令；不把那些未展示步驟冒充原文。建立網站時仍需確認 `myapp` 已正確設定、模板可被找到。

<a id="ai-p071"></a>

### AI-P071｜`views.py`：載入模型、回傳首頁及解碼 Canvas

[原講義《20260907AI應用(20260915).pdf》第71頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=71)

**本頁截圖可見的程式（已局部放大）**

```python
from django.shortcuts import render
from django.http import JsonResponse

import os
import base64
import joblib
import cv2
import numpy as np

from django.conf import settings

IMAGE_WIDTH = 64
IMAGE_HEIGHT = 64

MODEL_PATH = os.path.join(settings.BASE_DIR, 'knn_model_new2.pkl')
model = joblib.load(MODEL_PATH)

from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def index(request):
    return render(request, 'myapp/index.html')
```

`settings.BASE_DIR` 對應專案基礎位置，因此和前頁「把模型放在 manage.py 同層」互相配合。`joblib.load` 在模組層載入模型，`index` 以模板產生首頁。截圖已包含 `@ensure_csrf_cookie`，即使講義後面第 75 頁才再次敘述此修正，也不能聲稱這張圖還沒有它。

**截圖下半段：`preprocess_canvas_image(image_data)`**

函式說明列出八個步驟：

1. 解開 Base64 圖片資料。
2. 轉成 OpenCV 圖片。
3. 灰階處理。
4. 二值化。
5. 找出數字範圍。
6. 調整成 28×28（原文舊註解，和上面 `64` 設定不一致）。
7. 轉成 0～1。
8. 攤平成模型需要的格式。

畫面真正可見的函式有效程式到此為止：

```python
def preprocess_canvas_image(image_data):
    # 去掉 base64 前面的資料格式說明
    image_data = image_data.split(',')[1]
    # base64 解碼
    image_bytes = base64.b64decode(image_data)
```

此處省略了剛列出的 docstring，不表示原始函式僅有兩行；圖片下緣在這裡截斷。圖中未展示 `predict_digit` 的完整實作或回應欄位，不能只憑路由名稱補造後端全文。

**頁末步驟 5**：「建立網頁 index.html」，程式畫面接到第 72 頁。

**補充辨析**

- Canvas Data URL 通常含 `data:image/...;base64,` 前綴，拆出逗號後的部分才能 Base64 解碼；實務上應驗證資料格式及大小，不能假設永遠有第二段。
- `ensure_csrf_cookie` 讓首頁回應確保設定 CSRF cookie；不等於關閉 CSRF 檢查，前端送 POST 時仍須正確帶 token。
- `JsonResponse` 的匯入表明這個網站要用 JSON 回傳資料，但本圖未給出回應的完整結構。

<a id="ai-p072"></a>

### AI-P072｜`index.html` 樣式與模型輸入尺寸一致性

[原講義《20260907AI應用(20260915).pdf》第72頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=72)

**圖 1：模板開頭與樣式（截圖顯示至 button 規則）**

檔案位置顯示為 `templates/myapp/index.html`；原頁面使用 `<!DOCTYPE html>`、`<html lang="zh-Hant">`、UTF-8 編碼，以及：

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>KNN 手寫數字辨識</title>
```

可見的樣式如下：

```css
body {
    font-family: Arial, "Microsoft JhengHei", sans-serif;
    text-align: center;
    background-color: #f5f5f5;
    margin: 0;
    padding: 20px;
}
h1 { margin-top: 20px; }
p { font-size: 18px; }
canvas {
    background-color: black;
    border: 3px solid #333;
    cursor: crosshair;
    /* 手機觸控時不要讓畫面跟著滑動 */
    touch-action: none;
    /* 手機畫面自動縮放 */
    max-width: 90vw;
    max-height: 90vw;
}
button {
    margin: 10px;
    padding: 10px 25px;
    font-size: 18px;
    cursor: pointer;
}
```

黑色 Canvas 背景配合模型要求的黑底白字；十字游標適合書寫；`touch-action: none` 防止手勢操作被瀏覽器當作捲動；`90vw` 將畫布的最大顯示寬高限制在視窗寬度的一定比例。

**圖 2／步驟 6：如果預測不準，最常見原因**

AI 回答提醒：網站前處理後的輸入形狀，一定要跟模型訓練時完全一樣。

- 如果 KNN 訓練時是 `28 × 28 = 784` 特徵：

  ```python
  IMAGE_WIDTH = 28
  IMAGE_HEIGHT = 28
  ```

- 如果訓練時是 `64 × 64 = 4096` 特徵：

  ```python
  IMAGE_WIDTH = 64
  IMAGE_HEIGHT = 64
  ```

本講義新模型對應第二組。這段是條件說明，不是讓同一個模型任意切換輸入大小。

**補充辨析與範圍限制**

- 本頁只截到 HTML/CSS 前段，尚未展示 Canvas 元素的完整標籤、滑鼠或觸控事件、送出請求的 JavaScript 全文。不能根據頁面外觀宣稱已讀到完整 `index.html`。
- CSS 的黑色背景不一定等於 Canvas 像素資料已填黑，實作時要確認畫布初始化確實填入黑色，再以白色描繪；此為技術提醒，不是截圖已展示的程式。
- 本頁沒有啟動伺服器的命令或成功輸出；其下方實際內容是模型特徵維度提醒。

---

<a id="ai-p073"></a>

### AI-P073｜第二、三次 AI 修改：加入手機觸控並索取完整模板

[原講義《20260907AI應用(20260915).pdf》第73頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=73)

**上方截圖**

`myapp/views.py` 中再次紅框圈選 `IMAGE_WIDTH = 64`、`IMAGE_HEIGHT = 64`，下方可見 `settings.BASE_DIR` 組合 `knn_model_new2.pkl` 路徑並 `joblib.load`。這是承接上一頁的尺寸配對提醒；本頁並沒有辨識結果畫面。

**第二次修改的提示詞（原文）**

> 若此網站換成手機瀏覽，我也希望可以用手機觸碰畫面寫字。

講義旁標：

- `生成式ai 範例：Django 手寫數字辨識網站設置／Django 手寫數字辨識網站設置.mhtml`
- `生成式ai 範例：第二次修改程式`

需求從「電腦滑鼠」擴充成「手機觸控」。核心改動是輸入互動方式，並不是替換 KNN 模型或新增分類類別。

**第三次修改的提示詞（原文）**

> 給我index.html完整程式

同一個 mhtml 參考名稱再次出現，標記「生成式ai 範例：第三次修改程式」。頁末敘述：「下面是支援『電腦滑鼠』與『手機觸控』的完整 index.html」。下一頁展示的是檔案畫面，但截圖只拍到開頭，不能因敘述中用了「完整」就把未出現在 PDF 裡的程式內容補寫成原文。

**補充辨析：需求迭代方式**

講義示範先描述新增能力，再要求一份完整檔案，減少初學者不知片段應插在哪裡的困難。實作觸控時還需正確處理座標換算、開始／移動／結束事件與頁面捲動衝突；本頁沒有顯示這些事件函式的實碼，僅能記錄其需求。

<a id="ai-p074"></a>

### AI-P074｜手機版模板截圖與接續錯誤案例

[原講義《20260907AI應用(20260915).pdf》第74頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=74)

**本頁內容及可見程式**

唯一的截圖顯示 `templates/myapp/index.html`，左側亦保留 `index_old.html`。內容重複第 72 頁已展示的 HTML/CSS 前段，並非新的一組模型程式：

- `<!DOCTYPE html>`、`lang="zh-Hant"`、UTF-8。
- viewport 為 `width=device-width, initial-scale=1.0`。
- title：「KNN 手寫數字辨識」。
- `body`：Arial／Microsoft JhengHei／sans-serif、置中、背景 `#f5f5f5`、`margin: 0`、`padding: 20px`。
- `h1`：上邊距 20px；`p`：字級 18px。
- `canvas`：黑底、`3px solid #333` 邊框、`cursor: crosshair`、`touch-action: none`、`max-width: 90vw`、`max-height: 90vw`。
- `button`：margin 10px、padding `10px 25px`、font-size 18px、`cursor: pointer`。

**操作意義**

畫布區的註解指出兩項手機適配：觸控時不要讓整頁跟著滑動，以及小螢幕上自動縮放。這些設定是畫面／手勢行為的一部分，並不是模型推論本身。

**頁末**

「出現錯誤如下：」是下一頁的引導。本頁尚未顯示錯誤訊息，也未展示 JavaScript 後半部，不能把下一頁的 JSON 解析錯誤當作本頁已顯示的 console log。

<a id="ai-p075"></a>

### AI-P075｜手機可書寫但預測失敗：HTML 被當成 JSON

[原講義《20260907AI應用(20260915).pdf》第75頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=75)

**手機畫面（已局部放大核對）**

- 瀏覽器地址列為 `192.168.57.246:8080`；這是講義區域網路範例地址，未實際連線，不代表讀者環境可用。
- 標題：「KNN 手寫數字辨識」。
- 指示：「請用滑鼠或手指在黑色區域寫一個 0～9 的數字」。
- 黑底畫布上已畫出白色直筆 1，下面有「預測」「清除」按鈕。
- 「預測結果：」後沒有數字；下方顯示紅字錯誤：

  ```text
  發生錯誤：SyntaxError: Unexpected token '<', "<!DOCTYPE "... is not valid JSON
  ```

  引號及 `<!DOCTYPE` 周邊空白在圖面／文字層排版略有差異，確定的核心是 `Unexpected token '<'` 與 `is not valid JSON`。

**提供給 ChatGPT 的錯誤回報**

講義把「使用手機出現 發生錯誤：SyntaxError: Unexpected token '<', " <!DOCTYPE "... is not valid JSON」作為問題，再記錄：

1. 「依照文chatGPT文件都無錯誤」（原頁語句，指作者依文件檢查的描述）。
2. `views.py` 的 `index` 建議加上：

   ```python
   @ensure_csrf_cookie
   ```

下方 AI 回答截圖也只展示這個裝飾器建議，匯入位置與完整函式在下一頁。

**錯誤意義與辨析（補充，不冒充已證實的唯一原因）**

- 此錯誤發生在把 HTTP 回應解析為 JSON 時，卻讀到以 `<`／`<!DOCTYPE` 開頭的 HTML。手機上能畫字，說明畫布互動與送出請求的回應解析是不同層的問題。
- Django CSRF 拒絕頁、錯誤 URL 的 404 HTML、伺服器 500 錯誤頁或重新導向頁，都可能導致相同現象。僅憑這一行 SyntaxError 不能唯一證明是 CSRF。
- 本講義採用的修正方向是確保首頁設定 CSRF cookie。若要嚴格驗證根因，應檢查請求網址、HTTP 狀態碼、Content-Type、回應本文及 Django 伺服器紀錄；這些診斷證據沒有出現在此頁。
- 不應以停用 CSRF 保護取代檢查。本頁所建議的裝飾器是確保 cookie 存在，不是繞過驗證。

<a id="ai-p076"></a>

### AI-P076｜加入 CSRF cookie 裝飾器，桌機與手機顯示成功結果

[原講義《20260907AI應用(20260915).pdf》第76頁](Django%E4%B8%8A%E8%AA%B2%E8%AC%9B%E7%BE%A9/20260907AI%E6%87%89%E7%94%A8%2820260915%29.pdf#page=76)

**圖 1：`views.py` 中的修改**

紅框圈住匯入及裝飾器，對應位置為首頁 `index`：

```python
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def index(request):
    return render(request, 'myapp/index.html')
```

上面仍是 `MODEL_PATH = os.path.join(settings.BASE_DIR, 'knn_model_new2.pkl')` 與 `model = joblib.load(MODEL_PATH)`；下面接著 `preprocess_canvas_image(image_data)`。這個修改針對首頁 cookie，不是改寫模型辨識算法。背景 docstring 仍可見「調整成 28×28」的舊註解，需與前面 64×64 設定區分。

**圖 2：桌機瀏覽器結果（已局部放大）**

- 網址：`192.168.57.246:8080`，地址列顯示「不安全」提示。
- 標題及操作指示同手機版；黑底白字畫出 2。
- 下方「預測」「清除」按鈕保留，藍色文字顯示 **「預測結果：2」**。
- 截圖證明講義展示的這次桌機操作已得到數字結果；本次筆記未重新執行該網站。

**圖 3：手機瀏覽器結果（已局部放大）**

- 同一個範例地址 `192.168.57.246:8080`。
- 畫布上是白色閉合、略傾斜的 0，黑色背景。
- 「預測結果：0」以藍字顯示，沒有前頁的紅色 JSON 解析錯誤。
- 講義以此說明觸控輸入及預測回應已能完成這個示例。

**整段知識串接（補充整理）**

離線圖片資料 → 黑底白字二值化 → 前景邊界裁切 → 統一為 64×64 → 轉成 0～1、4096 維特徵 → KNN 訓練與保存 `knn_model_new2.pkl` → Django 載入模型 → 網頁 Canvas 接收滑鼠／手指書寫 → 圖片編碼傳到後端 → 相同前處理 → 回傳數字 → 網頁顯示結果。

要分別檢驗三種問題：**模型準確性**（例如前處理與資料分布）、**輸入互動**（滑鼠／觸控、座標與尺寸）、**網路與安全驗證**（路由、JSON 格式、CSRF cookie/token）。講義最後兩張成功截圖並不代表所有字跡或所有手機瀏覽器均已測試，也不能取代正式部署的 HTTPS 與安全設定。

---


## 附錄：閱讀覆蓋與仍須留意的原稿問題

主講義已核對：286 個 PDF 頁面、286 個逐頁小節、286 筆圖像閱讀紀錄；無漏頁、無重複頁碼。這是閱讀覆蓋檢查，不是「全部程式都已實跑通過」的宣告。

下列事項包括原稿版本差異、錯字、圖像模糊或前提缺少；它們不是都代表看不清楚。各頁正文保留更完整的前後文。

- **P007**：原稿中文編碼必要性與關鍵字全小寫敘述須區分 Python 2/3。
- **P008**：原保留字表屬Python 2；Python 3 的print/exec為函式。
- **P009**：縮排錯誤不能一律歸因tab混用。
- **P011**：三引號是字串，不等同#註解。
- **P014**：long屬Python 2；Python 3 整數使用int。
- **P015**：int無法直接轉換含小數點的字串；舊轉型表有Python 2專屬名稱。
- **P016**：unichr、long、cmp及舊式八進位等需版本辨析。
- **P017**：str(-124.a)會先發生SyntaxError，不是str轉型本身失敗。
- **P020**：串列修改／刪除例子名稱不一致，正文已標明。
- **P022**：cmp/list.sort(cmp,...)為Python 2介面，Python 3不適用。
- **P024**：原稿字典無序敘述需區分Python版本。
- **P026**：Python 3字典視圖與popitem順序和舊稿不同。
- **P028**：<>屬Python 2；/、//不可混淆。
- **P030**：原稿優先序表不完整／有誤，正文另列Python 3校正。
- **P037**：原稿質數例子未處理0、1、負數；已實跑並列邊界結果。
- **P039**：opertion/operation拼字不一致，已實際重現NameError。
- **P042**：原稿混用Python 2與Python 3形式，print(a,b)的顯示語義不同。
- **P043**：dir()列出所有記憶體物件的敘述過度概括，筆記已更正。
- **P044**：do something不是可執行碼；with不會自動處理所有例外。
- **P046**：缺點說明放於兩圖中間，第一圖其實沒有計時。
- **P048**：裝飾器執行時機敘述錯誤，已明確更正。
- **P050**：章節1.6重複；self不是關鍵字。
- **P051**：雙底線不是不可繞過的安全機制。
- **P052**：原圖英文拼字hava/dollors保留；private註解不代表安全隔離。
- **P053**：子類別並非必然覆寫__init__，取決於是否自訂。
- **P056**：傳統套件__init__.py規則不可概括namespace package；self欄位非共享屬性。
- **P058**：混用Python 2 raw_input與Python 3 input；密碼輸入不隱藏。
- **P059**：已隔離實測else字串加整數造成未捕捉TypeError；ValueError表述過度簡化。
- **P060**：需區分併發和平行，Python GIL限制與記憶體釋放敘述已補充。
- **P061**：Python Thread需start；wait/notify通常是Condition方法。
- **P066**：JSON null大小寫、彎引號、布林函數與頂層值敘述已更正。
- **P067**：仍沿用NULL大寫誤寫。
- **P068**：原文提到上例輸出但頁面沒有該程式或輸出圖；Python2型態表須分版本。
- **P070**：僅列檔名未提供四份原始內容；連結目前可用性未驗證。
- **P071**：Djangle拼字疑誤；session與hash說明經簡化
- **P072**：折線圖未交代縱軸指標定義
- **P073**：URL重定向用詞不等同HTTP redirect
- **P074**：下載、安裝及終端截圖版本不同
- **P075**：卸載virtualenv不等同刪除環境；截圖版本混用
- **P076**：deactivate和後續啟動狀態不一致；ALLOWED_HOSTS並非來源IP白名單
- **P081**：runserver版本與P076不同；原藍色註解部分字樣排版重疊
- **P083**：Django Template僅名稱未示識別碼
- **P085**：範例專案、Python版本與前頁不同
- **P087**：歷史偵錯器type保留未更新
- **P090**：截圖混用UserCreationForm01、sample、test、homework範例名稱
- **P091**：3.5.3與3.9.2截圖混編；sudo差異；deactivate排列可能誤導
- **P092**：不同版本安裝畫面不連續
- **P096**：圖中auth僅至0011，與P080不同
- **P101**：顯示/bin/python未能確證venv實際路徑
- **P102**：上下截圖SSH主機不同
- **P105**：原稿建議刪整個.ssh風險高，筆記已明確反對無差別刪除
- **P106**：啟動路徑重複dvds，dvdsenv與先前環境不同；ls/tree不同階段
- **P107**：sudo python不能保證虛擬環境；tree沒有完整project1
- **P108**：111.222.333.444無效IPv4；TEMPATES拼字錯誤
- **P109**：版本寫法混編；正文命令和圖不同
- **P110**：環境路徑與app目錄均和前頁不連續
- **P111**：黃色便利貼WSGL疑為WSGI拼誤；無終端時間或修補版資訊
- **P112**：原稿Diango拼字、Controller句尾未完成；MVT與MTV混用。
- **P114**：slug字元描述錯誤；參數型別為字典、admin.site.urls函式等說法不精確，筆記已標明。
- **P115**：說明例與實際截圖hello/hello1、name/username不同；示意URL省略埠號。
- **P119**：原稿把static標籤版本差異歸因Windows；name與username不一致；未展示CSS內容。
- **P122**：原稿locals結果省略request等區域變數。
- **P123**：路由缺p，筆記標示訂正。
- **P124**：Python字典鍵缺引號、方法呼叫缺括號，已註記。
- **P126**：is/is not原图用值相同比喻不精確。
- **P127**：score>=60及>=60未分隔，筆記訂正。
- **P128**：elseif應elif；比較符號需空白。
- **P129**：counter0/revcounter0起訖說明有一位偏差。
- **P130**：保留Nacy拼法；原HTML h3內嵌h2/ul不合宜。
- **P132**：信封比喻把POST隱藏當安全、把query視為header，需限制解讀。
- **P133**：User-Agent右側截斷；Content-Length與可見body不可確證；GET body及POST安全說法過度絕對。
- **P134**：request模組、GET方法用語不精確。
- **P136**：僅檢查鍵存在不等於值有效。
- **P138**：GET傳密碼不安全；無其他mode或缺鍵處理；get1/get2尾斜線版本變動。
- **P139**：示範不適合真實帳密。
- **P140**：標題與帳密實作不符；route與action尾斜線不一致。
- **P141**：錯誤畫面為重用示意，不是本post1端點證據。
- **P142**：只展示成功畫面，未展示錯誤帳密測試。
- **P143**：頂部URL截短，無法知道此次錯誤帳密值。
- **P144**：PHP label錯配、缺form結尾，已標訂正。
- **P145**：表單與結果埠號不一致；未展示實際勾選瞬間，僅結果可證兩值。
- **P146**：原稿 unix_socker 拼字錯誤；套件截圖和正文版本不同。
- **P147**：遠端 root 問答紅字與圖片 Y 呈現不一致。
- **P150**：root 遠端萬用來源與 ALL PRIVILEGES 是高風險教材示範。
- **P151**：登入命令文字層用非 ASCII 破折號；PASSWORD() 具版本限制。
- **P152**：UTF8 與後文 utf8mb4 不應視為等價。
- **P153**：原稿救援尚未交代恢復一般服務的完整步驟。
- **P154**：未展示結束 skip-grant-tables 並恢復正式服務。
- **P155**：原稿 startapp 建庫、與 MySQL 相容及只改設定的說法過度簡化；設定缺括號。
- **P156**：正文與截圖帳號及 OPTIONS 層級不一致。
- **P157**：跨頁 PostgreSQL 片段缺外層結尾括號；sudo 與虛擬環境執行有風險。
- **P158**：BigInteger 名稱錯；decimal_places 說明錯。
- **P159**：EmailField 254 寫為硬上限不精確；自動主鍵型別依版本設定。
- **P161**：blank=True 不會自動 null=True；default=datetime.now 不會每次更新；auto_now 說明需限定 save 路徑。
- **P164**：電話長度圖文不一致；root 與 tony、student 與 students 不一致。
- **P165**：圖未證明 students migration 已生成／套用；專案命名混用。
- **P166**：中間 29–51 行未顯示；listall.html 命令與實際 list.html 不一致。
- **P167**：教材埠號不一致。
- **P168**：EmailField 示例值 aa 未通過有效 email 格式。
- **P169**：label for=fname 與 input id=cName 不一致；測試埠號 8080/8000 不同。
- **P170**：函式首尾及中段省略；既有路由 listone 與前文 list 不同。
- **P171**：index 模板不完整；a 元素註解 post 不會使連結本身用 POST。
- **P172**：project1/project2 路徑混用；生日顯示格式差異無交代。
- **P173**：SQL 字串拼接有 injection 風險；174–185 行不在頁面圖內。
- **P174**：type=mail 非 email；cEmail required 與模型 blank=True 不一致；無新增成功結果。
- **P176**：缺 delete.html 程式，不能確認 CSRF；無授權／不存在處理；仍用字串 SQL。
- **P177**：圖片不是刪除完成證據；GET 更新為不安全教材範例。
- **P178**：截圖跳行且行號重疊；GET 寫入、字串 SQL；未知 mode 無可見回應。
- **P179**：date input 格式可能無效；重複 radio id；模板与結果畫面版本不一。
- **P180**：完整 query 中段被原圖裁切，無法復原；測試圖非單一連續操作。
- **P181**：GET 標題與 P182 POST 實作不一致。
- **P182**：edit2.html 原碼在指定範圍未展示，無法核實 CSRF；SQL仍拼接；前後圖不同測試狀態。
- **P183**：原圖編輯URL被窄幅截斷；清單只顯一列不能當作總筆數；未提供HTTP POST日誌。
- **P184**：原文ORM全名先寫Object Relational Model；orcale為原圖拼字；QuerySet及換資料庫敘述過度簡化。
- **P185**：ORM缺點第一項語句缺少明確主詞；複雜查詢限制與體積資訊需依框架版本環境判斷。
- **P186**：速度及安全性是原稿概括比較，不代表所有版本與工作負載。
- **P187**：收購年份未區分宣布與完成；179項、10MB及流行度為原稿時點敘述；硬編碼密碼只作原稿示例。
- **P188**：USER與電話長度的跨圖文差異；PostgreSQL引擎為舊名稱。
- **P189**：截圖不足以證明students資料表已建立；專案project1與project2混用。
- **P190**：模板名稱衝突；註解-cID與實際id模型不合。
- **P191**：命令8080與瀏覽器8000不一致。
- **P192**：EmailField中示例aa不是有效郵件。
- **P193**：label的for=fname與input的id=cName不一致；埠號不一致。
- **P194**：路由圖中的listone實作未在此頁提供。
- **P195**：index完整原始碼未展示；生日直接輸出但畫面ISO格式，與前頁不一致；刪除連結get註解應理解為載入確認頁，P199實作是POST才刪除。
- **P196**：project1與project2混用；未展示伺服器欄位驗證。
- **P197**：type=mail無效應為email；radio id重複；模型信箱可空白而表單必填。
- **P198**：只有新增輸入頁，非新增成功證據；埠號不一致。
- **P199**：未展示delete.html源碼與刪後結果；不應把首頁get註解誤讀成GET即刪除；沒有處理不存在id。
- **P200**：GET更新有副作用與URL資料洩露風險；未知mode及缺欄未處理。
- **P201**：日期value受語系格式影響，應另補Y-m-d；radio id重複；無required。
- **P202**：長GET query於原圖裁切，不能補全；不同測試版本與姓名狀態混用；8000轉8080且主機不同。
- **P203**：標題GET與下頁POST實作不一致；郵件gmial.com00依原圖保留。
- **P204**：未提供edit2.html原始碼或CSRF token證據；不同示範狀態混用；錯誤與權限未處理。
- **P205**：僅第一列可見非總筆數1；沒有POST日誌，POST證據來自P204。
- **P206**：虛擬環境相對路徑須核對
- **P206**：DecimalField 敘述不精確
- **P207**：EmailField 長度參數說法須修正
- **P207**：auto_now 不等於任何更新都自動觸發
- **P208**：表格 DATE 與模型 DateTimeField 不同
- **P208**：外鍵預設 cID_id 與後圖 cID 不同
- **P208**：遷移截圖只列 Create model students
- **P209**：學生cID=6之cName末字無法可靠辨識，已記蔡中〔待辨〕
- **P209**：學生cID=7之cName末字無法可靠辨識，已記徐佳〔待辨〕
- **P209**：學生cID=8之cName末字無法可靠辨識，已記林雨〔待辨〕
- **P209**：學生cID=1之cAddr路名前二字無法可靠辨識，已記台北市〔待辨：路名前二字〕北路12號
- **P209**：未顯示的19筆成績不推造
- **P209**：截圖cID與模型預設外鍵欄名cID_id不一致
- **P210**：命令與瀏覽器port不一致
- **P210**：admin匯入在截圖範圍外
- **P211**：命令與瀏覽器port不一致
- **P212**：ValuesQuerySet為舊稱
- **P213**：values與values_list例子標題錯置
- **P213**：value_list拼字錯誤
- **P214**：SQL印刷欄名含尾端空白
- **P214**：get物件不可套用同頁QuerySet迴圈
- **P216**：NOT整組SQL與題意和結果不一致
- **P216**：exclude比較圖錯配
- **P217**：Book圖程式與題意否定及開頭條件不符
- **P219**：exclude IN說明漏否定
- **P220**：icontains欄位文字誤植
- **P220**：exact與ilike對照僅概念不是所有後端實際SQL
- **P225**：datas等號後版面換行需接回
- **P226**：scorelist規劃與模型null/ENUM不同
- **P226**：UNSIGNED拼字錯誤
- **P227**：aggregate範例缺右括號
- **P228**：國文字串版面斷行
- **P229**：SQL印刷COUNT(cID)但圖頭COUNT(*)
- **P230**：annotate回傳模型物件說法不適用本頁values_list
- **P231**：分組鍵可先WHERE，本例ORM未典型展示HAVING
- **P231**：題目1至5但條件只<=5
- **P232**：宣稱5人實際僅3人
- **P232**：SQL與ORM不同資料
- **P232**：中文男與F/M ENUM規格衝突
- **P232**：地址空白與日期時間型別須確認
- **P233**：UPDATE值不一致
- **P233**：DELETE條件不一致且破壞性
- **P234**：無論何種JOIN都需雙邊有資料的說法錯誤
- **P234**：外鍵實體欄名依schema不同
- **P235**：6號姓名末字待辨
- **P235**：7號姓名末字待辨
- **P235**：8號姓名末字待辨
- **P236**：表別名範例SELECT未改別名
- **P236**：只GROUP BY主鍵的接受程度依DB及schema
- **P237**：三個新增主鍵不連續，缺號經過原稿未說明
- **P238**：圖中 FULL OUTER JOIN 不是 MySQL 直接支援的語法，已另列補充。
- **P240**：已放大確認學生表身高體重 NULL 為否，與 P239 null=True 不符；原因原稿未交代。
- **P241**：原稿未展示匯入精靈或來源檔。
- **P241**：第一筆地址不常見路名依圖可辨文字轉錄，若作精確資料集需再核。
- **P242**：題幹電話 099999 與程式 09333333 不同。
- **P243**：輸出截圖未含上一頁新增的王大明。
- **P244**：第二種科目與題目不同；姓名字串空白有疑義。
- **P245**：座號8姓名末字因原圖低解析度仍不確定，已標為林雨〔末字不確定〕；數值皆可辨。
- **P246**：座號8姓名末字因原圖低解析度仍不確定，已標為林雨〔末字不確定〕；數值皆可辨。
- **P249**：題目 C# 與新增 c# 大小寫不同。
- **P250**：大小寫比對受定序影響。
- **P252**：SQL 表名外鍵名與 Django 實體表不一致。
- **P252**：彎引號及姓名疏排空白不得直接當可執行 SQL。
- **P253**：無狀態不等同連線必斷。
- **P253**：命令 CookieSession 與註解 project1 不符。
- **P254**：Cookie 數量限制非通用現行固定值。
- **P254**：停用 Cookie 仍能 Session 與 Django 預設機制不符。
- **P255**：TestCookie 缺字串引號、彎引號；Request 大小寫。
- **P258**：空字典 != None 導致無 Cookie 時空回應。
- **P259**：delete_cookie[名稱] 概括語法不正確。
- **P259**：本地 now 後加 GMT 不會轉 UTC。
- **P260**：刪除網址與畫面結果不一致，不能證明成功刪除。
- **P260**：下一頁 P261 另有正確刪除後圖，已在筆記區分兩個畫面時間點。
- **P261**：本地時間標 GMT、counter 可修改且 int 未處理無效輸入。
- **P262**：SessionID 加密敘述不精確。
- **P262**：sesson() 拼字/API 錯誤。
- **P262**：middleware 截圖未展示後續列表。
- **P263**：P263 get_session/未捕捉key，與P264成果及路由不一致。
- **P264**：原文將SessionID描述為加密／編碼，不足以精確描述所有backend；request.session!=None不代表存在內容。
- **P265**：範例只記Session標誌，並無票數保存，不能等同可靠防灌票。
- **P266**：5分與50*60不符；Request大小寫錯；del request.clear()無效。
- **P267**：文字路徑CookieSessionAPP與匯入CookieSessionApp大小寫不一致。
- **P269**：本版本login.html原碼未展示；已有Session時POST分支未設狀態。
- **P271**：auth.lgoin為錯字；cd後相對虛擬環境路徑可能多一層dvds；未列app建立步驟。
- **P272**：裸except把任何錯誤歸成不存在。
- **P273**：密碼加密應精確區分為雜湊；username字元與staff/active的敘述簡化。
- **P274**：adduser與useradd不一致；GET可建立staff示例不可直接部署。
- **P275**：test2紅框與前頁test1程式並非同一帳號。
- **P276**：示意If不是合法Python關鍵字；Session不只登出才會失效。
- **P277**：AllowAllUsersModelBackend需每個登入入口另行檢查is_active；locals包含password。
- **P278**：下一頁標題與失敗畫面不完全吻合本模板及view。
- **P279**：圖中首頁標題與P278不同；失敗仍顯示login表單但P277 POST render index。
- **P280**：本頁只展示成果，不含新版專案原碼或驗證邏輯。
- **P281**：useradd_success_sta...在原截圖尾端省略，無法復原完整參數。
- **P282**：無page1驗證碼，不能證明該頁受登入保護。
- **P283**：上方User範例與下方CustomUser為不同片段；範圍內無CustomUser完整定義。
- **P284**：重建文字與migrate無待套用結果不一致；未顯示cBirthday提示最後選項；刪庫有資料毀損風險。
- **P285**：useradd1/2與先前useradd成果不同；缺完整view/model/template，不能拼湊宣稱完整專案。
- **P286**：text-body不保證或專門設定16px；btn-block屬Bootstrap4用法，須與前頁Bootstrap5參考區分。

### 驗證邊界

本次未從頭架設並執行整本 Django/SQL 專案。下附輸出僅驗證標明的 Python 例子與邊界；其餘講義截圖結果是原稿證據，不冒充本次實測。正文中的安全補充不代表老師已要求你加入某項作業規格。


## 附錄：本次實際 Python 驗算

以下為隔離測試輸出；部分程式碼直接從本筆記擷取再執行。測試沒有碰你的資料庫。

```text
Python: 3.12.13
Scope: isolated tests of selected examples, not all course code.
int("124") => 124
int(123.45) => 123
int("-123.45") => ValueError: invalid literal for int() with base 10: '-123.45'
float("124") => 124.0
float("123.45") => 123.45
str(123.4) => '123.4'
str(-124.a) => SyntaxError: invalid decimal literal (<string>, line 1)
20/10 => 2.0
9//2 => 4
9.0//2.0 => 4.0
-9//2 => -5
int(-9/2) => -4
10**20 => 100000000000000000000
-2**2 => -4
2**-2 => 0.25
bitwise 10 20 {'&': 0, '|': 30, '^': 30, '~a': -11, 'a<<2': 40, 'a>>2': 2}
bitwise 60 13 {'&': 12, '|': 61, '^': 49, '~a': -61, 'a<<2': 240, 'a>>2': 15}
get c / get c default3 / dict after None 3 {'a': 1, 'b': 2}
d['c'] => KeyError: 'c'
dict views: dict_keys dict_values dict_items
popitem: ('b', 2)
True/print keywords: True False
ranges: [1, 2, 3, 4] [1, 3, 5, 7, 9] [10, 8, 6, 4, 2]
string slices: 'llo' 'llo World!' 'ytho'
EXTRACTED NOTES P018 BLOCK1:
A B
AB
A&BEXTRACTED NOTES P018 BLOCK2:
the length of (Hello World) is 11
PI = 3.141593
PI =      3.142
PI =      3
 王大明   10  100
EXTRACTED NOTES P018 BLOCK3:
林小明的成績為80
Hello, world
EXTRACTED NOTES P033 BLOCK1:
Checking if 4 exists in list ( using loop ) : 
Element Exists
Checking if 4 exists in list ( using in ) : 
Element Exists
EXTRACTED NOTES P034 BLOCK1:
current letter: p
current letter: y
current letter: t
current letter: h
current letter: o
current letter: n
current fruit: banana
current fruit: apple
current fruit: mango
1
2
3
4
1~10,num=num+2
1
3
5
7
9
EXTRACTED NOTES P035 BLOCK1:
10~1,num=num-2
10
8
6
4
2
EXTRACTED NOTES P036 BLOCK1:
1
2
3
4
5
1
2
3
4
5
7
8
9
10
EXTRACTED NOTES P039 BLOCK1:
multiply:6
operation:6
operation:5
operation:-1
operation:0.6666666666666666
original misspelling:
NameError: name 'opertion' is not defined
tuple item assignment:
TypeError: 'tuple' object does not support item assignment
prime -1 original: ValueError: math domain error fixed: False
prime 0 original: 0 是質數 fixed: False
prime 1 original: 1 是質數 fixed: False
prime 2 original: 2 是質數 fixed: True
prime 3 original: 3 是質數 fixed: True
prime 4 original: 4 是質數 fixed: False
prime 9 original: 9 是質數 fixed: False
prime 25 original: 25 是質數 fixed: False
prime 49 original: 49 是質數 fixed: False
prime 97 original: 97 是質數 fixed: True
Prime corrected -10 through 1000 inclusive: ALL PASS
```


## 附錄：Python 舊版差異的官方核對依據

這一節是整理者另外查核的資料，不是老師講義原文。原講義仍以每節的 Pxxx 頁碼定位；文中保留的其他教學連結只是原稿參考文獻，並不表示本次已讀取所有外部網站。

- Python 3 的比較、成員測試和物件身份測試具有相同優先級；`&`、`^`、`|` 各自處於不同層級，布林運算則依 `not`、`and`、`or` 排序。因此 P030 原表不可直接當成正確的 Python 3 優先表。[1]
- 字典保留插入順序，Python 3.7 起是語言保證；`popitem()` 在該版本起保證後進先出。這是 P024「無序」及 P026「隨機取一組」的版本辨析依據。[2]
- Python 3 只有一個整數型別 `int`，不再另用 `long`；整數 `/` 會得到浮點數；舊式前導零八進位改為 `0o`；`cmp()` 及 list.sort 的 cmp 參數不再提供。這些對應 P014–P016、P022、P025、P028 的舊版說明。[3]

上述來源不代表其他未列出的補充已逐條完成外部查核。若要把整份筆記升級為「所有範例都能在同一版 Django 直接執行」的實作教材，仍需要另外進行完整環境重建與測試；本次的主要任務是忠實整理講義及圖片知識。


## 附錄：主講義逐頁原始文字層對照

這是 PDF 文字層的逐頁保留版，便於核對原句、範例檔名與參考網址。**沒有文字層的圖片不會出現在此區；圖片資訊已在正文逐頁整理。** 排版换行、縮排、舊語法、錯字按來源保留，請勿直接複製當作完整可執行檔。

<details>
<summary>原始文字 P001</summary>

```text
                                  授課教師：葉呈祥


第一章：Python 程設語言 ..................................................................... 5

     1.1 基本概念 ........................................................................................................ 5
  交互式編程 .................................................................................... 5
 腳本 ................................................................................................ 6
   Python 中文编码 .......................................................................... 7
   Python 保留字符 ........................................................................... 7
  行和縮排 ........................................................................................ 8
  多行語句 ........................................................................................ 9
   Python 引號 ................................................................................ 10
   Python 註釋 ................................................................................. 10
   Python 空行 ................................................................................. 11
   多個語句構成代碼組 .................................................................. 12
   Python 變數類型 ........................................................................ 12
   Python 數據類型轉換 ................................................................. 15
    print():列印輸出內容 .................................................................. 18
    String（字串） ............................................................................ 18
   List (串列) ..................................................................................... 19
    Tuple（元組） ............................................................................. 23
     Dictionary（字典） ..................................................................... 24
     1.2 運算符 ........................................................................................................... 28
  比較運算符 .................................................................................. 28
  賦值運算符 .................................................................................. 28
  位運算符 ...................................................................................... 29
  運算符優先級 .............................................................................. 29
     1.3 條件語句&循環語句 .................................................................................... 31
   if…in .............................................................................................. 33
  循環語句 for ............................................................................... 33
   break 與continue 命令 ............................................................... 36
  循環使用 for else ........................................................................ 36
   While 循環語句 ........................................................................... 36
  無限循環 while ........................................................................... 37
   循環使用while else .................................................................... 37
     1.4 函數 .............................................................................................................. 39
     1.5 模組(module) ................................................................................................ 40
     1.6 補充 .............................................................................................................. 42
  區域變數 vs 全域變數 .............................................................. 42
    type()函式來顯示資料型態 ........................................................ 42





                                                                                        1
```

</details>

<details>
<summary>原始文字 P002</summary>

```text
   *args 的用法 (一個星號) .......................................................... 42
    **kwargs 的用法(二個星號) ...................................................... 43
    dir()的用法 ................................................................................... 43
   python 研究-with as 用法 ......................................................... 44
    help()的用法 ................................................................................ 45
     Decorator(裝飾器) ....................................................................... 45
     1.6 物件導向(Object Oriented Programming)程式開發 ................................... 50
    定義類別(Create Object) ............................................................. 50
  The __init__() Function ................................................................ 50
      封裝(Encapsulation) .................................................................... 51
     繼承(Inheritance) ......................................................................... 52
     覆寫函式(Override) ..................................................................... 53
     classmethod() ............................................................................... 55
     1.7 套件(Package) ............................................................................................... 56
     1.8 例外處理(try except) .................................................................................... 58
     1.9 多執行緒(Multi-Threads) ............................................................................. 60
  建立子執行緒 .............................................................................. 61
   多個子執行緒與參數 .................................................................. 62
   Multi threads by overriding the run() method in a subclass ....... 64
     1.10 Python 處理JSON ........................................................................................ 66
  如何建立 JSON 字串 ................................................................. 66
   JSON 在python 中的使用 ........................................................... 67

第三章：Python Web Djangle ............................................................... 71

   Django 網站框架 (Python)教學 ................................................ 73
     3-1 Django 平台建置(windows) .......................................................................... 74
     3-1 Django 平台建置(windows+ Visual Studio Code) ......................................... 83
     3-1 複製專案 ...................................................................................................... 88
     3-1 Django 平台建置(Linux) ................................................................................ 91
     3-1 Django 平台建置(Linux+ Visual Studio Code+Remote Development) ......... 98
     3-2 建立Django 專案 ....................................................................................... 106
     3-3 建立Application 應用程式 ........................................................................ 106
     3-4 視圖(view)與url ......................................................................................... 112
    Diango 的Framework 架構 ....................................................... 112
    設定urls.py ................................................................................ 114
    加入static 靜態檔案 ................................................................. 117
   從網址中載取資料 .................................................................... 119
     3-5 視圖、模版與Template 語言 ................................................................... 122





                                                                                          2
```

</details>

<details>
<summary>原始文字 P003</summary>

```text
                               授課教師：葉呈祥


3-6 模板(Template)語言-變量 .......................................................................... 124
 變量 ............................................................................................ 124
3-7 模板(Template)語言-標籤 .......................................................................... 126
3-8 以GET 及POST 傳送資料 ......................................................................... 132
3-9 Django 資料庫連結與應用(使用MariaDB) ............................................... 146
  安裝MariaDB ............................................................................ 146
  解決MariaDB(10.5.12)本地無密碼直接登錄的問題 .............. 146
  Setting MySQL/MariaDB root password .................................... 146
 MySQL 開啟遠端連線權限允許遠端裝置連線資料庫 ........... 148
  使用Wordbench 開啟MariaDB 資料庫 .................................. 152
 How to Reset MySQL/MariaDB Database Root Password? ....... 153
  安裝mysqlclient 與設定Django 參數 ...................................... 154
  Field Type 欄位型別 ................................................................. 158
  Field Option 欄位選項 .............................................................. 160
3-11 資料庫新增、刪除、修改與查詢(使用SQL 語法) ................................ 163
  資料庫查詢(SQL-SELECT 語法) ................................................. 165
  資料新增(SQL-INSERT 語法) ..................................................... 172
  資料刪除(SQL-DELETE 語法) ..................................................... 175
  資料更新(使用GET) (SQL-UPDATE 語法) ................................. 177
  資料更新(使用GET) (SQL-UPDATE 語法) ................................. 181
3-12 資料庫查詢 (使用ORM) ......................................................................... 184
  SQLite vs MySQL vs PostgreSQL ................................................. 185
  資料庫查詢(SQL-SELECT 語法) ................................................. 189
  資料新增(SQL-INSERT 語法) ..................................................... 196
  資料刪除(SQL-DELETE 語法) ..................................................... 198
  資料更新(使用GET) (SQL-UPDATE 語法) ................................. 199
  資料更新(使用GET) (SQL-UPDATE 語法) ................................. 203
3-13 Django 使用ORM vs SQL 語法 ................................................................. 206
 建立環境 .................................................................................... 206
 ORM 欄位與引數說明 .............................................................. 206
 建立資料表 ................................................................................ 207
 新增、更新、刪除 .................................................................... 231
 多資料表關聯查詢 .................................................................... 234
 使用 JOIN 結合資料表 by SQL ............................................... 234
  Django ORM 一對一、一對多、多對多 ................................. 238
  UPDATE using INNER JOIN.......................................................... 252
  Delete using INNER JOIN ............................................................ 252
3-14 Cookies 與Sessions ................................................................................... 253





                                                                                   3
```

</details>

<details>
<summary>原始文字 P004</summary>

```text
 建立環境 .................................................................................... 253
 關於 Cookie .............................................................................. 253
 關於 Session ............................................................................. 254
  Cookie 的使用 ........................................................................... 254
  Session 的使用 .......................................................................... 262
3-15 使用者管理 .............................................................................................. 271
 建立環境 .................................................................................... 271
  讀取Django auth 使用者 .......................................................... 271
   HttpRequest.user 物件 .............................................................. 272
 登入和登出 ................................................................................ 275
   Registration 小專案(會員註冊與登入) ..................................... 279





                                                                                     4
```

</details>

<details>
<summary>原始文字 P005</summary>

```text
                                  授課教師：葉呈祥

第一章：Python 程設語言

    1989 年，人在阿姆斯特丹的 Guido van Rossum 於耶誕假期著手開發
Python ，其目的是設計出一種優美而強大，提供給非專業程式設計師使用的語
言，同時採取開放策略，使 Python 能夠完美結合如 C 、 C++ 和 Java 等其他
語言。時至今日， Python 已經是相當受歡迎的入門教學語言。
    Python 程式語言有著程式碼易學、易讀、清晰等特性，因而被廣泛作為入門
程式語言教授，具有跨平台的特性加上強悍完整的模組支援，許多網頁程式或是
系統管理都是可以透過 Python 來完成。而在Raspberry Pi Linux 開放系統的支
援之下，顛覆了以往 Python 難以控制硬體的印象。
  傳統程式言語的學習過程，由於語法複雜且缺乏互動而使得學習程式枯燥乏
味且易產生挫折感，導致多樣性功能應用目的開發產生高門檻。透過 Raspberry
Pi 開放硬體架構，Python 高階語言的學習得以變得更為全面，Python 豐富的函
式庫，讓開發者足以應付許多中大型專案的需求。


教學資源:

https://www.python.org/
http://www.w3big.com/zh-TW/python3/default.html
http://www.w3big.com/
https://www.w3schools.com/python/
https://www.tutorialspoint.com/index.htm

http://www.w3big.com/python/default.html
http://www.runoob.com/



指令下達範例：

[root@ localhost ~]# apt-get  install  python  python3


1.1 基本概念

 交互式編程

交互式編程不需要創建腳本文件，是通過Python 解釋器的交互模式進來編寫代
碼。linux 上你只需要在命令行中輸入Python 命令即可啟動交互式編程,提示窗
口如下：


指令下達範例：





                                                                                        5
```

</details>

<details>
<summary>原始文字 P006</summary>

```text
[root@ localhost ~]# python

print(“Hello Python”)

[root@ localhost ~]# exit()

(離開直譯器的互動介面)

[root@ localhost ~]# python3

print(“Hello Python”)

[root@ localhost ~]# exit()

(離開直譯器的互動介面)

 腳本

  直譯器的互動介面便於直接測試程式碼，程式碼也可以寫到副檔名為 .py
的檔案之中：
  通過腳本參數調用解釋器開始執行腳本，直到腳本執行完畢。當腳本執行完
成後，解釋器不再有效。讓我們寫一個簡單的Python 腳本程序。所有Python 文
件將以.py 為擴展名。將以下的源代碼拷貝至test.py 文件中。


1、假設你已經設置了Python 解釋器PATH 變量
指令下達範例：

[root@ localhost ~]# nano  hello.py

內容:

print("Hello,Python!")

[root@ localhost ~]# python  hello.py

[root@ localhost ~]# python3  hello.py


2、假定您的Python 解釋器在/usr/bin 目錄中，使用以下命令執行腳本：
指令下達範例：

[root@ localhost ~]# which  python

[root@ localhost ~]# nano  hello.py

#!/usr/bin/python

print("Hello,Python!")




                                                                                          6
```

</details>

<details>
<summary>原始文字 P007</summary>

```text
                                  授課教師：葉呈祥


print("您好")

[root@ localhost ~]# chmod +x hello.py

[root@ localhost ~]# ./hello.py


  Python 中文编码

Python 文件中如果未指定編碼，在執行過程會出現錯誤：





解決方法為只要在文件開頭加入#coding=utf-8。
指令下達範例：

[root@ localhost ~]# nano  01.py

內容:

#!/usr/bin/python

#coding=utf-8

print("Hello,Python!")

print("您好")

[root@ localhost ~]# ./01.py


範例basic-01.py


  Python 保留字符

   下面的列表顯示了在Python 中的保留字。這些保留字不能用作常數或變數，
或任何其他標識符名稱。所有Python 的關鍵字只包含小寫字母。





                                                                                        7
```

</details>

<details>
<summary>原始文字 P008</summary>

```text
 行和縮排

   學習Python 與其他語言最大的區別就是，Python 的代碼塊不使用大括號（{}）
來控制類，函數以及其他邏輯判斷。python 最具特色的就是用縮進來寫模塊。
  縮進的空白數量是可變的，但是所有代碼塊語句必須包含相同的縮進空白數
量，這個必須嚴格執行。如下所示：





  以下代碼將會執行錯誤：





                                                                                          8
```

</details>

<details>
<summary>原始文字 P009</summary>

```text
                                  授課教師：葉呈祥





     IndentationError: unexpected indent 錯誤是python 編譯器是在告訴你"Hi，老
兄，你的文件里格式不對了，可能是tab 和空格沒對齊的問題"，所有python 對
格式要求非常嚴格。如果是IndentationError: unindent does not match any outer
indentation level 錯誤表明，你使用的縮進方式不一致，有的是tab 鍵縮進，有的
是空格縮進，改為一致即可。因此，在Python 的代碼塊中必須使用相同數目的
行首縮進空格數。建議在每個縮進層次使用「單個製表符」或「兩個空格」或「四
個空格」，切記不能混用。


 多行語句

    Python 語句中一般以新行作為謂語句的結束符。但是我們可以使用斜杠(  \)
將一行的語句分為多行顯示，如下所示：





語句中包含[], {} 或() 括號就不需要使用多行連接符。如下實例：





                                                                                        9
```

</details>

<details>
<summary>原始文字 P010</summary>

```text
  Python 引號

    Python 接收單引號(' )，雙引號(" )，三引號(“””) 來表示字符串，引號的開
始與結束必須的相同類型的。其中三引號可以由多行組成，編寫多行文本的快捷
語法，常用語文檔字符串，在文件的特定地點，被當做註釋。





  Python 註釋

    python 中單行註釋採用 # 開頭





                                                                                          10
```

</details>

<details>
<summary>原始文字 P011</summary>

```text
                                  授課教師：葉呈祥





  Python 空行

  函數之間或類的方法之間用空行分隔，表示一段新的代碼的開始。類和函數

入口之間也用一行空行分隔，以突出函數入口的開始。空行與代碼縮進不同，空
行並不是Python 語法的一部分。書寫時不插入空行，Python 解釋器運行也不會
出錯。但是空行的作用在於分隔兩段不同功能或含義的代碼，便於日後代碼的維
護或重構。記住：空行也是程序代碼的一部分。





                                                                                        11
```

</details>

<details>
<summary>原始文字 P012</summary>

```text
 多個語句構成代碼組

  縮進相同的一組語句構成一個代碼塊，我們稱之代碼組。像if、while、def
和class 這樣的複合語句，首行以關鍵字開始，以冒號( : )結束，該行之後的一行
或多行代碼構成代碼組。我們將首行及後面的代碼組稱為一個子句(clause)。如
下實例：





  Python 變數類型

變數存儲在內存中的值。這就意味著在創建變數時會在內存中開闢一個空間。
基於變數的數據類型，解釋器會分配指定內存，並決定什麼數據可以被存儲在內
存中。因此，變數可以指定不同的數據類型，這些變數可以存儲整數，小數或字
符。


Python 有五個標準的數據類型：
   1、 Numbers（數字）
   2、 String（字串）
   3、 List（串列）
   4、 Tuple（元組）
   5、 Dictionary（字典）


Python 本身無陣列類型，可以使用NumPy 來解決。
     補充NumPy：
NumPy 是Python 在進行科學運算時，一個非常基礎的Package，同時也是非常
核心的library，它具有下列幾個重要特色：
   1、 提供非常高效能的多維陣列(multi-dimensional array)數學函式庫。
   2、 可整合C/C++及Fortran 的程式碼。
   3、 方便有用的線性代數(Linear Algebra)及傅立葉轉換(Fourier Transform)
    能力。
   4、 利用NumPy Array 替代Python List。
   5、 可定義任意的數據型態(Data Type)，使得能輕易及無縫的與多種資料庫





                                                                                          12
```

</details>

<details>
<summary>原始文字 P013</summary>

```text
                                  授課教師：葉呈祥


    整合。
NumPy Array：
學習資料科學(Data Science)或機器學習(Machine Learning)時，利用NumPy 在陣
列的操作是非常重要，其主要功能都架構在多重維度(N-dimensional array)的
ndarray 上，ndarray 是一個可以裝載相同類型資料的多維容器，維度的大小及資
料類型分別由shape 及dtype 來定義。通常我們會稱一維陣列為向量(vector)，二
維陣列為矩陣(matrix)。


    變數附值
Python 中的變數不需要聲明，變數的賦值操作既是變量聲明和定義的過程。每個
變數在內存中創建，都包括變數的標識，名稱和數據這些信息。每個變數在使用
前都必須賦值，變數賦值以後該變數才會被創建。等號（=）用來給變數賦值。
等號（=）運算符左邊是一個變數名,等號（=）運算符右邊是存儲在變數中的值。
例如：



#!/usr/bin/python

#coding=utf-8



counter = 100 # 赋值整型变量

miles = 1000.0 # 浮点型

name = "John" # 字符串




print counter

print miles

print name


範例basic-02.py


    多個變數賦值
指令下達範例：

[root@ localhost ~]# python

=>a=b=c=1





                                                                                        13
```

</details>

<details>
<summary>原始文字 P014</summary>

```text
=>print a

=>print b

=>print c

=>a,b,c=1,2,”tony”

=>print a

=>print b

=>print c



     Numbers（數字）
  數字數據類型用於存儲數值。他們是不可改變的數據類型，這意味著改變數
字數據類型會分配一個新的對象。當你指定一個值時，Number 對象就會被創建：





                                                                                          14
```

</details>

<details>
<summary>原始文字 P015</summary>

```text
                                  授課教師：葉呈祥





  Python 數據類型轉換

  有時候，我們需要對數據內置的類型進行轉換，數據類型的轉換，你只需要
將數據類型作為函數名即可。以下幾個內置的函數可以執行數據類型之間的轉換。
這些函數返回一個新的對象，表示轉換的值。





                                                                                        15
```

</details>

<details>
<summary>原始文字 P016</summary>

```text
#!/usr/bin/python

#coding=utf-8

# INT 函數能夠

# 把符合數學格式的數字型字符串轉換成整數

# 把浮點數轉換成整數，但是只是簡單的取整，而非四捨五入。

aa = int("124")    #Correct

print "aa = ", aa  #result=124




bb = int(123.45) #correct

print "bb = ", bb #result=123



cc = int("-123.45")  #Error,Can't Convert to int

print "cc = ",cc



# float 將整數和字符串轉換成浮點數




aa = float("124")     #Correct




                                                                                          16
```

</details>

<details>
<summary>原始文字 P017</summary>

```text
                                  授課教師：葉呈祥


print "aa = ", aa     #result = 124.0

bb = float("123.45")  #Correct

print "bb = ", bb     #result = 123.45

cc = float(-123.6)    #Correct

print "cc = ",cc     #result = -123.6



# str 函數將數字轉換成字符

aa = str(123.4)     #Correct

print aa           #result = '123.4'

bb = str(-124.a)    #SyntaxError: invalid syntax

print bb

cc = str("-123.45") #correct

print cc           #result = '-123.45'





                                                                                        17
```

</details>

<details>
<summary>原始文字 P018</summary>

```text
 print():列印輸出內容

print(項目1, 項目2, sep=分隔字元, end=結束字元)

print(str1 + " " + str2)

print(str1 ,str2,sep=””,end=”\n”)
print(str1 ,str2,sep=”&”,end=””)



參數格式化:%

print("the length of (%s) is %d" %("Hello World",len("Hello World")))

print("PI = %f" % math.pi)

print("PI = %10.3f" % math.pi)
print("PI = %6d" % int(math.pi))
print("%4s %4d %4d" % ("王大明",10,100))


參數格式化:format()  (Python3 後新增)

name="林小明"

score=80
print("{}的成績為{}".format(name,score))


字串插值（Formatted String Literal）: f  (Python 3.6 後新增)

text = 'world'

print(f'Hello, {text}')


範例basic-03.py


 String（字串）

String（字串）是Python 中使用最頻繁的數據類型。字串可以完成大多數集合類
的數據結構實現。它支持字符，數字，字符串甚至可以包含字串。字串用[ ]標識。
是python 最通用的複合數據類型。看這段代碼就明白。字串中的值得分割也可
以用到變數[頭下標:尾下標]，就可以截取相應的字串，從左到右索引默認0 開始
的，從右到左索引默認-1 開始，下標可以為空表示取到頭或尾。加號（+）是字
串連接運算符，星號（*）是重複操作。如下實例：





                                                                                          18
```

</details>

<details>
<summary>原始文字 P019</summary>

```text
                                  授課教師：葉呈祥





#!/usr/bin/python

#coding=utf-8

str = 'Hello World!'

print  str #輸出完整字符串

print  str[0] #輸出字符串中的第一個字符

print  str[2:5] #輸出字符串中第三個至第五個之間的字符串

print  str[2:] #輸出從第三個字符開始的字符串

print  str * 2 #輸出字符串兩次

print  str  +  "TEST" #輸出連接的字符串

範例basic-04.py


  List (串列)

串列是Python 中最基本的數據結構。序列中的每個元素都分配一個數字-它的位
置或索引，第一個索引是0，第二個索引是1，依此類。Python 中有6 個序列的
內置類型，但最常見的是列表和元組。序列都可以進行的操作包括索引，切片，
加，乘，檢查成員。此外，python 已經內置確定序列的長度以及確定最大和最小
的元素的方法。列表是最常用的Python 的數據類型，它可以作為一個方括號內
的逗號分隔值出現。列表的數據項不需要具有相同的類型。創建一個列表，只要
把逗號分隔的不同的數據項使用方括號括起來即可如下所示：





與字符串的索引一樣，列表索引從0 開始。列表可以進行截取，組合等。




                                                                                        19
```

</details>

<details>
<summary>原始文字 P020</summary>

```text
建立與顯示串列：

#!/usr/bin/python

#coding=utf-8




list1 = ['physics', 'chemistry', 1997, 2000];

list2 = [1, 2, 3, 4, 5, 6, 7 ];




print "list1[0]: ", list1[0]

print "list2[1:5]: ", list2[1:5]




更新串列：
你可以對列表的數據項進行修改或更新，你也可以使用追加append（）方法來
添加列表項，如下所示：



#!/usr/bin/python

#coding=utf-8




list2 = [1, 2, 3, 4, 5, 6, 7 ];

list2[2]=20;

print list[2];


注意：我們會在接下來的章節討論append()方法的使用


刪除元素：
可以使用 del 語句來刪除清單的的元素，如下實例：



#!/usr/bin/python

#coding=utf-8




                                                                                          20
```

</details>

<details>
<summary>原始文字 P021</summary>

```text
                                  授課教師：葉呈祥





list2 = [1, 2, 3, 4, 5, 6, 7 ];

del list2[2];

print list2;


Python 列表腳本操作符：
清單對 + 和 * 的操作符與字串相似。+ 號用於組合清單，* 號用於重複列表。
如下所示：





Python 列表截取：





Python 列表函数&方法：





                                                                                        21
```

</details>

<details>
<summary>原始文字 P022</summary>

```text
22
```

</details>

<details>
<summary>原始文字 P023</summary>

```text
                                  授課教師：葉呈祥

範例basic-05.py


 Tuple（元組）

  元組是另一個數據類型，類似於List（串列）。元組用"()"標識。內部元素用
逗號隔開。但是元素不能二次賦值，也就是說不能刪除或修改元素，但可以刪除
此變數。





#!/usr/bin/python

#coding=utf-8



tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )

tinytuple = (123, 'john')



print tuple # 輸出完整元組

print tuple[0] # 輸出元組的第一個元素

print tuple[1:3] # 輸出第二個至第三個的元素

print tuple[2:] # 輸出從第三個開始至列表末尾的所有元素





                                                                                        23
```

</details>

<details>
<summary>原始文字 P024</summary>

```text
print tinytuple * 2 # 輸出元組兩次

print tuple + tinytuple # 打印組合的元組




#delete tuple

del tup

print tup




範例basic-06.py


  Dictionary（字典）

字典(Dictionary)是除列表以外python 之中最靈活的內置數據結構類型。串列(List)
是有序的對象結合，字典(Dictionary)是無序的對象集合。兩者之間的區別在於：
字典當中的元素是通過鍵來存取的，而不是通過偏移存取。字典用"{ }"標識。字
典由索引(key)和它對應的值value 組成。
(簡單說，就是索引值可以是字串或數字)





#!/usr/bin/python

#coding=utf-8




dict = {}

dict['one'] = "This is one"

dict[2] = "This is two"



tinydict = {'name': 'john','code':6734, 'dept': 'sales'}




                                                                                          24
```

</details>

<details>
<summary>原始文字 P025</summary>

```text
                                  授課教師：葉呈祥




print dict['one'] # 輸出鍵為'one' 的值

print dict[2] # 輸出鍵為 2 的值

print tinydict # 輸出完整的字典

print tinydict.keys() # 輸出所有鍵

print tinydict.values() # 輸出所有值



#修改字典

tinydict[‘name’]=”marry”

print tinydict[‘name’] # 輸出所有值



#删除字典元素

del tinydict[‘name’] # 删除键是'Name'的条目

print tinydict[‘name’] # 輸出所有值

範例basic-07.py



字典內置函數&方法：





                                                                                        25
```

</details>

<details>
<summary>原始文字 P026</summary>

```text
常用Methods





EX:
list_test = {'a': 1, 'b': 2}


list_test.get('a') # 得到結果1





                                                                                          26
```

</details>

<details>
<summary>原始文字 P027</summary>

```text
                                  授課教師：葉呈祥


list_test.get('c') # 得到結果none
list_test.get('c', 3) # 得到設定的默認值3
list_test['b'] # 得到結果 2
list_test['c'] # 返回一個鍵值錯誤類型


參考文獻:

https://www.tutorialspoint.com/python/python_dictionary.htm





                                                                                        27
```

</details>

<details>
<summary>原始文字 P028</summary>

```text
1.2 運算符





範例basic-08.py



 比較運算符





 賦值運算符





                                                                                          28
```

</details>

<details>
<summary>原始文字 P029</summary>

```text
                                  授課教師：葉呈祥





 位運算符





 運算符優先級





                                                                                        29
```

</details>

<details>
<summary>原始文字 P030</summary>

```text
30
```

</details>

<details>
<summary>原始文字 P031</summary>

```text
                                  授課教師：葉呈祥


1.3 條件語句&循環語句





if name == 'bill':

    flag = True

    print 'Wlecome boss'

else:

    print name




if flag:

    print name, "is my family!"

else:

    print "Who are you?"


當判斷條件為多個值時,可以使用以下形式:





                                                                                        31
```

</details>

<details>
<summary>原始文字 P032</summary>

```text
# elif 用法

if num == 3: # 判斷num 的值

  print 'boss'

elif num == 2:

  print 'user'

elif num == 1:

  print 'worker'

elif num < 0: # 值小於零時輸出

  print 'error'

else:

  print 'roadman' # 條件均不成立時輸出



# 判斷值是否在0~10 之間

if num >= 0 and num <= 10:

    print 'hello'



# 判斷值是否在0~5 或者10~15 之間

if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):

    print 'hello'

else:

    print 'undefine'


你也可以在同一行的位置上使用if 條件判斷語句，如下實例：

var = 100

if ( var  == 100 ) : print "變量 var 的值為100"

print "Good bye!"




                                                                                          32
```

</details>

<details>
<summary>原始文字 P033</summary>

```text
                                  授課教師：葉呈祥

範例basic-09.py
範例basic-10.py
範例basic-11.py

  if…in





範例basic-11-2.py


與Java、C\C++等語言不同，Python 中是不提供switch/case 語法。可以使用字典
實現switch/case 這種方式易維護，同時也能夠減少代碼量。如下是使用字典模
擬的switch/case 實現：
範例basic-12.py


參考文獻:
http://wyp8711.blogspot.com/2019/09/python-dict-caseswitch.html



 循環語句 for





                                                                                        33
```

</details>

<details>
<summary>原始文字 P034</summary>

```text
#! /usr/bin/python

#coding=utf-8




for letter in 'python':

    print 'current letter:',letter





#############################################



fruits = ['banana','apple', 'mango']




for fruit in fruits:

    print 'current fruit:', fruit




############################################





for num in range(1,5):

    print num



###########################################




print "1~10,num=num+2"

for num in range(1,10,2):

    print num





                                                                                          34
```

</details>

<details>
<summary>原始文字 P035</summary>

```text
                                  授課教師：葉呈祥


###########################################

print "10~1,num=num-2"

for num in range(10,1,-2):

    print num


範例basic-13.py
範例basic-14.py





                                                                                        35
```

</details>

<details>
<summary>原始文字 P036</summary>

```text
  break 與continue 命令



print("........1.........")

for i in range(1,11):
      if(i==6):
         break
      print(i)


print("........2.........")
for i in range(1,11):

      if(i==6):
         continue
      print(i)


範例basic-15.py


 循環使用 for else

for 變數 in 串列:
  程式區塊一
    if(條件式):
    程式區塊二
         break
else:
  程式區塊三
範例basic-16.py


若for 迴圈正常執行完每一次程式區塊，就會執行else 的程式區塊三；若迴圈中
任何一次條件成立就以break 命令離開迴圈，將不會執行else 的程式區塊三。


  While 循環語句

Python 編程中while 語句用於循環執行程序，即在某條件下，循環執行某段程
序，以處理需要重複處理的相同任務。其基本形式為：





                                                                                          36
```

</details>

<details>
<summary>原始文字 P037</summary>

```text
                                  授課教師：葉呈祥





count = 0

while (count < 9):

   print 'The count is:', count

   count = count + 1

範例basic-17.py



 無限循環 while



while(True):  # 該條件永遠為true，迴圈將無限執行下去

   num = raw_input("Enter a number  :")

   print "You entered: ", num




print "Good bye!"


範例basic-18.py


 循環使用while else


# 判斷質數

import math

num = int(input('請輸入一個整數？'))

j = 2

while j < math.sqrt(num):




                                                                                        37
```

</details>

<details>
<summary>原始文字 P038</summary>

```text
    if (num%j == 0):

       print(num, '不是質數')

       break

    j += 1

else:

    print(num, '是質數')





                                                                                          38
```

</details>

<details>
<summary>原始文字 P039</summary>

```text
                                  授課教師：葉呈祥


1.4 函數

將一堆程式包起來，形成一支函式，便於重複使用。


# 定義

def multiply(x,y):

    return x*y




def operation(x,y):

    multiply=x*y

    add=x+y

    minus=x-y

    divide=float(x)/float(y)

    return [multiply,add,minus,divide]





num1=multiply(2,3)

print ("multiply:"+str(num1))




num=opertion(2,3)

print ("operation:"+str(num[0]))

print ("operation:"+str(num[1]))

print ("operation:"+str(num[2]))

print ("operation:"+str(num[3]))



範例basic-19.py





                                                                                        39
```

</details>

<details>
<summary>原始文字 P040</summary>

```text
1.5 模組(module)

一個較大型專案，程式是由許多類別或函式組成，為了程式的分工和維護，可以
適度地將程式分割成許多模組，再匯入並呼叫這些模組。
建立math_operation.py
範例: math_operation.py


使用方法1(import 模組名稱)：
每次要加上hello_module，不方便。

import math_operation

num=math_operation.operation(4,6)


範例basic-20.py



使用方法2(匯入模組內所有函式):
匯入math_operation 模組內全部的東西後，便能直接呼叫函式hello，但有可能現
有程式碼同名之函式，會造成衝突。

from math_operation import *

num=operation(4,6)


範例basic-21.py


使用方法3(匯入模組內函式):
選擇性地只匯入需要的東西

from math_operation import operation

num=operation(10,33)

範例basic-22.py


使用方法4(使用as 指定模組別名):
可用import/as 語法，將匯入的命名空間取個簡短的名稱

import math_operation as m

num=m.operation(4,6)

範例basic-23.py




                                                                                          40
```

</details>

<details>
<summary>原始文字 P041</summary>

```text
                                  授課教師：葉呈祥



參考文獻:
http://wiki.alarmchang.com/index.php?title=Python_import_%E6%8C%87%E5%AE
%9A%E7%9B%AE%E9%8C%84%E8%A3%A1%E9%9D%A2%E7%9A%84_.py_
%E6%AA%94%E6%A1%88





                                                                                        41
```

</details>

<details>
<summary>原始文字 P042</summary>

```text
1.6 補充

 區域變數 vs 全域變數





範例basic-24.py
範例basic-25.py


 type()函式來顯示資料型態

type() 函數如果你只有第一個參數則返回對象的類型





  *args 的用法 (一個星號)

打星號可以引入不定數量的參數：





                                                                                          42
```

</details>

<details>
<summary>原始文字 P043</summary>

```text
                                  授課教師：葉呈祥


一個星號會以 tuple 的方式引入

def buy(*price):

    print price

buy(1,2,3,4)




data=("bill",1,"tt")

buy(*data)

範例basic-26.py


  **kwargs 的用法(二個星號)

打星號可以引入不定數量的參數：
兩個星號會以 dict 的方式引入

def sell(**price):

    print price




sell(apple=10, ball=15, cat=25)




data = {"arg3": 3, "arg2": "two"}

sell(**data)

範例basic-27.py


 dir()的用法

dir( [obj] ) 用於查詢指定物件 obj 的全部屬性與方法，當不帶參數時，列出目前
記憶體中的所有物件。

print(dir())





                                                                                        43
```

</details>

<details>
<summary>原始文字 P044</summary>

```text
  python 研究-with as 用法

有一些任務，可能事先需要設置，事後做清理工作。對於這種場景，Python 的
with 語句提供了一種非常方便的處理方式。一個很好的例子是文件處理，你需要
獲取一個文件句柄，從文件中讀取資料，然後關閉文件句柄。


如果不用with 語句，程式碼如下：


file = open("/tmp/foo.txt")
data = file.read()
file.close()


這裡有兩個問題：
一是可能忘記關閉文件句柄；

二是文件讀取資料發生異常，沒有進行任何處理。


下面是處理異常的加強版本：


try:
       f = open('xxx')
except:

     print 'fail to open'
      exit(-1)
try:

    do something
except:
    do something
finally:
      f.close()


雖然這段程式碼執行良好，但是太冗長了。


這時候就是with 一展身手的時候了。除了有更優雅的語法，with 還可以很好的
處理上下文環境產生的異常。


下面是with 版本的程式碼：


with open("/tmp/foo.txt") as file:





                                                                                          44
```

</details>

<details>
<summary>原始文字 P045</summary>

```text
                                  授課教師：葉呈祥


   data = file.read()


with 如何工作?
緊跟with 後面的語句被求值後，返回物件的 __enter__() 方法被呼叫，這個方法
的返回值將被賦值給as 後面的變數。
當with 後面的程式碼塊全部被執行完之後，將呼叫前面返回物件的 __exit__()
方法。


文獻:

https://icodding.blogspot.com/2016/05/python-with-as.html


  help()的用法

help( obj ) 函數：用於查詢物件 obj 的詳細操作說明

help(__builtins__)





參考文獻:

https://note.pcwu.net/2017/03/03/python-arbitrary/


  Decorator(裝飾器)

Decorator(裝飾器)被大量廣泛的使用在各方library，是非常實用和必須了解的基
礎。Decorator(裝飾器)是一個函式，用來包著其他的函式。裝飾其他的函式，讓
被裝飾或是說被包著的函式能力增強。使用時機，當一個函數中，不同邏輯混雜
在一起的時候，程序的可讀性會大打折扣。這個時候，可以考慮用一種叫做“裝
飾器”的東西來重新整理代碼。


裝飾詞的優點：




                                                                                        45
```

</details>

<details>
<summary>原始文字 P046</summary>

```text
1、降低程式碼重複率
2、易讀性高
3、靈活度高





範例basic-28_1.py


此程式的缺點，prime_nums()包含時間計算與判斷質數。





範例basic-28_2.py





                                                                                          46
```

</details>

<details>
<summary>原始文字 P047</summary>

```text
                                  授課教師：葉呈祥





範例basic-28_3.py





                                                                                        47
```

</details>

<details>
<summary>原始文字 P048</summary>

```text
將時間計算與判斷質數分開，可以使用裝飾詞(Decorator)。裝飾詞就是一個函數。
首先執行31 行prime_nums()，接著執行25 行裝飾詞，因此會執行第6 行
display_time()。接著執行wrapper()，先計算時間，在call func()，執行第26 行
prime_nums()，最後執行第10~12 行。
範例basic-28_4.py





                                                                                          48
```

</details>

<details>
<summary>原始文字 P049</summary>

```text
                                  授課教師：葉呈祥





範例basic-28_5.py



參考文獻:

https://www.maxlist.xyz/2019/12/07/python-decorator/
https://www.youtube.com/watch?v=QqRvteWBSWg





                                                                                        49
```

</details>

<details>
<summary>原始文字 P050</summary>

```text
1.6 物件導向(Object Oriented Programming)程式開發

Python 的類別機制是C++ 以及Modula-3 的綜合體，當我們在使用Python 的類
別時並不用去宣告該類別的型態，也不用去宣告這個類別是否為public 或private，
Python 所有的類別與其包含的成員都是public 的，對於類別（Class）來說最重
要的一些特性在Python 程式語言裡面都有完全的保留，如最重要的單一繼承與
多重繼承，一個衍生／子類別（Derived class）可以覆載（Override）其所有基礎
類別（base class）的任何方法（method），方法（method）也可以呼叫一個基礎
類別（base class）的同名方法。


 定義類別(Create Object)

在Python 程式語言裡要定義一個類別必須使用class 敘述句，然後在敘述句後
面接著類別的名稱，並不用去定義是否為public 或private 等，也不用去定義資
料型態，如下定義：





範例: class-01.py





範例: class-02.py

  The __init__() Function
類別內的方法（method）宣告方式跟函數一樣，您可以想像類別方法就像是將函
數放進類別裡面，差異性在於函數的引數部份必須要加入self 敘述句，self 敘述
句就像其他程式語言裡面的this。
Python 程式語言裡的類別有一個特別方法（method）稱為__init__()，當建立
一個實例（Instance）的同時類別就會去執行這個函數，其實這個就像其他程





                                                                                          50
```

</details>

<details>
<summary>原始文字 P051</summary>

```text
                                  授課教師：葉呈祥

式語言的類別所定義的建構函數（Constructors）。





範例: class-03.py





範例: class-04.py



  封裝(Encapsulation)

類別內的成員變數，可以讓外部引用的稱公有(public)屬性，而可以讓外部引用的
方法稱公有方法。但任何類別的屬性與方法可以供外部隨意存取，這個設計概念
最大的風險是有資訊安全的疑慮。
1、private 有安全性
2、外部無法存取private variable
3、private variable 僅供類別內部使用


在屬性和方法前面加上「__」兩個_字元，就成為private 屬性和方法。


補充：python 變量初始化為空值分別是
  數值: digital_value = 0
  字串: str_value = ""





                                                                                        51
```

</details>

<details>
<summary>原始文字 P052</summary>

```text
  串列: list_value = []
  字典: ditc_value = {}
  元組: tuple_value = ()





範例: class-05.py





範例: class-06.py


  繼承(Inheritance)

可以繼承原有的類別，修改延伸出新的類別，原有的類別被稱為基礎類別(base
class)或雙親類別(parent class)，新的類別被稱為衍生類別(derived class)或子類別
(child class)，這個衍生類別就自動擁有基礎類別的變數與函式。


使用「class 衍生類別(基礎類別)」來定義類別間的繼承關係，衍生類別就繼承了
基礎類別；在衍生類別中使用「super().基礎類別的函式」可以呼叫基礎類別的函





                                                                                          52
```

</details>

<details>
<summary>原始文字 P053</summary>

```text
                                  授課教師：葉呈祥


式來幫忙，若衍生類別所需要的功能已經在基礎類別定義過了，就可以呼叫基礎

類別幫忙，重複利用已經撰寫過的程式碼。


若繼承父類別，即擁有父類別的所屬性與方法，也可以修改原來屬性與方法的內
容。


設定格式如下：





範例: class-07py
其中，與java 不同，父類別的建構方法會被子類別覆寫。



  覆寫函式(Override)

衍生類別可以繼承基礎類別的資料與函式，在衍生類別內重新改寫基礎類別的函
式，讓衍生類別與基礎類別的相同函式有不同功能，這樣的改寫函式稱作「覆寫
(Override)」。





                                                                                        53
```

</details>

<details>
<summary>原始文字 P054</summary>

```text
範例: class-08py





範例: class-09py


補充:
In Python 2, a declaration __metaclass__ = type makes declarations that would
otherwise create old-style classes create new-style classes instead.





                                                                                          54
```

</details>

<details>
<summary>原始文字 P055</summary>

```text
                                  授課教師：葉呈祥





範例: class-10.py


補充(pass 語法)：
Python pass 是空語句，是為了保持程序結構的完整性。
pass 不做任何事情，一般用做佔位語句。





範例: class-11.py

  classmethod()
classmethod()是Python 中的內置函數，它為給定函數返回類方法。
用法： classmethod(function)
參數：該函數接受函數名稱作為參數。
參考文獻:

https://vimsky.com/zh-tw/examples/usage/classmethod-in-python.html





                                                                                        55
```

</details>

<details>
<summary>原始文字 P056</summary>

```text
1.7 套件(Package)

把兩個檔案包在一個新的目錄 sample_package 底下：





很重要的是新增那個 __init__.py 檔。它是空的沒關係，但一定要有，有點宣稱
自己是一個 package 的味道。


這時候如果是進到 sample_package 裡面跑一樣的指令，那沒差。但既然都打包
成 package 了，通常是在整個專案的其他地方需要用到的時候 import 它，這時
候裡面的 import 就要稍微做因應。


├── package-01.py
├── mypackage
   └── __init__.py
   └── Hello.py
   └── myClass.py





範例: package-01.py





                                                                                          56
```

</details>

<details>
<summary>原始文字 P057</summary>

```text
                                  授課教師：葉呈祥



參考文獻：
https://medium.com/pyladies-taiwan/python-%E7%9A%84-import-%E9%99%B7%E
9%98%B1-3538e74f57e3





                                                                                        57
```

</details>

<details>
<summary>原始文字 P058</summary>

```text
1.8 例外處理(try except)

在執行程式的過程中產生錯誤，程式會中斷執行，發出例外訊息，以下介紹例外
的程式區塊，與實作自訂的例外類別。





   try-except
使用程式區塊「try…except…」可以攔截例外，在try 區塊中撰寫可能發生錯誤
的程式，若發生錯誤，則會跳到except 區塊執行進行後續的處理。


try:                輸入數字與字元則不會發生錯誤，密碼
     pwd = raw_input('請輸入密碼')  會儲存在變數pwd，若輸入「ctrl+D」，
except:               則顯示「發生錯誤」。
      print('發生錯誤')
範例: try-01.py


   try-except-else
使用程式區塊「try…except…else…finally」可以攔截例外，在try 區塊中撰寫可
能發生錯誤的程式，若發生錯誤，則會跳到except 區塊進行後續的處理，若沒
有發生錯誤，則會跳到else 區塊執行。不論是否發生錯誤，都會執行finally 的程
式碼。


except 後可以接指定錯誤類型，常見錯誤類型，如下表。

錯誤類型      說明





                                                                                          58
```

</details>

<details>
<summary>原始文字 P059</summary>

```text
                                  授課教師：葉呈祥

KeyboardInterrupt   當使用者輸入中斷(Ctrl+C)時，發出此錯誤。
ZeroDivisionError   除以0 時，發出此錯誤。
EOFError         接受到EOF(end of file)訊息時，發出此錯誤。
NameError      區域變數或全域變數找不到時，發出此錯誤。
OSError       與作業系統有關的錯誤
FileNotFoundError  檔案或資料夾找不到時，發出此錯誤。
ValueError      輸入資料與程式預期輸入資料型別不同時，發出此錯誤。





範例: try-02.py





                                                                                        59
```

</details>

<details>
<summary>原始文字 P060</summary>

```text
1.9 多執行緒(Multi-Threads)

作業系統原理相關的書，基本都會提到一句很經典的話：「程序是資源分配的最
小單位，執行緒則是CPU 排程的最小單位」。
執行緒是作業系統能夠進行運算排程的最小單位。它被包含在程序之中，是程序
中的實際運作單位。一條執行緒指的是程序中一個單一順序的控制流，一個程序
中可以併發多個執行緒，每條執行緒並行執行不同的任務。
好處 ：
1.易於排程。
2.提高併發性。通過執行緒可方便有效地實現併發性。程序可建立多個執行緒來
執行同一程式的不同部分。
3.開銷少。建立執行緒比建立程序要快，所需開銷很少。
4.利於充分發揮多處理器的功能。通過建立多執行緒程序，每個執行緒在一個處
理器上執行，從而實現應用程式的併發性，使每個處理器都得到充分執行。


多執行緒似於同時執行多個不同程序，多執行緒有如下優點：
 使用線程可以把佔據長時間的程序中的任務放到後台去處理。
 用戶界面可以更加吸引人，這樣比如用戶點擊了一個按鈕去觸發某些事件的
  處理，可以彈出一個進度條來顯示處理的進度
 程序的運行速度可能加快
 在一些等待的任務實現上如用戶輸入，文件讀寫和網絡收發數據等，線程就
  比較有用了。在這種情況下我們可以釋放一些珍貴的資源如內存佔用等等。


執行緒的狀態





                                                                                          60
```

</details>

<details>
<summary>原始文字 P061</summary>

```text
                                  授課教師：葉呈祥


在這裡我簡單來解釋以下這幾種狀態的含義:
1.  New 新建:使用執行緒的第一步就是建立執行緒，建立後的執行緒只是進入
   可執行的狀態，也就是Runnable。
2.  Runnable:進入此狀態的執行緒還並未開始執行，一旦CPU 分配時間片給這
  個執行緒後，該執行緒才正式的開始執行。
3. Running:執行緒正式開始執行，在執行過程中執行緒可能會進入阻塞的狀態，
   即Blocked。
4.  Blocked:在該狀態下，執行緒暫停執行，解除阻塞後，執行緒會進入Runnable
  狀態，等待CPU 再次分配時間片給它。
5.  Dead 結束:執行緒方法執行完畢或者因為異常終止返回。


這就和人的一生——出生、學習(工作之前的準備)、工作、休假——是相似的。
其中最複雜的是執行緒從Running 進入Blocked 狀態,通常有三種情況:睡眠:執行
緒主動呼叫sleep 或join 方法後。等待：執行緒中呼叫wait 方法，此時需要有其
他執行緒通過notify 方法來喚醒。
同步:執行緒中獲取執行緒鎖，但是因為資源已經被其他執行緒佔用時。
到現在,我們對執行緒有個基本的概念,光說不練假把式,下面我們就通過是三個
小的示例來聊聊執行緒的使用以及執行緒中最終的兩個概念:同步和通訊。


https://docs.python.org/2/library/threading.html?highlight=threading#module-threa
ding


This class represents an activity that is run in a separate thread of control. There are
two ways to specify the activity: by passing a callable object to the constructor, or by

overriding the run() method in a subclass. No other methods (except for the
constructor) should be overridden in a subclass. In other words, only override the
__init__() and run() methods of this class.


 建立子執行緒



#!/usr/bin/python

#coding=utf-8

import threading

import time





                                                                                        61
```

</details>

<details>
<summary>原始文字 P062</summary>

```text
# 子執行緒的工作函數

def job():

  for i in range(5):

    print "Child thread:%d"% i

    time.sleep(1)



# 建立一個子執行緒

t = threading.Thread(target = job)



# 執行該子執行緒

t.start()



# 主執行緒繼續執行自己的工作

for i in range(3):

  print "Main thread:%d"% i

  time.sleep(1)



# 等待 t 這個子執行緒結束

t.join()



print("Done.")



範例: thread-01.py




 多個子執行緒與參數




                                                                                          62
```

</details>

<details>
<summary>原始文字 P063</summary>

```text
                                  授課教師：葉呈祥




#!/usr/bin/python

#coding=utf-8




import threading

import time



# 子執行緒的工作函數

def job(num):

    for i in range(10):

       print("Thread", num)

       time.sleep(1)



# 建立 5 個子執行緒

threads = []

for i in range(5):

  threads.append(threading.Thread(target = job, args = (i,)))

  threads[i].start()



# 主執行緒繼續執行自己的工作

# ...



# 等待所有子執行緒結束

for i in range(5):

  threads[i].join()





                                                                                        63
```

</details>

<details>
<summary>原始文字 P064</summary>

```text
print("Done.")



範例: thread-02.py



  Multi threads by overriding the run() method in a subclass


This class represents an activity that is run in a separate thread of control. There are
two ways to specify the activity: by passing a callable object to the constructor, or by
overriding the run() method in a subclass. No other methods (except for the

constructor) should be overridden in a subclass. In other words, only override the
__init__() and run() methods of this class.


#!/usr/bin/python

#coding=utf-8




import threading

import time



# 繼承threading.Thread 的子執行緒類別

class MyThread(threading.Thread):

 #建構子

  def __init__(self, num):

    threading.Thread.__init__(self)

    self.num = num

 #重新改寫基礎類別的函式run

  def run(self):

    print("Thread", self.num)

    time.sleep(1)





                                                                                          64
```

</details>

<details>
<summary>原始文字 P065</summary>

```text
                                  授課教師：葉呈祥




# 建立 5 個子執行緒

threads = []

for i in range(5):

  threads.append(MyThread(i))

  threads[i].start()



# 主執行緒繼續執行自己的工作

# ...



# 等待所有子執行緒結束

for i in range(5):

  threads[i].join()




print("Done.")




範例: thread-03.py





                                                                                        65
```

</details>

<details>
<summary>原始文字 P066</summary>

```text
1.10 Python 處理JSON

JSON(JavaScript Object Notation) 是一種輕量級的數據交換格式。它使得人們很
容易的進行閱讀和編寫。同時也方便了機器進行解析和生成。它是基於JavaScript
Programming Language , Standard ECMA-262 3rd Edition - December 1999 的一個
子集。 JSON 採用完全獨立於程序語言的格式，但是也使用了類似C 語言的習
慣（包括C, C++, C#, Java, JavaScript, Perl, Python 等）。這些特性使JSON 成為理
想的數據交換語言。


JSON 是個以純文字為基底去儲存和傳送簡單結構資料，你可以透過特定的格式
去儲存任何資料(字串,數字,陣列,物件)，也可以透過物件或陣列來傳送較複雜的
資料。一旦建立了您的 JSON 資料，就可以非常簡單的跟其他程式溝通或交換
資料，因為 JSON 就只是純文字個格式。
JSON 的優點如下:
1、相容性高
2、格式容易瞭解，閱讀及修改方便
3、支援許多資料格式 (number,string,booleans,nulls,array,associative array)
4、許多程式都支援函式庫讀取或修改 JSON 資料


 如何建立 JSON 字串

可以透過底下規則來建立 JSON 字串：
1、JSON 字串可以包含陣列 Array 資料或者是物件 Object 資料
2、陣列可以用[ ]來寫入資料
3、物件可以用{  }來寫入資料
4、name    /  value 是成對的，中間透過  (:) 來區隔


物件或陣列的 value 值可以如下：
1、數字 (整數或浮點數)
2、字串 (請用” ”括號)
3、布林函數 (boolean) (true 或 false)
4、陣列 (請用  [ ] )
5、物件 (請用 { } )
6、NULL





                                                                                          66
```

</details>

<details>
<summary>原始文字 P067</summary>

```text
                                  授課教師：葉呈祥


 JSON 在python 中的使用

    介紹
JSON(JavaScript Object Notation) 是一種輕量級的數據交換格式。它使得人們很
容易的進行閱讀和編寫。同時也方便了機器進行解析和生成。它是基於JavaScript
Programming Language , Standard ECMA-262 3rd Edition - December 1999 的一個
子集。 JSON 採用完全獨立於程序語言的格式，但是也使用了類似C 語言的習
慣（包括C, C++, C#, Java, JavaScript, Perl, Python 等）。這些特性使JSON 成為理
想的數據交換語言。


JSON 是個以純文字為基底去儲存和傳送簡單結構資料，你可以透過特定的格式
去儲存任何資料(字串,數字,陣列,物件)，也可以透過物件或陣列來傳送較複雜的
資料。一旦建立了您的 JSON 資料，就可以非常簡單的跟其他程式溝通或交換
資料，因為 JSON 就只是純文字個格式。
JSON 的優點如下:
1、相容性高
2、格式容易瞭解，閱讀及修改方便
3、支援許多資料格式 (number,string,booleans,nulls,array,associative array)
4、許多程式都支援函式庫讀取或修改 JSON 資料


可以透過底下規則來建立 JSON 字串：
1、JSON 字串可以包含陣列 Array 資料或者是物件 Object 資料
2、陣列可以用[ ]來寫入資料
3、物件可以用{  }來寫入資料
4、name    /  value 是成對的，中間透過  (:) 來區隔


物件或陣列的 value 值可以如下:
1、數字 (整數或浮點數)
2、字串 (請用” ”括號)
3、布林函數 (boolean) (true 或 false)
4、陣列 (請用  [ ] )
5、物件 (請用 { } )
6、NULL


     JSON 在python 中的使用
Python 2.6 開始加入了JSON 模塊，無需另外下載，Python 的JSON 模塊序列化
與反序列化的過程分別是 encoding 和 decoding。





                                                                                        67
```

</details>

<details>
<summary>原始文字 P068</summary>

```text
encoding：把一個python 對象編碼轉換成JSON 字符串
decoding：把json 格式字符串解碼轉換成Python 對象





通過輸出的結果可以看出，簡單類型通過encode 之後跟其原始的repr()輸出結果
非常相似，但是有些數據類型進行了改變，例如上例中的元組則轉換為了列表。
在json 的編碼過程中，會存在從python 原始類型向json 類型的轉化過程，具體
的轉化對照如下：





loads 方法返回了原始的對象，但是仍然發生了一些數據類型的轉化。比如，上
例中'abc'轉化為了unicode 類型。從json 到python 的類型轉化對照如下：





                                                                                          68
```

</details>

<details>
<summary>原始文字 P069</summary>

```text
                                  授課教師：葉呈祥





encoding & decoding

# josn encoding

import json

#list 內放dict

data = [{"ID":"1","STATUS":"0"},{"ID":"2","STATUS":"1"}]

data_string = json.dumps(data) #encoding




# json decoding

decoded = json.loads(data_string) # decoding




id1 = decoded[0]["ID"]

status1 = decoded[0]["STATUS"]




id2 = decoded[1]["ID"]

status2 = decoded[1]["STATUS"]





                                                                                        69
```

</details>

<details>
<summary>原始文字 P070</summary>

```text
範例: json-01.py
範例: json-02.py
範例: json-03.py
範例: json-04.py



參考文獻:
https://www.cnblogs.com/huchong/p/9037142.html
http://opendata2.epa.gov.tw/AQI.json





                                                                                          70
```

</details>

<details>
<summary>原始文字 P071</summary>

```text
                                  授課教師：葉呈祥

第三章：Python Web Djangle

Django 是一個高級的 Python 網路框架，可以快速開發安全和可維護的網站。
由經驗豐富的開發者構建，Django 負責處理網站開發中麻煩的部分，因此你可
以專注於編寫應用程序，而無需重新開發。它是免費和開源的，有活躍繁榮的社
區、豐富的文檔、以及很多免費和付費的解決方案。Django 可以使你的應用具
有以下優點:
  完備：Django 遵循“功能完備”的理念，提供開發人員可能想要“開箱即用”
  的幾乎所有功能。
  通用：Django 可以（並已經）用於構建幾乎任何類型的網站—從內容管理
  系統和維基，到社交網絡和新聞網站。它可以與任何客戶端框架一起工作，
  並且可以提供幾乎任何格式（包括 HTML、RSS、JSON、XML 等）的內容。
  安全：Django 幫助開發人員，通過提供一個被設計為 “做正確的事情” 來
  自動保護網站的框架，來避免許多常見的安全錯誤。例如，Django 提供了
  一種安全的方式，來管理用戶帳號和密碼，避免了常見的錯誤，比如將
     session 放在 cookie 中這種易受攻擊的做法（取而代之的是，cookies 只包
  含一個密鑰，實際數據存儲在數據庫中），或直接存儲密碼，而不是密碼的
    hash 值。
 密碼 hash ，是讓密碼通過加密 hash 函數，而創建的固定長度值。 Django
  能通過運行 hash 函數，來檢查輸入的密碼  - 就是將輸出的 hash 值，與存
  儲的 hash 值進行比較是否正確。然而由於功能的 “單向” 性質，假使存儲
  的 hash 值受到威脅，攻擊者也難以解出原始密碼。
  可擴展：Django 使用基於組件的 “無共享” 架構 (架構的每一部分獨立於
  其他架構，因此可以根據需要進行替換或更改)。在不同部分之間，有明確
  的分隔，意味著它可以通過在任何級別添加硬件，來擴展服務：緩存服務器，
  數據庫服務器，或應用程序服務器。
  可維護：Django 代碼編寫，是遵照設計原則和模式，鼓勵創建可維護和可
  重複使用的代碼。特別是，它使用了不要重複自己（DRY）原則，所以沒有
  不必要的重複，減少了代碼的數量。 Django 還將相關功能，分組到可重用
  的 “應用程序” 中，並且在較低級別，將相關代碼分組或模塊（模型視圖控
   制器Model View Controller (MVC)模式）。
  可移植：Django 是用 Python 編寫的，它在許多平台上運行。這意味著，
  你不受任務特定的服務器平台的限制，並且可以在許多種類的 Linux，
    Windows 和 Mac OS X 上運行應用程序。


Find your new favorite web framework：
https://hotframeworks.com/





                                                                                        71
```

</details>

<details>
<summary>原始文字 P072</summary>

```text
在傳統的數據驅動網站中，Web 應用程序會等待來自Web 瀏覽器（或其他客戶
端）的HTTP 請求。當接收到請求時，應用程序根據URL 和可能的POST 數據或
GET 數據中的信息確定需要的內容。根據需要，可以從數據庫讀取或寫入信息，
或執行滿足請求所需的其他任務。然後，該應用程序將返回對Web 瀏覽器的響
應，通常通過將檢索到的數據插入HTML 模板中的佔位符來動態創建用於瀏覽器
顯示的HTML 頁面。


Django 網絡應用程序通常將處理每個步驟的代碼分組到單獨的文件中：





                                                                                          72
```

</details>

<details>
<summary>原始文字 P073</summary>

```text
                                  授課教師：葉呈祥



     URLs:雖然可以通過單個功能來處理來自每個URL 的請求，但是編寫單
   獨的視圖函數來處理每個資源是更加可維護的。URL 映射器用於根據請求
     URL 將HTTP 請求重定向到相應的視圖。URL 映射器還可以匹配出現在
     URL 中的字符串或數字的特定模式，並將其作為數據傳遞給視圖功能。
     View:視圖是一個請求處理函數，它接收HTTP 請求並返回HTTP 響應。
   視圖通過模型訪問滿足請求所需的數據，並將響應的格式委託給模板。
     Models:模型是定義應用程序數據結構的Python 對象，並提供在數據庫中
   管理（添加，修改，刪除）和查詢記錄的機制。
     Templates:模板是定義文件（例如HTML 頁面）的結構或佈局的文本文
   件，用於表示實際內容的佔位符。一個視圖可以使用HTML 模板，從數據
   填充它動態地創建一個HTML 頁面模型。可以使用模板來定義任何類型的
   文件的結構;它不一定是HTML！



參考文獻:

https://developer.mozilla.org/zh-TW/docs/Learn/Server-side/Django/Introduction


  Django 網站框架 (Python)教學

1.   https://developer.mozilla.org/zh-TW/docs/Learn/Server-side/Django/Models
2.   https://www.liujiangblog.com/course/django/2





                                                                                        73
```

</details>

<details>
<summary>原始文字 P074</summary>

```text
3-1 Django 平台建置(windows)





# python --version

# python -V





# pip list (查看已安裝的套件)



                           Package listing（套件列表查詢）





安裝虛擬環境

# pip install virtualenv





                                                                                          74
```

</details>

<details>
<summary>原始文字 P075</summary>

```text
                                  授課教師：葉呈祥





virtualenv 這工具就是建立一個虛擬的環境，可以在這虛擬環境中安裝所需套

件或是函式庫。因為這建立起來的環境是虛擬的，當不需要只需刪除即可，完全

不會影響到原有作業系統。



# pip uninstall virtualenv(刪除虛擬環境套件)



# cd c:\    Change Directory（切換工作目錄）

# virtualenv dvds (建立一個虛擬環境dvds)





進入虛擬環境:

# cd dvds

# Scripts\activate





安裝Django 套件：

# pip install Django





                                                                                        75
```

</details>

<details>
<summary>原始文字 P076</summary>

```text
 # pip list





退出虛擬環境:

 # deactivate



建立專案：         使用 Django ，動作的指令詞

 # Django-admin startproject project1

 django-admin 是專屬Django ，用來執行各種建立、管理、測試網頁專案

建立應用程式：

 # cd project1            開始建立一個新的功能模組

 # python manage.py startapp myapp





  Make Directory（建立目錄）
 # mkdir templates  取名templates（範本），專門存放網頁的HTML畫面檔
               取名static（靜態），專門存放不會隨使用者動態改變的
 # mkdir static             檔案，例如圖片、樣式表以及前端程式碼

修改settings.py   →開啟vs code 選擇project1 的資料夾修改


安全性白名單變數，是Django用來限制哪些IP可以連進這個網站的名單變數
 ALLOWED_HOSTS = ['*']  *代表所有網域





                                                                                          76
```

</details>

<details>
<summary>原始文字 P077</summary>

```text
                                  授課教師：葉呈祥





只有被列在這個清單裡的模組，Django 才會去載入它、管理它的資料庫表格

INSTALLED_APPS = [

    'django.contrib.admin',

    'django.contrib.auth',

    'django.contrib.contenttypes',

    'django.contrib.sessions',

    'django.contrib.messages',

    'django.contrib.staticfiles',

    'myapp',

]





TEMPLATES = [





                                                                                        77
```

</details>

<details>
<summary>原始文字 P078</summary>

```text
    {

       'BACKEND': 'django.template.backends.django.DjangoTemplates',
       代表專案根目錄的絕對路徑
       'DIRS': [BASE_DIR / 'templates'],
 Django 用來尋找HTML 檔案的搜尋清單
       'APP_DIRS': True,

       'OPTIONS': {

           'context_processors': [

               'django.template.context_processors.debug',

               'django.template.context_processors.request',

               'django.contrib.auth.context_processors.auth',

               'django.contrib.messages.context_processors.messages',

           ],

       },

    },

]





決定網站預設顯示語系的變數

LANGUAGE_CODE = 'zh-Hant'  繁體中文

TIME_ZONE = 'Asia/Taipei'  時區改台北




                                                                                          78
```

</details>

<details>
<summary>原始文字 P079</summary>

```text
                                  授課教師：葉呈祥





 STATIC_URL = 'static/'

 STATICFILES_DIRS = [ 靜態檔案目錄配置變數

    BASE_DIR / 'static', 自訂的靜態檔案資料夾名稱
基礎目錄絕對路徑變數
 ]





                             檢視→終端





                                                                                         79
```

</details>

<details>
<summary>原始文字 P080</summary>

```text
 PowerShell為了系統安全，預設會啟動嚴格的指令碼執行原則，如果想在PowerShell裡啟動
 Python的虛擬環境，常會跳出無法載入指令碼，傳統CMD不會卡權限





               比對資料模型有沒有修改，     先啟動專案的虛擬環境
呼叫 Python 執行後面的程式  並把修改的內容記錄成一份遷移檔    ..\Scripts\activate
# python manage.py makemigrations myapp (建立migration 資料檔)   myapp可以省略
                                          ，讓 Django 全
                                          面掃描整個專案# python manage.py migrate (模型與資料庫同步)
                執行遷移





# dir  把目前資料夾所有的檔案、子資料夾、建立日期以及容量大小顯示在螢幕上





                                                                                          80
```

</details>

<details>
<summary>原始文字 P081</summary>

```text
                                  授課教師：葉呈祥





                Django 的內建指令，啟動開發伺服器  0.0.0.0為開放讓區網內的其他裝置也
                             能透過你的IP連線進來觀看Ə 0 0 為#python manage.py runserver 0.0.0.0:8080
                           恦開⎆㜓 000 噆墒其他䧲⻶Ἳ䔏





                                                                                        81
```

</details>

<details>
<summary>原始文字 P082</summary>

```text
82
```

</details>

<details>
<summary>原始文字 P083</summary>

```text
                                  授課教師：葉呈祥


3-1 Django 平台建置(windows+ Visual Studio Code)

安裝 VS Code 套件

1.   Python
2.   Django
3.   Django Template





2021 Django Python 開發 VSCode 套件推薦 Top 10 [必裝]:

https://www.codecroc.com.tw/2021/09/30/2021-django-python-dev-vscode-extensi
on-recommendation-top-10-must-have/



設定環境變數：
本機 > 內容 > 進階設定 > 環境變數，在Path 變數內新增以下兩個路徑，請依
據您 Python 安裝的路徑及名稱而定：

C:\dvds
C:\dvds\Scripts





                                                                                        83
```

</details>

<details>
<summary>原始文字 P084</summary>

```text
重啟vscode 後，進入到專案，點選最下一排(左下角或右下角)python…，選擇當
前專案使用的虛擬目錄，如下：





點選「start debugging」





                                                                                          84
```

</details>

<details>
<summary>原始文字 P085</summary>

```text
                                  授課教師：葉呈祥





點選Django





                                                                                        85
```

</details>

<details>
<summary>原始文字 P086</summary>

```text
輸入網頁測試如下：





參考文獻:

https://yijay131724.blogspot.com/2021/02/python-visual-studio-code-python.html
https://dotblogs.com.tw/brian90191/2019/04/02/115926



允許非本機連線:





                                                                                          86
```

</details>

<details>
<summary>原始文字 P087</summary>

```text
授課教師：葉呈祥





                      87
```

</details>

<details>
<summary>原始文字 P088</summary>

```text
3-1 複製專案

1、複製專案並重命名test，內層也要test





2、使用vscode 開啟此專案，更改檔案內的參數名稱
在settings.py、wsgi.py、manage.py 與asgi.py 中更改名稱
結果如下:





                                                                                          88
```

</details>

<details>
<summary>原始文字 P089</summary>

```text
授課教師：葉呈祥





                      89
```

</details>

<details>
<summary>原始文字 P090</summary>

```text
2、使用取代更改名稱





                                                                                          90
```

</details>

<details>
<summary>原始文字 P091</summary>

```text
                                  授課教師：葉呈祥


3-1 Django 平台建置(Linux)


# sudo apt-get update -y

# sudo apt-get upgrade –y (先不要用)

# python3 --version (確認版本)





 建立虛擬環境

# sudo pip3 install virtualenv (安裝)

# sudo pip3 uninstall virtualenv (刪除)

# pip3 list




# virtualenv dvds

(使用virtualenv 建立虛擬環境名稱為dvds)





# source dvds/bin/activate (啟動虛擬環境)




# python --version (查看python 版本)





# deactivate(離開虛擬環境)



  Installing Django:

# pip3 install django





                                                                                        91
```

</details>

<details>
<summary>原始文字 P092</summary>

```text
# pip3 list(查詢有哪些安裝的套件)





建立專案：

# cd dvds

# django-admin startproject project1

# ls





建立應用程式：

# cd project1

# python manage.py startapp myapp

# ls





# mkdir templates



                                                                                          92
```

</details>

<details>
<summary>原始文字 P093</summary>

```text
                                  授課教師：葉呈祥


# mkdir static



修改settings.py

# vim project1/settings.py




ALLOWED_HOSTS = ['*']




INSTALLED_APPS = [

    'django.contrib.admin',

    'django.contrib.auth',

    'django.contrib.contenttypes',

    'django.contrib.sessions',

    'django.contrib.messages',

    'django.contrib.staticfiles',

    'myapp',

]





                                                                                        93
```

</details>

<details>
<summary>原始文字 P094</summary>

```text
TEMPLATES = [


    {


       'BACKEND': 'django.template.backends.django.DjangoTemplates',


       'DIRS': [BASE_DIR / 'templates'],


       'APP_DIRS': True,


       'OPTIONS': {


           'context_processors': [


               'django.template.context_processors.debug',


               'django.template.context_processors.request',


               'django.contrib.auth.context_processors.auth',


               'django.contrib.messages.context_processors.messages',


           ],


       },


    },


]





                                                                                          94
```

</details>

<details>
<summary>原始文字 P095</summary>

```text
                                  授課教師：葉呈祥


LANGUAGE_CODE = 'zh-Hant'

TIME_ZONE = 'Asia/Taipei'





STATIC_URL = 'static/'

STATICFILES_DIRS = [

    BASE_DIR / 'static',

]





                                                                                        95
```

</details>

<details>
<summary>原始文字 P096</summary>

```text
# python manage.py makemigrations myapp (建立migration 資料檔)

# python manage.py migrate (模型與資料庫同步)





# ls





# python manage.py runserver 0.0.0.0:8080





                                                                                          96
```

</details>

<details>
<summary>原始文字 P097</summary>

```text
                                  授課教師：葉呈祥





參考文獻:

https://mikesmithers.wordpress.com/2017/02/21/configuring-django-with-apache-o
n-a-raspberry-pi/


https://www.cnblogs.com/baby123/p/12122703.html





                                                                                        97
```

</details>

<details>
<summary>原始文字 P098</summary>

```text
https://developer.mozilla.org/zh-TW/docs/Learn/Server-side/Django/skeleton_websi

te
Django 中直接使用sql 语句 操作数据库

https://blog.csdn.net/haeasringnar/article/details/82080476


https://openhome.cc/Gossip/CodeData/PythonTutorial/AppModelPy3.html


在 Django 使用 MySQL 資料庫

https://jerrynest.io/django-mysql-database/



3-1 Django 平台建置(Linux+ Visual Studio Code+Remote

Development)

1、安裝Remote- Development
2、建立連結





                                                                                          98
```

</details>

<details>
<summary>原始文字 P099</summary>

```text
                                  授課教師：葉呈祥





已連結如下圖





or 若未連結，則按「connect in current window」





                                                                                        99
```

</details>

<details>
<summary>原始文字 P100</summary>

```text
                                       or



注意:指定到/home/pi/dvds/，不要指定到專案之下/home/pi/dvds/projectName/





若已安裝資料夾連結，則由下圖操作





                                                                                          100
```

</details>

<details>
<summary>原始文字 P101</summary>

```text
                                  授課教師：葉呈祥





2、安裝python 套件:





                                                                                        101
```

</details>

<details>
<summary>原始文字 P102</summary>

```text
修正參數





                                                                                          102
```

</details>

<details>
<summary>原始文字 P103</summary>

```text
                                  授課教師：葉呈祥





若要重來，或改變專案，可以刪除或修正下圖參數





                                                                                        103
```

</details>

<details>
<summary>原始文字 P104</summary>

```text
104
```

</details>

<details>
<summary>原始文字 P105</summary>

```text
                                  授課教師：葉呈祥





注意:若連線有問題，請將windows 系統中，c:\使用者\user\.ssh 內的資料刪除





                                                                                        105
```

</details>

<details>
<summary>原始文字 P106</summary>

```text
3-2 建立Django 專案

  建立Django 專案:

# cd ~/dvds

# source ./dvds/dvdsenv/bin/activate (啟動虛擬環境)

# django-admin startproject project1 (建立project1 專案)

# cd project1





# tree





檔案或目錄    說明

manage.py        Python 命令檔，提供專案管理的功能，包含建立app、

             啟動Server 和Shell 等

__init__.py    一個空檔，使得該目錄成為一個Python package

settings.py   本專案的設定檔

urls.py          url 配置檔

wsgi.py       網頁伺服器和Django 的介面設定檔 (托管)


3-3 建立Application 應用程式

Application 應用程式相當於Project 專案的元件，簡稱為app, 而且是可以當作其
他專案的模組，每個Project 專案可以建立一個或多個Application 應用程式。


 建立應用程式




                                                                                          106
```

</details>

<details>
<summary>原始文字 P107</summary>

```text
                                  授課教師：葉呈祥


# sudo python3 manage.py startapp myapp (pyhton3)

# sudo python manage.py startapp myapp (pyhton2)



  建立templates 資料夾與static 資料夾

Diango 是使用MTV 的架構，將顯示的模版(.html)，放置templates 資料夾中，

其中資料夾須在專案的最上層目錄下建立。將使用的圖形、CSS、JavaScript

檔案，常以本機的方式儲存在static 資料夾中，其中資料夾須在專案的最上層

目錄下建立。




# mkdir templates static





# tree





 除錯模式設定與權限瀏覽

# vim project1/settings.py

其中，「*」是指全部ip





                                                                                        107
```

</details>

<details>
<summary>原始文字 P108</summary>

```text
add the original IP and/or hostname also:





  加入Application 應用程式:





  設定Template 路徑:

Django 是使用MTV 架構，將顯示的模版放置在templates 資料夾中，因此要

在TEMPATES 的DIRS 鍵中設定其路徑。

輸入前新增「import os」





                                                                                          108
```

</details>

<details>
<summary>原始文字 P109</summary>

```text
                                  授課教師：葉呈祥




 設定語系與時區:

# sudo vim project1/settings.py





  設定static 靜態檔的路徑:

# sudo vim project1/settings.py

STATIC_URL = 'static/'

    STATICFILES_DIRS = [

       BASE_DIR / 'static',

]





  建立migration 資料檔:

Diango 要使用資料庫，通常會將建立資料表的架構和版本記錄下來，以利以後

的追蹤。




# sudo python3 ./manage.py makemigrations (python3)

# sudo python ./manage.py makemigrations (python2)





                                                                                        109
```

</details>

<details>
<summary>原始文字 P110</summary>

```text
 模型與資料庫同步

# sudo python3 ./manage.py migrate (python3)

# sudo python ./manage.py migrate (python2)





# tree





                                                                                          110
```

</details>

<details>
<summary>原始文字 P111</summary>

```text
                                  授課教師：葉呈祥





  啟動Server

# sudo python3 manage.py runserver 0.0.0.0:8080





                                                                                        111
```

</details>

<details>
<summary>原始文字 P112</summary>

```text
3-4 視圖(view)與url

  Diango 的Framework 架構

MVC(Model-view-controller):
基本部分：模型（Model）、視圖（View）和控制器（Controller）。

         送出                儲存資料
 表單 View

                       Controller      Model                       資料庫

 表單 View
         顯示                讀取資料


模型（Model）：代表商業邏輯與資料庫存取有關的程式。
視圖（View）：代表輸入和輸出畫面的呈現。
控制器（Controller）：介於Model 及View 之間，判斷該呼叫哪一個Model 存取
資料庫並透過。


MVT(Model-view-template):
基本部分：模型（Model）、視圖（View）和模版（Template）。

                           儲存資料
        送出
  表單

                     View        Model   Template                  資料庫

  表單

        顯示                讀取資料


模型（Model）：代表商業邏輯與資料庫存取有關的程式。
視圖（View）：處理Model 存取資料庫和Template 介面資料的輸入或顯示。
模版（Template）：代表介面輸入表單或顯示資料。


MVC VS MVT
任務               MVC 架構            MTV
資料庫存取          M=Model=模型        M=Model=模型
輸入表單或顯示資料    V=View=視圖           T=Template=模版
控制與整合             C=Controller=控制      V=View=視圖





                                                                                          112
```

</details>

<details>
<summary>原始文字 P113</summary>

```text
                                  授課教師：葉呈祥





參考文獻:

https://blog.csdn.net/u014745194/article/details/73718041





                                                                                        113
```

</details>

<details>
<summary>原始文字 P114</summary>

```text
  設定urls.py

Django 的程式架構是採用urlpattern 網址和函式對照方式，主要有兩個步驟:
1、設定<url.py>檔urlpatterns 串列中url 網址和函式的對照。
2、在<views.py>中撰寫函式。


url 中可以傳遞任意數量的參數給 view 中對應的函式，參數型別為字典，且前
後必須加上 <> 字元，傳遞的參數會自動作型別轉換。
傳遞參數型別：
    str：字串，匹配任何非空字符串，但不含「/」字元，這是預設值。
     int：匹配 0 及正整數，傳回一個 int 型別。
     slug：匹配字母、數字以及 /、 組成的字串，是 url 在最後一部分的註
    釋文字。
     uuid：匹配格式化的 uuid，為了防止衝突，規定必須使用「-」字元，
    所有字母必須小寫。如 075194d3-6885-417e-a8a8-6c931e272f00。它會
    傳回一個 UUID 物件。
    path：匹配任何非空字符串，包含路徑分隔符號「/」


參考文獻:

http://blog.e-happy.com.tw/django2-0-%E4%BB%A5-path-%E5%87%BD%E5%BC%8F
%E8%A8%AD%E5%AE%9A-urlpatterns/




# sudo vim project1/urls.py





其中表示瀏覽「127.0.0.1:8000/admin/ 」這個網址，將會執行

admin.site.urls 函式，因為admin.site.urls 函式在django.contrib 模

組中的admin 中，因此必須import 進來。

url 語法: path(網址,函式)





                                                                                          114
```

</details>

<details>
<summary>原始文字 P115</summary>

```text
                                  授課教師：葉呈祥




 定義函式：

# sudo vim myapp/views.py





# sudo python3 manage.py runserver 0.0.0.0:8080





ex:

path(‘hello/<str:name>/’,hello)

即瀏覽「127.0.0.1/hello/david/」這個網址，就會執行hello 函式，並且

傳送「david」參數值給hello 函式。




# sudo vim project1/urls.py





定義函式：





                                                                                        115
```

</details>

<details>
<summary>原始文字 P116</summary>

```text
# sudo vim myapp/views.py





測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8080





 模版的使用

# vim templates/hello2.html





# sudo vim project1/urls.py





                                                                                          116
```

</details>

<details>
<summary>原始文字 P117</summary>

```text
                                  授課教師：葉呈祥





# sudo vim myapp/views.py





測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8080





  加入static 靜態檔案


在static 加入檔案





                                                                                        117
```

</details>

<details>
<summary>原始文字 P118</summary>

```text
# vim project1/settings.py

加入





# sudo vim project1/urls.py





# sudo vim myapp/views.py





# vim templates/hello3.html





                                                                                          118
```

</details>

<details>
<summary>原始文字 P119</summary>

```text
                                  授課教師：葉呈祥





注意:必須在.html 檔中以檔案中，以{% load staticfiles %}宣告使用靜態

檔案，同時以{% static 靜態檔案 %}格式設定靜態檔案的路徑。

注意:若是windows 請將{% load staticfiles %}改成{% load static %}



測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8080





 從網址中載取資料

ex:




                                                                                        119
```

</details>

<details>
<summary>原始文字 P120</summary>

```text
path(‘hello/<str:name1>/<str:name2>/’, function)

path(‘hello/<str:name1>/hello/’, function)


# sudo vim project1/urls.py





# sudo vim myapp/views.py





測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8080





                                                                                          120
```

</details>

<details>
<summary>原始文字 P121</summary>

```text
授課教師：葉呈祥





                      121
```

</details>

<details>
<summary>原始文字 P122</summary>

```text
3-5 視圖、模版與Template 語言

  傳遞變數到Template 模板檔案
使用render 函式，必須import 該模組，系統預設已經以from django.shortcuts
import render 加入模組，因此可以直接使用render 函式。


render 的語法如下：

render(request, template_name, locals())
第一個參數:HttpRequest 物件
第二個參數:模板名稱
第三個參數:傳遞所有區域變數給顯示的模版


no=1
dict1={“name”:”Amy”, ”age”:20}
return render(request, “dice.html”, locals())
or
return render(request, “dice.html”, {“no”:1, “dict1”: {“name”:”Amy”, ”age”:20} })


經過locals()函式轉換後會建立{“no”:1, “dict1”: {“name”:”Amy”, ”age”:20} }


 模版顯示變數
由於locals()將所有區域變數轉換成字典，在模版中要顯示locals()字典的內容，
就可以讀取字典的語法來讀取它。


no=1 已由locals()轉換為{“no”:1}

{{ no }}


若是字典的變數，語法如下:
{{ 字典變數.鍵  }}

{{  dict1.name }}



# sudo vim project1/urls.py





                                                                                          122
```

</details>

<details>
<summary>原始文字 P123</summary>

```text
                                  授課教師：葉呈祥





# sudo vim myapp/views.py





# vim templates/dice1.html





測試結果：



                                                                                        123
```

</details>

<details>
<summary>原始文字 P124</summary>

```text
# sudo python3 manage.py runserver 0.0.0.0:8080





3-6 模板(Template)語言-變量

Template 模板有自己的語言，可以顯示變數，同時也有if 條件指令和for 迴圈指
令，也可以加上註解。
名稱    說明               範例

變量      將views 傳送內容顯示在模版指定的   {{ username }}
      位置上。
標籤              If 條件指令和for 迴圈指令。         {% if  found %}
                                             {% for item in items %}
多行註解  語法:                    語法:

           {% comment %}                     {% comment %}
      註解文字一            註解文字一
      註解文字二            註解文字二

           {% endcomment %}                  {% endcomment %}
單行註解   語法:{# 註解文字 #}                    {# 這是註解文字#}
文字      HTML 標籤或文字                  <title>顯示的模板</title>


 變量

變量就是要顯示的變數，變數可是一般的變數，也可以使用字典或串列，分別以
「{{ 變數 }}」、「{{ 變數變數.鍵 }}」、「{{ 串列.索引 }}」語法來表示。


變量類型  Template 語法    Python 語法  說明

字典        {{dict1.name}}     dict1[name]     name 是字典的鍵
方法        {{obj1.show}}      obj1.show       show()是obj1 物件方法
串列         {{list1.0}}             list1[0]              list1 是串列，例如：
                                                     list1=[“a”,”b”,”c”]。





                                                                                          124
```

</details>

<details>
<summary>原始文字 P125</summary>

```text
                                  授課教師：葉呈祥





# sudo vim project1/urls.py





# sudo vim myapp/views.py





# vim templates/dice2.html





測試結果：





                                                                                        125
```

</details>

<details>
<summary>原始文字 P126</summary>

```text
# sudo python3 manage.py runserver 0.0.0.0:8080





3-7 模板(Template)語言-標籤

      Operators





Reference:

https://www.w3schools.com/django/ref_tags_if.php



    條件指令

{%  if 條件  %}

 程式區塊





                                                                                          126
```

</details>

<details>
<summary>原始文字 P127</summary>

```text
                                  授課教師：葉呈祥


{%  endif  %}




EX:

{%  if score >=60  %}

 及格

{%  endif  %}



{%  if 條件  %}

 程式區塊一

{%  else  %}

 程式區塊二

{%  endif  %}




EX:

{%  if score>=60  %}

 及格

{%  else  %}

 不及格

{%  endif  %}





{%  if 條件一  %}

 程式區塊一

{%  elif 條件二  %}

 程式區塊二





                                                                                        127
```

</details>

<details>
<summary>原始文字 P128</summary>

```text
{%  elif 條件三  %}

 程式區塊三

{%  else  %}

 程式區塊四

{%  endif  %}



EX:

{%  if score>= 90  %}

 優等

{%  elseif score>= 80  %}

 甲等

{%  elseif score>= 70  %}

 乙等

{%  else  %}

 丙等

{%  endif  %}





                                                                                          128
```

</details>

<details>
<summary>原始文字 P129</summary>

```text
                                  授課教師：葉呈祥





Rerence:
https://www.w3schools.com/django/django_tags_if.php


      for 迴圈指令


{% for 變數  in 串列  %}

程式區塊

{%  endfor  %}




EX:

list1 = range(1,6)

{% for  i  in  list1  %}

{{ i }}

{%  endfor  %}


forloop 屬性     說明
forloop.counter     由1 開始遞增到疊代總數。
forloop.counter0    由0 開始遞增到疊代總數。
forloop.revcounter   由串列元素總教開始遞減到1。
forloop.revcounter0  由串列元素總教開始遞減到0。
forloop.first       判斷是否第一次for 迴圈，其值為True 或False





                                                                                        129
```

</details>

<details>
<summary>原始文字 P130</summary>

```text
forloop.last       判斷是否最後一次for 迴圈，其值為True 或False
forloop.parentloop    父迴圈(上一層迴圈)的forloop




# sudo vim project1/urls.py





# sudo vim myapp/views.py





# vim templates/dice3.html





                                                                                          130
```

</details>

<details>
<summary>原始文字 P131</summary>

```text
                                  授課教師：葉呈祥





測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8080





Reference:
https://www.w3schools.com/django/django_tags_for.php





                                                                                        131
```

</details>

<details>
<summary>原始文字 P132</summary>

```text
3-8 以GET 及POST 傳送資料

網頁最常用來傳送資料的方式就是GET 及POST。HTTP Method：表單中的 GET
與 POST 有什麼差別？先舉個例子，如果 HTTP 代表現在我們現實生活中寄信
的機制，那麼信封的撰寫格式就是 HTTP。我們姑且將信封外的內容稱為
http-header，信封內的書信稱為 message-body，那麼 HTTP Method 就是你要告
訴郵差的寄信規則。
假設 GET 表示信封內不得裝信件的寄送方式，如同是明信片一樣，你可以把要
傳遞的資訊寫在信封(http-header)上，寫滿為止，價格比較便宜，但看的到不安
全。
然而 POST 就是信封內有裝信件的寄送方式（信封有內容物），不但信封可以寫
東西，信封內 (message-body) 還可以置入你想要寄送的資料或檔案，價格較貴，
包在裡面安全看不到。
使用 GET 的時候我們直接將要傳送的資料以 Query String（一種Key/Vaule 的
編碼方式）加在我們要寄送的地址(URL)後面，然後交給郵差傳送。使用 POST 的
時候則是將寄送地址(URL)寫在信封上，另外將要傳送的資料寫在另一張信紙後，
將信紙放到信封裡面，交給郵差傳送(message-body)。


接著我來介紹一下實際的運作情況：
我們先來看看 GET 怎麼傳送資料的，當我們送出一個 GET 表單時，如下範
例：





當表單 Submit 之後瀏覽器的網址就變成 "http://xxx.toright.com/?id=010101"，瀏
覽器會自動將表單內容轉為 Query String 加在 URL 進行連線。


當使用GET 的方法時，會將表單資訊附加在URL 上並作為QueryString 的一部
分，QueryString 是一種key/value 的組合，從問號「?」開始，每一組值都是用「&」
隔開，如下圖





這時後來看一下 HTTP Request 封包的內容：





                                                                                          132
```

</details>

<details>
<summary>原始文字 P133</summary>

```text
                                  授課教師：葉呈祥





  在 HTTP GET Method 中是不允許在 message-body 中傳遞資料的，因為是
GET 就是要取資料的意思。從瀏覽器的網址列就可以看見我們表單要傳送的資
料，若是要傳送密碼豈不是"一覽無遺".......這就是大家常提到安全性問題。


再來看看 POST 傳送資料





網址列沒有變化，那我們來看一下 HTTP Request 封包的內容：





看出個所以然了嗎？原來 POST 是將表單資料放在 message-body 進行傳送，
在不偷看封包的情況下似乎安全一些些。此外在傳送檔案的時候會使用到
multi-part 編碼，將檔案與其他的表單欄位一併放在 message-body 中進行傳送。
這就是 GET 與 POST 發送表單的差異。





                                                                                        133
```

</details>

<details>
<summary>原始文字 P134</summary>

```text
     以GET 傳送資料
以GET 傳送參數值的語法:
網路?參數1=值1 & 參數2=值2&參數3=值3

Ex:
http://127.0.0.1:5000/test?name=bill&tel=092322423


Django 使用request 模組的GET 方法即可取得GET 參數值，語法為：
request.GET[‘參數名稱’]


Django 使用request 模組的POST 方法即可取得POST 參數值，語法為：
request.POST[‘參數名稱’]


    使用GET 傳遞參數(有參數)

# sudo vim project1/urls.py





# sudo vim myapp/views.py





                                                                                          134
```

</details>

<details>
<summary>原始文字 P135</summary>

```text
                                  授課教師：葉呈祥





# sudo vim templates/get1.html





測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8000





    使用GET 傳遞參數(有參數與無參數)

# sudo vim project1/urls.py





                                                                                        135
```

</details>

<details>
<summary>原始文字 P136</summary>

```text
# sudo vim myapp/views.py





# sudo vim templates/get2.html





                                                                                          136
```

</details>

<details>
<summary>原始文字 P137</summary>

```text
                                  授課教師：葉呈祥





測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8000





    使用GET 傳遞參數(使用表單)





                                                                                        137
```

</details>

<details>
<summary>原始文字 P138</summary>

```text
# sudo vim project1/urls.py





# sudo vim myapp/views.py





# sudo vim templates/get3.html





                                                                                          138
```

</details>

<details>
<summary>原始文字 P139</summary>

```text
                                  授課教師：葉呈祥


# sudo vim templates/get3_response.html





測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8000





                                                                                        139
```

</details>

<details>
<summary>原始文字 P140</summary>

```text
     使用POST 傳遞參數(使用表單，單選題)

# sudo vim project1/urls.py





# sudo vim myapp/views.py





# sudo vim templates/post1.html





                                                                                          140
```

</details>

<details>
<summary>原始文字 P141</summary>

```text
                                  授課教師：葉呈祥





其中「{% csrf_token %}」是加入CSRF 驗證，在Django 中所有以POST 方式

送出資料的表單，都要加入「{% csrf_token %}」以增加安全性，如果沒有加

入，在送出表單時會產生錯誤如下:





# sudo vim templates/post1_response.html





                                                                                        141
```

</details>

<details>
<summary>原始文字 P142</summary>

```text
測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8000





                                                                                          142
```

</details>

<details>
<summary>原始文字 P143</summary>

```text
                                  授課教師：葉呈祥





     使用POST 傳遞參數(使用表單，複選題)

補充(表單使用post 傳送，複選題):

sudo vim project1/urls.py





# sudo vim myapp/views.py





# sudo vim templates/post2.html





                                                                                        143
```

</details>

<details>
<summary>原始文字 P144</summary>

```text
其中「{% csrf_token %}」是加入CSRF 驗證，在Django 中所有以POST 方式

送出資料的表單，都要加入「{% csrf_token %}」以增加安全性，如果沒有加

入，在送出表單時會產生錯誤如下:





# sudo vim templates/post2_response.html





                                                                                          144
```

</details>

<details>
<summary>原始文字 P145</summary>

```text
                                  授課教師：葉呈祥





測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8000





                                                                                        145
```

</details>

<details>
<summary>原始文字 P146</summary>

```text
3-9 Django 資料庫連結與應用(使用MariaDB)

 安裝MariaDB


# sudo  apt  update

# apt-cache  search  mysql-server





# sudo  apt-get  install  mariadb-server

# sudo  systemctl  status  mariadb.service


 解決MariaDB(10.5.12)本地無密碼直接登錄的問題

在Debian11 中安裝了MariaDB，版本號為10.5.12，安裝後輸入mysql 不需要密
碼便可直接登錄。

# sudo  mysql  -u  root  -p

-> use  mysql;

-> SELECT  *  FROM  global_priv;

(root 用戶默認是unix_socker 類型，)

-> ALTER USER root@localhost IDENTIFIED VIA mysql_native_password

USING PASSWORD("password");

->flush privileges;

(刷新權限)

->exit


Reference:
https://blog.csdn.net/csgd2000/article/details/82751606



  Setting MySQL/MariaDB root password





                                                                                          146
```

</details>

<details>
<summary>原始文字 P147</summary>

```text
                                  授課教師：葉呈祥


# sudo  mysql_secure_installation




You already have your root account protected, so you can safely

answer 'n'.

Switch to unix_socket authentication [Y/n]

n





其中：

依照提示輸入 root 的密碼 Change the root password? [Y/n]

移除匿名使用者  Remove anonymous users? [Y/n]

不允許 root 遠端登入 Disallow root login remotely? [Y/n]

移除 test 資料庫及存取權 Remove test database and access to it?

[Y/n]

重新載入權限的資料表  Reload privilege tables now? [Y/n]




# sudo  mysql  -u  root  -p

or

# sudo  mysql  -uroot  -p1qaz@wsx




                                                                                        147
```

</details>

<details>
<summary>原始文字 P148</summary>

```text
參考文獻:

https://websiteforstudents.com/mariadb-installed-without-password-prompts-for-ro
ot-on-ubuntu-17-10-18-04-beta/


 MySQL 開啟遠端連線權限允許遠端裝置連線資料庫


查看目前MySQL 所監聽的連接埠：

# sudo netstat -tlnp | grep mariadb

(netstat 指令可以顯示出網路連線、路由表、介面統計、偽裝連線和多播成員

的資訊。-l 參數可以只顯示正在監聽中的連線。若使用netstat 指令時都沒給

任何參數的話，會忽略掉監聽中的連線。-t 參數可以只顯示TCP 連線。-n 參數

可以讓IP 可以直接被輸出，而不需透過DNS 反查其對應的網域名稱。-p 參數可

以顯示佔用連線的行程。)



讓MySQL 監聽其它網路介面：

MySQL 的主設定檔路徑為/etc/mysql/my.cnf 或是/etc/my.cnf 內，在設定檔

中可能會看到其又引入了其它設定檔。

# sudo  vim  /etc/mysql/my.cnf





                                                                                          148
```

</details>

<details>
<summary>原始文字 P149</summary>

```text
                                  授課教師：葉呈祥





# ls  /etc/mysql/mariadb.conf.d/





# sudo  vim  /etc/mysql/mariadb.conf.d/50-server.cnf





                                                                                        149
```

</details>

<details>
<summary>原始文字 P150</summary>

```text
如果要綁定所有網路介面，那就把bind-address 欄位值設成0.0.0.0 吧！如

果要綁定多個網路介面，也是設成0.0.0.0，再用防火牆去擋住其它不需要用到

的網路介面。




# sudo  systemctl  restart  mysql

# sudo  netstat  -tlnp  |  grep  mariadbd





第一種方法：

MySQL 因為安全性root 帳號，預設只允許localhost 連線，想要遠端裝置連

線本地端的資料庫，需要設置帳號權限修改為所有host 均可訪問：

# update user set host = '%' where user = 'root';

(以上是直接修改root 權限的做法)，



第二種方法：

此方法較第一種好，新增一個使用者，給予hoot 均可訪問的權限'％'，或使指

定只能訪問指定某資料庫權限：

MySQL 創建一個新用戶：

# mysql -u root -p

mysql> CREATE USER admin IDENTIFIED BY 'password';

(建立使用者名稱及密碼)

admin 表示使用者帳號為admin，若後面有加入'admin'@'localhost'表示只

能localhost 本端連入，所以我們需要所有hoot 均可訪問權限的設置'％'，

這邊只需要填入帳號名稱即可'admin'




mysql> GRANT  ALL  PRIVILEGES  ON  *.*  TO  'admin';



                                                                                          150
```

</details>

<details>
<summary>原始文字 P151</summary>

```text
                                  授課教師：葉呈祥


(給定使用者存取權限，*.*為所有使用權限)




mysql> GRANT  ALL  PRIVILEGES  ON  database_name.*  TO  'admin';

(可針對資料庫database_name.*如下：只能訪問database_name 這個資料庫)




mysql> FLUSH PRIVILEGES;

(重新載入使用者權限設定)




=========================================

補充指令:

mysql> SELECT User FROM mysql.user;

(查詢資料庫使用者)

mysql> SELECT User, Host FROM mysql.user;

(查詢資料庫使用者與來源主機)

mysql> DROP USER 'admin';

(刪除使用者)



修改一般使用者密碼：

# mysql -uroot –p1qaz@wsx

# SET PASSWORD FOR 'admin'@'localhost' = PASSWORD('password');

(本機使用者)

# SET PASSWORD FOR 'admin' = PASSWORD('password');

(使用者可連遠端)




# flush privileges;





                                                                                        151
```

</details>

<details>
<summary>原始文字 P152</summary>

```text
匯入資料庫:

# mysql  -u  root  -p  class < students.sql

Enter password




# sudo  mysql  -u  root  -p

# CREATE DATABASE myproject CHARACTER SET UTF8;

# show databases;





參考文獻:

https://www.ucamc.com/articles/430-mysql
https://stackoverflow.com/questions/62564439/mysql-mariadb-server-raspberry-pi-r

emote-access
https://magiclen.org/mysql-remote/
https://emn178.pixnet.net/blog/post/87659567
https://www.dotblogs.com.tw/CodeBrewTea/2022/02/15/150432



 使用Wordbench 開啟MariaDB 資料庫





                                                                                          152
```

</details>

<details>
<summary>原始文字 P153</summary>

```text
                                  授課教師：葉呈祥





 How to Reset MySQL/MariaDB Database Root Password?

# sudo  systemctl  stop  mariadb




# sudo  mysqld_safe  --skip-grant-tables  --skip-networking  &




按enter




# sudo  mysql  -u  root





                                                                                        153
```

</details>

<details>
<summary>原始文字 P154</summary>

```text
# FLUSH  PRIVILEGES;

(重新載入使用者權限設定)

# ALTER  USER  'root'@'localhost'  IDENTIFIED  BY '1234';

# exit

# sudo  mysql  -u  root  -p


  安裝mysqlclient 與設定Django 參數

  安裝mysql 與設定Django 參數

Windows:

# pip install mysqlclient (Windows)




Linux:

# sudo apt-get install python3-dev default-libmysqlclient-dev

build-essential # Debian / Ubuntu




# sudo yum install python3-devel mysql-devel # Red Hat / CentOS




Then you can install mysqlclient via pip now:

# pip install mysqlclient



Refenrce:

https://pypi.org/project/mysqlclient/





                                                                                          154
```

</details>

<details>
<summary>原始文字 P155</summary>

```text
                                  授課教師：葉呈祥





 資料庫設定類型

sqlite3 vs MySQL vs PostgreSQL

在專案中建立第一個 App 時會在第一層專案目錄下產生預設的空白 SQLite

資料庫檔案 db.sqlite3，此資料庫優點是備份方便 (非伺服器型之單一檔案)

且與 MySQL 相容，適合測試開發或小型專案使用，但在擴充性與效能上較不

足，實際佈署營運時通常改用 MySQL 或 PostgreSQL 等資料庫 (Django 社群

較偏愛 PostgreSQL，例如免費主機 Heroku 支援 PostgreSQL)。

Django 採用 ORM 架構，因此只要修改資料庫設定，不需修改應用程式。




# vim project1/settings.py

使用SQLite 資料庫時，設定語法如下：

DATABASES = {

    'default': {

       'ENGINE': 'django.db.backends.sqlite3',

       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

    }





                                                                                        155
```

</details>

<details>
<summary>原始文字 P156</summary>

```text
使用MySQL 資料庫時，設定語法如下：

DATABASES = {

    'default': {

       'ENGINE': 'django.db.backends.mysql',

       'NAME': 'myproject',

       'USER': 'tony',

       'PASSWORD': '1qaz2wsx',

       'HOST': 'localhost',

       'PORT': '3306',

       'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",

       'charset': 'utf8mb4',

    }

}





使用Postgree 資料庫時，設定語法如下：

DATABASES = {

    'default': {

       'ENGINE': 'django.db.backends.postgresql_psycopg2',

       'NAME': 'myproject',

       'USER': 'tony',

       'PASSWORD': '1qaz2wsx',




                                                                                          156
```

</details>

<details>
<summary>原始文字 P157</summary>

```text
                                  授課教師：葉呈祥


       'HOST': 'localhost',

       'PORT': '5432',

    }



# sudo python3 manage.py makemigrations

(建立資料庫和Django 間的中介檔)(生成表結構的快取)

# sudo python3 manage.py migrate

(同步更新資料庫內容)(建立表結構)



# source ./dvdsenv/bin/activate (啟動虛擬環境)

# cd project1/

# vim project1/settings.py (確認myapp 加入)





  建立student 資料模型

# sudo vim myapp/models.py





from django.db import models

class student(models.Model):

                  cName = models.CharField(max_length=20, null=False)

                  cSex = models.CharField(max_length=2, default='M', null=False)





                                                                                        157
```

</details>

<details>
<summary>原始文字 P158</summary>

```text
                  cBirthday = models.DateField(null=False)

                  cEmail = models.EmailField(max_length=100, blank=True, default='')

                  cPhone = models.CharField(max_length=50, blank=True, default='')

                  cAddr = models.CharField(max_length=255,blank=True, default='')


預設已匯入 django.db.models 模組, 定義資料表結構 (資料模型) 只要加入下
列一個部份即可  :
繼承 models.Model 類別定義一個資料模型子類別 (即資料表)


Django 所有的資料模型都繼承自 django.db.models.Model 類別, 每一個繼承
Model 的子類別相當於是資料表  (table); 其實體 (物件) 對應到一筆紀錄 (row
或 record); 物件的屬性則對應到資料欄位 (fields)，而物件方法則對應到資料庫
的 CRUD 操作，如下表所示  :





  Field Type 欄位型別


欄位格式      參數             說明

BooleanField                                     True 或False 用於checkbox 輸入資料

CharField        max_length:最大字串長度   用於單行輸入字串資料

SlugField                           與CharField()相同，但用來儲存URL

                         的一部分

TextField                      多行輸入字串資料，用於HTML 表單的

                                                 textarea 欄位

IntegerField                      整數:

                                                 -2147483648~2147483647

BigInteger()                   儲存長度 64 位元的大整數

PositiveIntegerFi                   儲存正整數(0 ~ 2147483647)

eld()

DecimalField()    max_digits=最大位數     儲存固定精度之十進位數  (Decimal

                decimal_places=整數位數    物件)

FloatField()                   儲存浮點數

DateField()      auto_now=自動儲存今日日期  儲存日期，格式 datetime.date。

              auto_now_add=只在建立時儲存




                                                                                          158
```

</details>

<details>
<summary>原始文字 P159</summary>

```text
                                  授課教師：葉呈祥


          今日日期

DateTimeField()   auto_now=自動儲存今日日期時 儲 存 日 期 時 間 ， 格 式

          間                          datetime.datetime。

              auto_now_add=只在建立時儲存

          今日日期時間

EmailField()     max_length=最大字元數(上限 儲存有效之電子郵件

                   254)

FileField()                   檔案上傳欄位

ImageField()                        圖檔欄位(繼承自FileField，須配合使

                         用 Pillow 套件)

URLField()       max_length=最大字元數(預設 儲存完整的URL (繼承自 CharField)

                   200)

AutoField()         primary_key=True       自動增量主鍵欄位

ForeignKey()    第一參數=          關聯欄位，用來指向其他資料表的主鍵

          所指之資料表類別名         (預設=id)

           第二參數:

                    on_delete=models.CASCADE


參考文獻：

https://developer.mozilla.org/zh-TW/docs/Learn/Server-side/Django/Models


最後的兩個方法  AutoField() 與  ForeignKey() 所定義的欄位比較特殊，其中
AutoField()用來設定自動增量主鍵(primary_key)欄位，其實 Django 會自動為每一
個資料表添加一個主鍵欄位id，但若想自行指定主鍵欄位可以使用 AutoField()
方法。


ForeignKey()欄位則是用來關聯到其他資料表(稱為外部鍵)，此欄位的第一參數所
關聯之資料表類別名稱，用來指向該資料表的主鍵，Django 預設會自動將其關聯
到該資料表之  id 主鍵，例如上面的 users 資料表中可以添加一個 nationality
(國籍) 欄位指向另一個資料表 nations :


nationality=models.ForeignKey(nations, on_delete=models.CASCADE)





                                                                                        159
```

</details>

<details>
<summary>原始文字 P160</summary>

```text
ForeignKey()的第二參數用來設定當被參照的外部鍵被刪除時參照者應採取之動
作，Django 的 models 套件定義了如下常用之屬性值:
  models.CASCADE：同步執行刪除動作
  models.PROTECT：不刪除且拋出一個ProtectedError 例外
  models.SET_NULL：將此外部鍵設為null (須先以null=True 參數定義此欄位)
  models.SET_DEFAULT：將此外部鍵設為預設值 (須先以default 參數定義此欄
  位預設值)
  models.DO_NOTHING ：不採取動作


參考文獻：

https://docs.djangoproject.com/en/3.1/topics/db/models/#automatic-primary-key-fi

elds


  Field Option 欄位選項

呼叫欄位型態函數時除了必要參數外, 還可以傳入選項參數, 常用選項參數如下
表：

欄位選項       說明
null               欄位值是否可為null，值=True/False(預設)
blank             欄位值是否可為空白，值=True/False(預設)
default         欄位預設值(或可呼叫物件)
unique            欄位值是否為唯一，值=True/False(預設)
primary_key         欄位是否為主鍵，值=True/False(預設)
editable          欄位是否顯示於admin 後台，值=True(預設)/False
choices               設定select 欄位之選項(可用list 或tuple)
help_text        顯示於表單元件上的額外資訊
verbose_name      欄位之人類可讀名稱，未指定以欄位名稱代替(底線變
              空白)




                                                                                          160
```

</details>

<details>
<summary>原始文字 P161</summary>

```text
                                  授課教師：葉呈祥


補充:
使用blank=True(允許空值)，會設定null=True(欄位內容允許null)
空值=>白紙; null=>沒有東西


參考文獻：

https://docs.djangoproject.com/en/3.1/ref/models/fields/
https://sites.google.com/site/djangonote/basic/models/field-type


補充(要使用ORM 寫法才有效果):





Reference:
https://blog.csdn.net/kuanggudejimo/article/details/99291026





                                                                                        161
```

</details>

<details>
<summary>原始文字 P162</summary>

```text
參考文獻：

https://www.techiediaries.com/django/django-3-tutorial-and-crud-example-with-my
sql-and-bootstrap/
https://www.jianshu.com/p/02732229fe59
https://djangogirlstaipei.gitbooks.io/django-girls-taipei-tutorial/content/django/mod
els.html
https://my.oschina.net/yimingkeji/blog/2873227
https://www.jianshu.com/p/bc41a8bf9d9b





                                                                                          162
```

</details>

<details>
<summary>原始文字 P163</summary>

```text
                                  授課教師：葉呈祥


3-11 資料庫新增、刪除、修改與查詢(使用SQL 語法)

   CRUD 指的是，Create (新增)、Read (讀取)、Update (修改)、Delete (刪除) 等
常見的資料庫操作。
    Executing custom SQL directly 有時候 Manager.raw() 是不夠的，像是你可能
需要 queries 沒有完全 map 到 models 的資料，或是執行 UPDATE, INSERT, or
DELETE。當我們使用這個方法時，是完全的繞過 model，直接 access database。
你可以通過匯入django.db.connection 對像來輕鬆實現，它代表當前資料庫連線。
要使用它，需要通過connection.cursor()得到一個遊標對像。
參考文獻:

https://docs.djangoproject.com/en/3.2/topics/db/sql/

https://docs.djangoproject.com/zh-hans/4.2/topics/db/sql/
https://github.com/twtrubiks/django-rest-framework-tutorial



  設定Django 連mysql 的參數

# vim project2/settings.py

DATABASES = {

    'default': {

       #'ENGINE': 'django.db.backends.sqlite3',

       #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

       'ENGINE': 'django.db.backends.mysql',

       'NAME': 'myproject',

       'USER': 'tony',

       'PASSWORD': '1qaz2wsx',

       'HOST': 'localhost',

       'PORT': '3306',

       'OPTIONS':{

           'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",

           'charset': 'utf8mb4',

       }

    }

}





                                                                                        163
```

</details>

<details>
<summary>原始文字 P164</summary>

```text
  建立student 資料模型

# sudo vim myapp/models.py





from django.db import models



class students(models.Model):

                  cName = models.CharField(max_length=20, null=False)

                  cSex = models.CharField(max_length=2, default='M', null=False)

                  cBirthday = models.DateField(null=False)

                  cEmail = models.EmailField(max_length=100, blank=True, default='')

                  cPhone = models.CharField(max_length=50, blank=True, default='')

                  cAddr = models.CharField(max_length=255,blank=True, default='')





                                                                                          164
```

</details>

<details>
<summary>原始文字 P165</summary>

```text
                                  授課教師：葉呈祥



  建立migration 資料檔:

Diango 要使用資料庫，通常會將建立資料表的架構和版本記錄下來，以利以後

的追蹤。

# sudo python3 ./manage.py makemigrations





 模型與資料庫同步

# sudo python3 ./manage.py migrate





 資料庫查詢(SQL-SELECT 語法)


新增瀏覽位置(urls.py):

# sudo vim project2/urls.py





                                                                                        165
```

</details>

<details>
<summary>原始文字 P166</summary>

```text
新增view functions

# sudo vim myapp/views.py





新增template list.html

# sudo vim templates/listall.html





                                                                                          166
```

</details>

<details>
<summary>原始文字 P167</summary>

```text
                                  授課教師：葉呈祥





測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8080





                                                                                        167
```

</details>

<details>
<summary>原始文字 P168</summary>

```text
新增瀏覽位置(urls.py):

# sudo vim project2/urls.py





新增view functions





新增search_name.html





                                                                                          168
```

</details>

<details>
<summary>原始文字 P169</summary>

```text
                                  授課教師：葉呈祥





測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8080





                                                                                        169
```

</details>

<details>
<summary>原始文字 P170</summary>

```text
新增瀏覽位置(urls.py):

# sudo vim project2/urls.py





新增view functions

# sudo vim myapp/views.py





                                                                                          170
```

</details>

<details>
<summary>原始文字 P171</summary>

```text
                                  授課教師：葉呈祥




新增template base.html index.html

# vim templates/base.html





# vim templates/index.html





測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8080





                                                                                        171
```

</details>

<details>
<summary>原始文字 P172</summary>

```text
 資料新增(SQL-INSERT 語法)


新增瀏覽位置(urls.py):

# sudo vim project1/urls.py





新增view functions：

# sudo vim myapp/views.py





                                                                                          172
```

</details>

<details>
<summary>原始文字 P173</summary>

```text
                                  授課教師：葉呈祥





新增template post1.html：

# sudo vim templates/post1.html





                                                                                        173
```

</details>

<details>
<summary>原始文字 P174</summary>

```text
測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8080





                                                                                          174
```

</details>

<details>
<summary>原始文字 P175</summary>

```text
                                  授課教師：葉呈祥


 資料刪除(SQL-DELETE 語法)


新增瀏覽位置(urls.py):

# sudo vim project2/urls.py





新增view functions：

# sudo vim myapp/views.py





                                                                                        175
```

</details>

<details>
<summary>原始文字 P176</summary>

```text
測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8080





                                                                                          176
```

</details>

<details>
<summary>原始文字 P177</summary>

```text
                                  授課教師：葉呈祥





 資料更新(使用GET) (SQL-UPDATE 語法)


新增瀏覽位置(urls.py):

# sudo vim project2/urls.py





                                                                                        177
```

</details>

<details>
<summary>原始文字 P178</summary>

```text
新增view functions：

# sudo vim myapp/views.py





新增template edit1.html：

# sudo vim templates/edit1.html





                                                                                          178
```

</details>

<details>
<summary>原始文字 P179</summary>

```text
                                  授課教師：葉呈祥





測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8080





                                                                                        179
```

</details>

<details>
<summary>原始文字 P180</summary>

```text
測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8080





                                                                                          180
```

</details>

<details>
<summary>原始文字 P181</summary>

```text
                                  授課教師：葉呈祥





 資料更新(使用GET) (SQL-UPDATE 語法)


新增瀏覽位置(urls.py):

# sudo vim project2/urls.py





新增view functions：

# sudo vim myapp/views.py





                                                                                        181
```

</details>

<details>
<summary>原始文字 P182</summary>

```text
測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8080





                                                                                          182
```

</details>

<details>
<summary>原始文字 P183</summary>

```text
授課教師：葉呈祥





                      183
```

</details>

<details>
<summary>原始文字 P184</summary>

```text
3-12 資料庫查詢 (使用ORM)

Django 資料庫操作並不需要直接面對 SQL，而是使用抽象化的物件關聯對應模
型ORM (Object Relational Model) 將底層 SQL 操作包裝成物件方法，具體來說就
是提供了django.db.models.Model 類別作為應用程式與資料庫之間的介面 (MTV
架構中的 M 指的就是這個 Model 類別)，只要使用由這個類別所建立之資料庫
模型物件就能操作資料庫與資料表。由於各家資料庫系統所使用之 SQL 語法存
在差異，ORM 將操作 SQL 的細節包裝起來最大的好處就是幾乎可以無痛轉換資
料庫，從預設的SQLite 轉換至MySQL 或Postgre 等資料庫時只要改換設定即可，
不需要修改程式或與調整 SQL 語法。


CRUD 指的是，Create (新增)、Read (讀取)、Update (修改)、Delete (刪除) 等常見
的資料庫操作。ORM，即Object-Relational Mapping（Object-Relational Mapping，
Object-Relational Mapping），它的作用是在關係型數據庫和業務實體對像作一個
映射，ORM為之間關係型數據庫提供了抽象的抽象，它增加了開發人員不用SQL，
只需要數據寫代碼在數據庫中創建、讀取更新和刪除。開發人員能夠使用他們熟
悉的編程語言來處理數據庫，而無需寫入 SQL 語句或存儲過程。





ORM 主要任務是：
1. 可根據對象的類型生成表結構。
2. 將對象、列表的操作，轉換為sql 語句。
3.  將sql 查詢到的結果轉換為對象、列表。


ORM 的優點：
1. 隱藏數據訪問細節，ORM 提供了對數據庫的映射，不用sql 直接編碼，才能
  像操作對像一樣從數據庫獲取數據。





                                                                                          184
```

</details>

<details>
<summary>原始文字 P185</summary>

```text
                                  授課教師：葉呈祥


2. 提高了開發效率，幾乎所有的ORM 框架都通過對像模型構造關係數據庫結
  構的功能提供。
3. 實現了數據模型與數據庫的解耦，即數據模型的不需要設計依賴於特定的數
  據庫，通過簡單的配置就可以輕鬆更換數據庫。


ORM 的缺點：
1. 現在的各種ORM 框架都在嘗試使用各種方法來實踐這塊（LazyLoad，
    Cache）。
2.  對於復雜的查詢力不從心，例如分組算列，case，group，order by，exists
  等。
3. 需要消耗更多的記憶體，使用ORM 對像這樣的全部數據都再提取到記憶體
  對像中，然後進行過濾和加工處理，就容易產生性能問題。
4. 將復雜性從數據庫轉移到應用程序代碼中，沒有在應用程序和存儲過程之間
  將代碼進行分解，從而提高了Python 的總代碼量。



Django 模型（model）系統－常用查詢語法：

https://www.itread01.com/content/1543740968.html


Django 筆記-模型與資料庫:

http://dokelung-blog.logdown.com/posts/220606-django-notes-5-model-and-databa

se

  SQLite vs MySQL vs PostgreSQL
SQLite：
 優點：
 1、占用空間小：顧名思義，SQLite 庫非常輕巧。儘管它使用的空間因安裝的
 系統而異，但可以占用不到600KiB 的空間。此外，它是完全獨立的，這意味
 著您無需在系統上安裝任何外部依賴項即可運行SQLite。
 2、用戶友好：SQLite 有時被描述為「零配置」資料庫，可以直接使用。SQLite
 不會作為伺服器進程運行，這意味著它永遠都不需要停止，啟動或重新啟動，
 也不需要任何需要管理的配置文件。這些功能有助於簡化從安裝SQLite 到將其
 與應用程式集成的路徑。
 3、可移植：與通常將數據存儲為一大批單獨文件的其他資料庫管理系統不同，
  整個SQLite 資料庫存儲在單個文件中。該文件可以位於目錄層次結構中的任何
 位置，並且可以通過可移動媒體或文件傳輸協議共享。


 缺點：





                                                                                        185
```

</details>

<details>
<summary>原始文字 P186</summary>

```text
 1、有限的並發性：儘管多個進程可以同時訪問和查詢SQLite 資料庫，但是在
 任何給定時間只有一個進程可以對資料庫進行更改。這意味著與大多數其他嵌
 入式資料庫管理系統相比，SQLite 支持更大的並發性，但是不如MySQL 或
  PostgreSQL 這樣的客戶端/伺服器RDBMS。
 2、沒有用戶管理：資料庫系統通常帶有對用戶的支持，或具有對資料庫和表
 的預定義訪問權限的託管連接。由於SQLite 直接讀取和寫入普通磁碟文件，因
 此唯一適用的訪問權限是基礎作業系統的典型訪問權限。對於需要多個具有特
 殊訪問權限的用戶的應用程式，這使SQLite 成為糟糕的選擇。
 3、安全性：在某些情況下，使用伺服器的資料庫引擎比無伺服器的資料庫（如
 SQLite）可以更好地保護客戶端應用程式中的錯誤。例如，客戶端中的雜散指
 針不能破壞伺服器上的內存。而且，由於伺服器是單個持久性進程，因此與無
 伺服器的資料庫相比，客戶端-伺服器的資料庫可以更精確地控制數據訪問，
 從而實現更細粒度的鎖定和更好的並發性。


MySQL：
 優點：
 1、受歡迎程度和易用性：作為世界上最流行的資料庫系統之一，擁有使用
  MySQL 經驗的資料庫管理員並不乏。同樣，關於如何安裝和管理MySQL 資料
 庫，還有大量印刷和在線文檔，以及許多旨在簡化資料庫入門過程的第三方工
 具，例如phpMyAdmin。
 2、安全性：MySQL 隨附了一個腳本，該腳本可通過設置安裝的密碼安全級別，
  為root 用戶定義密碼，刪除匿名帳戶以及刪除默認情況下可訪問的測試資料
 庫來幫助您提高資料庫的安全性所有用戶。另外，與SQLite 不同，MySQL 確
 實支持用戶管理，並允許您逐個用戶授予訪問權限。
 3、速度：通過選擇不實現SQL 的某些功能，MySQL 開發人員可以優先考慮速
 度。儘管最近的基準測試表明，其他PostgreSQL 之類的RDBMS 在速度方面可
 以與MySQL 匹敵，或者至少接近MySQL，但MySQL 仍然享有極快的資料庫解
 決方案聲譽。
 4、複製：MySQL 支持許多不同類型的複製，這是在兩個或多個主機之間共享
 信息的實踐，以幫助提高可靠性，可用性和容錯能力。這對於設置資料庫備份
 解決方案或橫向擴展資料庫很有幫助。


 缺點：
 1、已知局限性：由於MySQL 是為了提高速度和易用性而不是完全符合SQL 的
 要求而設計的，因此它具有某些功能局限性。例如，它不支持FULL JOIN 子句。
 2、許可和專有功能：MySQL 是雙重許可的軟體，具有根據GPLv2 許可的免費
 開源社區版本，以及根據專有許可發行的若干付費商業版本。因此，某些功能
 和插件僅適用於專有版本。





                                                                                          186
```

</details>

<details>
<summary>原始文字 P187</summary>

```text
                                  授課教師：葉呈祥


 3、發展緩慢：自從MySQL 項目於2008 年被Sun Microsystems 收購，然後在
  2009 年被Oracle Corporation 收購後，用戶抱怨DBMS 的開發過程已經大大減
 慢了，因為社區不再擁有代理機構快速應對問題並實施更改。


PostgreSQL：
 優點：
  1、SQL 合規性：PostgreSQL 比SQLite 或MySQL 還要嚴格遵守SQL 標準。根據
  PostgreSQL 的官方文檔，除了一長串可選功能之外，PostgreSQL 還支持179 種
 完全符合SQL：2011 核心要求的功能。
 2、開源和社區驅動：PostgreSQL 的原始碼是一個完全開放原始碼的項目，它
 是由一個龐大而專門的社區開發的。同樣，Postgres 社區維護並提供了許多在
 線資源，這些資源描述了如何使用DBMS，包括官方文檔，PostgreSQL Wiki 和
 各種在線論壇。
 3、可擴展：用戶可以通過其目錄驅動的操作及其對動態加載的使用，以編程
 方式即時擴展PostgreSQL。可以指定一個目標代碼文件，例如共享庫，而
  PostgreSQL 將根據需要加載它。


 缺點:
 1、內存性能：對於每個新的客戶端連接，PostgreSQL 都會派生一個新進程。
 每個新進程都分配了大約10MB 的內存，對於具有大量連接的資料庫而言，這
 可以快速增加內存。因此，對於簡單的繁重的操作，PostgreSQL 通常比其他
 RDBMS（如MySQL）的性能要差。
 2、流行度：儘管近年來使用更為廣泛，但從歷史上看，PostgreSQL 在流行度
 方面一直落後於MySQL。其結果之一是，可以幫助管理PostgreSQL 資料庫的
 第三方工具仍然較少。同樣，與擁有MySQL 經驗的資料庫管理員相比，擁有
 經驗豐富的Postgres 資料庫的資料庫管理員也要少得多。


  設定Django 連mysql 的參數

# vim project2/settings.py

DATABASES = {

    'default': {

       #'ENGINE': 'django.db.backends.sqlite3',

       #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

       'ENGINE': 'django.db.backends.mysql',

       'NAME': 'myproject',

       'USER': 'tony',

       'PASSWORD': '1qaz2wsx',





                                                                                        187
```

</details>

<details>
<summary>原始文字 P188</summary>

```text
       'HOST': 'localhost',

       'PORT': '3306',

       'OPTIONS':{

           'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",

           'charset': 'utf8mb4',

       }

    }

}





  建立student 資料模型

# sudo vim myapp/models.py





                                                                                          188
```

</details>

<details>
<summary>原始文字 P189</summary>

```text
                                  授課教師：葉呈祥



from django.db import models



class students(models.Model):

                  cName = models.CharField(max_length=20, null=False)

                  cSex = models.CharField(max_length=2, default='M', null=False)

                  cBirthday = models.DateField(null=False)

                  cEmail = models.EmailField(max_length=100, blank=True, default='')

                  cPhone = models.CharField(max_length=50, blank=True, default='')

                  cAddr = models.CharField(max_length=255,blank=True, default='')


  建立migration 資料檔:

Diango 要使用資料庫，通常會將建立資料表的架構和版本記錄下來，以利以後

的追蹤。

# sudo python3 ./manage.py makemigrations





 模型與資料庫同步

# sudo python3 ./manage.py migrate





 資料庫查詢(SQL-SELECT 語法)


新增瀏覽位置(urls.py):





                                                                                        189
```

</details>

<details>
<summary>原始文字 P190</summary>

```text
# sudo vim project2/urls.py





新增view functions

# sudo vim myapp/views.py





新增template list.html

# sudo vim templates/listall.html





                                                                                          190
```

</details>

<details>
<summary>原始文字 P191</summary>

```text
                                  授課教師：葉呈祥





測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8080





                                                                                        191
```

</details>

<details>
<summary>原始文字 P192</summary>

```text
新增瀏覽位置(urls.py):

# sudo vim project2/urls.py





新增view functions





新增search_name.html





                                                                                          192
```

</details>

<details>
<summary>原始文字 P193</summary>

```text
                                  授課教師：葉呈祥





測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8080





                                                                                        193
```

</details>

<details>
<summary>原始文字 P194</summary>

```text
新增瀏覽位置(urls.py):

# sudo vim project2/urls.py





新增view functions

# sudo vim myapp/views.py





新增template base.html index.html

# vim templates/base.html





                                                                                          194
```

</details>

<details>
<summary>原始文字 P195</summary>

```text
                                  授課教師：葉呈祥


# vim templates/index.html





測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8080





                                                                                        195
```

</details>

<details>
<summary>原始文字 P196</summary>

```text
 資料新增(SQL-INSERT 語法)


新增瀏覽位置(urls.py):

# sudo vim project1/urls.py





新增view functions：

# sudo vim myapp/views.py





新增template post1.html：

# sudo vim templates/post1.html





                                                                                          196
```

</details>

<details>
<summary>原始文字 P197</summary>

```text
授課教師：葉呈祥





                      197
```

</details>

<details>
<summary>原始文字 P198</summary>

```text
測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8080





 資料刪除(SQL-DELETE 語法)


新增瀏覽位置(urls.py):

# sudo vim project2/urls.py





新增view functions：

# sudo vim myapp/views.py





                                                                                          198
```

</details>

<details>
<summary>原始文字 P199</summary>

```text
                                  授課教師：葉呈祥





測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8080





 資料更新(使用GET) (SQL-UPDATE 語法)





                                                                                        199
```

</details>

<details>
<summary>原始文字 P200</summary>

```text
新增瀏覽位置(urls.py):

# sudo vim project2/urls.py





新增view functions：

# sudo vim myapp/views.py





                                                                                          200
```

</details>

<details>
<summary>原始文字 P201</summary>

```text
                                  授課教師：葉呈祥





新增template edit1.html：

# sudo vim templates/edit1.html





測試結果：




                                                                                        201
```

</details>

<details>
<summary>原始文字 P202</summary>

```text
# sudo python3 manage.py runserver 0.0.0.0:8080





測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8080





                                                                                          202
```

</details>

<details>
<summary>原始文字 P203</summary>

```text
                                  授課教師：葉呈祥





 資料更新(使用GET) (SQL-UPDATE 語法)


新增瀏覽位置(urls.py):

# sudo vim project2/urls.py





新增view functions：





                                                                                        203
```

</details>

<details>
<summary>原始文字 P204</summary>

```text
# sudo vim myapp/views.py





測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8080





                                                                                          204
```

</details>

<details>
<summary>原始文字 P205</summary>

```text
授課教師：葉呈祥





                      205
```

</details>

<details>
<summary>原始文字 P206</summary>

```text
3-13 Django 使用ORM vs SQL 語法

 建立環境

  建立Django 專案:

# cd ~/dvds

# source ./dvds/dvdsenv/bin/activate (啟動虛擬環境)

# django-admin startproject DB (建立DB 專案)

# cd DB

# tree



 ORM 欄位與引數說明

每個欄位有一些特有的引數，例如，CharField 需要max_length 引數來指定
VARCHAR 資料庫欄位的大小。還有一些適用於所有欄位的通用引數。這些引數
在文件中有詳細定義，這裡我們只簡單介紹一些最常用的：



欄位      說明

CharField    字串欄位，用於較短的字串

        要求必須有一個引數 maxlength

IntegerField   用於儲存一個整數

FloatField        double

                   ex: models. FloatField(null=True)

DecimalField  一個浮點數，必須提供兩個引數

           max_digits：總位數(不包括小數點和符號)

             decimal_places：小數位數

                   ex:

        要儲存最大值為 999 (小數點後儲存2 位)，定義欄位:

                   models.DecimalField(..., max_digits=5, decimal_places=2)

AutoField    一個 IntegerField，新增記錄時它會自動增長。

                  EX:

                 my_id=models.AutoField(primary_key=True)

        如果你不指定主鍵的話，系統會自動新增一個主鍵欄位到你的model。

BooleanField    A true/false field。admin 用checkbox 來表示此類欄位。




                                                                                          206
```

</details>

<details>
<summary>原始文字 P207</summary>

```text
                                  授課教師：葉呈祥


TextField    一個容量很大的文字欄位。

EmailField     一個帶有檢查Email 合法性的CharField，不接受maxlength 引數。

DateField    一個日期欄位。共有下列額外的可選引數：

            Argument：描述

         auto_now：當物件被儲存時(更新或者新增都行)，自動將該欄位的值設定為

        當前時間。通常用於表示 "last-modified" 時間戳。

         auto_now_add：當物件首次被建立時，自動將該欄位的值設定為當前時間，

        通常用於表示物件建立時間。


DateTimeField  一個日期時間欄位。

        類似 DateField 支援同樣的附加選項。

ImageField   類似 FileField，不過要校驗上傳物件是否是一個合法圖片。

FileField    一個檔案上傳欄位




引數      說明

null          如果為True，Django 將用NULL 來在資料庫中儲存空值。 預設值是 False。

blank       如果為True，該欄位允許不填。預設為False。

default     欄位的預設值。可以是一個值或者可呼叫物件。如果可呼叫，每有新物件被

        建立它都會被呼叫，如果你的欄位沒有設定可以為空，那麼將來如果我們後

         新增一個欄位，這個欄位就要給一個default 值。

primary_key   如果為True，那麼這個欄位就是模型的主鍵。如果你沒有指定任何一個欄位

               的primary_key=True，Django 就會自動新增一個IntegerField 欄位做為主鍵，

       所以除非你想覆蓋預設的主鍵行為，否則沒必要設定任何一個欄位的

                primary_key=True。

unique     如果該值設定為True，這個資料欄位的值在整張表中必須是唯一的。


auto_now_add  配置auto_now_add=True，建立資料記錄的時候會把當前時間新增到資料庫。


auto_now    配置上auto_now=True，每次更新資料記錄的時候會更新該欄位，標識這條記

        錄最後一次的修改時間。


參考文獻:

https://iter01.com/432964.html


 建立資料表





                                                                                        207
```

</details>

<details>
<summary>原始文字 P208</summary>

```text
＃vim DBapp/models.py





# sudo python3 manage.py makemigrations

(建立資料庫和Django 間的中介檔)

# sudo python3 manage.py migrate

(同步更新資料庫內容)





                                                                                          208
```

</details>

<details>
<summary>原始文字 P209</summary>

```text
                                  授課教師：葉呈祥


 匯入資料表資料





 設定Django 平台

  url 配置檔

新增瀏覽位置(urls.py):

# sudo vim DB/urls.py





                                                                                        209
```

</details>

<details>
<summary>原始文字 P210</summary>

```text
     新增view functions

# sudo vim DBapp/views.py





測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8080





 查詢資料

選取所有的欄位：


SQL：

SELECT * FROM `students`;





                                                                                          210
```

</details>

<details>
<summary>原始文字 P211</summary>

```text
                                  授課教師：葉呈祥





ORM：

datas = students.objects.all()


     修改view functions

# sudo vim DBapp/views.py





測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8080





                                                                                        211
```

</details>

<details>
<summary>原始文字 P212</summary>

```text
ORM：

datas = students.objects.values('cID','cName', 'cEmail')



透過QuerySet 的.values()方法，將QuerySet 轉換為ValuesQuerySet




for data in datas:

  print('%s %s %s' % (data['cID'], data['cName'], data['cEmail']))





SELECT DISTINCT:去除重複資料顯示一筆：
Ex:想知道全班有幾種性別


SQL：

SELECT DISTINCT `cSex` FROM `students`;





                                                                                          212
```

</details>

<details>
<summary>原始文字 P213</summary>

```text
                                  授課教師：葉呈祥





ORM：

datas = students.objects.values('cSex').distinct()

print(datas)




datas = students.objects.values('cSex').distinct().count()

print(datas)





      values vs values_list

values
Returns a QuerySet that returns dictionaries, rather than model instances, when
used as an iterable.


Ex:
list(Article.objects.values_list('id', flat=True))
# flat=True will remove the tuples and return the list
[1, 2, 3, 4, 5, 6]


value_list
This is similar to values() except that instead of returning dictionaries,  it returns



                                                                                        213
```

</details>

<details>
<summary>原始文字 P214</summary>

```text
tuples when iterated over.

Ex:
list(Article.objects.values('id'))
[{'id':1}, {'id':2}, {'id':3}, {'id':4}, {'id':5}, {'id':6}]


    WHERE：設定篩選條件
在查詢資料時，並不是每一次都要顯示所有的內容。我們可能會為顯示的資料設
定一些條件，來篩選顯示的內容，這就是 WHERE 指令的功能。
WHERE 基本語法：
WHERE 的基本語法格式為：



Ex:想要由students 資料表中挑出cID 的學生資料


SQL:

SELECT * FROM `students` WHERE `cID `=1;





ORM：

獲取單條資料（有且僅有一條，id 唯一）(回傳物件)

datas = students.objects.get(cID=1)

or

datas = students.objects.filter(cID=1)(回傳QuerySet)

for data in datas:

    print('%s  %s  %s  %s  %s  %s  %s'  %  (data.cID,  data.cName,

data.cSex ,data.cBirthday, data.cEmail, data.cPhone, data.cAddr))





                                                                                          214
```

</details>

<details>
<summary>原始文字 P215</summary>

```text
                                  授課教師：葉呈祥



Ex:想要由students 資料表中挑出所有男性的資料


SQL:

SELECT * FROM `students` WHERE `cSex`='M';





ORM：

datas = students.objects.filter(cSex='M')

for data in datas:

       print('%s %s %s %s %s %s %s' % (data.cID, data.cName,

data.cSex ,data.cBirthday, data.cEmail, data.cPhone, data.cAddr))





比較運算子：

=           !=        <>        <

>         <=        >=           IS NULL


AND、OR、NOT：連接多個條件式：
Ex:想要由students 資料表中找出座號大於5 的男生


SQL:

SELECT * FROM `students` WHERE `cID`>5 AND `cSex`='M';





                                                                                        215
```

</details>

<details>
<summary>原始文字 P216</summary>

```text
ORM:

# 比較，gt:>，gte:>=，lt:<，lte:<=

# isnull：isnull=True 為空，isnull=False 不為空




datas = students.objects.filter(cID__gt=5,cSex='M')

for data in datas:

   print('%s  %s  %s  %s  %s  %s  %s'  %  (data.cID,  data.cName,

data.cSex ,data.cBirthday, data.cEmail, data.cPhone, data.cAddr))





Ex:想要由students 資料表中找出座號不大於5 的男生

SQL:

SELECT * FROM `students` WHERE !(`cID`>5 AND `cSex`='M');





                                                                                          216
```

</details>

<details>
<summary>原始文字 P217</summary>

```text
                                  授課教師：葉呈祥



Q 表達式：
通過objects.filter 傳入多個條件參數時，多個條件之間默認爲「與」的關係，如
果想要變成「或」、「非」等其他關係，就可以使用Q 表達式。Q 表達式可以使用
&（AND）、|（OR）、~（NOT）等運算符。





ORM:

from django.db.models import Q

    datas = students.objects.filter( ~Q(cID__gt=5),cSex='M')



for data in datas:

   print('%s  %s  %s  %s  %s  %s  %s'  %  (data.cID,  data.cName,

data.cSex ,data.cBirthday, data.cEmail, data.cPhone, data.cAddr))





                                                                                        217
```

</details>

<details>
<summary>原始文字 P218</summary>

```text
Ex:想要由students 資料表中找出座號等於1 號或座號大於等於9 號的人

SQL:

SELECT * FROM `dbapp_students` WHERE `cID`=1 OR `cID`>=9;





ORM:

from django.db.models import Q

    datas = students.objects.filter(

       Q(cID=1) | Q(cID__gte=9)

       )

for data in datas:

    print('%s  %s  %s  %s  %s  %s  %s'  %  (data.cID,  data.cName,

data.cSex ,data.cBirthday, data.cEmail, data.cPhone, data.cAddr))





設定數值篩選範圍：
EX:由students 資料表中找出座號大於等於4 且小於等於6 的學生資料

SQL

SELECT * FROM `students` WHERE `cID` BETWEEN 4 AND 6;





                                                                                          218
```

</details>

<details>
<summary>原始文字 P219</summary>

```text
                                  授課教師：葉呈祥





ORM:

datas = students.objects.filter(cID__range=[4,6])

for data in datas:

    print('%s  %s  %s  %s  %s  %s  %s'  %  (data.cID,  data.cName,

data.cSex ,data.cBirthday, data.cEmail, data.cPhone, data.cAddr))





    IN：指定多個篩選值
Ex:想要由students 資料表中找出座號為1,3,5,7,9 的學生資料：

SQL:

SELECT * FROM `students` WHERE `students`.`cID` IN (1,3,5,7,9)





                                                                                        219
```

</details>

<details>
<summary>原始文字 P220</summary>

```text
ORM:

datas = students.objects.filter(cID__in=[1,3,5,7,9])

for data in datas:

    print('%s  %s  %s  %s  %s  %s  %s'  %  (data.cID,  data.cName,

data.cSex ,data.cBirthday, data.cEmail, data.cPhone, data.cAddr))





    LIKE：設定字串比對的篩選值

SQL:





ORM
語法       等同於sql 語法

__exact           like 'aaa'
__iexact    忽略大小寫  ilike 'aaa'
__contains   包含 like '%aaa%'
__icontains  包含，忽然大小寫我喜歡 '%aaa%'，但對於sqlite 來說，包含的
           作用等同於icontains。
__startswith  以…開頭
__istartswith  以…開頭忽略大小寫
__endswith  以…结尾
__iendswith  以…結尾，忽略大小寫
__range    在…範圍內
__year    日期字段的年份
__month   日期字段的月份
__day     日期字段的日





                                                                                          220
```

</details>

<details>
<summary>原始文字 P221</summary>

```text
                                  授課教師：葉呈祥



Ex:想要由students 資料表中，出電話號碼是「0918」開頭的學生資料


SQL:

SELECT * FROM `students` WHERE `cPhone` LIKE '0918%';





ORM:

datas = students.objects.filter(cPhone__istartswith='0918')

for data in datas:

    print('%s  %s  %s  %s  %s  %s  %s'  %  (data.cID,  data.cName,

data.cSex ,data.cBirthday, data.cEmail, data.cPhone, data.cAddr))





Ex: 想要由students 資料表中，找出學生的地址中有「建國」這個字的資料。

SQL:

SELECT * FROM `students` WHERE `cAddr` LIKE '%建國%'





                                                                                        221
```

</details>

<details>
<summary>原始文字 P222</summary>

```text
ORM:

datas = students.objects.filter(cAddr__contains='建國')

for data in datas:

    print('%s  %s  %s  %s  %s  %s  %s'  %  (data.cID,  data.cName,

data.cSex ,data.cBirthday, data.cEmail, data.cPhone, data.cAddr))





     ORDER BY：設定查詢結果的排序
ORDER BY 的功能是用來設定欄位，進行排序查詢結果，它的基本語法如下：





其中排序方式有二種：
1.  ASC(ascending)：遞增排序，由小排到大，也是未指定時預設的排序方法。
2.  DESC(Descending)：遞減排序，由大排到小。


Ex: 想要由students 資料表所有同學的資料依生日遞減排序


SQL:

SELECT * FROM `students` ORDER BY `cBirthday` DESC;





                                                                                          222
```

</details>

<details>
<summary>原始文字 P223</summary>

```text
                                  授課教師：葉呈祥





ORM:

遞增排序:

datas = students.objects.all().order_by('cBirthday')



遞減排序:

datas = students.objects.all().order_by('-cBirthday')

for data in datas:

   print('%s  %s  %s  %s  %s  %s  %s'  %  (data.cID,  data.cName,

data.cSex ,data.cBirthday, data.cEmail, data.cPhone, data.cAddr))





                                                                                        223
```

</details>

<details>
<summary>原始文字 P224</summary>

```text
Ex: 想要由students 資料表所有同學的資料依性別遞增排序，再依生日遞減排序

SQL:

SELECT * FROM `students` ORDER BY `cSex` ASC, `cBirthday` DESC;





ORM:

datas = students.objects.all().order_by('cSex', '-cBirthday')

for data in datas:

   print('%s  %s  %s  %s  %s  %s  %s'  %  (data.cID,  data.cName,

data.cSex ,data.cBirthday, data.cEmail, data.cPhone, data.cAddr))





    LIMIT：設定查詢顯示的筆數
LIMIT 可以設定查詢後由哪一筆開始顯示，並顯示多少筆數，它的基本語法如
下：





                                                                                          224
```

</details>

<details>
<summary>原始文字 P225</summary>

```text
                                  授課教師：葉呈祥





LIMIT 是由查詢後的結果再進行擷取資料的動作，如果與 ORDER BY 進行排
序搭配可以輕易取得最前的 10 筆資料或是最後的 10 筆資料的結果。也因為如
此，LIMIT 在使用時必須放置在 ORDER BY 之後。


SQL:

SELECT  *  FROM  `students`  ORDER  BY  `students`.`cSex`  ASC,

`students`.`cBirthday` DESC LIMIT 5



SELECT * FROM `students` LIMIT 2

SELECT * FROM `students` LIMIT 0,2

SELECT * FROM `students` LIMIT 1,2

SELECT * FROM `students` LIMIT 4,2

SELECT * FROM `students` LIMIT 3,4





ORM:

datas =

students.objects.all().order_by('cSex', '-cBirthday')[:5]

for data in datas:

   print('%s  %s  %s  %s  %s  %s  %s'  %  (data.cID,  data.cName,

data.cSex ,data.cBirthday, data.cEmail, data.cPhone, data.cAddr))





                                                                                        225
```

</details>

<details>
<summary>原始文字 P226</summary>

```text
datas = students.objects.all()[:2]

datas = students.objects.all()[0:2]





datas = students.objects.all()[1:3]




datas = students.objects.all()[4:6]




datas = students.objects.all()[3:7]





    統計函式
MySQL 的 SQL 語法還提供許多統計函式，可以總計出一些資料表中的彙整資
料。為了以下的範例說明，我們要在「class」資料庫中再加入一個儲存成績的資
料表：「scorelist」，以下是這個資料表欄位的規劃：





                                                                                          226
```

</details>

<details>
<summary>原始文字 P227</summary>

```text
                                  授課教師：葉呈祥



SUM():合計值
EX:想要算出全班國文、英文及數學總分


SQL:

SELECT SUM(`score`) FROM `scorelist`;





aggregate：
用於執行聚合函數。




ORM:

from DBapp.models import scorelist

from django.db.models import Sum,Count,Max,Min,Avg

datas = scorelist.objects.aggregate(Sum('score')

print(datas)





EX:想要算出全班國文總分


SQL:

SELECT SUM(`score`) FROM `scorelist` WHERE `course`='國文';





                                                                                        227
```

</details>

<details>
<summary>原始文字 P228</summary>

```text
ORM:

from DBapp.models import scorelist

from django.db.models import Sum,Count,Max,Min,Avg

datas= scorelist.objects.filter(course='國文

').aggregate(Sum('score'))

print(datas)





AVG():平均值
EX:想要算出全班國文的平均分數


SQL:

SELECT AVG(`score`) FROM `scorelist` WHERE `course`='國文';





ORM:

from django.db.models import Sum,Count,Max,Min,Avg

datas = scorelist.objects.filter(course='國文

').aggregate(Avg('score'))

print(datas)





COUNT():計次
EX:由students 資料表統計全班人數


SQL:




                                                                                          228
```

</details>

<details>
<summary>原始文字 P229</summary>

```text
                                  授課教師：葉呈祥


SELECT COUNT(`students`.`cID`) FROM `students`





ORM:

from django.db.models import Sum,Count,Max,Min,Avg

datas = students.objects.aggregate(Count('cID'))

print(datas)





MAX()、MIN():最大值、最小值
EX:找出全班國文最高分


SQL:

SELECT MAX(`score`) FROM `scorelist` WHERE `course`='國文'



ORM:

from django.db.models import Sum,Count,Max,Min,Avg

datas = scorelist.objects.filter(course='國文

').aggregate(Max('score'))

print(datas)





EX:找出全班數學最低分


SQL:

SELECT MIN(`score`) FROM `scorelist` WHERE `course`='數學'





                                                                                        229
```

</details>

<details>
<summary>原始文字 P230</summary>

```text
ORM:

from django.db.models import Sum,Count,Max,Min,Avg

datas = scorelist.objects.filter(course='數學

').aggregate(Min('score'))

print(datas)





GROUP BY:分組排列
EX:想要顯示每個學生的總分


SQL:

SELECT `cID`, SUM(`score`) FROM `scorelist` GROUP BY `cID`


annotate：
給QuerySet 中的每個對象在執行SQL 時添加上一個查詢表達式（聚合函數、F
表達式、Q 表達式、Func 表達式等），表達式的查詢結果會以新欄位的方式添加
到結果對象中。返回值爲QuerySet 對象，QuerySet 中存儲的是模型對象。


ORM:

from django.db.models import Sum,Count,Max,Min,Avg

datas =

scorelist.objects.values_list('cID').annotate(Sum('score'))

print(datas)





HAVING:GROUP BY 的條件式





                                                                                          230
```

</details>

<details>
<summary>原始文字 P231</summary>

```text
                                  授課教師：葉呈祥


若希望對GROUP BY 的SQL 敘述加上條件式的限制，就不能使用WHERE 的方法，
而是用HAVING。
EX:想要顯示座號1 到5 同學的分數總計


SQL:

SELECT `cID`, SUM(`score`) FROM `scorelist` GROUP BY `cID` HAVING

`cID`<=5





ORM:

from django.db.models import Sum,Count,Max,Min,Avg

datas =

scorelist.objects.filter(cID__lte=5).values_list('cID').annota

te(Sum('score'))

print(datas)





 新增、更新、刪除

  查詢雖然是資料庫中重要的功能，但是新增、更新與刪除資料的動作，才是
維護資料庫內容的主要核心功能，以下將說明 SQL 語法中新增、更新與刪除資
料的指令與語法。
     INSERT:新增資料
可以使用 INSERT 語法為資料表新增資料，其基本語法如下：





                                                                                        231
```

</details>

<details>
<summary>原始文字 P232</summary>

```text
EX:新增繼續新增5 位同學進入students 資料表，
座號 姓  性別 生日    電子郵件   電話    地址 身高 體
   名                             重
        Bill1 男    1988-02-10  Bill1@bb.com  0925932221 台北  176   89
        Bill2 男    1988-02-10  Bill2@bb.com  0925932222 新竹  170   81
        Bill3 男    1988-02-10  Bill3@bb.com  0925932223 桃園  172   84


新增一筆資料:


SQL:

INSERT INTO `students`

(`cName`,`cSex`,`cBirthday`,`cEmail`,`cPhone`,`cAddr`,`cHeight

`,`cWeight`) VALUES('Bill1','男

','1988-02-10','Bill1@bb.com','0925932221','台北','176','89')



ORM:

add = students(cName="bill", cSex="M", cBirthday="2021-08-08",

cEmail="bill@yahoo.com.tw",  cPhone="0922222",  cAddr=" 新竹",

cHeight=0, cWeight=0)

add.save()


     UPDATE:更新資料
可以使用 UPDATE 語法為資料表更新資料，其基本語法如下：




UPDATE 更新資料的動作可以一次更動多筆資料的內容，所以 WHERE 後加上
的條件式十分重要，只要符合條件的資料內容即會進行更新的動作，要特別注
意。


EX:要修改座號為11 同學的身高體重




                                                                                          232
```

</details>

<details>
<summary>原始文字 P233</summary>

```text
                                  授課教師：葉呈祥



SQL:

UPDATE `students` SET `cHeight`=174, `cWeight`=92 WHERE `cID`=11


ORM:

update = students.objects.get(cID=11)

update.cHeight = 180

update.cWeight = 60

update.save()



     DELETE:刪除資料
可以使用 DELETE 語法為資料表刪除資料，其基本語法如下：




DELETE 刪除資料的動作可以一次刪除多筆資料的內容，所以 WHERE 後加上
的條件式十分重要，只要符合條件的資料內容即會進行刪除的動作，要特別注

意。


EX:刪除座號大於11 的同學的資料


SQL:

DELETE FROM `students` WHERE `cID`>11;


ORM:

delete = students.objects.filter(cID__lte=5) #(cID<=5)

delete.delete()


參考文獻:

https://www.geeksforgeeks.org/django-orm-inserting-updating-deleting-data/





                                                                                        233
```

</details>

<details>
<summary>原始文字 P234</summary>

```text
 多資料表關聯查詢

除了在一個資料表中選取欄位進行查詢，我們也可以在多個資料表中之中選取不
同的欄位，進行查詢的動作。這樣的查詢方式是必須有前提的，那就是資料表之
間要有一欄可以指定相關或是建立關聯。


 使用 JOIN 結合資料表 by SQL

     JOIN 的基本語法
若要 JOIN 語法結合二個資料表的基本語法如下：





無論何種方式結合資料表，會顯示的資料必須在兩邊資料表有資料，只要有一方
法有，即不會出現在結果中。例如有一個學生沒有登錄成績，就不會顯示結果中，
如此很容易有漏失資訊的情況。


Ex:顯示出學生座號、姓名及其國文成績的查詢，使用JOIN：



SELECT `students`.`cID`, `students`.`cName`, `scorelist`.`score`

FROM `students` JOIN `scorelist`

ON `students`.`cID` = `scorelist`.`cID`

WHERE `scorelist`.`course`='國文';





                                                                                          234
```

</details>

<details>
<summary>原始文字 P235</summary>

```text
                                  授課教師：葉呈祥





     LEFT JOIN、RIGHT JOIN 語法


SELECT 顯示欄位..
FROM 資料表A  LEFT|RIGHT  JOIN 資料表 B
ON A.相關欄位＝ B.相關欄位


EX:希望可以列出全班同學每個人的成績總分與平均。


使用結合資料表基本語法：

SELECT `students`.`cID`, `students`.`cName`

, SUM(`scorelist`.`score`), AVG(`scorelist`.`score`)

FROM `students`,`scorelist`

WHERE `students`.`cID` = `scorelist`.`cID`

GROUP BY `students`.`cID`, `students`.`cName`





                                                                                        235
```

</details>

<details>
<summary>原始文字 P236</summary>

```text
使用JOIN 基本語法：

SELECT `students`.`cID`, `students`.`cName`

, SUM(`scorelist`.`score`), AVG(`scorelist`.`score`)

FROM `students` INNER JOIN `scorelist`

ON `students`.`cID` = `scorelist`.`cID`

GROUP BY `students`.`cID`



補充：將表別設定別名使用

SELECT `students`.`cID`, `students`.`cName`

, SUM(`scorelist`.`score`), AVG(`scorelist`.`score`)

FROM `students` st INNER JOIN `scorelist` sc

ON st.`cID` = sc.`cID`

GROUP BY st.`cID`





                                                                                          236
```

</details>

<details>
<summary>原始文字 P237</summary>

```text
                                  授課教師：葉呈祥





使用LEFT JOIN：

SELECT `students`.`cID`, `students`.`cName`

, SUM(`scorelist`.`score`), AVG(`scorelist`.`score`)

FROM `students` LEFT JOIN `scorelist`

ON `students`.`cID` = `scorelist`.`cID`

GROUP BY `students`.`cID`, `students`.`cName`





                                                                                        237
```

</details>

<details>
<summary>原始文字 P238</summary>

```text
  Django ORM 一對一、一對多、多對多

一對一：一個人對應一個身份證號碼。
一對多：一個家庭有多個人，一般會使用外鍵來實現。
多對多：一個學生有多門課程，一個課程有很多學生，一般會使用第三個表來實
現關聯。





                                                                                          238
```

</details>

<details>
<summary>原始文字 P239</summary>

```text
                                  授課教師：葉呈祥





＃vim DBapp/models.py





# sudo python3 manage.py makemigrations

(建立資料庫和Django 間的中介檔)

# sudo python3 manage.py migrate

(同步更新資料庫內容)




                                                                                        239
```

</details>

<details>
<summary>原始文字 P240</summary>

```text
240
```

</details>

<details>
<summary>原始文字 P241</summary>

```text
                                  授課教師：葉呈祥





dbapp_book_authors(自動增加的表格)





 匯入資料表資料





                                                                                        241
```

</details>

<details>
<summary>原始文字 P242</summary>

```text
     ORM(One-To-One Relation)


＃vim DBapp/models.py





新增
Ex:新增一個學生
基本資料如下：
「王大明」、「M」、「2020-08-20」、「wang@yahoo.com.tw」、「099999」
、「新竹」、「120」、「40」，密碼為「0000」、level 為「0」

ORM:

datas = students.objects.create(cName='王大明

',cSex='M',cBirthday='2020-08-20', cEmail='wang@yahoo.com.tw',

cPhone='09333333', cAddr='新竹', cHeight=120, cWeight=40)





                                                                                          242
```

</details>

<details>
<summary>原始文字 P243</summary>

```text
                                  授課教師：葉呈祥





permissions.objects.create(cID=datas, passwd='0000', level='0')


查尋
Ex:顯示學生的座號、姓名、密碼、level

ORM:

datas =

students.objects.values('cID','cName','permissions__passwd',

'permissions__level')

for data in datas:

   print('%s %s %s %s' % (data['cID'], data['cName'],

data['permissions__passwd'] ,data['permissions__level']))





刪除
Ex:刪除「王大明」的基本資料與權限資料

第一種方法:

students.objects.get(cName='王大明').delete()

第二種方法:

students.objects.filter(cName='王大明').delete()


     ORM(One-To-Many Relation)

＃vim DBapp/models.py





                                                                                        243
```

</details>

<details>
<summary>原始文字 P244</summary>

```text
新增
Ex: 想新增姓名為「黃靖輪」的地理成績

ORM:

第一種寫法:

scorelist.objects.create(cID=students.objects.get(cName='黃靖輪

'), course='地理', score=60)



第二種寫法:

data  =  scorelist(cID=students.objects.get(cName=' 黃靖輪'),

course='音樂', score=60)

data.save()




查尋
Ex:顯示出學生座號、姓名及其國文成績的查詢。


ORM:

print(students.objects.filter(scorelist__course='國文

').values('cID','cName','scorelist__course','scorelist__score'

))





                                                                                          244
```

</details>

<details>
<summary>原始文字 P245</summary>

```text
                                  授課教師：葉呈祥





datas =

students.objects.filter(scorelist__course='國文

').values('cID','cName','scorelist__course','scorelist__score'

)

for data in datas:

  print('%s %s %s %s' % (data['cID'], data['cName'],

data['scorelist__course'] ,data['scorelist__score']))





EX:希望可以列出全班同學每個人的成績總分與平均。

ORM:

from django.db.models import Sum,Count,Max,Min,Avg

print(students.objects.values_list('cID','cName').annotate(Sum

('scorelist__score'), Avg('scorelist__score')))





from django.db.models import Sum,Count,Max,Min,Avg





                                                                                        245
```

</details>

<details>
<summary>原始文字 P246</summary>

```text
datas =

students.objects.values_list('cID','cName').annotate(Sum('scor

elist__score'), Avg('scorelist__score'))

for data in datas:

  print('%s %s %s %s' % (data[0], data[1], data[2] , data[3]))





修改

Ex:
將學號「03」的國文成績改成60 分。

ORM:

第一種寫法:

datas = students.objects.get(cID=3)

datas.scorelist_set.filter(course='國文').update(score=60)



第二種寫法:

scorelist.objects.filter(course='國文' ,cID=

students.objects.get(cID=3).cID).update(score=60)




Ex:
將姓名為「簡奉君」的國文成績改成100 分。

ORM:

第一種寫法:

datas = students.objects.get(cName='簡奉君')





                                                                                          246
```

</details>

<details>
<summary>原始文字 P247</summary>

```text
                                  授課教師：葉呈祥


(先查尋多對一的一那方)

datas.scorelist_set.filter(course='國文').update(score=100)

(再查尋多的那方，更新多的那方成績)



第二種寫法:

scorelist.objects.filter(course='國文' ,cID=

students.objects.get(cName='簡奉君').cID).update(score=100)

(內層為多對一的一那方的cID 等於多的那方的外來鍵，更新多的那方成績)


刪除
Ex: 將姓名簡奉君的學生資料與成績全部刪除。

ORM:

students.objects.get(cName='簡奉君').delete()


     ORM(Many-To-Many Relation)

# vim DBapp/models.py





新增
Ex: 第一次新增作者「小虎」與新增書名「C++」、「PHP」

ORM:

第一種寫法:

Author_obj = Author.objects.create(name="小虎")




Book_obj = Book.objects.create(name="C++")

Book_obj.authors.add(Author_obj)

Book_obj = Book.objects.create(name="PHP")




                                                                                        247
```

</details>

<details>
<summary>原始文字 P248</summary>

```text
Book_obj.authors.add(Author_obj)



第二種寫法

Author_obj = Author(name="小虎")

Author_obj.save()



Book_obj1 = Book(name="C++")

Book_obj1.save()

Book_obj2 = Book(name="PHP")

Book_obj2.save()




Book_obj1.authors.add(Author_obj)

Book_obj2.authors.add(Author_obj)





Ex: 已存在作者小虎，新增此作者的書「JAVA」、「Linux」

ORM:

第一種寫法:

Author_obj = Author.objects.get(name="小虎")

Book_obj = Book.objects.create(name="JAVA")

Book_obj.authors.add(Author_obj)

Book_obj = Book.objects.create(name="Linux")

Book_obj.authors.add(Author_obj)





                                                                                          248
```

</details>

<details>
<summary>原始文字 P249</summary>

```text
                                  授課教師：葉呈祥




第二種寫法:

Author_obj = Author.objects.get(name="小虎")

Book_obj1 = Book(name="JAVA")

Book_obj1.save()

Book_obj1.authors.add(Author_obj)




Book_obj2 = Book(name="Linux")

Book_obj2.save()

Book_obj2.authors.add(Author_obj)





Ex: 新增兩個「小明」、「大雄」均為「C#」書的作者

ORM:

第一種寫法:

Author_obj1 = Author.objects.create(name="小明")

Author_obj2 = Author.objects.create(name="大雄")

Book_obj = Book.objects.create(name="c#")

Book_obj.authors.add(Author_obj1, Author_obj2)



第二種寫法:

Author_obj1 = Author(name="小明")

Author_obj1.save()





                                                                                        249
```

</details>

<details>
<summary>原始文字 P250</summary>

```text
Author_obj2 = Author(name="大雄")

Author_obj2.save()

Book_obj = Book(name="c#")

Book_obj.save()

Book_obj.authors.add(Author_obj1, Author_obj2)





查詢:
Ex:「C#」書的作者有那些?

ORM:

print(Book.objects.filter(name="C#").values('name','authors__n

ame'))





Ex:作者「小虎」有出版那些書?

ORM:

第一種寫法:

print(Book.objects.filter(authors=Author.objects.get(name="小虎

")).values('name','authors__name'))



第二種寫法:

print(Book.objects.filter(authors__name="小虎

").values('name','authors__name'))





                                                                                          250
```

</details>

<details>
<summary>原始文字 P251</summary>

```text
                                  授課教師：葉呈祥


第三種寫法:

authors_id=Author.objects.get(name="小虎").id

print(Book.objects.filter(authors=authors_id).values('name','a

uthors__name'))




刪除:
Ex:刪除書名為「C#」的所有資料，但Author 資料表保留

Book.objects.get(name="C#").delete()


Ex:刪除作者為「小虎」的所有資料，但Book 資料表保留

Author.objects.get(name="小虎").delete()




參考文獻:

https://notes.andywu.tw/2018/%E8%B3%87%E6%96%99%E5%BA%AB-%E9%97%9C
%E8%81%AF%E4%BB%8B%E7%B4%B9-%E4%B8%80%E5%B0%8D%E4%B8%80%E3%

80%81%E4%B8%80%E5%B0%8D%E5%A4%9A%E3%80%81%E5%A4%9A%E5%B0%8D
%E5%A4%9A/
https://www.runoob.com/django/django-orm-2.html

https://www.cnblogs.com/pythonxiaohu/p/5814247.html





                                                                                        251
```

</details>

<details>
<summary>原始文字 P252</summary>

```text
 UPDATE using INNER JOIN


Format:
UPDATE T1
[INNER JOIN | LEFT JOIN] T2 ON T1.C1 = T2. C1
SET T1.C2 = T2.C2,
    T2.C3 = expr
WHERE condition





將cID 為「03」的國文成績改成60 分。


UPDATE `scorelist` SET `score`=60 WHERE `cID`=3 AND `course`=’國文’


將姓名為「簡奉君」的國文成績改成100 分。

UPDATE `students` INNER JOIN `scorelist` ON `students`.`cID`=`scorelist`.`cID` SET
`scorelist`.`score`='100'   WHERE    `students`.`cName`=' 簡 奉 君     '  AND
`scorelist`.`course`='國文'

  Delete using INNER JOIN
Format:
DELETE T1, T2

FROM T1
INNER JOIN T2 ON T1.key = T2.key
WHERE condition;


將姓名簡奉君的學生資料與成績全部刪除。

DELETE   `students`,`scorelist`  FROM   `students`  INNER  JOIN   `scorelist`  ON
`students`.`cID`=`scorelist`.`cID` WHERE `students`.`cName`="簡奉君"



參考資料:

http://www.mysqltutorial.org/mysql-update-join/
https://www.yiibai.com/mysql/update-join.html





                                                                                          252
```

</details>

<details>
<summary>原始文字 P253</summary>

```text
                                  授課教師：葉呈祥


3-14 Cookies 與Sessions

  使用者在瀏覽網頁時並不是一直與伺服器保持在連線的狀態下，事實上當瀏
覽者送出需求到伺服器端處理後將結果回傳顯示，就已經結束與伺服器的連線。
所以當需要新資料或是更新顯示內容時，都必須重新載入頁面或是重新送出需
求。
  但遇到在網站運作上有些需要「維持記憶」的狀況時，例如記住當前登入使
用者的資訊，或是保持在購物車裡未結帳的商品以供下次繼續使用時，該怎麼辦？
Cookie 與 Session 的存在就是為了要解決網站不能保存狀態的問題。
  以一般網站最常見的會員系統來說，當會員以帳號密碼登入系統的同時，程
式可以有二個方式來記住登入會員的資料：一個方法是在登入者的電腦中放入一
個小檔案來記憶，這個就是 Cookie；另一個方法是在伺服器的記憶體產生一個
空間來記憶，這個就是 Session。





  當瀏覽者在成功登入後，在載入頁面的同時程式即可調出用戶端的Cookie
或是伺服器端的Session 來檢查並維特登入的狀態。當使用者要離開時，程式只
要清除用戶端的Cookie 或是伺服器端的Session，即可將原來的狀態清除。


 建立環境

  建立Django 專案:

# cd ~/dvds

# source ./dvds/dvdsenv/bin/activate (啟動虛擬環境)

# django-admin startproject CookieSession (建立project1 專案)


 關於 Cookie

    Cookie 是儲存在瀏覽者電腦中的小檔案，可以用來識別使用者的身份或是
相關資訊。因為是放置在用戶端的電腦，瀏覽者不必與伺服器溝通即可取得其中
的資訊，免除與伺服器之間多餘的連線。例如瀏覽者將未結帳的商品放置在購物
車中，中途可能因故離開或是關閉瀏覽器，都能藉由 Cookie 的幫忙在下一次回





                                                                                        253
```

</details>

<details>
<summary>原始文字 P254</summary>

```text
到原網站操作時，調出未結帳的商品繼續購物。
    Cookie 放置在瀏覽者的電腦中能保持一段較長的時間，在Cookie 未消失前
都能正確記錄資訊，撘配程式的應用即可免隱重複輸入資料的麻煩。例如當登入
會員系之後，程式則將該使用者的資訊紀入在Cookie 中，即使關閉瀏覽器後重
新開啟原來的頁面，該使用者依然能夠因為Cookie 的幫忙維持登入的狀態。
    Cookie 的限制：
           1. 目前每個瀏覽器最多只能儲存 300 個 cookie。
           2. 每個瀏覽器對單一網站只能儲存 20 的 cookie。
           3.  每個Cookie 的大小最多僅4k Bytes 的容量。
           4. 用戶端電腦的 cookie 只要關閉就沒辦法使用。


    Cookie 在使用時較讓人擔心的是資訊安全，因為它是以明確的方式儲存在
使用者的電腦中，有可能被擷取進行不當的利用。所以若記綠的資訊較為機密，
如帳號密碼、信用卡卡號等，就不適合。


 關於 Session

  當瀏覽者進入網站伺服器瀏覽時，在 Session 的開啟狀態下即會開始記錄使
用者所賦予的資訊，一直到關閉瀏覽器才結束 Session 的使用。在安全性的考量
下，許多人在設計程式時都會使用Session 而不用Cookie。因為Session 是產生
在伺服器端的，不易遭人利用進行其他的操作。在程式運作正常的考量下，Session
因為存在伺服器端，即使用戶端的瀏覽器關閉Cookie 的使用時，Session 仍可正
常運作。


  Cookie 的使用

Cookie 是將狀態資料記錄在用戶端電腦的技術，當瀏覽者開啟網站時即可在程
式的設定下將指定的資料儲存在用戶端電腦中，並可以設定該資料的有效時間、
存放路徑與有效網域。以下我們將介紹如何存取 Cooke 與設定 Cookie 的有效
時間。


     儲存Cookie 資料
格式如下：
set_cookie(key, value=’’, max_age=None, expires=None)
參數
key     變數名稱
value     值
max_age   持續時間，單位為秒





                                                                                          254
```

</details>

<details>
<summary>原始文字 P255</summary>

```text
                                  授課教師：葉呈祥


expires    到期時間





其中expires 是使用UTC(世界協調時間，Coordinated Universal Time)，在時刻上
儘量接近於格林威治標準時間。


Ex:
from django.http import HttpResponse
response = HttpResponse('TestCookie')
response.set_cookie(TestCookie,”這是cookie 內容”)
設定有效持續1 小時：
from django.http import HttpResponse
response = HttpResponse('TestCookie')
response.set_cookie(TestCookie,”這是cookie 內容”, max_age=3600)


     讀取Cookie 資料
Request.COOKIES[“名稱”]


範例：儲存並顯示Cookie 值


新增瀏覽位置(urls.py):

# sudo vim CookieSession/urls.py





新增view functions：




                                                                                        255
```

</details>

<details>
<summary>原始文字 P256</summary>

```text
# sudo vim CookieSessionApp/views.py





測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8080

按「F12」，開啟「開發人員工具」





                                                                                          256
```

</details>

<details>
<summary>原始文字 P257</summary>

```text
                                  授課教師：葉呈祥




新增瀏覽位置(urls.py):

# sudo vim CookieSession/urls.py





新增view functions：

# sudo vim CookieSessionApp/views.py





測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8080





Cookie 字典:
Cookie 的格式是字典，因此可以迴圈方式從字典的items()項目中，取得字典的




                                                                                        257
```

</details>

<details>
<summary>原始文字 P258</summary>

```text
key 與value。


新增瀏覽位置(urls.py):

# sudo vim CookieSession/urls.py





新增view functions：

# sudo vim CookieSessionApp/views.py





測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8080





      Cookie 的有效時間
當您關閉瀏覽器再重新開啟瀏覽器執行該程式，會發現原來儲存的Cookie 值已
消失，程式又必須重新加入。若想要保持Cookie 的存在，就必須設定Cookie 的
持續時間。





                                                                                          258
```

</details>

<details>
<summary>原始文字 P259</summary>

```text
                                  授課教師：葉呈祥

設定Cookie 的持續時間：
持續時間1 小時：
response.set_cookie(“TestCookie”,”內容”,max_age=3600)


設定到期時間：
tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
tomorrow = datetime.datetime.replace(tomorrow, hour=0, minute=0, second=0)
expires =  datetime.datetime.strftime(tomorrow,  “%a, %d-%b-%Y %H:%M:%S
GMT”)
response.set_cookie(“counter”, counter, expires= expires)


刪除Cookie：
delete_cookie[名稱]
Ex:
from django.http import HttpResponse
response = HttpResponse(‘Delete Cookie’)
response.delete_cookie(‘TestCookie’)


範例：設定Cookie 的持續時間

新增瀏覽位置(urls.py):

# sudo vim CookieSession/urls.py





新增view functions：

# sudo vim CookieSessionApp/views.py





                                                                                        259
```

</details>

<details>
<summary>原始文字 P260</summary>

```text
測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8080





關閉瀏覽起後再開啟此頁，cookie 的name 變數一樣會在





                                                                                          260
```

</details>

<details>
<summary>原始文字 P261</summary>

```text
                                  授課教師：葉呈祥





範例：顯示使用者今天瀏覽本頁面的次數

新增瀏覽位置(urls.py):

# sudo vim CookieSession/urls.py





新增view functions：

# sudo vim CookieSessionApp/views.py





測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8080




                                                                                        261
```

</details>

<details>
<summary>原始文字 P262</summary>

```text
  Session 的使用

Session 是瀏覽者與伺服器連線工作期間所保持的狀態，它的使用時間是在開啟
瀏覽器後進入啟動Session 機制的網站開始，只是Session 沒有到期，回到原網站
時會發現原來的Session 仍然有效。


Session 的運作原理：
當使用者使用瀏覽器連線到伺服網站時，網站伺服器會自動派發一個SessionID
給這次的連線動作，網站程式即可依照這個SessionID 分辨使用者來處理所儲存
的狀態。事實上：在預設的狀態下，Session 會將伺服器所派發的SessionID 加密
處理後以Cookie 的方式儲存在用戶端來記錄狀態，同一個站的不同網頁可以藉
由這個Cookie 的記錄來維持同一個SessionID 的狀態。


     安裝Session APP
使用Session，必須安裝Session 的APP。

# vim CookieSession/CookieSession/settings.py





     存取Session 資料
可以使用request 物件的sesson()函式，以字典方式存取session 資料。



                                                                                          262
```

</details>

<details>
<summary>原始文字 P263</summary>

```text
                                  授課教師：葉呈祥


儲存Session 資料：request.session[名稱]=值
讀取Session 資料：變數=request.session[名稱]


範例：儲存並顯示Session 值

新增瀏覽位置(urls.py):

# sudo vim CookieSession/urls.py





新增view functions：

# sudo vim CookieSessionApp/views.py





測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8080





                                                                                        263
```

</details>

<details>
<summary>原始文字 P264</summary>

```text
其中，Session 將伺服器所派發的SessionID 加密處理後以Cookie 的方式儲

存在用戶端，它的名稱是sessionid，內容是一個編碼過的字串。





Session 字典:
Session 的格式是字典，因此可以迴圈方式從字典的items()項目中，取得字典的
key 與value。


新增瀏覽位置(urls.py):

# sudo vim CookieSession/urls.py





新增view functions：

# sudo vim CookieSessionApp/views.py





測試結果：




                                                                                          264
```

</details>

<details>
<summary>原始文字 P265</summary>

```text
                                  授課教師：葉呈祥


# sudo python3 manage.py runserver 0.0.0.0:8080





範例：利用Session 防止灌票
利用Session 可以防止灌票動作，可以重新整頁面幾次，或是關閉瀏覽器後重新
啟動瀏覽，瀏覽的次數不會一直累加。

新增瀏覽位置(urls.py):

# sudo vim CookieSession/urls.py





新增view functions：

# sudo vim CookieSessionApp/views.py





測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8080





                                                                                        265
```

</details>

<details>
<summary>原始文字 P266</summary>

```text
      Session 的有效時間

參數        意義              預設值
SESSION_EXPIRE_AT_  決定session 是否在關閉時結束。若  False
BROWSER_CLOSE   設為True，在瀏覽器關閉後，該
                       session 將會自動結束。
SESSION_COOKIE_AG  session(cookie)的有效時間          1209600 秒，兩週
E


EX:
注意:要將cookie 刪除才可以測試
設定瀏覽器關閉時結束，Session 即自動結束

SESSION_EXPIRE_AT_BROWSER_CLOSE=True


設定Session 最大的有效時間為24 分

SESSION_COOKIE_AGE=1440


設定Session 持續時間為5 分

Request.session.set_expiry(50*60)


     刪除Session
刪除指定的Session
del request.session[名稱]
刪除所有的Session

del request.clear()



範例：設定Session 持續時間




                                                                                          266
```

</details>

<details>
<summary>原始文字 P267</summary>

```text
                                  授課教師：葉呈祥




新增瀏覽位置(urls.py):

# sudo vim CookieSession/urls.py





新增view functions：

# sudo vim CookieSessionAPP/views.py





測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8080





                                                                                        267
```

</details>

<details>
<summary>原始文字 P268</summary>

```text
30 秒後就自動消失：





新增一個seesion，再將seesion 刪除





                                                                                          268
```

</details>

<details>
<summary>原始文字 P269</summary>

```text
                                  授課教師：葉呈祥





範例：會員系統的登入與登出


新增瀏覽位置(urls.py):

# sudo vim CookieSession/urls.py





新增view functions：

# sudo vim CookieSessionAPP/views.py





                                                                                        269
```

</details>

<details>
<summary>原始文字 P270</summary>

```text
測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8080





                                                                                          270
```

</details>

<details>
<summary>原始文字 P271</summary>

```text
                                  授課教師：葉呈祥


3-15 使用者管理

在django.contrib 套件的auth 應用程式中，已內建，user 使用者的資料表，使用
這個內建的資料表就可以記錄使用者的資訊。以is_authenticated 可以檢使用者是
否認證過。如果是user 物件會傳回true，而AnonymousUser 物件則回傳false。
auth.lgoin()接收request、user 兩個參數，登入成功後會產生一個Session，因為這
個Session 的存在，使得該使用者可以跨頁面保存。auth.logout()可以進行登出動
作，登出後，原來的Session 將會被清除。


 建立環境

  建立Django 專案:

# cd ~/dvds

# source ./dvds/dvdsenv/bin/activate (啟動虛擬環境)

# django-admin startproject login (建立login 專案)


 讀取Django auth 使用者

使用auth 就可以達到使用者驗證的動作，其中的User 資料表就是使用者用戶的
資料，可以利用models 模組的objects.get()和objects.all()方法讀取資料。


範例：輸入會員姓名，判斷是否為使用者用戶

新增瀏覽位置(urls.py):

# sudo vim login/urls.py





新增view functions：

# sudo vim loginapp/views.py




                                                                                        271
```

</details>

<details>
<summary>原始文字 P272</summary>

```text
測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8080





  HttpRequest.user 物件

HttpRequest 物件中包含了一個user 屬性，利用HttpRequest.user 可以取得一個
User 物件或是一個AnonymousUser 物件，利用這個物件可以判斷是否已經登錄。
如果是User 物件代表該使用者已經登入，就是具名用戶，如果是AnonymousUser
物件代表該使用者未登入，就是匿名用戶。





User 物件中的常用屬性:




                                                                                          272
```

</details>

<details>
<summary>原始文字 P273</summary>

```text
                                  授課教師：葉呈祥



屬性      說明


username    使用者的帳號，由字母、數字和底線組成


is_anonymous   是否是匿名用戶，永遠回傳False，若為AnonymousUser 物件，則永遠回傳True


is_authenticated  用戶是否認證過，永遠回傳True，若為AnonymousUser 物件，則永遠回傳False


first_name    名字


last_name    姓氏


email      電子郵箱


password     加密(經編碼)過後的密碼


is_staff      真假值，若為True，該用戶可登入admin 後端


is_active     真假值，若為True，該用戶可登入


is_superuser   真假值，若為True，該用戶擁有全權限


last_login    用戶上一次登入的日期與時間


date_joined   用戶被創建的日期與時間

is_active 屬性可以設定該使用者是否有效，若設定為False 該帳號將失敗，即使
帳號、密碼均正確以auth.authenticate 驗證仍會傳回None。如果帳號不使用，
建議以is_active=False 設定讓帳號失效，而不要直接刪除帳號。


User 物件中的常用方法:

屬性          說明


get_username()      取得用戶帳號


get_full_name()      回傳完整的姓名


get_short_name()     只回傳名字


set_password(password)   設定密碼，會自動編碼加密，不包含User 物件的儲存


check_password(password) 確認密碼，正確會回傳True，會自動編碼加密才比較





                                                                                        273
```

</details>

<details>
<summary>原始文字 P274</summary>

```text
範例：新增使用者

新增瀏覽位置(urls.py):

# sudo vim login/urls.py





新增view functions：

# sudo vim loginapp/views.py





測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8080

登入127.0.0.1:8080/useradd/，畫面如下





                                                                                          274
```

</details>

<details>
<summary>原始文字 P275</summary>

```text
                                  授課教師：葉呈祥





再重新整理，畫面如下:





 登入和登出

登入驗證：
利用auth 物件內的authenticate 方法，可以完成使用者登入驗證。
user= auth.authenticate (username=帳號, password=’密碼’)
若密碼正確，會回傳具名的User 物件，否則回傳None。
user.is_active 可檢查帳戶是否有效，若False 表示失效，即使帳號密碼正確，以
auth. authenticate 驗證仍會傳回None。





登入：

auth.login(request, user)





                                                                                        275
```

</details>

<details>
<summary>原始文字 P276</summary>

```text
登入成功後，會產生session，因為這個session 的存在，使用該使用者可以跨頁
面保存，直到登出時刪除該session 為止。通過驗證使用者以user 物件進行登入。


If user.is_active:
     auth.login(request, user)


登出：
auth.logout()可進行登出動作，登出後，原來的session 即會被清除。

auth.logout(request)



範例：使用者登入和登出

新增瀏覽位置(urls.py):

# sudo vim login/urls.py





新增view functions：

# sudo vim loginapp/views.py





                                                                                          276
```

</details>

<details>
<summary>原始文字 P277</summary>

```text
                                  授課教師：葉呈祥





auth.authenticate()此方法預設，若帳號或密碼錯誤，或者帳號與密碼正確，

但未啟動(user.is_active=False)，會傳回None。因此無法判斷帳號密碼錯

誤或未啟動的差異，因此做以下修改即可判斷之間的差別。

新增參數(settings.py):

# sudo vim login/settings.py

AUTHENTICATION_BACKENDS =

['django.contrib.auth.backends.AllowAllUsersModelBackend']





參考文獻：

https://www.cnblogs.com/yoyoketang/p/13192138.html




                                                                                        277
```

</details>

<details>
<summary>原始文字 P278</summary>

```text
新增template index.html：

# sudo vim templates/index.html





新增template login.html：

# sudo vim templates/login.html





測試結果：

# sudo python3 manage.py runserver 0.0.0.0:8080





                                                                                          278
```

</details>

<details>
<summary>原始文字 P279</summary>

```text
                                  授課教師：葉呈祥





  Registration 小專案(會員註冊與登入)

結果如下：





                                                                                        279
```

</details>

<details>
<summary>原始文字 P280</summary>

```text
280
```

</details>

<details>
<summary>原始文字 P281</summary>

```text
授課教師：葉呈祥





                      281
```

</details>

<details>
<summary>原始文字 P282</summary>

```text
      Layout 參考
1、HTML/CSS 寫的簡單的註冊頁面

https://www.796t.com/content/1545570916.html


2、Registration form Bootstrap 5 Registration form componen

https://mdbootstrap.com/docs/standard/extended/registration/#docsTabsOverview


     How to add phone number to django user model?





                                                                                          282
```

</details>

<details>
<summary>原始文字 P283</summary>

```text
                                  授課教師：葉呈祥





http://139.155.2.227/di-qi-zhang-ff1a-zhong-jian-jian-he-zi-kuang-jia/di-er-jie-ff1a-yo
ng-hu-mo-xing.html


注意，自訂User 資料表後，要新增兩個位置要新增參數:
1、





2、





                                                                                        283
```

</details>

<details>
<summary>原始文字 P284</summary>

```text
      Django 變更模型(Models)過程中易出現的問題及解決方案
1、Adding custom fields to users in Django





刪除資料庫，再用以下指令重建





                                                                                          284
```

</details>

<details>
<summary>原始文字 P285</summary>

```text
                                  授課教師：葉呈祥





範例:專案UserCreationForm01



Bootstrap 4:


Colors:
https://getbootstrap.com/docs/4.0/utilities/colors/



{% comment %}

mt-4:margin-top

mb-5:margin-bottom

text-uppercase: 本文轉換大寫字母

text-muted:用于将元素中的文本设置为灰色

d-flex：這個類表示該元素採用 Flexbox 佈局，可以用於實現靈活的佈局方

案。

justify-content-center：這個類表示該元素的 Flexbox 容器採用水平居中

對齊方式，使其子元素在水平方向上居中對齊。

bg-danger:表示將該元素的背景色設置為"danger"主題顏色，即紅色。



                                                                                        285
```

</details>

<details>
<summary>原始文字 P286</summary>

```text
btn：這個類表示該元素是一個按鈕。

btn-success：這個類表示該按鈕採用定義的 "success" 主題顏色，即綠色。

btn-block：這個類表示該按鈕採用塊級元素（block element）的顯示方式，

佔據整個容器的寬度，以便更好地適應不同的屏幕尺寸。

btn-lg：這個類表示該按鈕採用大號（large）的樣式。

text-body：這個類表示該按鈕中的文本採用默認的文字顏色和字體大小，通常

是 Bootstrap 中定義的黑色和 16px。

{% endcomment %}





                                                                                          286
```

</details>



## 附錄：其餘六份講義的閱讀限制與原稿疑點

以下包括原稿錯字、版本差異、裁切缺失與圖像辨讀限制；各頁正文有完整解釋。它們不全是尚未讀懂的內容，也不代表已執行全部範例。

- **ENV-P007**：SECRET_KEY完整值被截圖裁切，無法讀取；與教學修改無關。
- **ENV-P010**：靜態檔案文件網址右側裁切，只記錄可見4.1版本與前段。
- **ENV-P013**：頁首ipconfig說明部分字被水印／破碎字形干擾，僅抄清楚內容。
- **ENV-P013**：紅箭頭遮住若干環境路徑片段，venv1由P014完整對話框交叉核對。
- **ENV-P015**：未顯示環境變數外層視窗，無法確認是使用者還是系統Path。
- **ENV-P016**：launch.json預設註解中的Microsoft文件網址右側被裁切，不猜完整URL。
- **PS-P001**：原稿未顯示變更確認與執行結果；沒有Activate.ps1路徑。
- **WEB-P001**：Javacript、Tomact、chrom拼字不完整；資料庫平台與規模只屬簡化分類。
- **API-P001**：Apache/Flask層級不同；json_encode位置不能解讀為MySQL自動編碼。
- **API-P002**：原圖拼字realy；未畫Pi請求箭頭或硬體腳位，不能推造輪詢/推播。
- **API-P003**：192.168.58.x是示意非有效IPv4；沒有API實作碼或安全規格。
- **DB-P023**：原頁未附實線／斷續底線的鍵符號圖例，故不能確定各線型在此頁的完整PK/FK語意；已保留外觀、不強行推定。
- **DB-P052**：原稿本頁由C系列課程代碼改為A系列，未說明原因；已忠實保留並標示差異。
- **DB-P053**：本頁沿用A系列而非前段C系列課碼；原稿未交代改碼理由。
- **AI-P013**：節名California Housing，但頁面為假設資料。
- **AI-P016**：總120筆僅顯示19筆；節名與台灣行政區資料不相符。
- **AI-P017**：正文類別示例不同於截圖；基準台中市西屯區為對照推論。
- **AI-P019**：未提供全部測試集與分割隨機種子。
- **AI-P025**：圖未標逐點數值，不從像素杜撰精確資料；未提供CSV模型完整指標。
- **AI-P026**：LE02.py完整內容及原始120筆CSV未在本段展示，未重跑驗證。
- **AI-P027**：Leweb與下一頁Lewweb不一致
- **AI-P028**：原提示詞專案名Lewweb與第27頁不同；未展示完整網站程式
- **AI-P032**：155與175同距離，教材未交代第三鄰居tie-breaking
- **AI-P034**：奇數K無平手為過度概括，已加註適用條件
- **AI-P034**：第五鄰居150與180同距離未說明取捨
- **AI-P035**：未展示knn01.py原始碼
- **AI-P037**：無knn02完整程式或Mac執行證據
- **AI-P038**：output改data之搬移操作未展示
- **AI-P039**：頂端啟動命令右側被截斷，不補造
- **AI-P041**：文字64×64與8×8操作關係未完整交代
- **AI-P042**：截圖BMP與文字PNG副檔名不同
- **AI-P043**：28×28註解與8×8流程矛盾，常數未在本頁定義
- **AI-P044**：784維註解與64維訓練輸出矛盾
- **AI-P045**：左欄和註解64×64、實際展示程式128×128不一致
- **AI-P045**：被視窗遮住程式不補造
- **AI-P046**：當次待測2完整路徑未在畫面明示
- **AI-P047**：train1000之每類或總數未明示；test數未指定
- **AI-P047**：未揭露生成方法
- **AI-P049**：捲動遮住的更早imports不補造
- **AI-P049**：下排部分檔名被截斷
- **AI-P050**：全訓練數與完整超參數未展示
- **AI-P051**：頁首sample01縮圖3、下方同檔名執行圖6，講義未交代時點差異
- **AI-P051**：本頁無最終預測結果，不推斷
- **AI-P052**：講義顯示尺寸文字與後續程式128x128顯示用尺寸不同。
- **AI-P053**：背景終端歷史命令小字未逐字轉錄；截圖舊註解28x28與實際64x64設定不一致。
- **AI-P055**：截圖28x28註解未同步更新。
- **AI-P061**：註解仍有28x28及784舊值，與64x64設定不一致。
- **AI-P066**：docstring沿用28x28/784，與實際模型64x64/4096不一致。
- **AI-P067**：64x64顯示註解與128x128參數不符。
- **AI-P069**：頁面只顯示mhtml名稱，未有可確定的外部網址。
- **AI-P071**：程式下緣在Base64解碼附近截斷，predict_digit全文未展示；docstring28x28是舊值。
- **AI-P072**：未展示index.html後段JavaScript；沒有伺服器啟動輸出。
- **AI-P073**：PDF未收錄提示所要求的完整index.html全文。
- **AI-P074**：截圖未展示JavaScript後段及本頁未顯示錯誤本體。
- **AI-P075**：DOCTYPE前後空白因排版不同；缺HTTP狀態/回應本文，不能唯一確認CSRF根因。
- **AI-P076**：背景docstring仍殘留28x28；截圖成功不代表本次實際運行網站。


## 附錄：其餘六份講義原始文字層對照

文字層依原稿保留；圖形／截圖的知識已在正文逐頁解讀。以下不是可直接執行的完整程式碼。


### 原始文字：《Django平台建置(windows) by venv(P).pdf》

<details>
<summary>原始文字 ENV-P001</summary>

```text
3-1 Django 平台建置(windows) 
 
 
 
 
 若已裝多個python 版本： 
 
 
 
 
 
 
 
若已裝兩種版本的python，也新增到環境變數中。
# python -–version (查看當下版本，Windows PATH 決定)
# python –V (查看當下版本，Windows PATH 決定)
如果有安裝多個Python，可以查看所有版本：
# py -0 
 
 
# py –V (由Python Launcher (C:\Windows\py.exe) 控制，可以透過 
py.ini 設定預設版本) 
PDNob
www.pdnob.com
```

</details>

<details>
<summary>原始文字 ENV-P002</summary>

```text
 
方法一：每次指定版本（最簡單，推薦） 
# py -3.9 (每次指定版本) 
方法二：修改 Python Launcher 的預設版本 
新增文件「C:\Users\tony\AppData\Local\py.ini」 
 
 
 
 
[defaults] 
python=3.14 
# py -V 
PDNob
www.pdnob.com
```

</details>

<details>
<summary>原始文字 ENV-P003</summary>

```text
 
 
 
 利用venv 建立虛擬環境： 
 
 
 
 
 
 
方法一:使用目前預設Python：
# python -m venv venv1
方法二（指定Python 版本）
# py -0 
 
# py -3.9 -m venv venv2 
 
啟動虛擬環境，venv1 
# cd c:\venv1 
# Scripts\activate 
 
 
 
呼叫 Python直譯器
執行某個特定的內建模組→venv(虛擬環境)
資料夾名稱
啟動虛擬環境
PDNob
www.pdnob.com
```

</details>

<details>
<summary>原始文字 ENV-P004</summary>

```text
 
# deactivate(離開虛擬環境) 
 
啟動虛擬環境，venv2 
 
 
 
 
# deactivate(離開虛擬環境) 
 
 
開發django 流程 
# python -m venv venv1 
# cd c:\venv1 
# Scripts\activate 
 
 
PDNob
www.pdnob.com
```

</details>

<details>
<summary>原始文字 ENV-P005</summary>

```text
 
 
 
 
 
安裝Django 套件：
# pip install Django
# pip list 
 
 
建立專案： 
# Django-admin startproject project1 
 
建立應用程式： 
# cd project1 
# python manage.py startapp myapp 
# mkdir templates 
# mkdir static 
下載套件的工具
安裝
套件清單檢視工具
開始一個新專案
資料夾名稱=專案的名字
Django專屬的管理員指令，執行建立專案、管理資料庫等全域性的任務
變更目前工作目錄
請 python 呼叫總管
建立新的應用程式（App）
建立templates的資料夾，用來放網頁前端畫面檔案(.html檔案)
建立static的資料夾，用來放網站的靜態檔案
PDNob
www.pdnob.com
```

</details>

<details>
<summary>原始文字 ENV-P006</summary>

```text
 
 
利用vscode 開啟與修改settings.py 
 
 
 
 
PDNob
www.pdnob.com
```

</details>

<details>
<summary>原始文字 ENV-P007</summary>

```text
 
 
ALLOWED_HOSTS = ['*'] 
 
 
INSTALLED_APPS = [ 
    'django.contrib.admin', 
    'django.contrib.auth', 
    'django.contrib.contenttypes', 
    'django.contrib.sessions', 
    'django.contrib.messages', 
    'django.contrib.staticfiles', 
    'myapp', 
] 
允許任何網域或 IP 位址的電腦連線參觀
已安裝應用程式清單，新功能要寫進清單，讓Django總管看到它
PDNob
www.pdnob.com
```

</details>

<details>
<summary>原始文字 ENV-P008</summary>

```text
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
TEMPLATES = [
{
'BACKEND': 'django.template.backends.django.DjangoTemplates',
'DIRS': [BASE_DIR / 'templates'],
'APP_DIRS': True,
'OPTIONS': {
'context_processors': [
'django.template.context_processors.debug',
'django.template.context_processors.request',
'django.contrib.auth.context_processors.auth',
'django.contrib.messages.context_processors.messages',
],
},
},
] 
Django設定網頁外觀的大字典
目錄列表
專案的根目錄
資料夾名稱
PDNob
www.pdnob.com
```

</details>

<details>
<summary>原始文字 ENV-P009</summary>

```text
 
 
LANGUAGE_CODE = 'zh-Hant' 
TIME_ZONE = 'Asia/Taipei' 
 
 
 
STATIC_URL = 'static/' 
STATICFILES_DIRS = [ 
    BASE_DIR / 'static', 
] 
繁體中文
網站預設語言環境的參數
管理時間與日期的參數
靜態檔案搜尋路徑清單
資料夾名稱
專案的根目錄
PDNob
www.pdnob.com
```

</details>

<details>
<summary>原始文字 ENV-P010</summary>

```text
 
 
 
 
以系統管理身分執行(PowerShell or VScode) 
 
 
 
 
 
 
# set-executionpolicy remotesigned
# get-executionpolicy -list
說明:PowerShell 更改執行原則 
Windows系統管理員設定PowerShell執行安全權限的指令
安全等級名稱，遠端下載的腳本必
須經過數位簽署才能執行，但本機
寫的腳本則可以直接執行
列出目前電腦中各個層級的權限分別是什麼狀態
調整後，LocalMachine（整台電腦）˚
CurrentUser（目前使用者）要變RemoteSigned
PDNob
www.pdnob.com
```

</details>

<details>
<summary>原始文字 ENV-P011</summary>

```text
Reference: 
https://learn.microsoft.com/zh-
tw/powershell/module/microsoft.powershell.core/about/about_exe
cution_policies?view=powershell-7.4 
 
 
 
 
 
 
# python manage.py makemigrations myapp (建立migration 資料檔)
# python manage.py migrate (模型與資料庫同步) 
 
or 
把在程式碼裡設計好的表格結構，轉換並寫進 myapp/migrations/ 資料夾裡的
專屬紀錄檔案，這份檔案就是未來的施工藍圖↓
資料庫遷移藍圖同步與結構更新
PDNob
www.pdnob.com
```

</details>

<details>
<summary>原始文字 ENV-P012</summary>

```text
 
 
#python manage.py runserver 0.0.0.0:8080 
 
Or 
 
 
Django 用來開機架站的指令，把網站跑在本地端
對所有網路開放
使用8080連接埠對外提供
服務，避免和其他程式衝撞
PDNob
www.pdnob.com
```

</details>

<details>
<summary>原始文字 ENV-P013</summary>

```text
 
 
設定vscode 要啟用那個虛擬環境: 
方法一(手動): 
 
 
127.0.0.1:8080 → 自己電腦關起門來自己看
實體IP:8080 → 模擬外部連線
ipconfig可✏䴩䫖㩆查詢ipἴ何
PDNob
www.pdnob.com
```

</details>

<details>
<summary>原始文字 ENV-P014</summary>

```text
 
 
 
 
方法二(新增環境變數): 
PDNob
www.pdnob.com
```

</details>

<details>
<summary>原始文字 ENV-P015</summary>

```text
 
 
新增組態（目的讓vscode 知道使用什麼平台）： 
 
 
 
PDNob
www.pdnob.com
```

</details>

<details>
<summary>原始文字 ENV-P016</summary>

```text
 
 
 
 
 
 
 
 
孺在 VS Code 裡面，只要按一下綠色播放鍵（或除錯按鈕），電腦能自動執行開機指令
PDNob
www.pdnob.com
```

</details>

<details>
<summary>原始文字 ENV-P017</summary>

```text
 
 
PDNob
www.pdnob.com
```

</details>


### 原始文字：《PowerShell更改執行原則.pdf》

<details>
<summary>原始文字 PS-P001</summary>

```text
進入虛擬環境(PowerShell): 
以系統管理身分執行(PowerShell or VScode) 
 
# set-executionpolicy remotesigned 
# get-executionpolicy -list 
說明:PowerShell 更改執行原則 
Reference: 
https://learn.microsoft.com/zh-
tw/powershell/module/microsoft.powershell.core/about/about_exe
cution_policies?view=powershell-7.4
```

</details>


### 原始文字：《網頁語言簡介P.pdf》

<details>
<summary>原始文字 WEB-P001</summary>

```text
前端
HTML(定義網頁內容)
JavaScript(定義網頁行為)
VBScript(IE)
CSS(定義網頁外觀)
後端
Database
PHP, Laravel MVC (PHP)
ASP.NET, ASP MVC (C#)
JSP/Servlet, Spring MVC(JAVA)
Flask, Django MVT (Python)
Javacript
Access(小型)(Windows)
SQLite(小型)(Linux)
MySQL(中型)(Linux, Windows)
MS-SQL(中型)(Windows Server)
Oracle(大型)(Linux)
----------------------
NoSQL
----------------------
第三方服務
Thingspeak
firebase
SQL指令
ORM
解析前端:
瀏覽器
chrom
edge 
ie
safari
Web Server:
Node.js (Javacript)
Apache or Nginx(PHP)
IIS(C#)
Tomact(JAVA)
Flask 
Django
MVC模式:Model–view–controller
ORM: Object Relational Mapping
```

</details>


### 原始文字：《api.pdf》

<details>
<summary>原始文字 API-P001</summary>

```text
Database
(MySQL)
WEB Server
(Apache or 
flask)
Client
Android app
App inventor
Pi
HTML
Postman
Arduino
url request
POST or 
GET
json decode
select
json_encode
insert
update
delete
```

</details>

<details>
<summary>原始文字 API-P002</summary>

```text
Database
(MySQL)
WEB Server
(Apache or 
flask)
Client
PI+Python
json decode
select
json_encode
PC(192.168.58.106)
PI(192.168.58.40)
realy
```

</details>

<details>
<summary>原始文字 API-P003</summary>

```text
Database
(MySQL)
WEB Server
WEB API
(Apache)
Client
PI+Python
json decode
select
json_encode
PC(192.168.58.106)
PI(192.168.58.40)
realy
Client
PHP+MySQL
select
add
Client
Android
url request
POST or 
GET
json decode
手機(192.168.58.x)
```

</details>


### 原始文字：《資料庫正規化.pdf》

<details>
<summary>原始文字 DB-P001</summary>

```text
第四章
資料庫正規化
課程名稱：資料庫系統
```

</details>

<details>
<summary>原始文字 DB-P002</summary>

```text
本章學習目標
1.讓讀者瞭解資料庫正規化的概念及目的。
2.讓讀者瞭解資料庫正規化(Normalization)
程序及規則。
```

</details>

<details>
<summary>原始文字 DB-P003</summary>

```text
本章內容
4-1正規化的概念
4-2 正規化的目的
4-3 功能相依(Functional Dependence; FD)
4-4 資料庫正規化(Normalization)
```

</details>

<details>
<summary>原始文字 DB-P004</summary>

```text
前言
㇐般的初學者在進行資料庫設計時，以為用㇐個資料表就可以儲存
全部的資料，或憑著自己的直覺而沒有經過完整的規劃，就隨意的將資
料表分割成許多小的資料表，這種設計方法，不但浪費儲存空間，更嚴
重影響到資料庫不㇐致的現象，以致於DBA(資料庫管理師)維護困難。
為了避免以上的問題產生，唯㇐的方法，就是在設計關聯式資料庫之前，
㇐定先要完成資料的正規化(Normalization)。
```

</details>

<details>
<summary>原始文字 DB-P005</summary>

```text
4-1  正規化的概念
資料庫是用來存放資料的地方，因此，如何妥善的規劃資料庫綱要
( Database Schema )是㇐件很重要的工作，但是，資料庫綱要的設計
必須要配合實務上的需要，因此，當資料庫綱要設計完成後，如何檢視
設計是否良好，就必需要使用正規化(Normalization)的方法論了。
何謂正規化(Normalization)？就是結構化分析與設計中，建構
「資料模式」所運用的㇐個技術，其目的是為了降低資料的「重覆性」
與避免「更新異常」的情況發生。
因此，就必須將整個資料表中重複性的資料剔除，否則在關聯表中
會造成新增異常、刪除異常、修改異常的狀況發生。
```

</details>

<details>
<summary>原始文字 DB-P006</summary>

```text
4-2 正規化的目的
㇐般而言，正規化的精神就是讓資料庫中重複的欄位資料減到最少，
並且能快速的找到資料，以提高關聯性資料庫的效能。
【目的】
1.降低資料重複性(Data Redundancy)。
2.避免資料更新異常(Anomalies)。
```

</details>

<details>
<summary>原始文字 DB-P007</summary>

```text
㇐、降低資料重複性(Data Redundancy)
正規化的目的是什麼呢？簡單來說，就是降低資料重複的狀況發生。
試想，當校務系統的「學籍資料」分別存放在「教務處」與「學務處」
時，不僅資料重覆儲存，浪費空間，更嚴重的是，當學生姓名變更時，
就必須要同時更改「教務處」與「學務處」的「學籍資料」，否則將導
致資料不㇐致的現象，因此，資料庫如果沒有事先進行正規化，將會增
加應用系統撰寫的困難，同時也會增加資料庫的處理負擔，所以降低資
料重複性是「正規化」的重要工作。
```

</details>

<details>
<summary>原始文字 DB-P008</summary>

```text
【方法】
將「教務處」與「學務處」中，把相同的資料項，抽出來組成㇐個新的資料表
(學籍資料表)，如下圖所示：
正規化：將兩個表格切成三個資料表
說明：在正規化之後，「學籍資料表」的主鍵(P.K.)分別與「學務處資料表」的
外鍵(F.K.)及「教務處資料表」的外鍵(F.K.)進行關聯，以產生關聯式資料庫。
```

</details>

<details>
<summary>原始文字 DB-P009</summary>

```text
二、避免資料更新異常(Anomalies)
(㇐)新增異常(Insert Anomalies)
新增某些資料時必須同時新增其他的資料，否則會產生新增異常現象。
亦即在另㇐個實體的資料尚未插入之前，無法插入目前這個實體的資料。
(二)修改異常(Update Anomalies)
修改某些資料時必須㇐併修改其他的資料，否則會產生修改異常現象。
(三)刪除異常(Delete Anomalies)
刪除某些資料時必須同時刪除其他的資料，否則會產生刪除異常現象。
亦即刪除單㇐資料列造成多個實體的資訊遺失。
```

</details>

<details>
<summary>原始文字 DB-P010</summary>

```text
【實例】
假設某國立大學開設「網路碩士學分班」，其學員課程收費表如下所示。
學員課程收費表
【說明】在上面的學員課程收費表中雖然僅僅只有三個欄位，但是已不算是
㇐個良好的儲存結構，因為此表格中有資料重覆現象。
【例如】有些課程的費用在許多學員身上重覆出現(S0001與S0003；S0002與
S0005)，因此可能會造成錯誤或不㇐致的異常(Anomalies)現象。
【分析】從下㇐頁開始
學號
課號
學分費
S0001
C001
3000
S0002
C002
4000
S0003
C001
3000
S0004
C003
5000
S0005
C002
4000
學員的選課需知如下：
1. 每㇐位學員只能選修㇐門課程。
2. 每㇐門課程均有收費標準。(C001為3000元，
C002為4000元，C003為5000元)
```

</details>

<details>
<summary>原始文字 DB-P011</summary>

```text
【分析】三種可能的異常(Anomalies)現象
(㇐)新增異常
假設學校又要新增C004課程，但此課程無法立即新增到資料表中，
除非至少有㇐位學員選修了C004這門課程。
```

</details>

<details>
<summary>原始文字 DB-P012</summary>

```text
(二)修改異常
假如C002課程的學分費由4000元調整為4500元時，若「C002課
程」有多位學員選修時，因此，修改「S0002」學員的學分費時，可能
有些記錄未修改到(S0005)，造成資料的不㇐致現象。
```

</details>

<details>
<summary>原始文字 DB-P013</summary>

```text
(三)刪除異常
假設學員S0004退選時，同時也刪除C003這門課程，由於該課程
只有S0004這位學員選修，因此若把這㇐筆記錄刪除，從此我們將失去
C003這門課程及其學分費的資訊。
```

</details>

<details>
<summary>原始文字 DB-P014</summary>

```text
【解決方法】正規化
由於上述的分析，發現學員課程收費表並不是㇐個良好的儲存結構，因
此，我們就必須要採用4-4節所要討論的正規化，將學員課程收費表分
割成兩個資料表，即「選課表」與「課程收費對照表」，因此，才不會
發生上述的異常現象。
學號
課號
學分費
S0001
C001
3000
S0002
C002
4000
S0003
C001
3000
S0004
C003
5000
S0005
C002
4000
課程收費表
學號
課號
S0001
C001
S0002
C002
S0003
C001
S0004
C003
S0005
C002
選課表
課號
學分費
C001
3000
C002
4000
C003
5000
課程收費對照表
正規化
正規化
```

</details>

<details>
<summary>原始文字 DB-P015</summary>

```text
4-3 功能相依(Functional Dependence; FD)
㇐、功能相依的概念
【定義】
是指資料表中各欄位之間的相依性。亦即某欄位不能單獨存在，必
須要和其他欄位㇐起存在時才有意義，稱這兩個欄位具有功能相依。
【例如】學生資料表
【說明】
在上面的資料表中, 「姓名」欄位的值必須搭配「學號」欄位才有意義, 
則我們說『姓名欄位相依於學號欄位』。
姓名
學號
性別
系所
電話
地址
```

</details>

<details>
<summary>原始文字 DB-P016</summary>

```text
換言之，在「學生資料表」中，「學號」決定了「姓名」，也決定了
「性別」、「系所」、「電話」、「地址」等資訊，我們可以用以下圖
示的方法來表示這些功能相依性。
【分析】
1. 學號→ 姓名
2. 學號→ {姓名，性別，系所，電話，地址}
3. 學號：為決定因素(∵學號姓名)
4. 姓名，性別，系所，電話，地址：為相依因素
因此，「學號」欄位為主鍵, 做為唯㇐辨識該筆記錄的欄位。「姓名」欄位
必須要相依於「學號」欄位, 對此資料表來說「姓名」欄位才有意義；同理可證,
「地址」欄位亦必須相依於「學號」欄位, 才有意義。
```

</details>

<details>
<summary>原始文字 DB-P017</summary>

```text
二、功能相依(FD)的表示方式
1.假設有㇐個資料表R，並且有三個欄位，分別為X,Y,Z，因此，我們就
可以利用㇐條數學式來表示：R={X,Y,Z}
2.假設在R={X,Y,Z}數學式中，X和Y之間存在「功能相依」時，並且
存在Y功能相依於X，則我們可以利用以下的表示式：
(1) Y 
X   (Y功能相依於X)
(2) XY    (X決定Y)
若XY時，在FD的左邊X稱為決定因素(Determinant)
在FD的右邊Y稱為相依因素(Dependent)
3.示意圖：
學號(X)
姓名(Y)
```

</details>

<details>
<summary>原始文字 DB-P018</summary>

```text
4-3.1 完全功能相依
（Full Functional Dependency）
【定義】
假設在關聯表R(X,Y,Z)中，包含㇐組功能相依(X,Y)Z，如果我們從關
聯表R中移除任㇐屬性X或Y時，則使得這個功能相依(X,Y)Z不存在，
此時我們稱Z為「完全功能相依」於(X,Y)。
反之，若(X,Y)Z存在，我們稱Z為「部份功能相依」於(X,Y) 。
【例如】
{學號(X)，課號(Y)} → 成績(Z)
這是「完全功能相依」
如果從關聯表中移除課號(Y)，則功能相依(X)Z不存在
因為，「學號」和「課號」兩者㇐起決定了「成績」，缺㇐不可。
否則，只有㇐個學號對應㇐個成績，無法得知該成績是那㇐門課程的分數。
亦即成績(Z)完全功能相依於{學號(X)，課號(Y)}
```

</details>

<details>
<summary>原始文字 DB-P019</summary>

```text
4-3.2 部份功能相依
（Partial Functional Dependency）
【定義】
假設在關聯表R(X,Y,Z)中包含㇐組功能相依(X,Y)Z，如果我們從關聯
表R中移除任㇐屬性X或Y時，則使得這個功能相依(X,Y)Z存在，此時
我們稱Z為「部份功能相依」於(X,Y)。
【例如】
{學號(X) ，身份證字號(Y)} → 姓名(Z)
這是「部份功能相依」
如果從關聯表中移除身份證字號(Y)，則功能相依(X)Z存在
因為，「學號」也可以決定「姓名」，他們之間也具有功能相依性。
```

</details>

<details>
<summary>原始文字 DB-P020</summary>

```text
4-3.3 遞移相依
（Transitive Dependency）
【定義】
是指在二個欄位間並非直接相依, 而是借助第三個欄位來達成資料
相依的關係。
【例如】
Y 相依於X；而Z 又相依於Y, 如此X 與Z 之間就是遞移相依的關係。
【示意圖】
在上面的關聯表R(X,Y,Z)中包含㇐組相依XY,YZ，則XZ，此時我
們稱Z遞移相依於X。
```

</details>

<details>
<summary>原始文字 DB-P021</summary>

```text
【舉例】
課程代號→ 老師編號
老師編號→ 老師姓名
這是遞移相依
因為，「課程代號」可以決定「老師編號」，並且「老師編號」又可以
決定「老師姓名」，因此，「課程代號」與「老師姓名」之間存在遞移
相依性。
遞移相依性
```

</details>

<details>
<summary>原始文字 DB-P022</summary>

```text
4-4 資料庫正規化(Normalization)
【定義】
是指將原先關聯(表格)的所有資訊，在「分解」之後，仍能由數個新關
聯(表格)中經過「合併」得到相同的資訊。即所謂的「無損失分解
(Lossless decomposition)」的觀念。
【無損失分解觀念】
當關聯表R被「分解」成數個關聯表R1, R2, …, Rn 時，則可以再透過
「合併」R1     R2      …      Rn得到相同的資訊R。如下圖所示。
分解
合併
合併
合併
分解
分解
```

</details>

<details>
<summary>原始文字 DB-P023</summary>

```text
【實例】
分解
合併
註：分解：是指透過「正規化」技術，將㇐個大資料表分割成二個小資料表。
《本章介紹》
合併：是指透過「合併」理論，將數個小資料表整合成㇐個大資料表。
《第八章介紹》
```

</details>

<details>
<summary>原始文字 DB-P024</summary>

```text
4-4.1 正規化示意圖
正規化就是對㇐個「非正規化」的原始資料表，進行㇐連串的「分割」，
並且分割成數個「不重複」儲存的資料表。如下圖所示：
在上圖中，利用㇐連串的「分割」，亦即利用所謂的「正規化的規則」，
循序漸進的將㇐個「重複性高」的資料表分割成數個「重複性低」或
「沒有重複性」的資料表。
分割
```

</details>

<details>
<summary>原始文字 DB-P025</summary>

```text
4-4.2 正規化的規則
引言
資料庫在正規化時會有㇐些規則，並且每條規則都稱為「正規形
式」。如果符合第㇐條規則，則資料庫就稱為「第㇐正規化形式
(1NF)」。如果符合前二條規則，則資料庫就被視為屬於「第二正規化
形式(2NF)」。雖然資料庫的正規化最多可以進行到第五正規化形式，
但是在實務上，BCNF被視為大部分應用程式所需的最高階正規形式。
```

</details>

<details>
<summary>原始文字 DB-P026</summary>

```text
從上圖中，我們可以清楚得知，正規化是循序漸進的過程，亦即資
料表必須滿足第㇐正規化的條件之後，才能進行第二正規化。換言之，
第二正規化必須建立在符合第㇐正規化的資料表上，依此類推。
```

</details>

<details>
<summary>原始文字 DB-P027</summary>

```text
正規化步驟
在資料表正規化的過程(1NF 到BCNF) 中, 每㇐個階段都是以欄位的
「相依性」, 做為分割資料表的依據之㇐。其完整的正規化步驟如下圖
所示：
```

</details>

<details>
<summary>原始文字 DB-P028</summary>

```text
正規化步驟<續>
1.第㇐正規化(First Normal Form; 1NF) ：由E.F.Codd 提出。
滿足所有記錄中的屬性內含值都是基元值(Atomic Value)。
即無重覆項目群。
2.第二正規化(Second Normal Form; 2NF) ：由E.F.Codd 提出。
符合1NF且每㇐非鍵值欄位「完全功能相依」於主鍵。
即不可「部分功能相依」於主鍵。
3.第三正規化(Third Normal Form; 3NF) ：由E.F.Codd 提出。
符合2NF且每㇐非鍵值欄位非「遞移相依」於主鍵。
即除去「遞移相依」問題。
```

</details>

<details>
<summary>原始文字 DB-P029</summary>

```text
正規化步驟<續>
4.Boyce-Codd正規化型式(Boyce-Codd Normal Form ;BCNF) ：
由R.F. Boyce 與E.F.Codd 共同提出。
符合3NF且每㇐決定因素(Determinant)皆是候選鍵，簡稱為BCNF。
5.第四正規化(Fourth Normal Form; 4NF) ：由R. Fagin 提出。
符合BCNF，再除去所有的多值相依。
6.第五正規化(Fifth Normal Form; 5NF) ：由R. Fagin 提出。
符合4NF，且沒有合併相依。
```

</details>

<details>
<summary>原始文字 DB-P030</summary>

```text
4-4.3  第㇐正規化(1NF)
【定義】
是指在資料表中的所有記錄之屬性內含值都是基元值(Atomic Value)。
亦即無重覆項目群。
【實例】
假設現在有㇐份某某科技大學的學生選課資料表，如表4-1(a)所示：
表4-1(a) 學生選課資料表
```

</details>

<details>
<summary>原始文字 DB-P031</summary>

```text
我們可以將表4-1(a)的原始資料利用二維表格來儲存，如表4-1(b)。
表4-1(a) 學生選課資料表
表4-1(b)未正規化的資料表：學生選課資料報表二維表格來儲存
```

</details>

<details>
<summary>原始文字 DB-P032</summary>

```text
但是，我們發現有許多屬性的內含值都具有二個或二個以上的值(亦稱
為重複資料項目)，其原因：尚未進行第㇐正規化。
表4-1(b)未正規化的資料表：學生選課資料報表
■未符合1NF 資料表的「缺點」
以上資料表中的『課程代碼』、『課程名稱』、『學分數』、『必選
修』、『成績』、『老師編號』及「老師姓名」欄位的⾧度無法確定，
因為學生要選修多少門課程，無法事先得知(李碩安同學選了2門，李碩崴同學
選了3門)，因此，必須要預留很大的空間給這七個欄位, 如此反而造成儲
存空間的浪費。
重複資料項目
```

</details>

<details>
<summary>原始文字 DB-P033</summary>

```text
第㇐正規化的規則
1.每㇐個欄位只能有㇐個基元值(Atomic)即單㇐值。
例如：課程名稱欄位中不能存入兩科或兩科以上的課程名稱。
2. 沒有任何兩筆以上的資料是完全重覆。
3.資料表中有主鍵, 而其他所有的欄位都相依於「主鍵」。
例如1：姓名與性別欄位都相依於「學號」欄位。
例如2：課程名稱、學分數、必選修、老師編號及老師姓名相依於「課程代
碼」欄位。
例如3：「成績」欄位相依於「學號」與「課程代碼」欄位。
《深入探討在下㇐頁》
```

</details>

<details>
<summary>原始文字 DB-P034</summary>

```text
《深入探討》
Q：為什麼「成績」欄位㇐定要相依於「學號」與「課程代碼」欄位？
分析㇐：
如果「成績」欄位本身單獨存在時，則沒有意義，因為只有「成績」卻無法讓
同學或老師清楚得知該「成績」是屬於哪㇐位學生的哪㇐門課的成績。
分析二：
如果「成績」欄位只相依於「課程編號」也是沒有意義的，因為只有「成績」
也是無法讓同學或老師清楚得知該「成績」是屬於哪㇐位學生所修課的成績。
課程代碼
成績
C001
74
C002
93
沒有意義
成績
74
93
沒有意義
```

</details>

<details>
<summary>原始文字 DB-P035</summary>

```text
分析三：
如果「成績」欄位只相依於「學號」也是沒有意義的，因為只有「成績」也是
無法讓同學或老師清楚得知該「成績」是屬於哪㇐門課的成績。
分析四：
但是，如果「成績」欄位相依於「課程編號」及「學號」二個欄位時, 就可
以了解某個學生修某堂課的成績, 這樣的成績資料才有意義。
學號
課程代碼
成績
001
C001
74
001
C002
93
有意義
學號
成績
001
74
001
93
沒有意義
```

</details>

<details>
<summary>原始文字 DB-P036</summary>

```text
第㇐正規化的作法：
【作法】將重複的資料項分別儲存到不同的記錄中, 並加上適當的主鍵。
步驟㇐：檢查是否存在「重複資料項」
```

</details>

<details>
<summary>原始文字 DB-P037</summary>

```text
步驟二：將重複資料項分別儲存到不同的記錄中, 並加上適當的主鍵
未經正規化前的學生選課表
經過正規化後的學生選課表(1NF)
重複資料項
儲存到不同的記錄
```

</details>

<details>
<summary>原始文字 DB-P038</summary>

```text
經過正規化後的學生選課表(1NF)
在經由第㇐正規化之後，使得每㇐個欄位內只能有㇐個資料(基元值)。
雖然增加了許多記錄, 但每㇐個欄位的「⾧度」及「數目」都可以固定, 
而且我們可用「課程代碼」欄位加上「學號」欄位當作主鍵,使得在查詢
某學生修某課程的「成績」時, 就非常方便而快速了。
```

</details>

<details>
<summary>原始文字 DB-P039</summary>

```text
4-4.4 第二正規化(2NF)
在完成了第㇐正規化之後，讀者是否發現在資料表中產生許多重複
的資料。如此, 不但浪費儲存的空間, 更容易造成新增、刪除或更新資料
時的異常狀況，說明如下。
(1) 新增異常檢查(Insert Anomaly)
無法先新增課程資料，如「課程代碼」及「課程名稱」，要等選課之後，才能新增。
原因：以上的新增動作違反「實體完整性規則」，因為，主鍵或複合主鍵不可以為空值
NULL。
```

</details>

<details>
<summary>原始文字 DB-P040</summary>

```text
(2)修改異常檢查(Update Anomaly)
「網頁設計」課程重覆多次，因此，修改「網頁設計」課程的成績時，
可能有些記錄未修改到，造成資料的不㇐致現象。
例如：有選「網頁設計」課程的同學之成績各加5分，可能會有些同學
有加分，而有些同學卻沒有加分，導致資料不㇐致的情況。
```

</details>

<details>
<summary>原始文字 DB-P041</summary>

```text
(3)刪除異常檢查(Delete Anomaly)
當刪除#4學生的記錄時，同時也會刪除課程名稱、學分數及相關的資料。
所以導致「計概」課程的2學分數也同時被刪除了。
綜合上述的三種異常現象，所以, 我們必須進
行「第二階正規化」, 來消除這些問題。
```

</details>

<details>
<summary>原始文字 DB-P042</summary>

```text
第二正規化的規則
如果資料表符合以下的條件, 我們說這個資料表符合第二階正規化的形
式(Second Normal Form, 簡稱2NF)：
符合1NF
每㇐非鍵屬性(如：姓名、性別…)必須「完全相依」於主鍵(學號)；即
不可「部分功能相依」於主鍵。
換言之，「部分功能相依」只有當「主鍵」是由「多個欄位」組成
時才會發生(亦即複合主鍵)，也就是當某些欄位只與「主鍵中的部分欄
位」有「相依性」, 而與另㇐部分的欄位沒有相依性。
```

</details>

<details>
<summary>原始文字 DB-P043</summary>

```text
第二正規化的作法
分割資料表；亦即將「部分功能相依」的欄位「分割」出去，
再另外組成「新的資料表」。其步驟如下：
步驟㇐：檢查是否存在「部分功能相依」
「姓名」只相依於「學號」
「課程名稱」只相依於「課程代碼」
在上面的資料表中，主鍵是由「學號+課程代碼」兩個欄位所組成，但「姓名」和「性別」只
與「學號」有「相依性」，亦即(姓名，性別)相依於學號，而「課程名稱」只與「課程代碼」有
「相依性」，亦即(課程名稱，學分數，必選修，老師編號，老師姓名)相依於課程代碼。
因此，學號是複合主鍵(學號,課程代碼)的㇐部份。
∴存在部分功能相依。
```

</details>

<details>
<summary>原始文字 DB-P044</summary>

```text
步驟二：將「部分功能相依」的欄位分割出去，再另外組成新的資料表
我們將「選課資料表」分割成三個較小的資料表(加「底線」的欄位為
主鍵)：
㇐、學生資料表(學號，姓名，性別)
二、成績資料表(學號，課程代碼，成績)
學號
姓名
性別
001
李碩安
男
002
李碩崴
男
學號
課程代碼
成績
001
C001
74
001
C002
93
002
C002
63
002
C003
82
002
C005
94
```

</details>

<details>
<summary>原始文字 DB-P045</summary>

```text
三、課程資料表(課程代碼，課程名稱，學分數，必選修，
老師編號，老師姓名)
在第二正規化之後，產生三個資料表，分別為學生資料表、成績資料表
及課程資料表，除了「課程資料表」之外，其餘兩個資料表(學生資料
表與成績資料表)都已符合2NF, 3NF及BCNF。
課程代碼
課程名稱
學分數
必選修
老師編號
老師姓名
C001
程式語言
4
必
T001
李安
C002
網頁設計
3
選
T002
張三
C003
計
概
2
必
T003
李四
C005
網路教學
4
選
T005
王五
```

</details>

<details>
<summary>原始文字 DB-P046</summary>

```text
4-4.5 第三正規化(3NF)
在完成了第二正規化之後，其實還存在以下三種異常現象,亦即新增、刪
除或更新資料時的異常狀況，說明如下：
(1)新增異常(Insert Anomaly)
以上無法先新增老師資料，要等確定課程代碼之後，才能輸入。
原因為：新增動作違反「實體完整性規則」，因為主鍵或複合主鍵不可以為空值NULL。
```

</details>

<details>
<summary>原始文字 DB-P047</summary>

```text
(2)修改異常(Update Anomaly)
假如「李安」老師開設多門課程時，則欲修改「李安」老師姓名為
「李碩安」時，可能有些記錄未修改到，造成資料的不㇐致現象。
未修改到
```

</details>

<details>
<summary>原始文字 DB-P048</summary>

```text
(3)刪除異常(Delete Anomaly)
當刪除#1課程的記錄時，同時也刪除老師編號T001。
所以導致老師編號T001及老師姓名的資料也同時被刪除了。
綜合上述的三種異常現象，所以, 我們必須進
行「第三階正規化」, 來消除這些問題。
記錄
課程代碼
課程名稱
學分數
必選修
老師編號
老師姓名
#1
C001
程式語言
4
必
T001
李安
#2
C002
網頁設計
3
選
T002
張三
#3
C003
計
概
2
必
T003
李四
#4
C005
網路教學
4
選
T005
王五
```

</details>

<details>
<summary>原始文字 DB-P049</summary>

```text
第三正規化的規則
如果資料表符合以下條件, 我們就說這個資料表符合第三階正規化的形
式(Third Normal Form, 簡稱3NF)：
符合2NF
各欄位與「主鍵」之間沒有「遞移相依」的關係。
【注意】
若要找出資料表中各欄位與「主鍵」之間的遞移相依性, 最簡單的方法
就是從左到右掃瞄資料表中各欄位有沒有『與主鍵無關的相依性』存在。
可能的情況如下：
1.如果有存在時，則代表有「遞移相依」的關係
2.    如果有不存在時，則代表沒有「遞移相依」的關係
```

</details>

<details>
<summary>原始文字 DB-P050</summary>

```text
第三正規化的作法
分割資料表；亦即將「遞移相依」或「間接相依」的欄位「分割」
出去，再另外組成「新的資料表」。其步驟如下：
步驟㇐：檢查是否存在「遞移相依」
由於每㇐門課程都會有授課的老師,因此，「老師編號」相依於「課程代
碼」。並且「老師姓名」相依於「教師編號」,因此，存在有『與主鍵無
關的相依性』。亦即存在「老師姓名」與主鍵(課程代碼)無關的相依性。
∴存在遞移相依。
```

</details>

<details>
<summary>原始文字 DB-P051</summary>

```text
上述「課程資料表」中的[課程名稱]、[學分數]、[必選修]、[老師編號]
都直接相依於主鍵[課程代碼](簡單的說，這些都是課程資料的必需欄位
)，而[老師名稱]是直接相依於[老師編號]，然後才間接相依於[課程代碼
]，它並不是直接相依於[課程代碼]，稱為「遞移相依」『Transitive 
Dependency』或「間接相依」。例如：當AB, BC，則AC(稱為遞
移相依)。因此，在「課程資料表」中存在「遞移相依」關係現象，
```

</details>

<details>
<summary>原始文字 DB-P052</summary>

```text
步驟二：將「遞移相依」的欄位「分割」出去，再另外組成「新的資料表」
因此，我們將「課程資料表」分割為二個資料表，並且利用外鍵
(F.K.)來連接二個資料表。如下圖所示。
```

</details>

<details>
<summary>原始文字 DB-P053</summary>

```text
在我們完成第三正規化後，共產生了四個表格，如下表所示：
第三正規化後的四個表格
第二正規化產生的表格
第三正規化產生的表格
```

</details>


### 原始文字：《20260907AI應用(20260915).pdf》

<details>
<summary>原始文字 AI-P001</summary>

```text
授課教師：葉呈祥 
~ 1 ~ 
第四章 機器學習分類器 ........................................................................ 2 
4.1 機器學習演算法分類 .................................................................................... 2 

 
監督式學習（Supervised Learning） ........................................... 2 

 
非監督式學習（Unsupervised Learning） .................................. 3 

 
線性預測（Linear Prediction） .................................................... 4 

 
線性模型特色 ................................................................................ 5 

 
建議的教學順序（適合初學者） ................................................ 6 
4.2 Linear Regression： ......................................................................................... 7 

 
說明 ................................................................................................ 7 

 
房價預測1（California Housing） ............................................. 12 

 
房價預測2（California Housing） ............................................. 15 

 
房價預測(已訓練好模型+Django Web) ..................................... 27 
4.2 KNN（K-Nearest Neighbors，K 最近鄰演算） ............................................ 31 

 
說明 .............................................................................................. 31 

 
利用身高來判斷男生或女生，使用knn 演算法...................... 32 

 
利用knn 的手寫數字辨識系統(使用學者的資料庫與方法) ... 36 

 
利用knn的手寫數字辨識系統（匯出資料庫成圖片、匯出模型、
測試圖片） .................................................................................................. 37 

 
利用knn 的手寫數字辨識系統修改1(重新產生與訓練資料庫)
 
47 

 
利用knn 的手寫數字辨識系統修改2 ...................................... 55 

 
利用knn 的手寫數字辨識系統 by Django Web ....................... 66
```

</details>

<details>
<summary>原始文字 AI-P002</summary>

```text
~ 2 ~ 
第四章 機器學習分類器 
4.1 機器學習演算法分類 
 
監督式學習（Supervised Learning） 
 
非監督式學習（Unsupervised Learning） 
 
強化式學習（Reinforcement Learning） 
 
 監督式學習（Supervised Learning） 
定義： 
資料已經具有正確答案(Label)，模型利用大量已知答案的資料進行學習，之後預
測新的資料。 
 
 
模型知道答案，因此稱為監督式。 
 
流程： 
資料特徵(X) 模型訓練建立模型新資料預測 
 
監督式主要工作： 
(1) 分類(Classification)，預測是哪一類。 
例如： 
垃圾郵件、正常郵件，貓、狗，數字0~9，好瓜、壞瓜 
 
常見演算法： 
  KNN  
  Decision Tree  
  Random Forest  
  Logistic Regression  
  SVM  
  Naive Bayes
```

</details>

<details>
<summary>原始文字 AI-P003</summary>

```text
授課教師：葉呈祥 
~ 3 ~ 
  XGBoost  
  LightGBM  
  CNN（影像）  
  RNN/LSTM（時間序列）  
  Transformer（文字） 
 
(2) 回歸(Regression)，預測數值 
例如： 
房價、股票價格、溫度、銷售額 
 
常見演算法： 
 
Linear Regression  
 
Polynomial Regression  
 
Ridge  
 
Lasso  
 
Elastic Net  
 
SVR  
 
Random Forest Regression  
 
XGBoost Regression 
 
 
 非監督式學習（Unsupervised Learning） 
定義： 
沒有Label，只有大量資料，希望讓電腦自己找出規律。 
 
例如：10000 位客戶資料、沒有標示VIP、沒有標示一般客戶，模型自己分群。 
 
流程： 
資料(X)沒有答案(Label)找規律得到群組 
 
常見工作： 
(1) 分群(Clustering) 
 
例如： 
電商，學生A、學生B、學生C...，自動分成 
第一群、第二群、第三群、
```

</details>

<details>
<summary>原始文字 AI-P004</summary>

```text
~ 4 ~ 
常見演算法： 
 
K-Means 
 
GMM 
 
DBSCAN 
 
Hierarchical Clustering 
 
Mean Shift 
 
(2) 降維 
目的：將很多特徵，例如1000 個特徵，變成20 個特徵 
方便：視覺化、降低運算量、去除雜訊 
 
常見演算法： 
 
PCA 
 
t-SNE 
 
UMAP 
 
(3) 異常偵測 
例如： 
信用卡盜刷、設備故障、網路攻擊 
演算法： 
 
Isolation Forest  
 
One-Class SVM  
 
LOF 
 
 線性預測（Linear Prediction） 
線性預測通常指線性模型（Linear Models），屬於監督式學習，主要用於建立輸
入與輸出之間的線性關係。 
定義： 
假設資料之間可以用一直線（或超平面）表示： 
 
其中：x：特徵（Feature）、w：權重（Weight）、b：偏差（Bias）、y：預測值 
 
模型的目標是找到最合適的權重與偏差，使預測結果最接近真實值。
```

</details>

<details>
<summary>原始文字 AI-P005</summary>

```text
授課教師：葉呈祥 
~ 5 ~ 
常見線性模型： 
(1) 線性迴歸（Linear Regression） 
用途：預測連續數值 
例如：房價預測、氣溫預測、銷售量預測 
 
(2) Logistic Regression（邏輯斯迴歸） 
名稱雖然有「Regression」，實際上是分類演算法。 
用途： 
 
是否違約 
 
是否生病 
 
是否為垃圾郵件 
輸出通常是機率（0～1），再依門檻值分類。 
 
 線性模型特色 
優點： 
 
容易理解與解釋 
 
訓練速度快 
 
適合作為機器學習入門 
 
可分析各特徵的重要影響方向 
 
限制： 
 
假設資料呈線性關係 
 
對複雜的非線性問題表現有限 
 
需要適當的特徵工程才能提升效果
```

</details>

<details>
<summary>原始文字 AI-P006</summary>

```text
~ 6 ~ 
 建議的教學順序（適合初學者） 
1. 機器學習概觀：監督式、非監督式、強化式學習的差異。 
2. 監督式學習：從線性迴歸開始，再介紹分類（Logistic Regression、KNN、
Decision Tree、Random Forest、CNN）。  
3. 非監督式學習：介紹 K-Means、GMM、PCA，讓學生理解資料探索與分群。  
4. 實作案例：  
o Linear Regression：房價預測（Boston Housing 或 California Housing）  
o KNN：手寫數字辨識（MNIST）  
o Random Forest：鳶尾花（Iris）分類  
o CNN：MNIST 手寫數字辨識  
o K-Means：客戶分群  
o PCA：資料降維與視覺化  
這樣的安排能讓學生先理解機器學習的基本概念，再透過代表性的演算法建立完
整的知識架構，並銜接到深度學習（如 CNN）與實際應用。
```

</details>

<details>
<summary>原始文字 AI-P007</summary>

```text
授課教師：葉呈祥 
~ 7 ~ 
4.2 Linear Regression： 
 說明 
Linear Regression（線性迴歸）是一種監督式學習（Supervised Learning）演算法。 
目的：找出 X 與 Y 的線性關係，建立一條最佳直線，用來預測未知資料。
```

</details>

<details>
<summary>原始文字 AI-P008</summary>

```text
~ 8 ~
```

</details>

<details>
<summary>原始文字 AI-P009</summary>

```text
授課教師：葉呈祥 
~ 9 ~
```

</details>

<details>
<summary>原始文字 AI-P010</summary>

```text
~ 10 ~ 
 
 
公式如下：
```

</details>

<details>
<summary>原始文字 AI-P011</summary>

```text
授課教師：葉呈祥 
~ 11 ~
```

</details>

<details>
<summary>原始文字 AI-P012</summary>

```text
~ 12 ~ 
 
 
 房價預測1（California Housing）
```

</details>

<details>
<summary>原始文字 AI-P013</summary>

```text
授課教師：葉呈祥 
~ 13 ~ 
 
 
結果如下:
```

</details>

<details>
<summary>原始文字 AI-P014</summary>

```text
~ 14 ~ 
 
 
流程如下： 
房屋資料(坪數、房價)建立 X、yLinear Regression模型訓練 fit()得到方
程式Y = 100 + 20Xpredict()預測新房價
```

</details>

<details>
<summary>原始文字 AI-P015</summary>

```text
授課教師：葉呈祥 
~ 15 ~ 
 
 
範例:LE01.py 
 
 房價預測2（California Housing） 
原始資料：
```

</details>

<details>
<summary>原始文字 AI-P016</summary>

```text
~ 16 ~ 
 
共120 筆，80%用於訓練，20%用於測試。 
 
使用訓練模型:  
Linear Regression 
 
目標： 
#預測新房子 
例如： 
#中壢區 
#35 坪 
#屋齡 8 年 
#3 房 
#12 樓 
#捷運 400 公尺 
#學校 600 公尺 
#有車位 
預測房價： 1022.9 萬元 
 
流程如下：
```

</details>

<details>
<summary>原始文字 AI-P017</summary>

```text
授課教師：葉呈祥 
~ 17 ~ 
CSV 房價資料 → 讀取資料(pandas) → 資料前處理(文字轉數字) → 建立X/y 
→ 切分Train/Test → 建立Linear Regression → 模型訓練fit() → 模型預測
predict() → 模型評估(MAE、RMSE、R²) → 預測新房價 
 
步驟如下： 
1、讀取csv 資料 
 
2、將文字轉成數字： 
df = pd.get_dummies(df, columns=["行政區"], drop_first=True)  
# 將行政區欄位轉換為虛擬變數，並刪除第一個欄位以避免多重共線性 
例如：行政區_中壢區、行政區_桃園區、行政區_平鎮區、行政區_八德區 
全部變成0、1，方便模型學習。 
 
轉換後如下： 
 
 
Linear Regression 公式：
```

</details>

<details>
<summary>原始文字 AI-P018</summary>

```text
~ 18 ~ 
 
 
3、建立 X、y 
X（Features，特徵、輸入資料）：模型拿來學習的資料
 
 
y（Target，Label、目標值）：模型要預測的答案 
 
 
4、切分Train/Test 
20%的數據用於測試，80%的數據用於訓練 
 
5、建立Linear Regression 與模型訓練fit() 
若只有一個特徵（坪數），模型就是圖形是一條直線。 
如果特徵超過兩個（例如你的模型有 10 個特徵），就變成超平面 (Hyperplane)，
已經無法直接畫在三維空間中。
```

</details>

<details>
<summary>原始文字 AI-P019</summary>

```text
授課教師：葉呈祥 
~ 19 ~ 
 
 
 
6、模型預測與模型預測predict() 
預測資料如下: 
 
 
結果如下: 
 
 
7、模型評估 
 
MAE: mean absolute error(平均絕對誤差)
```

</details>

<details>
<summary>原始文字 AI-P020</summary>

```text
~ 20 ~ 
 
 
RMSE: mean squared error(中文:均方誤差)
```

</details>

<details>
<summary>原始文字 AI-P021</summary>

```text
授課教師：葉呈祥 
~ 21 ~ 
 
 
 
 
8、模型評估(MAE、RMSE、R²)
```

</details>

<details>
<summary>原始文字 AI-P022</summary>

```text
~ 22 ~
```

</details>

<details>
<summary>原始文字 AI-P023</summary>

```text
授課教師：葉呈祥 
~ 23 ~
```

</details>

<details>
<summary>原始文字 AI-P024</summary>

```text
~ 24 ~
```

</details>

<details>
<summary>原始文字 AI-P025</summary>

```text
授課教師：葉呈祥 
~ 25 ~ 
 
 
實際房價與預測房價的圖表結果如下:
```

</details>

<details>
<summary>原始文字 AI-P026</summary>

```text
~ 26 ~ 
# 如果預測效果好，大部分點會靠近紅色對角線。 
 
9、預測新房價： 
 
 
範例:LE02.py
```

</details>

<details>
<summary>原始文字 AI-P027</summary>

```text
授課教師：葉呈祥 
~ 27 ~ 
 房價預測(已訓練好模型+Django Web) 
# pip install Django 
# Django-admin startproject Leweb 
# cd Leweb 
# python manage.py startapp myapp 
# mkdir templates 
# mkdir static 
修改settings.py 
 
ALLOWED_HOSTS = ['*'] 
 
INSTALLED_APPS = [ 
    'django.contrib.admin', 
    'django.contrib.auth', 
    'django.contrib.contenttypes', 
    'django.contrib.sessions', 
    'django.contrib.messages', 
    'django.contrib.staticfiles', 
    'myapp', 
] 
 
TEMPLATES = [ 
    { 
        'BACKEND': 'django.template.backends.django.DjangoTemplates', 
        'DIRS': [BASE_DIR / 'templates'], 
        'APP_DIRS': True, 
        'OPTIONS': { 
            'context_processors': [ 
                'django.template.context_processors.debug', 
                'django.template.context_processors.request', 
                'django.contrib.auth.context_processors.auth', 
                'django.contrib.messages.context_processors.messages', 
            ], 
        }, 
    }, 
]
```

</details>

<details>
<summary>原始文字 AI-P028</summary>

```text
~ 28 ~ 
 
LANGUAGE_CODE = 'zh-Hant' 
 
TIME_ZONE = 'Asia/Taipei' 
 
STATIC_URL = 'static/' 
STATICFILES_DIRS = [ 
    BASE_DIR / 'static', 
] 
 
# python manage.py makemigrations (建立migration 資料檔) 
# python manage.py migrate (模型與資料庫同步) 
# python manage.py runserver 0.0.0.0:8080 
 
 
尋問ChaptGPT: 
欄位名稱: 
坪數,屋齡,房間數,樓層,捷運距離公尺,學校距離公尺,有車位,行政區_台北市信義
區,行政區_台北市大安區,行政區_台南市東區,行政區_新北市新店區,行政區_新
北市板橋區,行政區_桃園市中壢區,行政區_高雄市左營區 
 
資料: 
59.3,23,5,15,1267,1540,1,True,False,False,False,False,False,False 
 
利用Linear Regression 建立模型， 
LinearRegressionModel.pkl 
 
我想建立一個django 網站使用初學者的程式寫法， 
專案名為Lewweb，app 名為myapp 
讓使用者輸入如下的資料:   
new_house = pd.DataFrame({ 
    "坪數":[35], 
    "屋齡":[8], 
    "房間數":[3], 
    "樓層":[12], 
    "捷運距離公尺":[400], 
    "學校距離公尺":[600], 
    "有車位":[1],
```

</details>

<details>
<summary>原始文字 AI-P029</summary>

```text
授課教師：葉呈祥 
~ 29 ~ 
    "行政區_台北市信義區":[0], 
    "行政區_台北市大安區":[0], 
    "行政區_台南市東區":[0], 
    "行政區_新北市新店區":[0], 
    "行政區_新北市板橋區":[0], 
    "行政區_桃園市中壢區":[1], 
    "行政區_高雄市左營區":[0] 
}) 
其中 
"行政區_台北市信義區":[0], 
 
    "行政區_台北市大安區":[0], 
 
    "行政區_台南市東區":[0], 
 
    "行政區_新北市新店區":[0], 
 
    "行政區_新北市板橋區":[0], 
 
    "行政區_桃園市中壢區":[1], 
 
    "行政區_高雄市左營區":[0] 
讓使用者選擇 
最後產生預測房價結果 
 
生成式AI 範例 範例:Django 房價預測網站(LE).mhtml 
 
 
結果:
```

</details>

<details>
<summary>原始文字 AI-P030</summary>

```text
~ 30 ~
```

</details>

<details>
<summary>原始文字 AI-P031</summary>

```text
授課教師：葉呈祥 
~ 31 ~ 
4.2 KNN（K-Nearest Neighbors，K 最近鄰演算） 
 說明 
KNN（K-Nearest Neighbors）是一種監督式學習（Supervised Learning）演算法。
它的核心概念非常直觀：「物以類聚，人以群分」當有一筆新的資料要判斷時，
KNN 會找出距離它最近的 K 個已知資料，再依照這些鄰居的結果進行預測。KNN 
不會先建立數學公式，而是：看附近有哪些資料，再投票決定答案。KNN 最重
要的是計算距離，最常用的是歐氏距離（Euclidean Distance）： 
 
 
 
KNN 的優點： 
 
演算法簡單，容易理解。 
 
不需要建立複雜模型。 
 
適合小型資料集。 
 
可用於分類與迴歸。 
 
KNN 的缺點： 
 
資料量大時，預測速度較慢（需要與所有資料比較距離）。 
 
對雜訊（Noise）較敏感。 
 
K 值選擇會影響結果。 
 
不同特徵尺度差異大時，需先進行資料標準化（Standardization）或正規化
（Normalization）。
```

</details>

<details>
<summary>原始文字 AI-P032</summary>

```text
~ 32 ~ 
 利用身高來判斷男生或女生，使用knn 演算法 
舉例：假設要判斷一個人是男生還是女生。 
 
 
現在來一位新的人、身高 = 165 cm、想知道是男還是女。 
步驟如下：
```

</details>

<details>
<summary>原始文字 AI-P033</summary>

```text
授課教師：葉呈祥 
~ 33 ~
```

</details>

<details>
<summary>原始文字 AI-P034</summary>

```text
~ 34 ~ 
 
 
流程： 
訓練資料不建立公式輸入新資料計算與所有資料的距離找最近 K 個
鄰居投票輸出分類結果 
 
平手問題: 
方法一：K 選奇數（就沒有平手問題） 
方法二：看誰距離最近 
 
 
方法三：距離加權投票（Weighted KNN）
```

</details>

<details>
<summary>原始文字 AI-P035</summary>

```text
授課教師：葉呈祥 
~ 35 ~ 
 
 
程式結果如下： 
 
 
範例：knn01.py
```

</details>

<details>
<summary>原始文字 AI-P036</summary>

```text
~ 36 ~ 
 
 
 
 利用knn 的手寫數字辨識系統(使用學者的資料庫與方法) 
Reference: 
https://archive.ics.uci.edu/ml/datasets/Optical+Recognition+of+Handwritten+Digits 
 
Reference paper: 
Methods of Combining Multiple Classifiers and Their Applications to Handwritten 
Digit Recognition
```

</details>

<details>
<summary>原始文字 AI-P037</summary>

```text
授課教師：葉呈祥 
~ 37 ~ 
 
 
 
 
範例:knn02.py 
 
 利用knn 的手寫數字辨識系統（匯出資料庫成圖片、匯出模型、
測試圖片） 
1、將現有資料庫匯出成圖片： 
尋問chatGPT: 
我是一位初階python 程師 
我的訓練來源為: digits = load_digits() #共有1797 筆資料，每筆資料是8x8 的灰階
圖片，標籤是0~9 的數字。 
 
我想要將資料匯出成圖片檔案，並依照標籤分類存放。 
 
將全部資料存成圖片bmp 檔到output 中的handwritten 資料夾，並分類別存放
「train」、「test」兩類，數量為80%與20%。 
 
另外，要顯示執行完成度、程式寫法mac 也要能使用，請給我程式python 碼。 
 
生成式AI 範例: Python 圖片匯出分類.mhtml 
 
結果如下:
```

</details>

<details>
<summary>原始文字 AI-P038</summary>

```text
~ 38 ~ 
 
 
 
 
範例:knn03.py 
 
 
2、讀取現有的資料庫，再利用KNN 訓練與測試，最後匯出模型「knn_model.pkl」 
尋問chatGPT： 
 
我的訓練與測試資料夾如下: 
data/ 
└── handwritten/ 
    ├── train/                # 訓練資料 
    │   ├── 0/                # 數字 0 
    │   ├── 1/                # 數字 1 
    │   ├── 2/
```

</details>

<details>
<summary>原始文字 AI-P039</summary>

```text
授課教師：葉呈祥 
~ 39 ~ 
    │   ├── ... 
    │   └── 9/ 
    │ 
    └── test/                 # 測試資料 
        ├── 0/ 
        ├── 1/ 
        ├── 2/ 
        ├── ... 
        └── 9/ 
 
內的圖片為.bmp，名稱無固定 
請給我簡單好理解的python 程式，將這些資料讀取。 
利用knn 訓練，再進行測式。 
 
生成式AI 範例: KNN 訓練與測試.mhtml 
 
結果如下：
```

</details>

<details>
<summary>原始文字 AI-P040</summary>

```text
~ 40 ~ 
 
 
 
 
範例:knn04.py
```

</details>

<details>
<summary>原始文字 AI-P041</summary>

```text
授課教師：葉呈祥 
~ 41 ~ 
其中讀取圖片的前處理流程如下： 
開始 
  │ 
  ▼ 
讀取 0~9 資料夾 
  ──► 讀取 BMP 圖片 
  ──► 灰階化 
  ──► 縮放成 8×8 
  ──► 二值化 
  ──► 正規化 (0~1) 
  ──► 攤平成 64 維特徵 
  ──► 加入訓練資料 (X) 
  ──► 加入標籤 (y) 
  ──► 全部圖片完成 
  ──► 回傳 X、y、file_paths 
  ──► 結束 
 
3、讀取「knn_model.pkl」，再利用一樣的前處理方式，預測手繪文字。 
將knn04.py 程式所產生出來的模型，將output 資料夾內的「knn_model.pkl」，放
到data 資料夾內「knn_model.pkl」。 
 
使用小畫家寫出圖片（64x64）並存檔成「hand_sample01.png」 
一定要用圖形大約：8x8（不然縮小後會變形）、背景為黑色、前景白色
```

</details>

<details>
<summary>原始文字 AI-P042</summary>

```text
~ 42 ~ 
 
 
尋問chatGPT: 
def load_images(folder_path): 
    """ 
    讀取資料夾中的 BMP 圖片。 
 
    資料夾格式： 
    folder_path/ 
    ├── 0/ 
    ├── 1/ 
    ├── ... 
    └── 9/ 
 
    回傳： 
    X：圖片資料 
    y：圖片標籤 
    file_paths：圖片路徑 
    """ 
 
    images = [] 
    labels = [] 
    file_paths = [] 
 
    # 依序讀取數字 0 到 9 
    for label in range(10): 
 
        # 例如：data/handwritten/train/0 
        number_folder = os.path.join(folder_path, str(label)) 
 
        # 檢查資料夾是否存在
```

</details>

<details>
<summary>原始文字 AI-P043</summary>

```text
授課教師：葉呈祥 
~ 43 ~ 
        if not os.path.exists(number_folder): 
            print(f"找不到資料夾：{number_folder}") 
            continue 
 
        # 取得資料夾內所有檔案 
        filenames = os.listdir(number_folder) 
 
        # 計算成功讀取的圖片數量 
        image_count = 0 
 
        for filename in filenames: 
 
            # 只處理 BMP 圖片 
            if not filename.lower().endswith(".bmp"): 
                continue 
 
            image_path = os.path.join(number_folder, filename) 
 
            # 以灰階方式讀取圖片 
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE) 
 
 
            # 如果讀取失敗 
            if image is None: 
                print(f"圖片讀取失敗：{image_path}") 
                continue 
 
            # 將圖片統一成 28 x 28 
            image = cv2.resize( 
                image, 
                (IMAGE_WIDTH, IMAGE_HEIGHT) 
            ) 
 
            # 二值化 
            # 大於 127 的像素變成 255 
            # 小於或等於 127 的像素變成 0 
            _, image = cv2.threshold( 
                image,
```

</details>

<details>
<summary>原始文字 AI-P044</summary>

```text
~ 44 ~ 
                127, 
                255, 
                cv2.THRESH_BINARY 
            ) 
 
            # 將像素由 0～255 轉成 0～1 
            image = image.astype("float32") / 255.0 
 
            # 將 28 x 28 圖片攤平成 784 個數字 
            image_data = image.flatten() 
 
            # 儲存圖片資料 
            images.append(image_data) 
 
            # 儲存正確答案 
            labels.append(label) 
 
            # 儲存檔案路徑 
            file_paths.append(image_path) 
 
            image_count += 1 
 
        print(f"數字 {label}：讀取 {image_count} 張圖片") 
 
    # 轉成 NumPy 陣列 
    X = np.array(images) 
    y = np.array(labels) 
 
    return X, y, file_paths 
讀取文字與前處理的程式如下，請產生一個新程式，假設我已建立好的knn 模式
為「./data/knn_model.pkl」 
我新手寫的圖片檔為hand_sample01.png，請讀取此檔並做前處理，再預測 
生成式AI 範例: 手寫數字預測程式.mhtml
```

</details>

<details>
<summary>原始文字 AI-P045</summary>

```text
授課教師：葉呈祥 
~ 45 ~ 
顯示原圖，並放大成 64 
x 64，方便觀看，並顯示
視窗1 
 
將圖片調整成8x8，並
顯示視窗2 
 
二值化，並顯示視窗3 
 
預測結果，並顯示視窗
4
```

</details>

<details>
<summary>原始文字 AI-P046</summary>

```text
~ 46 ~ 
顯示原圖，並放大成 64 
x 64，方便觀看，並顯示
視窗1 
 
將圖片調整成8x8，並
顯示視窗2 
 
二值化，並顯示視窗3 
 
預測結果，並顯示視窗
4
```

</details>

<details>
<summary>原始文字 AI-P047</summary>

```text
授課教師：葉呈祥 
~ 47 ~ 
 
問題： 
1、讀取訓練資料庫圖片太小8x8，容易失真 
 
範例:knn05.py 
 
 利用knn 的手寫數字辨識系統修改1(重新產生與訓練資料庫) 
尋問chatGPT: 
請幫我產生64x64 的手寫資料庫，train1000 張 
data/ 
└── handwritten/ 
    ├── train/                # 訓練資料 
    │   ├── 0/                # 數字 0 
    │   ├── 1/                # 數字 1 
    │   ├── 2/ 
    │   ├── ... 
    │   └── 9/ 
    │ 
    └── test/                 # 測試資料 
        ├── 0/ 
        ├── 1/ 
        ├── 2/ 
        ├── ... 
        └── 9/ 
 
生成式AI 範例:手寫資料庫生成.mhtml 
檔案: handwritten_64x64_dataset.zip 
 
將產生的資料庫複製並重新命名為「handwritten_new」
```

</details>

<details>
<summary>原始文字 AI-P048</summary>

```text
~ 48 ~
```

</details>

<details>
<summary>原始文字 AI-P049</summary>

```text
授課教師：葉呈祥 
~ 49 ~ 
 
 
將knn04.py 程式複製並更名為knn06.py 
將knn05.py 程式複製並更名為knn07.py 
 
更改訓練資料與圖片大小
```

</details>

<details>
<summary>原始文字 AI-P050</summary>

```text
~ 50 ~ 
更改模型儲存成檔案 
 
 
訓練與測試結果: 
 
 
範例:knn06.py
```

</details>

<details>
<summary>原始文字 AI-P051</summary>

```text
授課教師：葉呈祥 
~ 51 ~ 
開啟knn07.py，修改模組來源、測試檔與大小參數 
 
 
手寫文字測試結果如下： 
顯示原圖並放大成 64 x 
64，方便觀看，並顯示視
窗1 
 
將圖片調整成64x64，並
顯示視窗2
```

</details>

<details>
<summary>原始文字 AI-P052</summary>

```text
~ 52 ~ 
二值化，並顯示視窗3 
 
預測結果，並顯示視窗4 
 
 
顯示原圖，並放大成 64 x 
64，方便觀看，並顯示視
窗1 
 
# 將圖片調整成64x64，
並顯示視窗2
```

</details>

<details>
<summary>原始文字 AI-P053</summary>

```text
授課教師：葉呈祥 
~ 53 ~ 
二值化，並顯示視窗3 
 
預測結果，並顯示視窗4
```

</details>

<details>
<summary>原始文字 AI-P054</summary>

```text
~ 54 ~ 
 
 
範例:knn07.py 
問題: 
1、使用的特徵為相對位置，因此背景的資訊容易讓訓練產生錯誤資訊。
```

</details>

<details>
<summary>原始文字 AI-P055</summary>

```text
授課教師：葉呈祥 
~ 55 ~ 
 利用knn 的手寫數字辨識系統修改2 
問題: 
使用的特徵為相對位置，因此背景的資訊容易讓訓練產生錯誤資訊。 
解決: 
將前景字找到邊界並載取出來，再放大成64x64。 
 
將knn04.py 程式複製並更名為knn08.py 
將knn05.py 程式複製並更名為knn09.py 
 
修改成式如下: 
 
 
利用github copilot 修改程式: 
寫註解如下: 
#將前景切割出來，自動產生程式 
#再將大小調整回 IMAGE_WIDTH、IMAGE_HEIGHT 
#show image
```

</details>

<details>
<summary>原始文字 AI-P056</summary>

```text
~ 56 ~ 
 
 
 
 
測試時先跑幾張圖，比較切割前與切割後差異
```

</details>

<details>
<summary>原始文字 AI-P057</summary>

```text
授課教師：葉呈祥 
~ 57 ~
```

</details>

<details>
<summary>原始文字 AI-P058</summary>

```text
~ 58 ~ 
再註解顯示程式，並更改模型輸出名稱，並執行： 
 
 
 
訓練與測試結果:
```

</details>

<details>
<summary>原始文字 AI-P059</summary>

```text
授課教師：葉呈祥 
~ 59 ~ 
 
 
 
範例:knn08.py 
 
結果：明顯提高辨識率
```

</details>

<details>
<summary>原始文字 AI-P060</summary>

```text
~ 60 ~ 
開啟knn09.py，修改模組來源、測試檔、大小參數、取出前景，方法與knn08
相同，如下：
```

</details>

<details>
<summary>原始文字 AI-P061</summary>

```text
授課教師：葉呈祥 
~ 61 ~ 
 
 
 
 
手寫文字測試結果如下： 
顯示原圖並放大成 64 x 
64，方便觀看，並顯示視
窗1
```

</details>

<details>
<summary>原始文字 AI-P062</summary>

```text
~ 62 ~ 
將圖片調整成64x64，並
顯示視窗2 
 
二值化，並顯示視窗3 
 
切割並大小正規化到
64x64，並顯示視窗4
```

</details>

<details>
<summary>原始文字 AI-P063</summary>

```text
授課教師：葉呈祥 
~ 63 ~ 
預測結果，並顯示視窗5 
 
 
顯示原圖並放大成 64 x 
64，方便觀看，並顯示視
窗1 
 
將圖片調整成64x64，並
顯示視窗2
```

</details>

<details>
<summary>原始文字 AI-P064</summary>

```text
~ 64 ~ 
二值化，並顯示視窗3 
 
切割並大小正規化到
64x64，並顯示視窗4 
 
預測結果，並顯示視窗5
```

</details>

<details>
<summary>原始文字 AI-P065</summary>

```text
授課教師：葉呈祥 
~ 65 ~ 
 
 
 
 
範例:knn09.py
```

</details>

<details>
<summary>原始文字 AI-P066</summary>

```text
~ 66 ~ 
 利用knn 的手寫數字辨識系統 by Django Web 
尋問chaptGPT: 
我利用knn 演算法，產生出辨識手寫數字的模型，模型名稱為
「knn_model_new2.pkl」，其中前景為白色、背景為黑色。 
輸入圖片前的前處理程式如下，我想建立一個django 網站使用初學者的程式寫
法，專案名為knnweb，app 名為myapp，讓使用者可以用滑鼠寫數字，利用模
型預測0-9 的數字。 
 
再將程式貼入，如下： 
def preprocess_image(image_path): 
    """ 
    讀取單張手寫數字圖片並進行前處理。 
 
    處理流程： 
    1. 灰階讀取 
    2. 調整成 28 x 28 
    3. 二值化 
    4. 像素轉成 0～1 
    5. 攤平成 784 個數字 
 
    回傳： 
    image_data：提供模型預測的資料 
    processed_image：處理完成的 28 x 28 圖片 
    """ 
 
    # 檢查圖片是否存在 
    if not os.path.exists(image_path): 
        raise FileNotFoundError(f"找不到圖片：{image_path}") 
 
    # 以灰階方式讀取圖片 
    image = cv2.imread( 
        image_path, 
        cv2.IMREAD_GRAYSCALE 
    ) 
 
    ## 顯示並放大成 64 x 64，方便觀看 
    display_image = cv2.resize(
```

</details>

<details>
<summary>原始文字 AI-P067</summary>

```text
授課教師：葉呈祥 
~ 67 ~ 
        image, 
        (128, 128), 
        interpolation=cv2.INTER_NEAREST 
    ) 
    cv2.imshow("Processed Image1", display_image) 
    cv2.waitKey(0) 
 
    # 檢查圖片是否讀取成功 
    if image is None: 
        raise ValueError(f"圖片讀取失敗：{image_path}") 
 
    # 將圖片調整成 64 x 64 
 
    image = cv2.resize( 
        image, 
        (IMAGE_WIDTH, IMAGE_HEIGHT) 
    ) 
 
    ## 顯示並放大成 64 x 64，方便觀看 
    display_image = cv2.resize( 
        image, 
        (128, 128), 
        interpolation=cv2.INTER_NEAREST 
    ) 
    cv2.imshow("Processed Image2", display_image) 
    cv2.waitKey(0) 
 
    # 二值化 
    # 大於 127 的像素變成 255 
    # 小於或等於 127 的像素變成 0 
    _, image = cv2.threshold( 
        image, 
        127, 
        255, 
        cv2.THRESH_BINARY 
    ) 
 
     ## 將前景切割出來
```

</details>

<details>
<summary>原始文字 AI-P068</summary>

```text
~ 68 ~ 
    x, y, w, h = cv2.boundingRect(image) 
    image = image[y:y+h, x:x+w] 
    # 再將大小調整回 IMAGE_WIDTH、IMAGE_HEIGHT 
    image = cv2.resize( 
        image,  
        (IMAGE_WIDTH, IMAGE_HEIGHT) 
    ) 
 
    # show image 
    cv2.imshow("Processed Image3", image) 
    cv2.waitKey(0) 
 
    # 保留一份處理後的圖片，方便顯示 
    processed_image = image.copy() 
 
 
    # 將像素由 0～255 轉成 0～1 
    image = image.astype("float32") / 255.0 
 
    ## 顯示並放大成 64 x 64，方便觀看 
    display_image = cv2.resize( 
        image, 
        (128, 128), 
        interpolation=cv2.INTER_NEAREST 
    ) 
    cv2.imshow("Processed Image4", display_image) 
    cv2.waitKey(0) 
 
    # 將 64 x 64 攤平成 4096 個數字 
    image_data = image.flatten() 
 
    # 模型要求二維資料 
    # 原本：(4096,) 
    # 轉成：(1, 4096) 
 
    image_data = image_data.reshape(1, -1) 
 
    return image_data, processed_image
```

</details>

<details>
<summary>原始文字 AI-P069</summary>

```text
授課教師：葉呈祥 
~ 69 ~ 
 
 
 
生成式ai 範例：Django 手寫數字辨識網站設置／Django 手寫數字辨識網站設置.mhtml 
生成式ai 範例：第一次修改程式 
 
步驟如下： 
# pip install django opencv-python numpy scikit-learn joblib pillow 
1、 
請把模型檔案：knn_model_new2.pkl 放在跟 manage.py 同一層。
```

</details>

<details>
<summary>原始文字 AI-P070</summary>

```text
~ 70 ~ 
 
 
2、修改 knnweb/urls.py 
 
 
3、建立 myapp/urls.py 
 
 
4、撰寫 myapp/views.py
```

</details>

<details>
<summary>原始文字 AI-P071</summary>

```text
授課教師：葉呈祥 
~ 71 ~ 
 
 
5、建立網頁 index.html
```

</details>

<details>
<summary>原始文字 AI-P072</summary>

```text
~ 72 ~ 
 
 
6、
```

</details>

<details>
<summary>原始文字 AI-P073</summary>

```text
授課教師：葉呈祥 
~ 73 ~ 
 
 
尋問chatGPT: 
若此網站換成手機瀏覽，我也希望可以用手機觸碰畫面寫字。 
生成式ai 範例：Django 手寫數字辨識網站設置／Django 手寫數字辨識網站設置.mhtml 
生成式ai 範例：第二次修改程式 
 
 
尋問chatGPT: 
給我index.html 完整程式 
生成式ai 範例：Django 手寫數字辨識網站設置／Django 手寫數字辨識網站設置.mhtml 
生成式ai 範例：第三次修改程式 
 
1、下面是支援「電腦滑鼠」與「手機觸控」的完整index.html
```

</details>

<details>
<summary>原始文字 AI-P074</summary>

```text
~ 74 ~ 
 
 
出現錯誤如下:
```

</details>

<details>
<summary>原始文字 AI-P075</summary>

```text
授課教師：葉呈祥 
~ 75 ~ 
 
 
尋問chatGPT: 
使用手機出現 發生錯誤：SyntaxError: Unexpected token '<', " <!DOCTYPE "... is not valid 
JSON 
1、依照文chatGPT 文件都無錯誤 
2、views.py 的 index 建議加上：
```

</details>

<details>
<summary>原始文字 AI-P076</summary>

```text
~ 76 ~ 
 
 
結果如下:
```

</details>



## 附錄：正規化範例的隔離實測（整理者補充）

從本筆記 DB-P053 的四張 Markdown 表直接抽出資料，在 SQLite 記憶體資料庫建立對應主鍵／外鍵後實測；未連線或修改你的 MySQL。這是驗證本組表格可正確連接，不是僅憑有限資料就證明所有業務規則或正規形式。

- 學生／成績／課程／老師表筆數：{'students': 2, 'scores': 5, 'courses': 4, 'teachers': 4}。
- 四表 JOIN 回傳 5 筆選課成績，保留學號前導零。
- 學號001有 2 種成績；課程A002也有 2 種成績，不能只用其中一個欄位定位個別選課成績。
- 僅在記憶體測試中將T002改為「測試改名」，實際只UPDATE 1 筆老師資料，JOIN後 2 筆相關選課都顯示新名稱。正式筆記中的原稿資料仍保留張三。
- 此處照P053保留A開頭課碼，沒有默默改成前頁的C開頭課碼。

```json
[
  [
    "001",
    "李碩安",
    "男",
    "A001",
    "程式語言",
    "4",
    "必",
    "74",
    "T001",
    "李安"
  ],
  [
    "001",
    "李碩安",
    "男",
    "A002",
    "網頁設計",
    "3",
    "選",
    "93",
    "T002",
    "張三"
  ],
  [
    "002",
    "李碩崴",
    "男",
    "A002",
    "網頁設計",
    "3",
    "選",
    "63",
    "T002",
    "張三"
  ],
  [
    "002",
    "李碩崴",
    "男",
    "A003",
    "計概",
    "2",
    "必",
    "82",
    "T003",
    "李四"
  ],
  [
    "002",
    "李碩崴",
    "男",
    "A005",
    "網路教學",
    "4",
    "選",
    "94",
    "T005",
    "王五"
  ]
]
```


## Sources

[1] https://docs.python.org/3.12/reference/expressions.html
    > "Note that comparisons, membership tests, and identity tests, all have the same precedence"
[2] https://docs.python.org/3.12/library/stdtypes.html
    > "Dictionaries preserve insertion order."
[3] https://docs.python.org/3.12/whatsnew/3.0.html
    > "there is only one built-in integral type"
[4] https://learn.microsoft.com/zh-tw/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.4 — Microsoft Learn：about_Execution_Policies
    > "PowerShell 的執行原則是一項安全功能，可控制 PowerShell 載入組態檔和執行腳本的條件。"
