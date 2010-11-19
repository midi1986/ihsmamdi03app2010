#import <UIKit/UIKit.h>
#import "MensaTag.h"


@interface MensaDetailViewController : UIViewController {

	IBOutlet UITableView *tableView;
	
	MensaTag *mensaTag;
}

@property (nonatomic, retain) MensaTag *mensaTag;

@end
