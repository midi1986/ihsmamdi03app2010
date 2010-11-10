#import <UIKit/UIKit.h>

@class MensaAppDelegate, Mensa;

@interface MensaParser : NSObject {

	NSMutableString *currentElementValue;
	
	MensaAppDelegate *appDelegate;
	Mensa *aMensa; 
}

- (MensaParser *) initMensaParser;

@end
