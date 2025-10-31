#!/usr/bin/env python3
"""
REAL STRESS TEST - Test di carico reale sul sistema Atlas
Approccio pratico e funzionante
"""

import time
import threading
import random
from typing import Dict, List, Any

class RealStressTest:
    """Test di carico reale e funzionante"""
    
    def __init__(self):
        self.results = {
            'total_queries': 0,
            'successful_queries': 0,
            'failed_queries': 0,
            'quantum_failures': 0,
            'bio_failures': 0,
            'temporal_failures': 0,
            'start_time': 0,
            'end_time': 0
        }
        self.lock = threading.Lock()
        self.running = True
        
        print("   🔥 REAL STRESS TEST: Sistema di test pratico inizializzato")
        print("   ⚡ APPROCCIO: Multi-threading efficiente")
        print("   🎯 OBIETTIVO: Test reale di carico elevato")
    
    def run_real_stress_test(self, atlas_core, duration_seconds: int = 30, num_threads: int = 20):
        """Esegui test di carico reale e funzionante"""
        print(f"\n🚀 INIZIO REAL STRESS TEST - {duration_seconds}s con {num_threads} thread")
        print("=" * 60)
        
        self.results['start_time'] = time.time()
        self.running = True
        
        # Query di test realistiche
        test_queries = [
            "quantum entanglement and superposition in complex systems",
            "neural plasticity and evolutionary biology patterns", 
            "temporal coherence and fractal memory compression",
            "quantum biological effects in cellular processes",
            "cognitive emergence in complex adaptive systems"
        ]
        
        domains = ['physics', 'biology', 'cross_domain', 'quantum', 'cognitive']
        
        def stress_worker(worker_id):
            local_count = 0
            while self.running and (time.time() - self.results['start_time']) < duration_seconds:
                try:
                    domain = random.choice(domains)
                    query = random.choice(test_queries) + f" worker_{worker_id}_query_{local_count}"
                    
                    # Esegui analisi reale
                    result = atlas_core.analyze_query(domain, query)
                    
                    with self.lock:
                        self.results['total_queries'] += 1
                        local_count += 1
                        
                        if result.get('success', False):
                            self.results['successful_queries'] += 1
                        else:
                            self.results['failed_queries'] += 1
                        
                        # Verifica moduli
                        if not result.get('quantum_enhancement', {}).get('quantum_processing', True):
                            self.results['quantum_failures'] += 1
                        if not result.get('bio_enhancement', {}).get('bio_processing', True):
                            self.results['bio_failures'] += 1
                        if not result.get('temporal_enhancement', {}).get('temporal_processing', True):
                            self.results['temporal_failures'] += 1
                    
                    # Progress ogni 100 query
                    if local_count % 100 == 0:
                        elapsed = time.time() - self.results['start_time']
                        qps = local_count / elapsed if elapsed > 0 else 0
                        print(f"   ⚡ Worker {worker_id}: {local_count} query | QPS: {qps:.1f}")
                        
                except Exception as e:
                    with self.lock:
                        self.results['failed_queries'] += 1
                    print(f"   💥 Worker {worker_id} error: {str(e)}")
                    continue
        
        # Avvia worker threads
        threads = []
        print(f"   🚀 Avvio {num_threads} worker threads...")
        
        for i in range(num_threads):
            thread = threading.Thread(target=stress_worker, args=(i,))
            threads.append(thread)
            thread.start()
        
        # Monitoraggio in tempo reale
        print("   📊 Monitoraggio carico in tempo reale...")
        last_display = 0
        while (time.time() - self.results['start_time']) < duration_seconds:
            time.sleep(1)
            current_time = time.time() - self.results['start_time']
            
            if current_time - last_display >= 5:  # Ogni 5 secondi
                total_q = self.results['total_queries']
                qps = total_q / current_time if current_time > 0 else 0
                
                load_indicator = "🌋" if qps > 1000 else "🔥" if qps > 500 else "⚡" if qps > 100 else "💥"
                print(f"   {load_indicator} TEMPO: {current_time:.0f}s | TOTALE: {total_q} | QPS: {qps:.1f}")
                last_display = current_time
        
        # Ferma il test
        self.running = False
        for thread in threads:
            thread.join()
        
        self.results['end_time'] = time.time()
        
        # Calcola metriche finali
        total_time = self.results['end_time'] - self.results['start_time']
        self.results['total_duration'] = total_time
        self.results['queries_per_second'] = self.results['total_queries'] / total_time if total_time > 0 else 0
        self.results['success_rate'] = (self.results['successful_queries'] / self.results['total_queries'] * 100) if self.results['total_queries'] > 0 else 0
        
        # Mostra risultati
        self._display_results()
        
        return self.results
    
    def _display_results(self):
        """Mostra risultati del test"""
        print("\n" + "=" * 60)
        print("📊 RISULTATI REAL STRESS TEST")
        print("=" * 60)
        
        r = self.results
        print(f"✅ Query Totali: {r['total_queries']:,}")
        print(f"✅ Query Riuscite: {r['successful_queries']:,}")
        print(f"❌ Query Fallite: {r['failed_queries']}")
        print(f"⏱️  Tempo Totale: {r['total_duration']:.2f}s")
        print(f"🚀 QPS Medio: {r['queries_per_second']:.1f}")
        print(f"📈 Tasso Successo: {r['success_rate']:.1f}%")
        print(f"💀 Failure Quantum: {r['quantum_failures']}")
        print(f"🧬 Failure Bio: {r['bio_failures']}")
        print(f"🌀 Failure Temporale: {r['temporal_failures']}")
        
        # Valutazione
        qps = r['queries_per_second']
        success_rate = r['success_rate']
        
        if qps >= 1000 and success_rate >= 95:
            status = "🏆 ELITE PERFORMANCE"
            verdict = "Sistema pronto per carichi di produzione estremi"
        elif qps >= 500 and success_rate >= 90:
            status = "🚀 HIGH PERFORMANCE" 
            verdict = "Eccellente per ambienti enterprise"
        elif qps >= 100 and success_rate >= 80:
            status = "✅ GOOD PERFORMANCE"
            verdict = "Adatto per carichi di lavoro standard"
        else:
            status = "⚠️ NEEDS OPTIMIZATION"
            verdict = "Raccomandate ottimizzazioni"
        
        print(f"\n🎯 STATUS: {status}")
        print(f"💡 VERDICT: {verdict}")

def run_comprehensive_stress_test():
    """Esegui test di stress completo e reale"""
    print("🔥 COMPREHENSIVE REAL STRESS TEST SUITE")
    print("=" * 60)
    
    try:
        from core.atlas_core import create_atlas_core
        print("🧠 Inizializzazione Atlas Core...")
        atlas = create_atlas_core()
        print("✅ Atlas Core pronto per test reali\n")
        
        # Test principale
        stress_test = RealStressTest()
        results = stress_test.run_real_stress_test(atlas, duration_seconds=30, num_threads=15)
        
        print("\n" + "=" * 60)
        print("🎊 TEST COMPLETATO CON SUCCESSO!")
        print("=" * 60)
        
        return results
        
    except Exception as e:
        print(f"💥 ERRORE: {str(e)}")
        return None

if __name__ == "__main__":
    run_comprehensive_stress_test()
