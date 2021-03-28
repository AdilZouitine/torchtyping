import pytest
import torch
from torchtyping import TensorType
import typeguard


@typeguard.typechecked
def _3_dim_checker(x: TensorType[3]):
    pass


@typeguard.typechecked
def _3m1_dim_checker(x: TensorType[3, -1]):
    pass
    
@typeguard.typechecked
def _4_dim_checker(x: TensorType[4]):
    pass
    
    
@typeguard.typechecked
def _4m1_dim_checker(x: TensorType[4, -1]):
    pass
    

@typeguard.typechecked
def _m14_dim_checker(x: TensorType[-1, 4]):
    pass    
    
    
@typeguard.typechecked
def _m1m1_dim_checker(x: TensorType[-1, -1]):
    pass
    
    
@typeguard.typechecked
def _34_dim_checker(x: TensorType[3, 4]):
    pass
    
    
@typeguard.typechecked
def _34m1_dim_checker(x: TensorType[3, 4, -1]):
    pass
    
    
@typeguard.typechecked
def _m14m1_dim_checker(x: TensorType[-1, 4, -1]):
    pass
    

def test_fixed_int_dim():
    x = torch.rand(3)
    _3_dim_checker(x)
    with pytest.raises(TypeError):
        _3m1_dim_checker(x)
        _4_dim_checker(x)
        _4m1_dim_checker(x)
        _m14_dim_checker(x)
        _m1m1_dim_checker(x)
        _34_dim_checker(x)
        _34m1_dim_checker(x)
        _m14m1_dim_checker(x)
        
    x = torch.rand(3, 4):
    _3m1_dim_checker(x)
    _m14_dim_checker(x)
    _m1m1_dim_checker(x)
    _34_dim_checker(x)
    with pytest.raises(TypeError):
        _3_dim_checker(x)
        _4_dim_checker(x)
        _4m1_dim_checker(x)
        _34m1_dim_checker(x)
        _m14m1_dim_checker(x)
        
    x = torch.rand(4, 3):
    _4m1_dim_checker(x)
    _m1m1_dim_checker(x)
    with pytest.raises(TypeError):
        _3_dim_checker(x)
        _3m1_dim_checker(x)
        _4_dim_checker(x)
        _m14_dim_checker(x)
        _34_dim_checker(x)
        _34m1_dim_checker(x)
        _m14m1_dim_checker(x)


@typeguard.typechecked
def _a_dim_checker(x: TensorType["a"]):
    pass
    
        
@typeguard.typechecked
def _ab_dim_checker(x: TensorType["a", "b"]):
    pass
    
    
@typeguard.typechecked
def _abc_dim_checker(x: TensorType["a", "b", "c"]):
    pass
        

@typeguard.typechecked
def _cb_dim_checker(x: TensorType["c", "b"]):
    pass
    
    
@typeguard.typechecked
def _am1_dim_checker(x: TensorType["a", -1]):
    pass
    
    
@typeguard.typechecked
def _m1b_dim_checker(x: TensorType[-1, "b"]):
    pass
    
    
@typeguard.typechecked
def _abm1_dim_checker(x: TensorType["a", "b", -1]):
    pass
    
    
@typeguard.typechecked
def _m1bm1_dim_checker(x: TensorType[-1, "b", -1]):
    pass

    
def test_str_dim():
    x = torch.rand(3, 4):
    _ab_dim_checker(x)
    _cb_dim_checker(x)
    _am1_dim_checker(x)
    _m1b_dim_checker(x)
    with pytest.raises(TypeError):
        _a_dim_checker(x)
        _abc_dim_checker(x)
        _abm1_dim_checker(x)
        _m1bm1_dim_checker(x)


@typeguard.typechecked
def _a_dim_checker1(x: TensorType["a": 3]):
    pass
    
    
@typeguard.typechecked
def _a_dim_checker2(x: TensorType["a": -1]):
    pass
    
        
@typeguard.typechecked
def _ab_dim_checker1(x: TensorType["a": 3, "b": 4]):
    pass
    
    
@typeguard.typechecked
def _ab_dim_checker2(x: TensorType["a": 3, "b": -1]):
    pass


@typeguard.typechecked
def _ab_dim_checker3(x: TensorType["a": -1, "b": 4]):
    pass
    

@typeguard.typechecked
def _ab_dim_checker4(x: TensorType["a": 3, "b"]):
    pass


@typeguard.typechecked
def _ab_dim_checker5(x: TensorType["a", "b": 4]):
    pass

    
@typeguard.typechecked
def _ab_dim_checker6(x: TensorType["a": 5, "b": 4]):
    pass


@typeguard.typechecked
def _ab_dim_checker7(x: TensorType["a": 5, "b": -1]):
    pass

    
@typeguard.typechecked
def _m1b_dim_checker(x: TensorType[-1, "b": 4]):
    pass
    
    
@typeguard.typechecked
def _abm1_dim_checker(x: TensorType["a": 3, "b": 4, -1]):
    pass
    
    
@typeguard.typechecked
def _m1bm1_dim_checker(x: TensorType[-1, "b": 4, -1]):
    pass
    

def test_int_str_dim():
    x = torch.rand(3, 4)
    _ab_dim_checker1(x)
    _ab_dim_checker2(x)
    _ab_dim_checker3(x)
    _ab_dim_checker4(x)
    _ab_dim_checker5(x)
    _m1b_dim_checker(x)
    with pytest.raises(TypeError):
        _a_dim_checker1(x)
        _a_dim_checker2(x)
        _ab_dim_checker6(x)
        _ab_dim_checker7(x)
        _abm1_dim_checker(x)
        _m1bm1_dim_checker(x)