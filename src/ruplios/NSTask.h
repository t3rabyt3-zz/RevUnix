

#import <Foundation/NSObject.h>

@class NSString, NSArray, NSDictionary;

typedef NS_ENUM(NSInteger, NSTaskTerminationReason) {
    NSTaskTerminationReasonExit = 1,
    NSTaskTerminationReasonUncaughtSignal = 2
} NS_ENUM_AVAILABLE(10_6, NA);

@interface NSTask : NSObject
- (id)init;

- (void)setLaunchPath:(NSString *)path;
- (void)setArguments:(NSArray *)arguments;
- (void)setEnvironment:(NSDictionary *)dict;
- (void)setCurrentDirectoryPath:(NSString *)path;
- (void)setStandardInput:(id)input;
- (void)setStandardOutput:(id)output;
- (void)setStandardError:(id)error;

- (NSString *)launchPath;
- (NSArray *)arguments;
- (NSDictionary *)environment;
- (NSString *)currentDirectoryPath;


- (id)standardInput;
- (id)standardOutput;
- (id)standardError;


- (void)launch;

- (void)interrupt; 
- (void)terminate; 
- (BOOL)suspend;
- (BOOL)resume;

- (int)processIdentifier; 
- (BOOL)isRunning;

- (int)terminationStatus;
- (NSTaskTerminationReason)terminationReason NS_AVAILABLE(10_6, NA);

@property (copy) void (^terminationHandler)(NSTask *) NS_AVAILABLE(10_7, NA);


@end

@interface NSTask (NSTaskConveniences)

+ (NSTask *)launchedTaskWithLaunchPath:(NSString *)path arguments:(NSArray *)arguments;

- (void)waitUntilExit;


@end

FOUNDATION_EXPORT NSString * const NSTaskDidTerminateNotification;

