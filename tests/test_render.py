from uneedtest import TestCase

from pyggdrasil import render_list, render_tree


class TestRenderTree(TestCase):
    def test_render_simple_list(self):
        data = ["1", "2", "3"]
        result = render_list(data)
        expected = """
├─ 1
├─ 2
└─ 3"""
        self.assert_equal(result, expected)

    def test_render_indented_list(self):
        data = ["1", "2", "3"]
        result = render_list(data, level=1)
        expected = """
   ├─ 1
   ├─ 2
   └─ 3"""
        self.assert_equal(result, expected)

    def test_render_nested_list(self):
        data = ["1", "2", "3"]
        result = render_list(data, level=1, nesting=[True])
        expected = """
│  ├─ 1
│  ├─ 2
│  └─ 3"""
        self.assert_equal(result, expected)

    def test_render_simple_dict(self):
        data = {
            1: ["a"],
            2: ["b"],
            3: ["c"],
        }
        result = render_tree(data)
        expected = """
├─ 1
│  └─ a
├─ 2
│  └─ b
└─ 3
   └─ c"""
        self.assert_equal(result, expected)

    def test_render_nested_dict(self):
        data = {
            1: {
                "a": [1, 2, 3],
                "b": [1, 2, 3],
                "c": [1, 2, 3],
            },
            2: {
                "a": [1, 2, 3],
                "b": [1, 2, 3],
                "c": [1, 2, 3],
            },
            3: {
                "a": [1, 2, 3],
                "b": [1],
            },
        }
        result = render_tree(data)
        expected = """
├─ 1
│  ├─ a
│  │  ├─ 1
│  │  ├─ 2
│  │  └─ 3
│  ├─ b
│  │  ├─ 1
│  │  ├─ 2
│  │  └─ 3
│  └─ c
│     ├─ 1
│     ├─ 2
│     └─ 3
├─ 2
│  ├─ a
│  │  ├─ 1
│  │  ├─ 2
│  │  └─ 3
│  ├─ b
│  │  ├─ 1
│  │  ├─ 2
│  │  └─ 3
│  └─ c
│     ├─ 1
│     ├─ 2
│     └─ 3
└─ 3
   ├─ a
   │  ├─ 1
   │  ├─ 2
   │  └─ 3
   └─ b
      └─ 1"""
        self.assert_equal(result, expected)
