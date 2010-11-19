//
//  MensaKategorie.h
//  Mensa
//
//  Created by emc on 19.11.10.
//  Copyright 2010 __MyCompanyName__. All rights reserved.
//

@interface MensaKategorie : NSObject {
	
	NSString *name;
	NSMutableArray *mensaEssens;

}

@property (nonatomic, retain) NSString *name;
@property (nonatomic, retain) NSMutableArray *mensaEssens;

@end
