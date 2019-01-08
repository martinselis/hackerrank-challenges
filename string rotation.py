class Rotation():

    def is_rotation(s1, s2):
        if len(s1) != len(s2):
            return False
        if set(s1).issubset(set(s2)):
            return True
        return False

a = Rotation.is_rotation('', '')
print (a)

##        assert_equal(rotation.is_rotation(None, 'foo'), False)
##        assert_equal(rotation.is_rotation('', 'foo'), False)
##        assert_equal(rotation.is_rotation('', ''), True)
##        assert_equal(rotation.is_rotation('foobarbaz', 'barbazfoo'), True)
