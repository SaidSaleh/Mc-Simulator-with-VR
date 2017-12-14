# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from unity_package/UnityMsg.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class UnityMsg(genpy.Message):
  _md5sum = "8e63d3aac35859f6526118315ffe95ce"
  _type = "unity_package/UnityMsg"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """bool running
bool offroad
int32 crash
float32 incline
float32 leaning
"""
  __slots__ = ['running','offroad','crash','incline','leaning']
  _slot_types = ['bool','bool','int32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       running,offroad,crash,incline,leaning

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(UnityMsg, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.running is None:
        self.running = False
      if self.offroad is None:
        self.offroad = False
      if self.crash is None:
        self.crash = 0
      if self.incline is None:
        self.incline = 0.
      if self.leaning is None:
        self.leaning = 0.
    else:
      self.running = False
      self.offroad = False
      self.crash = 0
      self.incline = 0.
      self.leaning = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_2Bi2f().pack(_x.running, _x.offroad, _x.crash, _x.incline, _x.leaning))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 14
      (_x.running, _x.offroad, _x.crash, _x.incline, _x.leaning,) = _get_struct_2Bi2f().unpack(str[start:end])
      self.running = bool(self.running)
      self.offroad = bool(self.offroad)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_2Bi2f().pack(_x.running, _x.offroad, _x.crash, _x.incline, _x.leaning))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 14
      (_x.running, _x.offroad, _x.crash, _x.incline, _x.leaning,) = _get_struct_2Bi2f().unpack(str[start:end])
      self.running = bool(self.running)
      self.offroad = bool(self.offroad)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2Bi2f = None
def _get_struct_2Bi2f():
    global _struct_2Bi2f
    if _struct_2Bi2f is None:
        _struct_2Bi2f = struct.Struct("<2Bi2f")
    return _struct_2Bi2f
