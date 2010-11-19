#import <UIKit/UIKit.h>

@class MensaPlan;

@interface MensaAppDelegate : NSObject <UIApplicationDelegate> {
    
    UIWindow *window;
    UINavigationController *navigationController;
	
	MensaPlan *mensaPlan;
}

@property (nonatomic, retain) IBOutlet UIWindow *window;
@property (nonatomic, retain) IBOutlet UINavigationController *navigationController;

@property (nonatomic, retain) MensaPlan *mensaPlan;

@end

