// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn add_two_numbers(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut carry = 0;
        let mut result = Box::new(ListNode::new(0));
        let mut cursor = &mut result;
        
        let mut one = l1.clone();
        let mut two = l2.clone();
        
        while one.is_some() || two.is_some() || carry != 0 {
            if let Some(cell) = one {
                carry += cell.val;
                one = cell.next;
            }
            
            if let Some(cell) = two {
                carry += cell.val;
                two = cell.next;
            }
            
            cursor.next = Some(Box::new(ListNode::new(carry % 10)));
            cursor = cursor.next.as_mut().unwrap();
            
            carry = carry / 10;
        }
        
        return result.next;
    }
}