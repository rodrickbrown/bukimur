#!/usr/bin/env ruby

#require 'pry'

class Rummikub

  def initialize(players)

    @players = players
    @decks = [0, 1]
    @colors = %w(red black blue orange)
    @numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    @jokers = [{color: 'black', number: 0, deck: 0},{color: 'red', number: 0, deck: 1}]

    @bag = @jokers

    # binding.pry

    puts "----- Initializing game with #{@players} -----"

    @decks.each do |deck|
      @colors.each do |color|
        @numbers.each do |num|
          @bag << { deck: deck, color: color, number: num}
        end
      end
    end
  end

  def deal_tiles(n)
    @tiles = []

    (0...n).each do
      @tiles << @bag.pop
    end
    return @tiles
  end

  def show_bag
    return @bag
  end

  def shuffle_bag
    @bag.shuffle!
  end
end

game = Rummikub.new(4)

puts "size of bag is now " + game.show_bag.count.to_s
game.shuffle_bag
puts(game.deal_tiles(2))
puts "size of bag is now " + game.show_bag.count.to_s
game.shuffle_bag
puts(game.deal_tiles(2))
puts "size of bag is now " + game.show_bag.count.to_s
