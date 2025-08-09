import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium", auto_download=["html"])


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Day 1：marimo Notebook 簡介""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""[![Open in molab](https://molab.marimo.io/molab-shield.png)](https://molab.marimo.io/notebooks/nb_6f8De15Pis5Aog9Kyem23A)""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## 什麼是 marimo？

    marimo 是一個開源的 Python 筆記本工具，專為現代資料科學、AI 開發與協作而設計。它強調「反應式（reactive）」、「可重現（reproducible）」、「Git 友善（Git-friendly）」與「AI 原生（AI-native）」等特性，讓你能更高效地撰寫、分享、協作與部署 Python 筆記本。

    marimo 的目標是解決傳統 Jupyter Notebook 在可重現性、版本控制、協作與自動化上的痛點，並提供更現代化的互動體驗。
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## marimo 與 Jupyter Notebook 的差異

    | 特性             | marimo                        | Jupyter Notebook           |
    |------------------|-------------------------------|---------------------------|
    | 檔案格式         | 純 Python (.py)               | JSON (.ipynb)             |
    | 反應式運算       | 支援，cell 依賴自動更新       | 不支援，需手動執行        |
    | 可重現性         | 高，每次執行結果一致           | 低，執行順序易出錯        |
    | Git 友善         | 是，易於版本控制與 diff        | 否，JSON 格式不易比對     |
    | AI 原生          | 內建 AI/LLM 整合              | 需額外安裝套件            |
    | SQL 內建         | 支援                          | 需安裝 magic 指令         |
    | 可部署為 Web App | 是                            | 需額外工具                |
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## marimo 的核心理念""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### 1. 反應式（Reactive）""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""marimo 採用 reactive notebook 架構，當你修改某個 cell 的內容時，所有依賴該 cell 的內容會自動重新計算，確保 notebook 狀態始終一致。""")
    return


@app.cell
def _(mo):
    mo.md("""### 互動式 UI 範例：Slider 與 Textbox""")
    return


@app.cell
def _(mo):
    # 建立一個滑桿 (slider) 讓使用者調整數值
    slider = mo.ui.slider(label="請選擇一個數字", start=0, stop=100, value=50)
    # 建立一個文字輸入框 (text_area)
    text_area = mo.ui.text_area(label="請輸入你的名字", value="marimo user")
    return slider, text_area


@app.cell
def _(slider):
    slider
    return


@app.cell
def _(text_area):
    text_area
    return


@app.cell
def _(slider, text_area):
    number = slider.value
    name = text_area.value
    return name, number


@app.cell
def _(mo, name, number):
    mo.md(f"Hi **{name}**，你選擇的數字是 **{number}**，它的平方是 **{number**2}**。")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### 2. 可重現（Reproducible）""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""傳統的 notebook 存在可重現性危機。2019 年，紐約大學與巴西聯邦弗盧米嫩塞大學的一項[研究發現](https://leomurta.github.io/papers/pimentel2019a.pdf)，在 GitHub 上近 100 萬個具有有效執行順序的 Jupyter notebook 中，只有 24% 能夠重新執行，僅有 4% 能產生相同的結果。2020 年 JetBrains 的[另一項研究](https://blog.jetbrains.com/datalore/2020/12/17/we-downloaded-10-000-000-jupyter-notebooks-from-github-this-is-what-we-learned/#)也指出，GitHub 上超過三分之一的 notebook 具有無效的執行歷史。""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""傳統 notebook 會累積隱藏狀態：當你執行或刪除某個 cell 時，程式的記憶體會被命令式地改變，卻不會考慮頁面上其他程式碼的狀態。這會導致程式碼與輸出結果不同步。雖然這是 REPL（互動式直譯器）的特性之一，但當你想要做出可重現的工作時，這種隱藏狀態反而成為阻礙。""")
    return


@app.cell
def _(mo):
    mo.image(
        src="images/jupyter.JPG",
        alt="傳統 notebook 中的程式碼與輸出結果可能會不同步",
        rounded=True,
        caption="傳統 notebook 中的程式碼與輸出結果可能會不同步",
    )
    return


@app.cell
def _(mo):
    mo.md(r"""在 marimo notebook 中，每個 cell 之間的變數依賴關係會自動追蹤。當你執行某個 cell，marimo 會自動重新執行所有依賴該 cell 的下游 cell，確保執行結果一致，避免傳統 notebook「執行順序錯亂」的問題。""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""example""")
    return


@app.cell
def _():
    # Cell 1
    a = 10
    return (a,)


@app.cell
def _(a):
    # Cell 2
    b = a + 5
    return (b,)


@app.cell
def _(b):
    # Cell 3
    c = b * 2
    print(f"c = {c}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""操作說明：""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""1. 當你修改 Cell 1（例如把 a = 10 改成 a = 20）並執行，Marimo 會自動偵測到 Cell 2 與 Cell 3 依賴於 a，因此會自動重新執行 Cell 2 和 Cell 3。""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""2. 這樣就算你沒有按照「從上到下」的順序執行，Marimo 也能保證每個 cell 的結果都是最新且一致的。""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""這種「反應式（Reactive）」執行方式，讓 notebook 更加可重現、可靠，也大幅減少因執行順序錯誤導致的 bug。""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### 3. Git 友善（Git-friendly）""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Marimo notebook 以純 Python 檔案儲存，方便用 Git 進行版本控制、協作與差異比對。""")
    return


@app.cell
def _():
    # 你可以直接用 git 管理這個 .py notebook 檔案
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### 4. AI 原生（AI-native）""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Marimo 內建 AI/LLM 整合，讓你可以在 notebook 內直接呼叫 AI 助手、生成程式碼或進行自然語言互動。""")
    return


@app.cell
def _(mo):
    mo.image(
        src="images/marimo_genai.JPG",
        alt="在 notebook 內直接呼叫 AI 助手、生成程式碼或進行自然語言互動",
        rounded=True,
        caption="在 notebook 內直接呼叫 AI 助手、生成程式碼或進行自然語言互動",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## 小結""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""marimo Notebook 以現代開發需求為核心，結合反應式運算、可重現性、Git 友善與 AI 原生等特性，是 Python 資料科學與 AI 開發的新選擇。接下來30天，將帶你一步步深入體驗 marimo 的強大功能！""")
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Reference

    - [A reactive Python notebook that's reproducible, git-friendly, and deployable as scripts or apps.](https://marimo.io/)
    - [Python notebooks as dataflow graphs: reactive, reproducible, and reusable](https://marimo.io/blog/dataflow)
    - [A Large-scale Study about Quality and
    Reproducibility of Jupyter Notebooks](https://leomurta.github.io/papers/pimentel2019a.pdf)
    - [We Downloaded 10,000,000 Jupyter Notebooks From Github – This Is What We Learned](https://blog.jetbrains.com/datalore/2020/12/17/we-downloaded-10-000-000-jupyter-notebooks-from-github-this-is-what-we-learned/#)
    """
    )
    return


if __name__ == "__main__":
    app.run()
