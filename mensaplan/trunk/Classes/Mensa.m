#import "Mensa.h"

@implementation Mensa

@synthesize tag, kategorie, name, beschreibung, preis, essenID;

- (void) dealloc {
	
	[tag release];
	[kategorie release];
	[name release];
	[beschreibung release];
	[preis release];
	[super dealloc];
}

@end
