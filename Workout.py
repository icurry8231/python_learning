
q=1
w=1
while q==1:
    i=raw_input('What day of the week is it?:')
    if i=='wednesday' or i=='Wednesday':
        q=0
        x='16 sets for back'
        y='14 sets for biceps'
        z=x + ' and ' + y
        print('you have ' + z + '.')
    elif i=='thursday' or i=='Thursday':
        q=0
        x='16 sets for chest'
        y='14 sets for triceps'
        z=x + ' and ' + y
        print('you have ' + z + '.')
    elif i=='saturday' or i=='Saturday':
        q=0
        x='20 sets for legs(8-quads,6-hamstrings,6-calves/hips/glutes)'
        y='12 sets for biceps'
        z=x + ' and ' + y
        print('you have ' + z + '.')
    elif i=='sunday' or i=='Sunday':
        q=0
        x='16 sets for shoulders'
        y='12 sets for chest'
        z=x + ' and ' + y
        print('you have ' + z + '.')
    elif i=='monday' or i=='Monday' or i=='tuesday' or i=='Tuesday' or i=='friday' or i=='Friday':
            print('You have no workout scheduled for today.')
            print('However, you may have soccer practice.')
            if i=='monday' or i=='Monday':
                q=0
                time='9pm-11pm'
                loc='football field'
                print('You have soccer practice from ' + time + ' at the ' + loc + '.')
            elif i=='tuesday' or i=='Tuesday':
                q=0
                time='9pm-11pm'
                loc='baseball field'
                print('You have soccer practice from ' + time + ' at the ' + loc + '.')
            elif i=='friday' or i=='Friday':
                while w==1:
                    j=raw_input('has Kevin emailed you back about Friday practices? (Y or N)')
                    if j=='Y' or j=='y':
                        q=0
                        w=0
                        time='(time placeholder)' #edit this when I have the info
                        loc='(location placeholder)' #edit this when I have the info
                        print('You have soccer practice from ' + time + ' at the ' + loc + '.')
                    elif j=='N' or j=='n':
                        q=0
                        w=0
                        print("You have no practice today, as we have not heard back from Kevin.")
                    else:
                        q=0
                        w=1
                        print('please enter Y or N.')
    else:
        q=1
        print('Please enter a day of the week.')
