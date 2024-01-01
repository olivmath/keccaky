# Keccaky

Secure and easy-to-use keccak

> **🚨 WARNING:** Not yet ready for production!!!


## Roadmap

- [ ] Create Keccak 256 hash
- [ ] Validate Collision Attack
- [ ] Validate Pre Image Attack
- [ ] Validate Second Pre Image Attack
- [ ] Validate Birthday Attack
- [ ] Validate Length Extension Attack
- [ ] Validate Brute Force Attack
- [ ] Validate Side Channel Attack
- [ ] Validate Specific Attacks


## Docs

**INSTALL**

```
pip install keccaky
```

```
poetry add keccaky
```

**USE**


```python
import keccak

assert keccak("Hello, world") == bytes.fromhex("db99debe7fc546756227481ecaf5136f5b86180d99c5666a14421367c7187e5c")
assert keccak("Hello, world").hex() == "db99debe7fc546756227481ecaf5136f5b86180d99c5666a14421367c7187e5c"
```