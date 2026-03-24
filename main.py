from cache import LRUCache

def test_lru_cache():
    cache = LRUCache(capacity=2)
    
    # Test set and get
    cache.set("a", "1")
    assert cache.get("a") == "1", "Failed to get value"
    
    # Test capacity limit
    cache.set("b", "2")
    cache.set("c", "3")
    assert cache.get("a") == -1, "LRU item should be evicted"
    assert cache.get("b") == "2", "Should retrieve b"
    assert cache.get("c") == "3", "Should retrieve c"
    
    # Test get moves item to end
    cache.set("d", "4")
    assert cache.get("b") == -1, "b should be evicted"
    assert cache.get("c") == "3", "c should still exist"
    
    # Test rem
    cache.rem("c")
    assert cache.get("c") == -1, "Removed key should not exist"
    
    # Test update existing key
    cache.set("d", "5")
    assert cache.get("d") == "5", "Updated value should be retrieved"
    
    print("All tests passed!")

if __name__ == "__main__":
    test_lru_cache()