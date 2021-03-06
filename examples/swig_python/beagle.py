# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_beagle', [dirname(__file__)])
        except ImportError:
            import _beagle
            return _beagle
        if fp is not None:
            try:
                _mod = imp.load_module('_beagle', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _beagle = swig_import_helper()
    del swig_import_helper
else:
    import _beagle
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0



def new_intp():
  return _beagle.new_intp()
new_intp = _beagle.new_intp

def copy_intp(*args):
  return _beagle.copy_intp(*args)
copy_intp = _beagle.copy_intp

def delete_intp(*args):
  return _beagle.delete_intp(*args)
delete_intp = _beagle.delete_intp

def intp_assign(*args):
  return _beagle.intp_assign(*args)
intp_assign = _beagle.intp_assign

def intp_value(*args):
  return _beagle.intp_value(*args)
intp_value = _beagle.intp_value

def new_doublep():
  return _beagle.new_doublep()
new_doublep = _beagle.new_doublep

def copy_doublep(*args):
  return _beagle.copy_doublep(*args)
copy_doublep = _beagle.copy_doublep

def delete_doublep(*args):
  return _beagle.delete_doublep(*args)
delete_doublep = _beagle.delete_doublep

def doublep_assign(*args):
  return _beagle.doublep_assign(*args)
doublep_assign = _beagle.doublep_assign

def doublep_value(*args):
  return _beagle.doublep_value(*args)
doublep_value = _beagle.doublep_value

def new_intArray(*args):
  return _beagle.new_intArray(*args)
new_intArray = _beagle.new_intArray

def delete_intArray(*args):
  return _beagle.delete_intArray(*args)
delete_intArray = _beagle.delete_intArray

def intArray_getitem(*args):
  return _beagle.intArray_getitem(*args)
intArray_getitem = _beagle.intArray_getitem

def intArray_setitem(*args):
  return _beagle.intArray_setitem(*args)
intArray_setitem = _beagle.intArray_setitem

def new_doubleArray(*args):
  return _beagle.new_doubleArray(*args)
new_doubleArray = _beagle.new_doubleArray

def delete_doubleArray(*args):
  return _beagle.delete_doubleArray(*args)
delete_doubleArray = _beagle.delete_doubleArray

def doubleArray_getitem(*args):
  return _beagle.doubleArray_getitem(*args)
doubleArray_getitem = _beagle.doubleArray_getitem

def doubleArray_setitem(*args):
  return _beagle.doubleArray_setitem(*args)
doubleArray_setitem = _beagle.doubleArray_setitem
BEAGLE_SUCCESS = _beagle.BEAGLE_SUCCESS
BEAGLE_ERROR_GENERAL = _beagle.BEAGLE_ERROR_GENERAL
BEAGLE_ERROR_OUT_OF_MEMORY = _beagle.BEAGLE_ERROR_OUT_OF_MEMORY
BEAGLE_ERROR_UNIDENTIFIED_EXCEPTION = _beagle.BEAGLE_ERROR_UNIDENTIFIED_EXCEPTION
BEAGLE_ERROR_UNINITIALIZED_INSTANCE = _beagle.BEAGLE_ERROR_UNINITIALIZED_INSTANCE
BEAGLE_ERROR_OUT_OF_RANGE = _beagle.BEAGLE_ERROR_OUT_OF_RANGE
BEAGLE_ERROR_NO_RESOURCE = _beagle.BEAGLE_ERROR_NO_RESOURCE
BEAGLE_ERROR_NO_IMPLEMENTATION = _beagle.BEAGLE_ERROR_NO_IMPLEMENTATION
BEAGLE_ERROR_FLOATING_POINT = _beagle.BEAGLE_ERROR_FLOATING_POINT
BEAGLE_FLAG_PRECISION_SINGLE = _beagle.BEAGLE_FLAG_PRECISION_SINGLE
BEAGLE_FLAG_PRECISION_DOUBLE = _beagle.BEAGLE_FLAG_PRECISION_DOUBLE
BEAGLE_FLAG_COMPUTATION_SYNCH = _beagle.BEAGLE_FLAG_COMPUTATION_SYNCH
BEAGLE_FLAG_COMPUTATION_ASYNCH = _beagle.BEAGLE_FLAG_COMPUTATION_ASYNCH
BEAGLE_FLAG_EIGEN_REAL = _beagle.BEAGLE_FLAG_EIGEN_REAL
BEAGLE_FLAG_EIGEN_COMPLEX = _beagle.BEAGLE_FLAG_EIGEN_COMPLEX
BEAGLE_FLAG_SCALING_MANUAL = _beagle.BEAGLE_FLAG_SCALING_MANUAL
BEAGLE_FLAG_SCALING_AUTO = _beagle.BEAGLE_FLAG_SCALING_AUTO
BEAGLE_FLAG_SCALING_ALWAYS = _beagle.BEAGLE_FLAG_SCALING_ALWAYS
BEAGLE_FLAG_SCALING_DYNAMIC = _beagle.BEAGLE_FLAG_SCALING_DYNAMIC
BEAGLE_FLAG_SCALERS_RAW = _beagle.BEAGLE_FLAG_SCALERS_RAW
BEAGLE_FLAG_SCALERS_LOG = _beagle.BEAGLE_FLAG_SCALERS_LOG
BEAGLE_FLAG_INVEVEC_STANDARD = _beagle.BEAGLE_FLAG_INVEVEC_STANDARD
BEAGLE_FLAG_INVEVEC_TRANSPOSED = _beagle.BEAGLE_FLAG_INVEVEC_TRANSPOSED
BEAGLE_FLAG_VECTOR_SSE = _beagle.BEAGLE_FLAG_VECTOR_SSE
BEAGLE_FLAG_VECTOR_NONE = _beagle.BEAGLE_FLAG_VECTOR_NONE
BEAGLE_FLAG_THREADING_OPENMP = _beagle.BEAGLE_FLAG_THREADING_OPENMP
BEAGLE_FLAG_THREADING_NONE = _beagle.BEAGLE_FLAG_THREADING_NONE
BEAGLE_FLAG_PROCESSOR_CPU = _beagle.BEAGLE_FLAG_PROCESSOR_CPU
BEAGLE_FLAG_PROCESSOR_GPU = _beagle.BEAGLE_FLAG_PROCESSOR_GPU
BEAGLE_FLAG_PROCESSOR_FPGA = _beagle.BEAGLE_FLAG_PROCESSOR_FPGA
BEAGLE_FLAG_PROCESSOR_CELL = _beagle.BEAGLE_FLAG_PROCESSOR_CELL
BEAGLE_FLAG_FRAMEWORK_CUDA = _beagle.BEAGLE_FLAG_FRAMEWORK_CUDA
BEAGLE_FLAG_FRAMEWORK_OPENCL = _beagle.BEAGLE_FLAG_FRAMEWORK_OPENCL
BEAGLE_OP_COUNT = _beagle.BEAGLE_OP_COUNT
BEAGLE_OP_NONE = _beagle.BEAGLE_OP_NONE
class BeagleInstanceDetails(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BeagleInstanceDetails, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BeagleInstanceDetails, name)
    __repr__ = _swig_repr
    __swig_setmethods__["resourceNumber"] = _beagle.BeagleInstanceDetails_resourceNumber_set
    __swig_getmethods__["resourceNumber"] = _beagle.BeagleInstanceDetails_resourceNumber_get
    if _newclass:resourceNumber = _swig_property(_beagle.BeagleInstanceDetails_resourceNumber_get, _beagle.BeagleInstanceDetails_resourceNumber_set)
    __swig_setmethods__["resourceName"] = _beagle.BeagleInstanceDetails_resourceName_set
    __swig_getmethods__["resourceName"] = _beagle.BeagleInstanceDetails_resourceName_get
    if _newclass:resourceName = _swig_property(_beagle.BeagleInstanceDetails_resourceName_get, _beagle.BeagleInstanceDetails_resourceName_set)
    __swig_setmethods__["implName"] = _beagle.BeagleInstanceDetails_implName_set
    __swig_getmethods__["implName"] = _beagle.BeagleInstanceDetails_implName_get
    if _newclass:implName = _swig_property(_beagle.BeagleInstanceDetails_implName_get, _beagle.BeagleInstanceDetails_implName_set)
    __swig_setmethods__["implDescription"] = _beagle.BeagleInstanceDetails_implDescription_set
    __swig_getmethods__["implDescription"] = _beagle.BeagleInstanceDetails_implDescription_get
    if _newclass:implDescription = _swig_property(_beagle.BeagleInstanceDetails_implDescription_get, _beagle.BeagleInstanceDetails_implDescription_set)
    __swig_setmethods__["flags"] = _beagle.BeagleInstanceDetails_flags_set
    __swig_getmethods__["flags"] = _beagle.BeagleInstanceDetails_flags_get
    if _newclass:flags = _swig_property(_beagle.BeagleInstanceDetails_flags_get, _beagle.BeagleInstanceDetails_flags_set)
    def __init__(self): 
        this = _beagle.new_BeagleInstanceDetails()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _beagle.delete_BeagleInstanceDetails
    __del__ = lambda self : None;
BeagleInstanceDetails_swigregister = _beagle.BeagleInstanceDetails_swigregister
BeagleInstanceDetails_swigregister(BeagleInstanceDetails)

class BeagleResource(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BeagleResource, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BeagleResource, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _beagle.BeagleResource_name_set
    __swig_getmethods__["name"] = _beagle.BeagleResource_name_get
    if _newclass:name = _swig_property(_beagle.BeagleResource_name_get, _beagle.BeagleResource_name_set)
    __swig_setmethods__["description"] = _beagle.BeagleResource_description_set
    __swig_getmethods__["description"] = _beagle.BeagleResource_description_get
    if _newclass:description = _swig_property(_beagle.BeagleResource_description_get, _beagle.BeagleResource_description_set)
    __swig_setmethods__["supportFlags"] = _beagle.BeagleResource_supportFlags_set
    __swig_getmethods__["supportFlags"] = _beagle.BeagleResource_supportFlags_get
    if _newclass:supportFlags = _swig_property(_beagle.BeagleResource_supportFlags_get, _beagle.BeagleResource_supportFlags_set)
    __swig_setmethods__["requiredFlags"] = _beagle.BeagleResource_requiredFlags_set
    __swig_getmethods__["requiredFlags"] = _beagle.BeagleResource_requiredFlags_get
    if _newclass:requiredFlags = _swig_property(_beagle.BeagleResource_requiredFlags_get, _beagle.BeagleResource_requiredFlags_set)
    def __init__(self): 
        this = _beagle.new_BeagleResource()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _beagle.delete_BeagleResource
    __del__ = lambda self : None;
BeagleResource_swigregister = _beagle.BeagleResource_swigregister
BeagleResource_swigregister(BeagleResource)

class BeagleResourceList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BeagleResourceList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BeagleResourceList, name)
    __repr__ = _swig_repr
    __swig_setmethods__["list"] = _beagle.BeagleResourceList_list_set
    __swig_getmethods__["list"] = _beagle.BeagleResourceList_list_get
    if _newclass:list = _swig_property(_beagle.BeagleResourceList_list_get, _beagle.BeagleResourceList_list_set)
    __swig_setmethods__["length"] = _beagle.BeagleResourceList_length_set
    __swig_getmethods__["length"] = _beagle.BeagleResourceList_length_get
    if _newclass:length = _swig_property(_beagle.BeagleResourceList_length_get, _beagle.BeagleResourceList_length_set)
    def __init__(self): 
        this = _beagle.new_BeagleResourceList()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _beagle.delete_BeagleResourceList
    __del__ = lambda self : None;
BeagleResourceList_swigregister = _beagle.BeagleResourceList_swigregister
BeagleResourceList_swigregister(BeagleResourceList)


def beagleGetResourceList():
  return _beagle.beagleGetResourceList()
beagleGetResourceList = _beagle.beagleGetResourceList

def beagleCreateInstance(*args):
  return _beagle.beagleCreateInstance(*args)
beagleCreateInstance = _beagle.beagleCreateInstance

def beagleFinalizeInstance(*args):
  return _beagle.beagleFinalizeInstance(*args)
beagleFinalizeInstance = _beagle.beagleFinalizeInstance

def beagleFinalize():
  return _beagle.beagleFinalize()
beagleFinalize = _beagle.beagleFinalize

def beagleSetTipStates(*args):
  return _beagle.beagleSetTipStates(*args)
beagleSetTipStates = _beagle.beagleSetTipStates

def beagleSetTipPartials(*args):
  return _beagle.beagleSetTipPartials(*args)
beagleSetTipPartials = _beagle.beagleSetTipPartials

def beagleSetPartials(*args):
  return _beagle.beagleSetPartials(*args)
beagleSetPartials = _beagle.beagleSetPartials

def beagleGetPartials(*args):
  return _beagle.beagleGetPartials(*args)
beagleGetPartials = _beagle.beagleGetPartials

def beagleSetEigenDecomposition(*args):
  return _beagle.beagleSetEigenDecomposition(*args)
beagleSetEigenDecomposition = _beagle.beagleSetEigenDecomposition

def beagleSetStateFrequencies(*args):
  return _beagle.beagleSetStateFrequencies(*args)
beagleSetStateFrequencies = _beagle.beagleSetStateFrequencies

def beagleSetCategoryWeights(*args):
  return _beagle.beagleSetCategoryWeights(*args)
beagleSetCategoryWeights = _beagle.beagleSetCategoryWeights

def beagleSetCategoryRates(*args):
  return _beagle.beagleSetCategoryRates(*args)
beagleSetCategoryRates = _beagle.beagleSetCategoryRates

def beagleSetPatternWeights(*args):
  return _beagle.beagleSetPatternWeights(*args)
beagleSetPatternWeights = _beagle.beagleSetPatternWeights

def beagleUpdateTransitionMatrices(*args):
  return _beagle.beagleUpdateTransitionMatrices(*args)
beagleUpdateTransitionMatrices = _beagle.beagleUpdateTransitionMatrices

def beagleSetTransitionMatrix(*args):
  return _beagle.beagleSetTransitionMatrix(*args)
beagleSetTransitionMatrix = _beagle.beagleSetTransitionMatrix

def beagleGetTransitionMatrix(*args):
  return _beagle.beagleGetTransitionMatrix(*args)
beagleGetTransitionMatrix = _beagle.beagleGetTransitionMatrix

def beagleSetTransitionMatrices(*args):
  return _beagle.beagleSetTransitionMatrices(*args)
beagleSetTransitionMatrices = _beagle.beagleSetTransitionMatrices
class BeagleOperation(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BeagleOperation, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BeagleOperation, name)
    __repr__ = _swig_repr
    __swig_setmethods__["destinationPartials"] = _beagle.BeagleOperation_destinationPartials_set
    __swig_getmethods__["destinationPartials"] = _beagle.BeagleOperation_destinationPartials_get
    if _newclass:destinationPartials = _swig_property(_beagle.BeagleOperation_destinationPartials_get, _beagle.BeagleOperation_destinationPartials_set)
    __swig_setmethods__["destinationScaleWrite"] = _beagle.BeagleOperation_destinationScaleWrite_set
    __swig_getmethods__["destinationScaleWrite"] = _beagle.BeagleOperation_destinationScaleWrite_get
    if _newclass:destinationScaleWrite = _swig_property(_beagle.BeagleOperation_destinationScaleWrite_get, _beagle.BeagleOperation_destinationScaleWrite_set)
    __swig_setmethods__["destinationScaleRead"] = _beagle.BeagleOperation_destinationScaleRead_set
    __swig_getmethods__["destinationScaleRead"] = _beagle.BeagleOperation_destinationScaleRead_get
    if _newclass:destinationScaleRead = _swig_property(_beagle.BeagleOperation_destinationScaleRead_get, _beagle.BeagleOperation_destinationScaleRead_set)
    __swig_setmethods__["child1Partials"] = _beagle.BeagleOperation_child1Partials_set
    __swig_getmethods__["child1Partials"] = _beagle.BeagleOperation_child1Partials_get
    if _newclass:child1Partials = _swig_property(_beagle.BeagleOperation_child1Partials_get, _beagle.BeagleOperation_child1Partials_set)
    __swig_setmethods__["child1TransitionMatrix"] = _beagle.BeagleOperation_child1TransitionMatrix_set
    __swig_getmethods__["child1TransitionMatrix"] = _beagle.BeagleOperation_child1TransitionMatrix_get
    if _newclass:child1TransitionMatrix = _swig_property(_beagle.BeagleOperation_child1TransitionMatrix_get, _beagle.BeagleOperation_child1TransitionMatrix_set)
    __swig_setmethods__["child2Partials"] = _beagle.BeagleOperation_child2Partials_set
    __swig_getmethods__["child2Partials"] = _beagle.BeagleOperation_child2Partials_get
    if _newclass:child2Partials = _swig_property(_beagle.BeagleOperation_child2Partials_get, _beagle.BeagleOperation_child2Partials_set)
    __swig_setmethods__["child2TransitionMatrix"] = _beagle.BeagleOperation_child2TransitionMatrix_set
    __swig_getmethods__["child2TransitionMatrix"] = _beagle.BeagleOperation_child2TransitionMatrix_get
    if _newclass:child2TransitionMatrix = _swig_property(_beagle.BeagleOperation_child2TransitionMatrix_get, _beagle.BeagleOperation_child2TransitionMatrix_set)
    def __init__(self): 
        this = _beagle.new_BeagleOperation()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _beagle.delete_BeagleOperation
    __del__ = lambda self : None;
BeagleOperation_swigregister = _beagle.BeagleOperation_swigregister
BeagleOperation_swigregister(BeagleOperation)


def beagleUpdatePartials(*args):
  return _beagle.beagleUpdatePartials(*args)
beagleUpdatePartials = _beagle.beagleUpdatePartials

def beagleWaitForPartials(*args):
  return _beagle.beagleWaitForPartials(*args)
beagleWaitForPartials = _beagle.beagleWaitForPartials

def beagleAccumulateScaleFactors(*args):
  return _beagle.beagleAccumulateScaleFactors(*args)
beagleAccumulateScaleFactors = _beagle.beagleAccumulateScaleFactors

def beagleRemoveScaleFactors(*args):
  return _beagle.beagleRemoveScaleFactors(*args)
beagleRemoveScaleFactors = _beagle.beagleRemoveScaleFactors

def beagleResetScaleFactors(*args):
  return _beagle.beagleResetScaleFactors(*args)
beagleResetScaleFactors = _beagle.beagleResetScaleFactors

def beagleCopyScaleFactors(*args):
  return _beagle.beagleCopyScaleFactors(*args)
beagleCopyScaleFactors = _beagle.beagleCopyScaleFactors

def beagleCalculateRootLogLikelihoods(*args):
  return _beagle.beagleCalculateRootLogLikelihoods(*args)
beagleCalculateRootLogLikelihoods = _beagle.beagleCalculateRootLogLikelihoods

def beagleCalculateEdgeLogLikelihoods(*args):
  return _beagle.beagleCalculateEdgeLogLikelihoods(*args)
beagleCalculateEdgeLogLikelihoods = _beagle.beagleCalculateEdgeLogLikelihoods

def beagleGetSiteLogLikelihoods(*args):
  return _beagle.beagleGetSiteLogLikelihoods(*args)
beagleGetSiteLogLikelihoods = _beagle.beagleGetSiteLogLikelihoods

def beagleGetSiteDerivatives(*args):
  return _beagle.beagleGetSiteDerivatives(*args)
beagleGetSiteDerivatives = _beagle.beagleGetSiteDerivatives

def new_BeagleOperationArray(*args):
  return _beagle.new_BeagleOperationArray(*args)
new_BeagleOperationArray = _beagle.new_BeagleOperationArray

def delete_BeagleOperationArray(*args):
  return _beagle.delete_BeagleOperationArray(*args)
delete_BeagleOperationArray = _beagle.delete_BeagleOperationArray

def BeagleOperationArray_getitem(*args):
  return _beagle.BeagleOperationArray_getitem(*args)
BeagleOperationArray_getitem = _beagle.BeagleOperationArray_getitem

def BeagleOperationArray_setitem(*args):
  return _beagle.BeagleOperationArray_setitem(*args)
BeagleOperationArray_setitem = _beagle.BeagleOperationArray_setitem
def createStates(st,ttab):
    states = new_intArray(len(st))
    for i in range(0,len(st)):
        intArray_setitem(states,i,ttab[st[i]])
    return states

def make_intarray(ia):
    result = new_intArray(len(ia))
    for i in range(0,len(ia)):
        intArray_setitem(result,i,ia[i])
    return result

def make_doublearray(da):
    result = new_doubleArray(len(da))
    for i in range(0,len(da)):
        doubleArray_setitem(result,i,da[i])
    return result

def make_operation(arg):
    o = BeagleOperation()
    o.destinationPartials = arg[0]
    o.destinationScaleWrite = arg[1]
    o.destinationScaleRead = arg[2]
    o.child1Partials = arg[3]
    o.child1TransitionMatrix = arg[4]
    o.child2Partials = arg[5]
    o.child2TransitionMatrix = arg[6]
    return o

def createPatternWeights(wts):
    weights = new_doubleArray(len(wts))
    for i in range(0,len(wts)):
        doubleArray_setitem(weights,i,wts[i])
    return weights



