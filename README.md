# 📊 Excel Deduplicator

Remove duplicated rows from `.xlsx` files with elegance and precision.  
This script was crafted to **quickly clean and filter your Excel data**, ensuring you're working only with **relevant and unique entries**.

---

## 🚀 Features

✅ Uploads an `.xlsx` file directly via Google Colab  
✅ Automatically detects the first four columns of your sheet  
✅ Filters out rows with missing values in those columns  
✅ Removes exact duplicates based on those same columns  
✅ Exports a clean, processed file ready for use  
✅ Provides a clear summary of the process  

---

## 🔧 How It Works

Behind the scenes, the script uses **Pandas** to read and manipulate your spreadsheet, ensuring accurate filtering and performance.  
It was designed with simplicity and robustness in mind, handling user mistakes and file structure issues gracefully.

---

## 🧠 Usage

> Run this script in **Google Colab**.

1. Upload your `.xlsx` file when prompted  
2. The script will:
   - Read the file
   - Check the **first four columns**
   - Remove rows with empty values
   - Remove duplicated rows  
3. It will then automatically **download a clean file** with `_processado_recebimento` appended to the original name.

---

## 📁 Output Example

If you upload a file called:

```
clientes.xlsx
```

The script will generate and download:

```
clientes_processado_recebimento.xlsx
```

---

## 💡 Example Output Summary

```
Processing complete! File saved as clientes_processado_recebimento.xlsx  
Original rows: 1200  
Rows after removing empty values: 1153  
Final unique rows: 1090  
```

---

## 👨‍💻 Tech Used

- [Python 3.x](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- Google Colab’s `files.upload()` and `files.download()`

---

## 🌟 Why Use This?

Because data hygiene is important — and this script **automates a boring task** so you can focus on analysis, reporting, or decision-making.

Make your datasets leaner, cleaner, and more trustworthy with just one click.
