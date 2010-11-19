//
//  MensaKategorie.m
//  Mensa
//
//  Created by emc on 19.11.10.
//  Copyright 2010 __MyCompanyName__. All rights reserved.
//

#import "MensaKategorie.h"


@implementation MensaKategorie

@synthesize name, mensaEssens;

- (void) dealloc {
	
	[name release];
	[mensaEssens release];
	[super dealloc];
}

@end
