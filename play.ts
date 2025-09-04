export interface Foo {
  name: string;
  size: number;
}

export interface Bar {
  address: string;
  size: string;
}

export interface Baz {
  fooOrBar: Foo | Bar;
}
