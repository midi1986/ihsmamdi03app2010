//
//  MensaTag.h
//  Mensa
//
//  Created by emc on 19.11.10.
//  Copyright 2010 __MyCompanyName__. All rights reserved.
//

//#import <Cocoa/Cocoa.h>


@interface MensaTag : NSObject {
	
	NSString *name;
	NSMutableArray *mensaKategorien;
	
}

@property (nonatomic, retain) NSString *name;
@property (nonatomic, retain) NSMutableArray *mensaKategorien;


@end
