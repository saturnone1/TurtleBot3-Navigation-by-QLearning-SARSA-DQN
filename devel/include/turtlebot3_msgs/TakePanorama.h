// Generated by gencpp from file turtlebot3_msgs/TakePanorama.msg
// DO NOT EDIT!


#ifndef TURTLEBOT3_MSGS_MESSAGE_TAKEPANORAMA_H
#define TURTLEBOT3_MSGS_MESSAGE_TAKEPANORAMA_H

#include <ros/service_traits.h>


#include <turtlebot3_msgs/TakePanoramaRequest.h>
#include <turtlebot3_msgs/TakePanoramaResponse.h>


namespace turtlebot3_msgs
{

struct TakePanorama
{

typedef TakePanoramaRequest Request;
typedef TakePanoramaResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct TakePanorama
} // namespace turtlebot3_msgs


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::turtlebot3_msgs::TakePanorama > {
  static const char* value()
  {
    return "ae9e615a5f5b5081544bd9259c9e0f4e";
  }

  static const char* value(const ::turtlebot3_msgs::TakePanorama&) { return value(); }
};

template<>
struct DataType< ::turtlebot3_msgs::TakePanorama > {
  static const char* value()
  {
    return "turtlebot3_msgs/TakePanorama";
  }

  static const char* value(const ::turtlebot3_msgs::TakePanorama&) { return value(); }
};


// service_traits::MD5Sum< ::turtlebot3_msgs::TakePanoramaRequest> should match
// service_traits::MD5Sum< ::turtlebot3_msgs::TakePanorama >
template<>
struct MD5Sum< ::turtlebot3_msgs::TakePanoramaRequest>
{
  static const char* value()
  {
    return MD5Sum< ::turtlebot3_msgs::TakePanorama >::value();
  }
  static const char* value(const ::turtlebot3_msgs::TakePanoramaRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::turtlebot3_msgs::TakePanoramaRequest> should match
// service_traits::DataType< ::turtlebot3_msgs::TakePanorama >
template<>
struct DataType< ::turtlebot3_msgs::TakePanoramaRequest>
{
  static const char* value()
  {
    return DataType< ::turtlebot3_msgs::TakePanorama >::value();
  }
  static const char* value(const ::turtlebot3_msgs::TakePanoramaRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::turtlebot3_msgs::TakePanoramaResponse> should match
// service_traits::MD5Sum< ::turtlebot3_msgs::TakePanorama >
template<>
struct MD5Sum< ::turtlebot3_msgs::TakePanoramaResponse>
{
  static const char* value()
  {
    return MD5Sum< ::turtlebot3_msgs::TakePanorama >::value();
  }
  static const char* value(const ::turtlebot3_msgs::TakePanoramaResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::turtlebot3_msgs::TakePanoramaResponse> should match
// service_traits::DataType< ::turtlebot3_msgs::TakePanorama >
template<>
struct DataType< ::turtlebot3_msgs::TakePanoramaResponse>
{
  static const char* value()
  {
    return DataType< ::turtlebot3_msgs::TakePanorama >::value();
  }
  static const char* value(const ::turtlebot3_msgs::TakePanoramaResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // TURTLEBOT3_MSGS_MESSAGE_TAKEPANORAMA_H
