
--
# Options Trading

Options (διαφορικά σύμβολα) είναι συμβόλαια παράγωγα που δίνουν το δικαίωμα, αλλά όχι την υποχρέωση, να αγοράσετε ή να πουλήσετε ένα πέρασμα σε προκαθορισμένη τιμή (strike) μέχρι μια συγκεκριμένη ημερομηνία λήξης (expiration). Χρησιμοποιούνται για εύνοια (leverage), ασφάλιση (hedging) και παραγωγή εισπράξεων (income generation) μέσω πώλησης premium.

## Βασικές Έννοιες

### Call Option
Δικαίωμα αγοράς υποπτώματος σε strike price. Κερδοφόρη όταν η τιμή του υποπτώματος υπερβαίνει το strike + premium. Χρήση: αγορά call για αισιόδοξη σpekουλάτσια, leveraged upside, ή income generation μέσω covered calls.

### Put Option
Δικαίωμα πώλησης υποπτώματος σε strike price. Κερδοφόρη όταν η τιμή του υποπρώματος είναι κάτω από το strike - premium. Χρήση: αγορά put για αρνητική σpekουλάτσια, ασφάλιση portfolίου (protective puts), ή income μέσω cash-secured puts.

## Οι Έλληνες (The Greeks)

### Δέλτα (Delta)
Δείχνει πόσο κινείται η τιμή του option για $1 αλλαγή στη μετοχή. Πλάτος 0-1 για calls, -1 έως 0 για puts. Χρησιμοποιείται ως αναλογία ασφαλείας (hedge ratio).

### Γάμμα (Gamma)
Δείχνει πόσο αλλάζει το delta για $1 αλλαγή στη μετοχή. Υψηλό gamma σημαίνει γρήγορες αλλαγές στο delta, ιδίως κοντά στην expiration.

### Θήτα (Theta)
Ημερήσια απώλεια αξίας λόγω κίνησης χρόνου. Είναι εχθρός του αγοραστή και φίλος του πωλητή. Τυπικές τιμές: -$0.01/ημέρα μακρινά από expiration, -$0.10/ημέρα κοντά στην expiration.

### Βήτα (Vega)
Ευαισθησία στην αλλαγή μεταβλητότητας. Υψηλό vega σημαίνει μεγάλη ευαισθησία σε αλλαγές vol.

### Ρο (Rho)
Ευαισθησία στις αλλαγές процентτικού επιτοκίου. Σημαντικό για LEAPS (μακροπρόθεσμα options).

## Στρατηγικές

### Covered Call
Κατέχω μετοχή + πωλώ call option. Παράγει εισπράξεις σε μετοχές που κατέχω. Κίνδυνος: απάθεια στην άνοδο αν η μετοχή ξεπεράσει το strike.

### Protective Put (Married Put)
Κατέχω μετοχή + αγοράζω put option. Λειτουργεί ως ασφάλιση κατά τη πτώση της αγοράς. Κόστος: το premium που πληρώνω.

### Long Straddle
Αγοράζω call + put στο ίδιο strike και expiration. Κερδοφόρη αν υπάρξει μεγάλη κίνηση σε οποιαδήποτε κατεύθυνση. Break-even: strike ± κόστος.

### Vertical Spread
Αγοράζω option σε ένα strike και πωλώ σε διαφορετικό. Bull Call Spread (αγορά χαμηλού strike call, πώληση υψηλού) ή Bear Put Spread. Περιορισμένος κίνδυνος με leveraged directional bet.

### Iron Condor
Bull put spread + bear call spread. Παράγει εισπράξεις όταν περιμένω χαμηλή μεταβλητότητα. Max loss γνωστό και περιορισμένο.

## Διαχείριση Κινδύνου

- **Position Sizing**: Μην ρισκάρεις πάνω από 2-5% του portfolίου ανά συναλλαγή.
- **Greeks Limits**: Γνωρίζω την έκθεση μου σε delta, gamma, theta.
- **Stop Losses**: Ψηλές πώληση αν χάσω 50%, χρονικά σTOP αν δεν λειτουργεί.
- **Αποφυγή naked options**: Απέvaitε πώληση calls χωρίς μετοχή ή puts χωρίς ρεσέρβες.

## Μεταβλητότητα

- **Implied Volatility (IV)**: Οι προσδοκίες της αγοράς για μελλοντική μεταβλητότητα.
- **Historical Volatility (HV)**: Η πραγματική μεταβλητότητα στο παρελθόν.
- **Mean Reversion**: Υψηλή IV τείνει να πέσει, χαμηλή IV τείνει να ανεβαίνει. Αγορά options όταν η IV είναι χαμηλή, πώληση όταν είναι υψηλή.

## Φορολογία

- **Section 1256**: Non-equity options (indices, futures) — 60% κέρδος φορολογείται ως long-term, 40% ως short-term. Επιfavorώμενη από την ordinary income tax.
- **Wash Sale Rule**: 30-day window — δεν μπορείτε να εκφράσετε ζημιά στην ίδια εξάσκηση.

## Πότε είναι κατάλληλα τα Options

**Κατάλληλα για**: έμπειρους επενδυτές, με κατανόηση derivatives, σαφήνεια σε risk tolerance, χρόνο για παρακολούθηση, επαρκές κεφάλαιο (>25κ).

**Μη κατάλληλα για**: αρχάριους, συνταξιοδοτικούς λογαριασμούς (εκτός εγκρίσεων), επενδυτές που δεν μπορούν να παρακολουθούν, περιορισμένο κεφάλαιο, ατρόμοι.

## Εναλλακτικές

- ETFs με options exposure (covered call ETFs, protective put ETFs, put-write ETFs)
- Leveraged ETFs (2x/3x) — μόνο για βραχυπρόθεσμη συναλλαγή
- Απευθείας ιδιοκτησία μετοχών και ευρετικών δείκτες

## Βαστικά Λάθη

- Αγορά OTM options με χαμηλή πιθανότητα κερδοφόρησης
- ΠαραIgnoring time decay
- Πώληση naked options με απεριόριστο κίνδυνο
- Overleveraging με πάρα πολλές συμβάσεις
- Μη κατανόηση των Greeks

## Κοινές Πρακτικές

1. Ξεκινήστε μικρά (1-2 συμβάσεις)
2. Κατανοήστε τα μαθηματικά πριν εισέλθετε
3. Σεβαστείτε το time decay
4. Διαχειριστείτε τα Greeks
5. Χρησιμοποιήστε stop losses
6. Απέvaitε naked selling
7. Συναλλάγεστε liquid options
8. Σκεφτείτε τη μεταβλητότητα (buy low IV, sell high IV)
9. Σχεδιάστε για assignment
10. Paper trade πρώτα

## Σχετικές Έννοιες
- [[risk-management]]
- [[real-options-analysis]]
- [[probability-and-judgment-under-uncertainty]]
- [[decision-tracking]]
- [[kelly-criterion]]
- [[martingale-strategy]]

See also: [[retirement-planning]]

See also: [[alternative-investments]]

See also: [[decision-making-frameworks]]
