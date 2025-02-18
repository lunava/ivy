# global
import ivy


def tile(A, reps):
    return ivy.tile(A, reps)


tile.unsupported_dtypes = {
    "tensorflow": ("uint8", "uint16", "uint32", "int8", "int16"),
}


def repeat(a, repeats, axis=None):
    return ivy.repeat(a, repeats, axis=axis)
