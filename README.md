# Keccaky

Secure and easy-to-use keccak

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