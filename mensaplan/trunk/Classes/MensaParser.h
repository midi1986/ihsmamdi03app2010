#import <UIKit/UIKit.h>
#import "MensaTag.h"
#import "MensaPlan.h"
#import "MensaKategorie.h"
#import "MensaEssen.h"

@class MensaAppDelegate;

@interface MensaParser : NSObject {

	NSMutableString *currentElementValue;
	
	MensaAppDelegate *appDelegate;
	
	MensaTag *mensaTag;
	MensaKategorie *mensaKategorie;
	MensaEssen *mensaEssen;
	
}

- (MensaParser *) initMensaParser;

@end
