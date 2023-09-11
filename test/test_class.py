# class FooParent(object):
#     parent_attr1 = "parent_attr1"
#     parent_attr2 = "parent_attr2"


class Foo():
    cls_attr1 = "cls_attr1"
    cls_attr2 = "cls_attr2"

    def __init__(self):
        self.ins_attr1 = "ins_attr1"
        self.cls_attr1 = "ins_cls_attr1"
        self.parent_attr1 = "ins_parent_attr1"

    def __getattribute__(self, name):
        print("=======>__getattribute__")
        return super().__getattribute__(name)

    def __getattr__(self, name):
        print("=======>__getattr__")


foo = Foo()
# print("__dict__: %s" % Foo.__dict__)
print(foo.ins_attr1)
# print(foo.cls_attr1)
# print(foo.cls_attr2)
# print(foo.parent_attr1)
# print(foo.parent_attr2)
# print(foo.x)