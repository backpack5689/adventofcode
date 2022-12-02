use std::io;
use std::io::prelude::*;

fn main(){

    let reader = io::stdin();
    // flag: tells us new elf
    // max: value to hold max amount of calories
    // calories: array of all calories, using -1 to denote a elf change
    // elfCalories: running total of calories
    // elfNumber: Current Elf Position
    // winningElf: Elf with the most calories in bag
    let mut flag: i64 = -1;
    let mut max: i64 = -1;
    let mut max2: i64 = -1;
    let mut max3: i64 = -1;
    let mut totalmax: i64 = -1;
    let mut calories = vec![];
    let mut elfCalories: i64 = 0;
    let mut elfNumber: i64 = 0;
    let mut winningElf: i64 = 0;
    let mut entry = String::new();
    let mut elfTotals = vec![];

    for entry in reader.lock().lines() {
        let value = entry.unwrap();
        if value == "" {
            // DEBUG: println!("");
            calories.push(-1);
        }
        else{
            // DEBUG: println!("{value}");
            calories.push(value.parse::<i64>().unwrap());
        }
    }

    for foodItem in calories.iter_mut(){
        if *foodItem == flag {
            elfTotals.push(elfCalories);
            elfCalories = 0;
        }
        else{
            elfCalories += *foodItem;
        }
    }

    elfTotals.sort_by(|a, b| b.cmp(a));
    println!("{:?}", elfTotals);
    totalmax = elfTotals[0] + elfTotals[1] + elfTotals[2];
    //DEBUG: println!("----------");
    println!("Elf with the most calories: {}", winningElf);
    println!("Number of Calories: {}", totalmax);
}