# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from open_manipulator_msgs/GetKinematicsPoseRequest.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class GetKinematicsPoseRequest(genpy.Message):
  _md5sum = "d41d8cd98f00b204e9800998ecf8427e"
  _type = "open_manipulator_msgs/GetKinematicsPoseRequest"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """
"""
  __slots__ = []
  _slot_types = []

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GetKinematicsPoseRequest, self).__init__(*args, **kwds)

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
      pass
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      pass
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from open_manipulator_msgs/GetKinematicsPoseResponse.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import open_manipulator_msgs.msg

class GetKinematicsPoseResponse(genpy.Message):
  _md5sum = "c8178071274fe9988bb6f690a77025ca"
  _type = "open_manipulator_msgs/GetKinematicsPoseResponse"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """KinematicsPose position_ctrl_kinematics_pose


================================================================================
MSG: open_manipulator_msgs/KinematicsPose
string    	        group_name
geometry_msgs/Pose  pose
float64             move_time

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
"""
  __slots__ = ['position_ctrl_kinematics_pose']
  _slot_types = ['open_manipulator_msgs/KinematicsPose']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       position_ctrl_kinematics_pose

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GetKinematicsPoseResponse, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.position_ctrl_kinematics_pose is None:
        self.position_ctrl_kinematics_pose = open_manipulator_msgs.msg.KinematicsPose()
    else:
      self.position_ctrl_kinematics_pose = open_manipulator_msgs.msg.KinematicsPose()

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
      _x = self.position_ctrl_kinematics_pose.group_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_8d().pack(_x.position_ctrl_kinematics_pose.pose.position.x, _x.position_ctrl_kinematics_pose.pose.position.y, _x.position_ctrl_kinematics_pose.pose.position.z, _x.position_ctrl_kinematics_pose.pose.orientation.x, _x.position_ctrl_kinematics_pose.pose.orientation.y, _x.position_ctrl_kinematics_pose.pose.orientation.z, _x.position_ctrl_kinematics_pose.pose.orientation.w, _x.position_ctrl_kinematics_pose.move_time))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.position_ctrl_kinematics_pose is None:
        self.position_ctrl_kinematics_pose = open_manipulator_msgs.msg.KinematicsPose()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.position_ctrl_kinematics_pose.group_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.position_ctrl_kinematics_pose.group_name = str[start:end]
      _x = self
      start = end
      end += 64
      (_x.position_ctrl_kinematics_pose.pose.position.x, _x.position_ctrl_kinematics_pose.pose.position.y, _x.position_ctrl_kinematics_pose.pose.position.z, _x.position_ctrl_kinematics_pose.pose.orientation.x, _x.position_ctrl_kinematics_pose.pose.orientation.y, _x.position_ctrl_kinematics_pose.pose.orientation.z, _x.position_ctrl_kinematics_pose.pose.orientation.w, _x.position_ctrl_kinematics_pose.move_time,) = _get_struct_8d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.position_ctrl_kinematics_pose.group_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_8d().pack(_x.position_ctrl_kinematics_pose.pose.position.x, _x.position_ctrl_kinematics_pose.pose.position.y, _x.position_ctrl_kinematics_pose.pose.position.z, _x.position_ctrl_kinematics_pose.pose.orientation.x, _x.position_ctrl_kinematics_pose.pose.orientation.y, _x.position_ctrl_kinematics_pose.pose.orientation.z, _x.position_ctrl_kinematics_pose.pose.orientation.w, _x.position_ctrl_kinematics_pose.move_time))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.position_ctrl_kinematics_pose is None:
        self.position_ctrl_kinematics_pose = open_manipulator_msgs.msg.KinematicsPose()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.position_ctrl_kinematics_pose.group_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.position_ctrl_kinematics_pose.group_name = str[start:end]
      _x = self
      start = end
      end += 64
      (_x.position_ctrl_kinematics_pose.pose.position.x, _x.position_ctrl_kinematics_pose.pose.position.y, _x.position_ctrl_kinematics_pose.pose.position.z, _x.position_ctrl_kinematics_pose.pose.orientation.x, _x.position_ctrl_kinematics_pose.pose.orientation.y, _x.position_ctrl_kinematics_pose.pose.orientation.z, _x.position_ctrl_kinematics_pose.pose.orientation.w, _x.position_ctrl_kinematics_pose.move_time,) = _get_struct_8d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_8d = None
def _get_struct_8d():
    global _struct_8d
    if _struct_8d is None:
        _struct_8d = struct.Struct("<8d")
    return _struct_8d
class GetKinematicsPose(object):
  _type          = 'open_manipulator_msgs/GetKinematicsPose'
  _md5sum = 'c8178071274fe9988bb6f690a77025ca'
  _request_class  = GetKinematicsPoseRequest
  _response_class = GetKinematicsPoseResponse
