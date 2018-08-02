#ifndef __BOOTSTRAP_H__
#define __BOOTSTRAP_H__
#include <AvailabilityMacros.h>
#include <mach/std_types.h>
#include <mach/message.h>
#include <sys/types.h>
#include <sys/cdefs.h>
#include <stdbool.h>

__BEGIN_DECLS

#pragma GCC visibility push(default)

#define	BOOTSTRAP_MAX_NAME_LEN			128
#define	BOOTSTRAP_MAX_CMD_LEN			512

typedef char name_t[BOOTSTRAP_MAX_NAME_LEN];
typedef char cmd_t[BOOTSTRAP_MAX_CMD_LEN];
typedef name_t *name_array_t;
typedef int bootstrap_status_t;
typedef bootstrap_status_t *bootstrap_status_array_t;
typedef unsigned int bootstrap_property_t;
typedef bootstrap_property_t * bootstrap_property_array_t;

typedef boolean_t *bool_array_t;

#define	BOOTSTRAP_MAX_LOOKUP_COUNT		20

#define	BOOTSTRAP_SUCCESS				0
#define	BOOTSTRAP_NOT_PRIVILEGED		1100
#define	BOOTSTRAP_NAME_IN_USE			1101
#define	BOOTSTRAP_UNKNOWN_SERVICE		1102
#define	BOOTSTRAP_SERVICE_ACTIVE		1103
#define	BOOTSTRAP_BAD_COUNT				1104
#define	BOOTSTRAP_NO_MEMORY				1105
#define BOOTSTRAP_NO_CHILDREN			1106

#define BOOTSTRAP_STATUS_INACTIVE		0
#define BOOTSTRAP_STATUS_ACTIVE			1
#define BOOTSTRAP_STATUS_ON_DEMAND		2

extern mach_port_t bootstrap_port;

kern_return_t bootstrap_create_server(
		mach_port_t bp,
		cmd_t server_cmd,
		uid_t server_uid,
		boolean_t on_demand,
		mach_port_t *server_port);

kern_return_t bootstrap_subset(
		mach_port_t bp,
		mach_port_t requestor_port,
		mach_port_t *subset_port);

kern_return_t bootstrap_unprivileged(
		mach_port_t bp,
		mach_port_t *unpriv_port)
		AVAILABLE_MAC_OS_X_VERSION_10_0_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_5;

kern_return_t bootstrap_parent(
		mach_port_t bp,
		mach_port_t *parent_port);

AVAILABLE_MAC_OS_X_VERSION_10_0_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_5
kern_return_t
bootstrap_register(mach_port_t bp, name_t service_name, mach_port_t sp);
#ifdef AVAILABLE_MAC_OS_X_VERSION_10_0_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_6
AVAILABLE_MAC_OS_X_VERSION_10_0_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_6
#endif
kern_return_t
bootstrap_create_service(mach_port_t bp, name_t service_name, mach_port_t *sp);

kern_return_t bootstrap_check_in(
		mach_port_t bp,
		const name_t service_name,
		mach_port_t *sp);


kern_return_t bootstrap_look_up(
		mach_port_t bp,
		const name_t service_name,
		mach_port_t *sp);


kern_return_t bootstrap_status(
		mach_port_t bp,
		name_t service_name,
		bootstrap_status_t *service_active)
		AVAILABLE_MAC_OS_X_VERSION_10_0_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_5;


const char *bootstrap_strerror(kern_return_t r) __attribute__((__nothrow__, __pure__, __warn_unused_result__));

#pragma GCC visibility pop

__END_DECLS

#endif