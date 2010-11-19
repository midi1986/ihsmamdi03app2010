//
//  MensaEssen.m
//  Mensa
//
//  Created by emc on 19.11.10.
//  Copyright 2010 __MyCompanyName__. All rights reserved.
//

#import "MensaEssen.h"


@implementation MensaEssen

@synthesize sorte, name, beschreibung, preis, essenID;

- (void) dealloc {

	[sorte release];
	[name release];
	[beschreibung release];
	[preis release];
	[super dealloc];
}

@end
