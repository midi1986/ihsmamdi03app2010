#import <UIKit/UIKit.h>

@interface Mensa : NSObject {
	
	NSInteger essenID;
	NSString *tag;	
	NSString *kategorie;	
	NSString *name;
	NSString *beschreibung;
	NSString *preis;
}

@property (nonatomic, readwrite) NSInteger essenID;
@property (nonatomic, retain) NSString *tag;
@property (nonatomic, retain) NSString *kategorie;
@property (nonatomic, retain) NSString *name;
@property (nonatomic, retain) NSString *beschreibung;
@property (nonatomic, retain) NSString *preis;


@end
