//
//  MensaPlan.m
//  Mensa
//
//  Created by emc on 19.11.10.
//  Copyright 2010 __MyCompanyName__. All rights reserved.
//

#import "MensaPlan.h"


@implementation MensaPlan

@synthesize mensaTage;


- (void)dealloc {
	[mensaTage release];
	[super dealloc];
}

@end
