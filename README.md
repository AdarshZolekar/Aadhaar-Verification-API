## Aadhaar Verification API

Python API to verify Aadhaar numbers using web scraping on the [UIDAI](https://uidai.gov.in/) website.
This is an unofficial project for educational purposes only.

---

## Features
- Fetch Aadhaar verification captcha.
- Submit Aadhaar number + captcha for verification.
- Parse UIDAI response into structured Python dictionary.
- Wrapper over `requests` with error handling.

---

## Example output:
  ```
  Age Band : 30-40,
  Gender : MALE,
  Mobile Number : xx68545202,
  State : Delhi,
  Aadhar : 123412341234.
  ```

---

## Learning Outcome 

- Learned how to build Python APIs using web scraping.

- Understood captcha handling and data parsing with BeautifulSoup.

- Gained experience in organizing and publishing code on GitHub.

---

## Code Improvements

1. Changed `urlparse` imports to Python 3 style.  
2. Added type hints and docstrings.  
3. Fixed variable naming (`adhar` → `aadhaar` internally, keep alias for backward compatibility).  
4. Added exceptions handling with clearer messages.  
5. Added unit tests folder.  

---

## License

This project is open-source and free to use for educational purposes.

---

## Contributing

Contributions are welcome! Fork the repo, make changes and submit a PR.

---

<p align="center">
  <a href="#top">
    <img src="https://img.shields.io/badge/%E2%AC%86-Back%20to%20Top-blue?style=for-the-badge" alt="Back to Top"/>
  </a>
</p>