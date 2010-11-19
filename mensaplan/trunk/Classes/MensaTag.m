//
//  MensaTag.m
//  Mensa
//
//  Created by emc on 19.11.10.
//  Copyright 2010 __MyCompanyName__. All rights reserved.
//

#import "MensaTag.h"


@implementation MensaTag

@synthesize name, mensaKategorien;


- (void)dealloc {
	[name release];
	[mensaKategorien release];
	[super dealloc];
}


@end
