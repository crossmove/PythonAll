class TestClass:                        #Prefix should be Test for TestClass

    def test_one(self):                 #Prefix should be _test for test methods
        x = "this"
        assert "h" in x

    def test_two(self):                 #this test will fail, intentional
        x = "hello"
        assert hasattr(x, "check")
