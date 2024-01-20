# Keccaky

Secure and easy-to-use keccak

> **✅ ready for production!!!**

## Roadmap

- [x] Create Keccak 256 hash
- [x] Create massive tests agains pycryptodome (575 tests)
- [x] Create benchmark tests agains pycryptodome
- [x] API made easy for client
- [x] Docs for dev
- [ ] Re-write Keccak algorithm in Rust using FFI

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
from keccaky import ethereum_hash, hash_it

assert "0xff7e4a2e488ac0d8ed435b41979a0c1defeae30231dc5338a1b3a39c86adfd3c" == ethereum_hash("keccaky")
assert "ff7e4a2e488ac0d8ed435b41979a0c1defeae30231dc5338a1b3a39c86adfd3c" == hash_it("keccaky")
```
