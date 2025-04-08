# 🎵 RecSysEcho

**RecSysEcho** is a modular, MLOps-ready recommender system project built using the **Echo Nest Million Song Dataset**. Originally developed as part of the MIT Professional Education Applied Data Science Program, it has been refactored into a clean, reproducible pipeline designed for portfolio presentation and real-world deployment.

---

## 📌 Project Goals

- Implement multiple music recommendation models (KNN, matrix factorization, etc.)
- Compare performance using industry-standard evaluation metrics
- Leverage year and genre features to improve predictions
- Showcase MLOps best practices (testing, CI/CD, modular codebase, etc.)

---

## 🗂️ Repository Structure

```bash
RecSysEcho/
├── data/                # Raw and processed data (git-ignored)
├── notebooks/           # Original exploratory notebooks (MIT course)
├── src/                 # Modular source code
│   └── recommenders/    # Model implementations
├── tests/               # Unit tests
├── scripts/             # CLI wrappers to run pipeline steps
├── Makefile             # Command automation (clean, test, run)
├── LICENSE              # MIT License
├── README.md            # You're here
├── requirements.txt     # Python dependencies
└── setup.py             # (optional) installable package structure
```

## 🚀 Getting Started
1. Clone the repository
```bash
Copy
Edit
git clone https://github.com/AntoineHocquet/RecSysEcho.git
cd RecSysEcho
```
2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # or `.\venv\Scripts\activate` on Windows
```
3. Install dependencies
```bash
pip install -r requirements.txt
```

## 📊 Features & Models
Content-based filtering

User-based and item-based KNN

Matrix Factorization (SVD/SVD++)

Year feature enhancements

Top-N recommender evaluation

## 🧪 Testing
```bash
make test
```
Tests live in the tests/ folder and follow pytest conventions.


## 🤝 Contributing
Contributions are welcome! Please open issues or submit pull requests.

## 📄 License
This project is licensed under the MIT License – see the LICENSE file for details.

## 👤 Author
Antoine Hocquet
Data Scientist & Applied Mathematician
📫 LinkedIn • 📁 Portfolio